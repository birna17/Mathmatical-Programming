# -*- coding: UTF-8 -*-
import math
from sympy import *

def m3p1(L):
    '''Output the center of gravity for the List of tuples L
    '''
    sum_x = 0
    sum_y = 0
    count = 0
    for i in L:
        count+=1
        x = i[0]
        y = i[1]
        sum_x += x
        sum_y += y
    return sum_x/count , sum_y/count


def m3p2(p,q):
    '''Calculate the Euclidean distance between p and q. As a float rounded to 2 decimal places
    '''
    x1 = p[0]
    x2 = q[0]
    y1 = p[1]
    y2 = q[1]

    x = ((x2-x1)**2)+((y2-y1)**2)
    return round(math.sqrt(x),2)

def m3p3(p,q):
    '''Calculate the Manhattan distance between p and q. As a float rounded to 2 decimal places
    '''
    x1 = p[0]
    x2 = q[0]
    y1 = p[1]
    y2 = q[1]

    x = float(round(abs(x1-x2)+abs(y1-y2)))

    return x
        
def m3p4(sites, gridsize, B, f = 1/2, g = 1, d = m3p3):
    '''Write a function that implements Rossmo's equation. Note that we
give default values for the inputs f, g and d. The input sites should be a list
of sites of interest, gridsize is a tuple giving the size of the grid and B is an
integer giving the size of the buffer zone.
    '''
    M = [[0 for i in range(gridsize[0])] for j in range(gridsize[1])]
    for x in range(len(M)):
        for y in range(len(M)):
            for s in sites:
                d = m3p3((x,y), s)
                if d > B:
                    M[x][y] += (1/d**f)
                else:
                    M[x][y] += ((1-0)*B**(g-f))/(((2*B)-d)**g)
    
    m = [[round((num),2) for num in i] for i in M]
    return m

def m3p5(sites, gridsize, B):
    '''Write a function m3p5(sites, gridsize, B) that finds a cell
(or cells) in the matrix m3p4(sites, gridsize, B) with the highest Rossmo value.
    '''
    #brute force
    m = m3p4(sites, gridsize, B)
    mx = max(row for row in m)
    return set([i for i in mx])    

    # M = m3p4(sites, gridsize, B)
    # m = set()
    # for x, i in enumerate(M):
    #     for y, j in enumerate(M):
    #         if max(i):
    #             m.add((x,y))
    # return m
    # for i in range(len(M)):
    #     i_row = 0
    #     max_row = max(M[i])
    #     for row in range(len(M)):
    #         if max(M[row]) > max_row:
    #             max_row = max(M[row])
    #             i_row = row
    # for j in range(len(M)):
    #     i_col = 0
    #     max_col = max(M[j])
    #     for col in range(len(M)):
    #         if max(M[col]) > max_col:
    #             max_col = max(M[col])
    #             i_col = col
    # m.add((row, col))


import itertools
from itertools import permutations

def m3p6():
    '''Write a function m3p6() that outputs the optimal stackings for player one of Kuhn poker.
    '''
    cards = ['J','Q','K']
    perm = itertools.permutations(cards)

    opt = set()
    for i in cards:
        for j, card in enumerate(perm):
            if card[0]:
                if card[0] == 'K':
                    s = ''
                    s+=str(card[0]+card[1]+card[2])                
                    opt.add(s)
                elif card[0] == 'Q' and card[1] == 'J':
                    s = ''
                    s+=str(card[0]+card[1]+card[2])                
                    opt.add(s)
            elif card[1]:
                if card[1] == 'K':
                    opt.add('K'+str(card[2]+str(card[0])))
                if card[1] == 'Q' and card[2] == 'J':
                    opt.add(str(card[1])+str(card[2])+str(card[0]))
    return opt

def m3p7(k):
    '''Write a function m3p7(k) that outputs the optimal stackings for player one of K poker.
        The cards in the deck range from 2 to k, one of each value. 
        Again, to avoid redundancy only list the cut of an optimal deck that starts with 2.
    '''
    cards = ['J','Q','K']
    for c in range(2, k+1):
        pass
    return None


if __name__ == "__main__":
    richardChaseSites = [(17,3), (3,15), (27,19), (22,21), (18,25)]
    print(m3p1(richardChaseSites))
    
    # p, q = ((11.0, 27.0), (24.0, 17.0))
    # print(m3p2(p, q))
    # print(m3p3(p, q))
    
    # sites = [(0, 0), (2, 2)]
    # gridsize = (3, 3)
    # B = 1
    # print(m3p4(sites, gridsize, B))
    print(m3p5([(16, 15), (29, 6), (15, 16), (26, 23), (23, 19), (4, 25), (23, 28), (14, 18), (20, 12)], (30, 30), 8))

    # print(m3p6())
    # print(m3p7(10))
