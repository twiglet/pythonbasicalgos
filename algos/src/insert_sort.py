'''
Created on Dec 30, 2012

@author: keving
'''
import random

def insert_sort(xs):
    ## first 'i' elements are sorted, remainder unsorted
    ## for each unsorted' element move it to its position in the sorted part
    for i in range(len(xs)):
        for j in reversed(range(i)):
            if xs[j] <= xs[j+1]:
                ## done
                break
            ## swap elements and continue
            t = xs[j]
            xs[j] = xs[j+1]
            xs[j+1] = t
            
    


if __name__ == '__main__':
    arr = [random.randrange(0,100) for i in range(100) ]
    insert_sort(arr) 
    for i,v in enumerate(arr):
        print i, v