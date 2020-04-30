####################################################################
#Havar18
#STFO
#University of Reykjavík

from itertools import permutations
import math
from sympy import *


def mCp1(x,y):
    '''Return the Euclidean distance between x and y
    '''
    dist = 0

    for i in range(len(x)):
        dist += abs(x[i]-y[i])**2


    return math.sqrt(dist)


def mCp2(x, y):
    '''Return the Manhattan distance between x and y
    '''
    dist = 0

    for i in range(len(x)):
        dist += abs(x[i]-y[i])

    return dist

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
        try:             
            if (x[i] != y[i]) and (x[i+1] != y[i+1]):
                    lev_dist += 1
                    i +=1
            else:
                if x[i] != y[i]:
                    lev_dist += 1
        except:
            if x[i] != y[i]:
                lev_dist += 1    
            
    return lev_dist

def mCp5(x, y):
    '''Return the rank distance of the matrices constructed from x and y
    '''
    dim = sqrt(len(x)) #size of matrix

    xm = []
    ym = []

    index = 0
    for i in range(0,dim):
        xrow, yrow = [], []
        for j in range(0, dim):
            xrow.append(x[index])
            yrow.append(y[index])
            index += 1
        xm.append(xrow)
        ym.append(yrow)

    xm = Matrix(xm)
    ym = Matrix(ym)

    zm = xm-ym

    return zm.rank()

def find_nearest_neighbor(c, L):
    pass

def mCp6(L):
    '''Check whether L satisfies the axiom of neighborliness w.r.t the Hamming distance
    '''

    COORDS = 0
    LABEL = 1
    num_of_points = len(L)

    if num_of_points == 0: return True
    if num_of_points == 1: return True


    for point in L:
        resemblance = 0
        curr_resemblance = 0
        point_len = len(point)
        nearest = (0,0)
        for i in range(num_of_points):
            curr_resemblance = (point_len - mCp3(point[0], L[i][0]))
            if curr_resemblance == point_len:
                pass
            else:
                if curr_resemblance > resemblance:
                    resemblance = curr_resemblance
                    nearest = L[i]
        print(nearest)
        print(point[1])

        if (nearest[1] != point[1]):
            return False

    return True

    # #create a list of the labels
    # labels = []
    # for i in range(len(L)):
    #     labels.append(L[i][1])
    # labels = sorted(list(set(labels)))
    # print(labels)

    # #create a list of the points on the format [ [point, x] ] where x will be updated to its nearest neigh
    # points = []
    # for pnt in L:
    #     points.append([(pnt[COORDS], pnt[LABEL]), ()])

    # #here we get the nearest neighbor of each points in the form [ [ (point) , (nearest) ], ]
    # for i in range(num_of_points):
    #     dist = 10
    #     for j in range(num_of_points):
    #         if i == j:
    #             pass
    #         else:
    #             # print("dist from " + str(L[i][COORDS]) + " to " + str(L[j][COORDS]) + " is " + str(mCp3(L[i][COORDS], L[j][COORDS])))
    #             curr_dist = mCp3(L[i][COORDS], L[j][COORDS])
    #             if curr_dist < dist:
    #                  points[i][1] = (L[j][COORDS], L[j][LABEL])
    #                  dist = curr_dist

    # print(points)


def mCp7(L, J):
    '''Use the labeled points in L to label the points in J using the nearest neighbor in the Hamming distance
    '''
    COORDS = 0
    LABEL = 1
    num_of_points = len(L)

    ret = []

    if num_of_points == 0: return True
    if num_of_points == 1: return True

    for point in J:
        resemblance = 0
        curr_resemblance = 0
        label_guess = 0
        point_len = len(point)

        for i in range(num_of_points):
            curr_resemblance = (point_len - mCp3(point, L[i][0]))
            if curr_resemblance == resemblance:
                if L[i][1] < label_guess:
                    label_guess = L[i][1]
            if curr_resemblance > resemblance:
                resemblance = curr_resemblance
                label_guess = L[i][1]
        ret.append(((point), label_guess))
        
    return ret

