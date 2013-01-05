'''
Created on Dec 30, 2012

@author: keving
'''
import random


## Returns an array with a random permutation of the integers 0..n-1
def shuffle(n):
    arr = [0]
    for i in range(1,n):
        # extend array
        arr.append(-1)
        # pick a random entry in existing array and move to the
        # end, replace with next index 
        j = random.randint(0,i)
        arr[i] = arr[j]
        arr[j] = i
    return arr        

def printarr(arr,n=None):
    if not n:
        n = len(arr)
    for i in range(0,n):
        print arr[i],  
    print      
    
if __name__ == '__main__':
    arr = shuffle(10)

    printarr(arr)
