'''
Created on Dec 30, 2012

@author: keving
'''
import random

## A heap, h, is an array starting at index 1 (we ignore h[0]) 
## representing a binary tree where h[i]
## has children at h[i*2], h[i*2+1]
## each parent is smaller than its children

class Heap:
    def __init__(self, initSize=0):
        self.heap = []
        self.size = initSize 
        
    def __str__(self):
        ret = "" 
        first = True
        for i in range(1,self.size+1):
            if not first:
                ret = ret + " "
            first = False
            ret = ret + str(self.heap[i])   
        return ret
        
        

## take the element at xs[i] and push it down through
## the heap to its rightful position
## pre:  xs is a valid heap except for the element at xs[i]
## post: xs is a valid heap
def pushdown(h,i):
    ## find position of smallest child
    mi = i*2
    if mi > h.size:
        return
    if mi+1 <= h.size and h.heap[mi+1] < h.heap[mi]:
        mi = mi+1
    ## Are we already there?
    if h.heap[i] < h.heap[mi]:
        return
    ## no, swap with smallest child and recurse
    t = h.heap[mi]
    h.heap[mi] = h.heap[i]
    h.heap[i] = t
    pushdown(h,mi)
    
## take the element at h.heap[i] and push it up through
## the heap to its rightful position
## pre:  h is a valid heap except for the element at h.heap[i]
## post: h is a valid heap
def pushup(h,i):
    ## If we are at the root then we are done
    #print "pushing", i
    #print h
    if i == 1:
        return
    ## If we are bigger than our parent then we are done
    if h.heap[i] > h.heap[i / 2]:
        return

    ## no, swap with parent and recurse
    t = h.heap[i]
    h.heap[i] = h.heap[i/2]
    h.heap[i/2] = t
    pushup(h,i/2)
 
def extractmin(h):
    # min element is at h.heap[1]
    ret = h.heap[1]
    # put last element at h.heap[1] and push it down
    h.heap[1] = h.heap[h.size]
    h.size = h.size-1
    pushdown(h,1)
    #print is_heap(xs,n-1)
    return ret

def is_heap(xs,n):
    print n
    for i in range(1,n+1):
        if i*2 > n:
            return True
        if xs[i] > xs[i*2]:
             print "1 False", i
             #printarr(xs,n)
             return False
        if i*2+1 > n:
            return True
        if xs[i] > xs[i*2+1]:
             print "2 False", i
             #printarr(xs,n)
             return False
         

if __name__ == '__main__':
    
    size = 10
    
    heap = Heap()
    heap.heap = [random.randrange(0,size) for i in range(size+1)]
    heap.size = size
    
    print heap
    
    ## Turn into a heap
    for i in range(2,heap.size+1):
        heap.size = i
        pushup(heap,i)

    print heap
        
    for i in range(1,heap.size+1):
        print i, extractmin(heap)
        

    
    
   # for i,v in enumerate(arr):
    #    print i, v