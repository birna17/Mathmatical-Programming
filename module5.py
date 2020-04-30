# ----- Bernie ------
# ----- STFO ------
import sympy
from sympy.abc import x, y
import pulp
import math
def example():
    p = pulp.LpProblem("Example", pulp.LpMaximize)
    goods = ['m','h','c','o','g']
    worth = [200,50,300,250,200]
    vol = [3,1,5,4,3.5]
    amount = [4,7,2,9,11]
    
    v = pulp.LpVariable.dicts("v", goods, lowBound=0, cat="Integer")
    # We want to maximize this:
    p += pulp.lpSum( worth[i]*v[goods[i]]
                    for i in range(len(goods)) )
    # We are constrained by how much we have of each:
    for i in range(len(goods)):
        p += v[goods[i]] <= amount[i]
    # And we are constrained by the space in the truck:
    p += pulp.lpSum( vol[i]*v[goods[i]] for i in range(len(goods)) ) <= 10
    print(p)
    p.solve()
    print("Status: {}".format(pulp.LpStatus[p.status]))
    print("Answer: {}".format(pulp.value(p.objective)))
    print("-------------------------------")
    print("How much of each:")
    for variable in p.variables():
        print("{} = {}".format(variable.name, variable.varValue))

def m5p1(G):
    '''Return the size of the largest clique
    '''  
    
    p = pulp.LpProblem('Maximum Clique', pulp.LpMaximize)
    goods = [i for i in G.keys()]
    v = pulp.LpVariable.dicts('v',goods,lowBound=0,upBound=1,cat='Binary')
    n = len(goods)
    # we want to maximize:
    p += pulp.lpSum((v[goods[i]]) for i in range(n)) 
    # constrains 

    #solve
    print(p)
    p.solve()
    print("Status: {}".format(pulp.LpStatus[p.status]))
    print("Answer: {}".format(pulp.value(p.objective)))
    for variable in p.variables():
        print("{} = {}".format(variable.name, variable.varValue))

    return int(pulp.value(p.objective))

def m5p2(G):
    '''Return the size of the largest independent set
    '''
    p = pulp.LpProblem('Largest Indipendent', pulp.LpMaximize)
    ves = [i for i in G.keys()]
    n = len(ves)
    # print(ves)
    # vess = (i for i in list(ves))
    v = pulp.LpVariable.dicts('v',ves,lowBound=0,upBound=1,cat='Binary')
    # print(v)
    # want to maximize
    p += pulp.lpSum((v[ves[i]]) for i in range(n)) 
    # for i in range()
    
    # for i in vess:
    #     max = vess.count(len(i))
    # p+=max
    # constraint:
    # p += v.isMIP
    print(p)
    p.solve()
    print("Status: {}".format(pulp.LpStatus[p.status]))
    # print("Answer: {}".format(pulp.value(p.objective)))

def m5p3(U, S):
    '''Return the lowest number of subsets from S to cover U
    '''
    return None

def m5p4(xmin, xmax, ymin, ymax):
    return lambda x,y: (xmin <= x <= xmax) and (ymin <= y <= ymax)

def m5p5(x0,y0,r):
    return lambda x,y: ((x0-r) <= x <= (x0+r)) and ((y0-r) <= y <= (y0+r))

def m5p6(x0,y0,r):
    return lambda x,y: (math.sqrt((x-x0)**2 + (y-y0)**2) <= r)

from random import uniform
def hits(P, n=1000, xmin=-1, xmax=1, ymin=-1, ymax=1):
    print(P)
    out = []
    for i in range(n):
        x = uniform(xmin, xmax)
        y = uniform(ymin, ymax)
        if P(x, y):
            out.append((x, y))
    return out


def area_approx(P, n, xmin, xmax, ymin, ymax):

    hit_count = hits(P, n, xmin, xmax, ymin, ymax)

    area = (xmax-xmin) * (ymax - ymin)

    est_area = (len(hit_count)/n) * area

    return (est_area)


def m5p7(P, n=10000, xmin=-1, xmax=1, ymin=-1, ymax=1):
    return area_approx(P, n, xmin, xmax, ymin, ymax)


def P_mp8(f, x, y,z, xmin, xmax, ymin, ymax, zmax):
    return lambda x,y,z: (xmin <= x <= xmax) and (0 <= y <=ymax) and (0 <= z <= zmax)

# def P_mp8(f, x, y, xmin, xmax, ymin, ymax, zmax):
#     z = f.subs({'x': x, 'y' : y})
#     return lambda x,y,z: (xmin <= x <= xmax) and (0 <= y <=ymax) and (0 <= z <= zmax)

def hits3D(P, f, n=10000, xmin=-1, xmax=1, ymin=-1, ymax=1, zmax=1):
    out = []
    for i in range(n):
        xc = uniform(xmin, xmax)
        yc = uniform(ymin, ymax)
        zc = f.subs({'x': xc, 'y' : yc})
        if P(xc, yc, zc):
            out.append((xc, yc, zc))
    return out
    
def m5p8(f, n=10000, xmin=-1, xmax=1, ymin=-1, ymax=1, zmax=1):

    f = sympy.sympify(f)
    z = f.subs({'x': x, 'y' : y})

    P = P_mp8(f, x, y,z, xmin, xmax, ymin, ymax,zmax)

    # print(f)
    area = abs(xmax-xmin) * abs(ymax - ymin) * zmax
    # area = abs(xmax-xmin) * abs(ymax-max(ymin, 0)) * zmax
    # print(area)
    hit_count = hits3D(P,f, n, xmin, xmax, ymin, ymax, zmax)
    # print(len(hit_count))

    est_area = (len(hit_count)/n) * area

    return round((est_area), 1)

if __name__ == "__main__":
    # Linear programming example
    # example()
    
    # G = {0:{1,2},1:{0,2},2:{0,1}}
    # print(m5p1(G))
    # G = {0:set(), 1:{4}, 2:set(), 3:set(), 4:{1}}
    # print(m5p2(G))
    # U = {1, 2, 3, 4, 5}
    # S = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
    # print(m5p3(U, S))
    
    # print(m5p4(1,2,3,4))
    # print(m5p5(2,3,4))
    #print(m5p6(2,3,4))
    # fu = m5p6(0,0,1)
    # print(fu(0,1))
    # print(m5p7(m5p6(0,0,1)))
    f = x**2 + y**2
    print(m5p8(f, 1000, -1, 1, -1, 1, 1))