'''
Created on Dec 30, 2012

@author: keving

Algorithms follow those in Skiena's The Algorithm Design Manual, 2nd Ed
'''
from random import randrange, seed
from collections import deque

## General Purpose holder so that we can pass by reference
class Ref:
    def __init__(self, initv):
        self.value = initv
    
    def apply(self, f):
        self.value = f(self.value)
        
    def get(self):
        return self.value

## We store a graph by an adjacency list
## Its a dictionary from vertices to a list of arcs, each arc is a tuple of end and weight 
class Graph:
    def __init__(self, directed=True):
        self.vertices = {}
        self.directed = directed
        
    def add_edge(self, x, y, w):
        ## Ignore this edge if we already have an edge from x to y
        if y in [a for (a, _) in self.vertices.get(x, [])]:
            return
        ## If first edge to y then create an empty list of edges from x
        if not self.vertices.has_key(x):
            self.vertices[x] = []

        self.vertices[x].append((y, w,))
        
    def delete_edge(self, x, y):
        ys = [a for (a, _) in self.vertices[x]]
        if y in ys:
            del self.vertices[x][ys.index(y)]

    def is_edge(self, x, y):
        return y in [a for (a, _) in self.vertices[x]]
    
    ## return weight of edge x,y
    ## pre: x,y must exist in graph
    def edge_weight(self, x, y):
        return filter(lambda (t, w): t == y, self.vertices[x])[0][1]

    def mk_undirected(self):

        # collect edges to add (back links)
        new_edges = []
        # collect edges to replace (existing has forward and back, replace with min weight)
        replace_edges = {}
    
        for (x, es) in self.vertices.iteritems():
            for (y, w) in es:
                if self.is_edge(y, x):
                    # We already have a back edge, replace with min weight
                    replace_edges[(x, y)] = min(w, self.edge_weight(y, x))
                else:
                    new_edges.append((y, x, w))
        # add new edges to graph
        for ((x, y), w) in replace_edges.iteritems():
            self.delete_edge(x, y)
            self.add_edge(x, y, w)
        for (x, y, w) in new_edges:
            self.add_edge(x, y, w)
        self.directed = False
    
    def __str__(self):
        ret = "{\n"
        for v, e in self.vertices.iteritems():
            ret = ret + "  %s: %s\n" % (v, e)
        ret = ret + "}"
        return ret


def bfs(g,s, parent = None, enter_node_f = None, exit_node_f = None, edge_f = None):
    
    if parent == None:
        parent = {}
    ## has node v been seen?
    found = {}
    # has node v been fully processed?
    processed = {}
    for v in g.vertices.keys():
        found[v] = False
        processed[v] = False

    ## Stores order we discovered nodes  
    # Put initial node on work queue
    workq = deque([s])
    found[s] = True

    while len(workq) > 0:
        x = workq.popleft()
        processed[x] = True
        if enter_node_f != None:
            enter_node_f(x) 
        for (y,w) in g.vertices[x]:
            if not processed[y]:
                if edge_f != None:
                    edge_f(x,y,w)
            if not found[y]:
                workq.append(y)
                found[y] = True
                parent[y] = x
        if exit_node_f != None:
            exit_node_f(x)

def dfs(g, s, parent = None, found = None, discovered = None, finished = None,
        entry_time = None, exit_time = None, 
        enter_node_f = None, exit_node_f = None, edge_f = None):

    def _dfs(x, time, processed, parent):
        
        ## Set finished to terminate early
        if finished.get():
            return
        
        entry_time[x] = time.get()
        
        time.apply(lambda v: v+1)
    
        if enter_node_f != None:
            enter_node_f(x)
     
        found[x] = True    
     
        for (y,w) in g.vertices[x]:
            if not found.get(y, False):
                # Never seen before, Tree edge
                parent[y] = x
                if edge_f != None:
                    edge_f(x,y,w)
                _dfs(y, time, processed, parent)
            elif g.directed or (not processed.get(y, False) and not parent.get(x, None) == y) :
                # back link
                if edge_f != None:
                    edge_f(x,y,w)
            if finished.get():
                return
        if exit_node_f != None:
            exit_node_f(x)

        exit_time[x] = time.get()
        time.apply(lambda v: v+1)
        
        processed[x] = True
        
    if parent == None:
        parent = {}
    if found == None:
        found = {}
    if entry_time == None:
        entry_time = {}
    if exit_time == None:
        exit_time = {}
    if finished == None:
        finished = Ref(False)
    # global counter to mark times we first enter and exit nodes
    time = Ref(0)
    processed = {}
    _dfs(s, time, processed, parent)
                
                
def print_path(parent, start, end):
    if start == end or parent.get(end, None) == None:
        print end
    else:
        print_path(parent, start, parent[end])
        print end

def pprint(*args):
     print args
            
if __name__ == '__main__':
    
    ## Comment for random graphs
    seed("InitialSeed")
    
    edge_count = 10
    # List of vertices from A .. H
    vertices = [chr(i) for i in range(ord('A'),ord('H')+1)]
    vertices_count = len(vertices)
    edges = [(vertices[randrange(vertices_count)],vertices[randrange(vertices_count)], randrange(10*edge_count)) for i in range((vertices_count**2) / 4)]
    g = Graph()
    for (x,y,w) in edges:
        if x != y:
            g.add_edge(x,y,w)
    g.mk_undirected()
    print "Our Graph"
    print g
    
    print "BFS"
    parent_reln = {}
    bfs(g, 'A', parent=parent_reln, edge_f = pprint)
    print_path(parent_reln, 'A', 'D')
    
    print "DFS"
    parent_reln = {}
    entry_time_map = {} 
    exit_time_map = {}
    dfs(g, 'A', parent=parent_reln, entry_time = entry_time_map, exit_time = exit_time_map, edge_f = pprint)
    print_path(parent_reln, 'A', 'B')
    
    # print cycles
    print "Find Cycles"
    parent_reln = {}
    found_map = {}
    finished_ref = Ref(False)
    def print_cycle(x,y,w):
        if found_map.get(y, False) and parent_reln.get(y, None) != x:
            print "cycle", y, x
            print_path(parent_reln, y, x)
            finished_ref.apply(lambda _:True)
            
    dfs(g, 'A', parent = parent_reln, found = found_map, finished = finished_ref, edge_f = print_cycle)
