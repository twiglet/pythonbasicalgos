'''
Created on Dec 30, 2012

@author: keving

Algorithms follow those in Skiena's The Algorithm Design Manual, 2nd Ed
'''
from random import randrange, seed
from collections import deque


class SOSNode:
        def __init__(self, value):
            self.parent = self
            self.value = value
            self.child_count = 1
        
        def __str__(self):
            root = ""
            if self.parent != self:
                root = str(self.parent)
            else:
                root = "ROOT"
            return self.value + " -> (" + root + ")"
            
def get_root(n):
    root = n
    while root.parent != root:
        root = root.parent
    return root

def is_equivalent(n1, n2):
    r1 = get_root(n1)
    r2 = get_root(n2)
    return get_root(n1) == get_root(n2)

def union(n1, n2):
    r1 = get_root(n1)
    r2 = get_root(n2)
    
    if r1.child_count > r2.child_count:
        # make r1 new root of r2
        r2.parent = r1
        r1.child_count += r2.child_count
    else:
        # make r2 new root of r1
        r1.parent = r2
        r2.child_count += r1.child_count
    
if __name__ == '__main__':
    
    n1 = SOSNode('a')
    n2 = SOSNode('b') 
    print is_equivalent(n1,n2)
    union(n1,n2)
    print is_equivalent(n1,n2)
    print n1
    print n2    
    