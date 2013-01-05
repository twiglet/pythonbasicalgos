'''
Created on Dec 30, 2012

@author: keving
'''
from random import randrange


## We store a graph by an adjacency list
## Its a dictionary from vertices to a list of arcs, each arc is a tuple of end and weight 
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_edge(self, x, y, w):
        ## Ignore this edge if we already have an edge from x to y
        if y in [a for (a,_) in self.vertices.get(x, [])]:
            return
        ## If first edge to y then create an empty list of edges from x
        if not self.vertices.has_key(x):
            self.vertices[x] = []

        self.vertices[x].append((y,w,))
 
    def __str__(self):
        ret = "{\n"
        for v,e in self.vertices.iteritems():
            ret = ret + "  %s: %s\n" % (v, e)
        ret = ret + "}"
        return ret

def mk_undirected(g):
    new_edges = []
    for (v,es) in g.vertices.iteritems():
        for (y,w) in es:
            new_edges.append((y,v,w))
    for (x,y,w) in new_edges:
        g.add_edge(x,y,w)


if __name__ == '__main__':
    edge_count = 10
    # List of vertices from A .. H
    vertices = [chr(i) for i in range(ord('A'),ord('H')+1)]
    vertices_count = len(vertices)
    edges = [(vertices[randrange(vertices_count)],vertices[randrange(vertices_count)], randrange(10*edge_count)) for i in range((edge_count**2) / 4)]
    
    g = Graph()
    for (x,y,w) in edges:
        if x != y:
            g.add_edge(x,y,w)
    print g
    mk_undirected(g)
    print g