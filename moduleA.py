# Havar18 - Birna17
#STFO
#University of Reykjavík

# -*- coding: UTF-8 -*-


def is_alive(A, cell):
    if A[cell[0]][cell[1]] == 1:
        return True
    return False

def check_neighbors(A, cell):
    alive = 0
    x_c = cell[0]
    y_c = cell[1]
    cords = (-1, 0, 1)

    for x in cords:
        for y in cords:
            if x_c+x >= 0 and y_c+y >= 0:
                try:
                    if A[x_c+x][y_c+y] == 1: alive += 1
                except:
                    pass

    if is_alive(A, cell) and alive > 0:  alive -= 1

    return alive

def check_neighbors_torus(A, cell):
    alive = 0
    x_c = cell[0]
    y_c = cell[1]
    cords = (-1, 0, 1)
    dim = len(A)

    for x in cords:
        for y in cords:
            if A[(x_c+x)%dim][(y_c+y)%dim] == 1: alive += 1

    if is_alive(A, cell) and alive > 0:  alive -= 1

    return alive

def check_neighbors_klein(A, cell):
    alive = 0
    x_c = cell[0]
    y_c = cell[1]
    cords = (-1, 0, 1)
    dim = len(A)-1

    for x in cords:
        for y in cords:
            if x_c+x == dim+1:
                if A[0][dim-(y_c)] == 1: 
                    alive += 1
                    break
            if x_c+x == -1:
                if A[dim][dim-(y_c)] == 1: 
                    alive += 1
                    break
            # if x_c <= dim and x_c >= 0:
            #     try:
            #         if A[x_c+x][y_c+y] == 1: alive += 1
            #     except:
            #         pass
            # if x_c+x > dim:
            #     if A[(dim-x_c+x)][(y_c+y)%dim] == 1: alive += 1
            # if x_c+x < 0:
            #     if A[(dim-x_c+x)][(y_c+y)%dim] == 1: alive += 1

    if is_alive(A, cell) and alive > 0:  alive -= 1

    return alive

def next_state(A, cell):
    alive = is_alive(A, cell)
    neighbors = check_neighbors(A, cell)
    if alive and neighbors < 2:
        return 0
    if alive  and neighbors >= 4:
        return 0
    if alive and (neighbors == 2 or neighbors == 3):
        return 1
    if not alive and neighbors == 3:
        return 1
    return 0

def next_state_torus(A, cell):
    alive = is_alive(A, cell)
    neighbors = check_neighbors_torus(A, cell)
    if alive and neighbors < 2:
        return 0
    if alive  and neighbors >= 4:
        return 0
    if alive and (neighbors == 2 or neighbors == 3):
        return 1
    if not alive and neighbors == 3:
        return 1
    return 0

def next_state_klein(A, cell):
    alive = is_alive(A, cell)
    neighbors = check_neighbors_klein(A, cell)
    if alive and neighbors < 2:
        return 0
    if alive  and neighbors >= 4:
        return 0
    if alive and (neighbors == 2 or neighbors == 3):
        return 1
    if not alive and neighbors == 3:
        return 1
    return 0


def mAp1(A,c):
    '''Output the state of the cell after one iteration
    '''
    return next_state(A, c)

def mAp1_torus(A,c):
    '''Output the state of the cell after one iteration
    '''
    return next_state_torus(A, c)

def mAp1_klein(A,c):
    '''Output the state of the cell after one iteration
    '''
    return next_state_klein(A, c)

def mAp2(A):
    '''Output the state of the matrix after one iteration
    '''
    new_state = [[0 for x in range(len(A))] for j in range(len(A[1]))]

    for x in range(len(A)):
        for y in range(len(A[0])):
            new_state[x][y] = mAp1(A, (x,y))
            
    return new_state

def mAp2_torus(A):
    '''Output the state of the matrix after one iteration
    where world is torus
    '''
    new_state = [[0 for x in range(len(A))] for j in range(len(A[1]))]

    for x in range(len(A)):
        for y in range(len(A[0])):
            new_state[x][y] = mAp1_torus(A, (x,y))
            
    return new_state

def mAp2_klein(A):
    '''Output the state of the matrix after one iteration
    where world is torus
    '''
    new_state = [[0 for x in range(len(A))] for j in range(len(A[1]))]

    for x in range(len(A)):
        for y in range(len(A[0])):
            new_state[x][y] = mAp1_klein(A, (x,y))
            
    return new_state

def mAp3(A,k):
    '''Output the state of the matrix after k iterations
    '''
    state = A

    for i in range(k):
        state = mAp2(state)

    return state


mp = {}
def mAp4(A,k):
    '''Output the state of the matrix after k iterations,
doing as little work as possible
    '''
    if k == 0: return A
    a = (i for i in A)
    if (a,k) in mp: return mp[(a,k)]
    mp[(a,k)] = mAp4(mAp2(A), k-1)
    return mp[(a,k)]

def mAp5():
    '''Output 10 different states which remain unchanged
    '''
    st1 = [[1,1,0],[1,1,0],[0,0,0]]
    st2 = [[0,0,0],[0,0,0],[0,0,0]] #all ded
    st3 = [[0,1,1,0,0],[1,0,0,1,0],[0,1,0,0,1],[0,0,1,1,0],[0,0,0,0,0]]
    st4 = [[1,1],[1,1]] #block
    st5 = [[0,1,1,0],[1,0,0,1],[0,1,1,0],[0,0,0,0]] #beehive
    st6 = [[0,1,1,0],[1,0,0,1],[0,1,0,1],[0,0,1,0]] #loaf
    st7 = [[1,1,0],[1,0,1],[0,1,0]]
    st8 = [[0,1,0],[1,0,1],[0,1,0]]
    st9 = [[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]
    st10 = [[1,1,0,0], [1,0,0,1],[0,0,1,1], [0,0,0,0]]

    return [st1,st2,st3,st4,st5,st6,st7,st8,st8,st9,st10]

def mAp6():
    '''Output 2 states which return to them selves after at most 5 iterations
    '''
    blinker = [[0,1,0],[0,1,0],[0,1,0]]
    glider = [[0,0,0],[1,1,1],[0,0,0]]
    return [blinker, glider]

def mAp7(A,k):
    '''Output the state of the matrix after k iterations if the
universe is a torus
    '''
    state = A

    for i in range(k):
        state = mAp2_torus(state)

    return state

def mAp8(A,k):
    '''Output the state of the matrix after k iterations if the
universe is a Klein bottle
    '''
    state = A

    for i in range(k):
        state = mAp2_klein(state)

    return state

if __name__ == "__main__":

    # print(mAp1([[1,0,1,0],
    #             [0,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]],
    #             (1,1)))


    # print(mAp2([[1,0,1,0],
    #             [0,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]]))
    # print(mAp3([[1,0,1,0],
    #             [0,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]], 3))

    #print(mAp3([[0, 0, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 1]], 8))
    # print(mAp4([[1,0,1,0],
    #             [0,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]], 2))
    # print(mAp5())
    # print(mAp6())
    # print(mAp7([[1,0,1,0],
    #             [0,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]], 1))

    # print(mAp7([[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1], [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1]], 10))
    # print(mAp8([[1,0,1,0],
    #             [0,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]], 1))
    print(mAp8([[0, 0, 1], [1, 0, 1], [0, 1, 1]], 72))
