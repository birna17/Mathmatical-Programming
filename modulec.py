import math
import sympy
import numpy
import matplotlib

# Write a functionmCp1(x,y)that given two vectorsxandyof the same length,
# computes the Euclidean distance betweenxandy.
# Input: x = (1,2,3)y = (0,-1,0.5)
# Run: mCp1(x,y)Output: 4.03

def mCp1(x,y):
    eu_dis = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x,y)]))
    return eu_dis

def mCp2(x,y):
    man_dis = sum([(abs(a-b)) for a, b in zip(x,y)])
    return man_dis

def mCp3(x, y):
    '''Return the Hamming distance between x and y
    '''
    ham_dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            ham_dist += 1
    return ham_dist

def mCp4(x, y):
    '''Return the Levenshtein distance between x and y
    '''
    lev_dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            lev_dist += 1
    return lev_dist

def mCp5(x, y):
    '''Return the rank distance of the matrices constructed from x and y
    '''
    dim_x, dim_y = math.sqrt(len(x)), math.sqrt(len(y))
    xm = [[[0] for i in range(int(dim_x))]]
    # rankar inni fallinu 
    print(xm)
    return 

def mCp6(L):
    '''Check whether L satisfies the axiom of neighborliness w.r.t the Hamming distance
    '''
    return None

def mCp7(L, J):
    '''Use the labeled points in L to label the points in J using the nearest neighbor in the Hamming distance
    '''
    return None

def mCp8(L, J, k):
    '''Use the labeled points in L to label the points in J using the k nearest neighbors in the Hamming distance
    '''
    return None


if __name__ == "__main__":

    # x = (1,2,3)
    # y = (0,-1,0.5)
    # print(mCp1(x, y))
    # print(mCp2(x, y))

    x = (1,0,1,0)
    y = (1,1,0,1)
    print(mCp3(x, y))
    print(mCp4(x, y))

    x = (1,0,1,1,1,1,0,0,1)
    y = (1,17,1,0,0,1,0,1,1)
    print(mCp5(x, y))

    L = [ ( (1,1,1), 2),
        ( (0,0,0), 1),
        ( (1,0,1), 2),
        ( (0,0,-1), 1) ]
    print(mCp6(L))

    J = [ (1,1,0) ]
    print(mCp7(L, J))

    k = 2
    print(mCp8(L, J, k))