def mCp8(L, J, k):
    '''Use the labeled points in L to label the points in J using the k nearest neighbors in the Hamming distance
    '''
    COORDS = 0
    LABEL = 1
    num_of_points = len(L)

    ret = []

    if num_of_points == 0: return True
    if num_of_points == 1: return True

    def most_frequent(List): 
        return max(set(List), key = List.count) 

    # for point in J:
    #     label_guess = []
    #     point_len = len(point)
    #     nearest_neighs = []
    #     for kth in range(k+1):
    #         resemblance = 0
    #         curr_resemblance = 0
    #         for i in range(num_of_points):
    #             #if we have already added the point as neigh
    #             if L[i][0] in nearest_neighs or (point == L[i][0]):
    #                 pass
    #             else:
    #                 curr_resemblance = (point_len - mCp3(point, L[i][0]))
    #                 if curr_resemblance > resemblance:
    #                     resemblance = curr_resemblance
    #                     label_guess.append(L[i][1])
    #             nearest_neighs.append(L[i][0])

    

    for point in J:
        label_guess = []
        points = [i for i in L]
        point_len = len(point)
        
        for kth in range(k+1):
            curr_resemblance = 0
            resemblance = 0
            for checkpoint in points:
                curr_resemblance = (point_len - mCp3(point, checkpoint[0]))
                if curr_resemblance >= resemblance:
                    resemblance = curr_resemblance
                    label_guess.append(checkpoint[1])
                    points.remove(checkpoint)
        
        # for i in range(num_of_points):
        #         #if we have already added the point as neigh
        #         if L[i][0] in nearest_neighs: # or (point[0] == L[i][0]):
        #             pass
        #         else:
        #             curr_resemblance = (point_len - mCp3(point, L[i][0]))
        #             if curr_resemblance >= resemblance:
        #                 resemblance = curr_resemblance
        #                 label_guess.append(L[i][1])
        #         nearest_neighs.append(L[i][0])
        # ret.append(((point), label_guess))
        
        most_common_label = most_frequent(label_guess)

        ret.append(((point), most_common_label))
        
    return ret


if __name__ == "__main__":

    # x = (1,2,3)
    # y = (0,-1,0.5)
    # print(mCp1(x, y))
    # print(mCp2(x, y))

    # x = (1,0,1,0)
    # y = (1,1,0,1)
    # print(mCp3(x, y))

    x = (0,0,-1)
    y = (1,0,1)
    print(mCp3(x, y))

    print(mCp4(x, y))

    # x = (1,0,1,1,1,1,0,0,1)
    # y = (1,17,1,0,0,1,0,1,1)
    # print(mCp5(x, y))

    # print(mCp5((-15.262457187811947, 64.09152513192561, -15.44149943998596, -83.31531698241115), (-6.536306138077336, 83.31054276779753, -59.41228190638246, 21.77160865316661)))

    # L = [ ( (1,1,1), 2),
    #       ( (0,0,0), 1),
    #       ( (1,0,1), 2),
    #       ( (0,0,-1), 1) ]
    # print(mCp6(L))
    # L = [ ( (0, 1), 7),
    #       ( (0, 0), 5),
    #       ( (1, 1), 1)  ]

    # print(mCp6((L)))

    # L = [((0, 0, 1, 1, 0, 1, 0, 0, 0), 2), ((1, 0, 0, 1, 1, 0, 0, 0, 1), 5), ((0, 0, 1, 0, 0, 0, 1, 0, 1), 6), ((0, 0, 1, 0, 1, 0, 1, 0, 0), 1), ((1, 0, 1, 1, 1, 0, 0, 0, 1), 7)]
    # print(mCp6((L)))
    # J = [ (1,1,0) ]
    # print(mCp7(L, J))
    # L = [ ( (1,1,1), 2),
    # ( (0,0,0), 1),
    # ( (1,0,1), 2),
    # ( (0,0,-1), 1) ]
    # J = [ (1,1,0) ]
    # print(mCp7(L, J))

    # L = [ ( (1,1,1), 2),
    # ( (0,0,0), 1),
    # ( (1,0,1), 2),
    # ( (0,0,1), 1) ]
    # J = [ (1,1,0) ]
    # k = 2
    # print(mCp8(L, J, k))

    # print(mCp8([((0, 1), 7), ((0, 0), 6), ((1, 1), 4)], [(0, 1), (1, 0), (0, 0)], 2))
