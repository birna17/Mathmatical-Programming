from itertools import permutations
from sympy.combinatorics.partitions import Partition 
from sympy.combinatorics.permutations import Permutation 
from math import factorial
from sympy import *

def Permutations(n):
    return permutations(list(range(1, n+1)))
#Problem 1(5 points).
# Implement a functionm4p1(p)which counts the numberof inversions for a given permutationp.
# •Input:m4p1([2,4,1,5,3])  •Output:4
def m4p1(p):
    '''Output the number of inversions
    '''
    permL = [i for i in p]
    n = len(permL)
    return inv_count(p, len(p))
def inv_count(p, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (p[i] > p[j]):
                count += 1
    return count
        
def m4p2(p):
    '''Return the number of descents
    '''
    des_count = 0
    for i, val in enumerate(p):
        pair = p[i:i+2]
        if len(pair) >= 2 and pair[0] > pair[1]:
            des_count += 1
    return des_count
            

mp = {}
def m4p3(n):
    '''Return the number of permutations that have the same amount of inversions and descents
    '''
    if n in mp: return mp[n]
    if n in [1,2]: return n
    mp[n] = m4p3(n-1) + m4p3(n-2)
    return mp[n]


# import itertools as it
# for x in it.permutations([l1, .. ln]):
#     print(x)
m = {}
def m4p4(p, cl):
    '''Input True if the permutation p contains the classical pattern cl
    ''' #    print(m4p4((1,5,2,4,3), (3,1,2)))
    if cl in m: return m[cl]
    if cl in p: return cl
    m[cl] = m4p4(p, cl[-1]) + m4p4(p, cl[-2])
    if m[cl] in p: return True
    return False


    
    # p_set = set((permutations(p)))

    # for i in range(len(cl)+1):
    #     for j in range(i,len(cl)+1):
    #         print(cl[i:j])
    # sub_p = set(subsets(p,len(cl),repetition=False))
    # for t in sub_p:
    #     if t in sub_p:
    #         return True
    

def m4p5(p):
    '''Return the permutation after one pass with bubble-sort
    '''  
    pl = [i for i in p]
    for i in range(1,len(p)):
        if pl[i] < pl[i-1]:
            tmp = pl[i-1]
            pl[i-1] = pl[i]
            pl[i] = tmp
    return tuple(pl)
    # return bubblesort(pl)

def bubblesort(pl):
    for num in range(len(pl)-1,0):
        for i in range(num):
            if pl[i] > pl[i+1]:
                tmp = pl[i]
                pl[i] = pl[i+1]
                pl[i+1] = tmp
    return pl


def m4p6():
    '''Return the correct classical patterns
    '''
    


def m4p7(p):
    '''Return the standardization of p
    '''
    return None

mpp = {}
def m4p8(L):
    '''Return the classical patterns the permutaions in L avoid, if possible. Otherwise False
    # '''
    return None



if __name__ == "__main__":
    # print(m4p1([2,4,1,5,3]))
    # print(m4p2([2,4,1,5,3]))
    # print(m4p2([23, 15, 16, 19, 4, 9, 24, 5, 20, 7, 26, 27, 18, 3, 12, 17, 11, 2, 22, 8, 25, 14, 6, 10, 13, 1, 21],))
    print(m4p3(4))
    # print(m4p4((1,5,2,4,3), (3,1,2)))
    print(m4p5((5,3,2,6,1,4)))
    # print(m4p6())
    # print(m4p7((1,3,7,5)))
    # print(m4p8({(4, 1, 2, 3), (1, 3, 2), (3, 4, 1, 2), (1, 3, 4, 5, 2), (2, 1), (1, 4, 2, 3), (3, 1, 4, 5, 2), (2, 3, 1), (2, 4, 1, 3), (1, 2), (2, 1, 3, 4), (2, 3, 1, 4, 5), (3, 1, 4, 2), (1,), (2, 3, 4, 1, 5), (1, 5, 2, 3, 4), (3, 4, 1, 2, 5), (2, 3, 1, 5, 4), (2, 3, 5, 1, 4), (1, 4, 5, 2, 3), (5, 1, 2, 3, 4), (2, 3, 4, 5, 1), (2, 1, 3, 4, 5), (3, 1, 2), (3, 5, 1, 2, 4), (1, 2, 4, 5, 3), (2, 1, 4, 5, 3), (1, 2, 3, 5, 4), (1, 2, 5, 3, 4), (2, 1, 3, 5, 4), (2, 1, 5, 3, 4), (1, 2, 3, 4, 5), (4, 1, 2, 5, 3), (4, 1, 5, 2, 3), (1, 3, 4, 2), (1, 2, 3), (1, 2, 4, 3), (3, 1, 2, 4), (2, 1, 3), (4, 1, 2, 3, 5), (2, 4, 1, 5, 3), (2, 3, 1, 4), (2, 4, 5, 1, 3), (1, 2, 3, 4), (3, 1, 2, 5, 4), (3, 1, 5, 2, 4), (3, 1, 2, 4, 5), (3, 4, 1, 5, 2), (3, 4, 5, 1, 2), (2, 5, 1, 3, 4), (4, 5, 1, 2, 3), (2, 3, 4, 1), (2, 1, 4, 3)}))
