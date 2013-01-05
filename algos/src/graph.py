'''
Created on Dec 30, 2012

@author: keving
'''
import random

def basic_comp(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1     

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_edge(self, x, y, w):
            
        
    def __str__(self):
        return self.vertices.__str__()

class Node:
    def __init__(self, value, l=None, r=None):
        self.left = l
        self.right = r
        self.payload = value
        
    def __str__(self):
        return "%s: ( %s %s )" % (self.payload, self.left, self.right)
   

def bst_insert(bst, v):
    ## pre: node is a BST Node
    ## post: v is inserted into node, respecting BST
    def insert(node):
        if bst.comp(v,node.payload) >= 0:
            if node.right == None:
                node.right = Node(v)
            else:
                insert(node.right)
        else:
            if node.left == None:
                node.left = Node(v)
            else:
                insert(node.left)

    if bst.tree == None:
        bst.tree = Node(v)
    else:
        insert(bst.tree)
 
 
def in_order(t, f):
    def _inorder(node):
        if node == None:
            return
        else:
            _inorder(node.left)
            f(node.payload)
            _inorder(node.right)
    
    _inorder(t.tree) 

def pprint(x):
    print x
    
if __name__ == '__main__':
    size = 10
    xs = [random.randrange(0,size) for i in range(size)]
    tree = Tree()
    for x in xs:
        bst_insert(tree, x)
   
    in_order(tree, pprint)
        

    
    
   # for i,v in enumerate(arr):
    #    print i, v