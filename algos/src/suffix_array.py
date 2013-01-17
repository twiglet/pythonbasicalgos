'''
Created on Dec 30, 2012

@author: keving

Algorithms follow those in Skiena's The Algorithm Design Manual, 2nd Ed
'''
from random import randrange, seed
from collections import deque


def mk_suffix_array(s):
    sa = []
    for i in range(len(s)):
        sa.append((s[i:], i))
    sa.sort()
    return sa
            
            
def find_in_suffix_array(p, sa):
    lo = 0
    hi = len(sa)-1
    # loop assertion: forall i, sa[i].startswith(p) p  then lo <= i <= hi
    while hi >= lo:
        mid = lo + ((hi - lo) // 2)
        print mid
        if sa[mid][0].startswith(p):
            return sa[mid][1]
        elif sa[mid][0] > p:
            hi = mid - 1
        else:
            lo = mid + 1
    return None

def print_substrings(str, pats):

    sa = mk_suffix_array(str)
    print sa
    for p in pats:
        pos = find_in_suffix_array(p, sa)
        if pos != None:
            print p, "found at", pos
        else:
            print p, "not found"
            


if __name__ == '__main__':
    
    print_substrings("hello world", ["fred", "llo", "d"])