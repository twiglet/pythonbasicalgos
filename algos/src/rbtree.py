'''
Created on Dec 30, 2012

@author: keving
'''
import random
import sys

def basic_comp(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1     

class RBTree:
    def __init__(self, comp = basic_comp):
        self.tree = None
        self.comp = comp
        
    def __str__(self):
        return self.tree.__str__()

class Node:
    def __init__(self, value, parent=None, left=None, right=None, colour="B"):
        self.left = left
        self.right = right
        self.payload = value
        self.parent = parent
        self.colour = colour
        
    def __str__(self):
        def tree_to_string(n, depth):
            ret = ""
            if n.right != None:
                ret = tree_to_string(n.right, depth+1)
            ret = ret + ("\n%s(%s,%s)" % ("  " * depth, n.payload, n.colour))
            if n.left != None:
                ret = ret + tree_to_string(n.left, depth+1)
            return ret
        return tree_to_string(self, 0)      

## Make A the left child of its right child, B
#     A
#   a    B
#      b    c
#
#     B
#   A    c
# a   b
def left_rotate(t,n):
    r = n.right
    r.parent = n.parent
    n.parent = r
    n.right = r.left
    r.left = n
    
    ## replace n with r in n's parent
    if r.parent == None:
        ## root
        t.tree = r
    elif r.parent.left == n:
        r.parent.left = r
    else:
        r.parent.right = r

## Make B the right child of its left child, A
#     B
#   A    c
# a   b
#
#     A
#   a    B
#      b    c
#

def right_rotate(t,n):
    l = n.left
    l.parent = n.parent
    n.parent = l
    n.left = l.right
    l.right = n
    
    ## replace n with r in n's parent
    if l.parent == None:
        ## root
        t.tree = l
    elif l.parent.left == n:
        l.parent.left = l
    else:
        l.parent.right = l


def rb_insert(bst, v):
    ## pre: node is a BST Node
    ## post: v is inserted into node, respecting BST
    def insert(node):
        if bst.comp(v,node.payload) >= 0:
            if node.right == None:
                node.right = Node(v,parent=node,colour="R")
                return node.right
            else:
                return insert(node.right)
        else:
            if node.left == None:
                node.left = Node(v,parent=node, colour="R")
                return node.left
            else:
                return insert(node.left)
    ## red_node is a node which possibly violates r/b because its red and its parent is red        
    def rb_fixup(red_node):
        if red_node.parent == None:
            ## its the root, make it b and we are done
            red_node.colour = "B"
        elif red_node.parent.colour == "B":
            ## all is good, exit
            pass
        else:
            ## we are red and so is parent, fixup
            
            ## grandparent must exist because parent is red, but root node would be black
            parent = red_node.parent
            grandparent = parent.parent
            if grandparent.left == parent:
                uncle = grandparent.right
                if uncle != None and uncle.colour == "R":
                    ## parent and uncle are red, make them black, grandparent red and recurse
                    uncle.colour = "B"
                    parent.colour = "B"
                    grandparent.colour = "R"
                    rb_fixup(grandparent)
                else:
                    if parent.right == red_node:
                        left_rotate(bst, parent)
                        ## parent and red_node have swapped
                        parent = red_node
                    right_rotate(bst, grandparent)
                    grandparent.colour = "R"
                    parent.colour = "B" 
            else:
                ## mirror of above
                uncle = grandparent.left
                if uncle != None and uncle.colour == "R":
                    ## parent and uncle are red, make them black, grandparent red and recurse
                    uncle.colour = "B"
                    parent.colour = "B"
                    grandparent.colour = "R"
                    rb_fixup(grandparent)
                else:
                    if parent.left == red_node:
                        right_rotate(bst, parent)
                        ## parent and red_node have swapped
                        parent = red_node
                    left_rotate(bst, grandparent)
                    grandparent.colour = "R"
                    parent.colour = "B" 
               
        
    if bst.tree == None:
        bst.tree = Node(v,colour="B")
    else:
        new_node = insert(bst.tree)
        ## Now restore r/b
        rb_fixup(new_node)
 
 
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
    size = 20
    xs = [random.randrange(0,size) for i in range(size)]
    tree = RBTree()
    for x in xs:
        rb_insert(tree, x)
    print tree
    xs = [i for i in range(size)]
    tree = RBTree()
    for x in xs:
        rb_insert(tree, x)
    print tree
    in_order(tree, pprint)
        

    
    
   # for i,v in enumerate(arr):
    #    print i, v