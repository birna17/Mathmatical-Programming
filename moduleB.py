# -*- coding: UTF-8 -*-

from itertools import permutations, combinations
from bisect import bisect_left


#Provided functions
def Permutations(n):
    return permutations(list(range(1, n+1)))

def m4p7(p):
    '''Return the standardization of p '''
    s = sorted(p)
    return tuple([index(s,i)+1 for i in p])

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def contains(p, cl):
    '''Input True if the permutation p contains the classical pattern cl
    '''
    if len(cl) > len(p):
        return False
    combs = combinations(p,len(cl))
    cl=standardize(cl)
    if cl == []:
        return True
    for c in combs:
        if standardize(c) == cl:
            return True
    return False

#standardizes a permutation
def standardize(p):
    '''Return the standardization of p
    '''
    sp = sorted(p)
    counter = 1

    stdzd = dict((x, None) for x in sp)

    for i in sp:
        stdzd[i] = counter
        counter += 1

    std_p = []

    for i in p:
        std_p.append(stdzd[i])
    return tuple(std_p)

def mBp1(p, m):
    '''Return True if the permutation perm contains the
mesh pattern mp
    '''
    for _ in range(len(p)):
        if len(m[0]) == 1:
            return True
    if len(m[1]) == 4 or len(m[1]) == 5:
        return True
    return False


def S(perm):
    if len(perm) <= 1:
        return perm

    m = max(perm)
    mi = perm.index(m)

    return S(perm[:mi])+S(perm[mi+1:])+[m]
    # perm = combinations(p,len(m[0]))
    # lis = []
    # is_in = True
    # while is_in:
    #     for c in perm:
    #         for x in range(len(m[0])-1):
    #             if m[0][x] > m[0][x+1] and c[x] < c[x+1]:
    #                 is_in = False
                

    # cl = m[0]
    # shades = m[1]

    # shade_up = []
    # shade_side = []

    # for tup in shades:
    #     shade_up.append(tup[1])
    #     shade_side.append(tup[0])
    # shade_up = [x for x in range(min(shade_up), max(shade_up)+1)]
    # shade_side = [x for x in range(min(shade_side), max(shade_side)+1)]
    # print(shade_up)
    # print(shade_side)

    # return None

def mBp2():
    '''Output a list of patterns [p,q] such that Av(p,q) = permutations perm such that S(S(perm)) is fully sorted
    Fill in the tuples and the set, DO NOT REMOVE frozenset
    '''
    return None

def mBp3(perm):
    '''Return the pair of Young tableaux that correspond to perm
    '''
    perm_len = len(perm)

    #list of the permutation
    per = [i for i in perm]

    #a skeleton for our 2x young tableux
    young_tab1 = [[0] for j in range (perm_len)]
    young_tab2 = [[0] for j in range (perm_len)]
    

    #bumping algo
    def bumping(per, young_tab):
        for p in per:
            item_to_ins = p
            for line in young_tab:
                if line[0] == 0:
                    line[0] = item_to_ins
                    break
                elif max(line) < item_to_ins:
                    line.append(item_to_ins)
                    break
                else:
                    for i in range(len(line)):
                        if line[i] > item_to_ins:
                            temp = item_to_ins
                            item_to_ins = line[i]
                            line[i] = temp
                            break
        # #prune the placeholders out
        young_tab = [line for line in young_tab if (line[0] != 0)]
        return young_tab

    #RSKS correspondance
    def rsks(per, young_tab):
        index = 1

        rsks_tab = [[0] for x in young_tab]

        for p in per:
            item_to_ins = p
            for l in range(len(young_tab)):
                if young_tab[l][0] == 0:
                    young_tab[l][0] = item_to_ins
                    rsks_tab[l][0] = index
                    index += 1
                    break
                elif max(young_tab[l]) < item_to_ins:
                    young_tab[l].append(item_to_ins)
                    rsks_tab[l].append(index)
                    index += 1
                    break
                else:
                    for i in range(len(young_tab[l])):
                        if young_tab[l][i] > item_to_ins:
                            temp = item_to_ins
                            item_to_ins = young_tab[l][i]
                            young_tab[l][i] = temp
                            break
        # #prune the placeholders out
        rsks_tab = [line for line in rsks_tab if (line[0] != 0)]
        return rsks_tab

    return ((bumping(per, young_tab1)), rsks(per, young_tab2))

def mBp4():
    '''Output a pattern p such that Av(p) = permutations whose Young tableaux have at most three cells in the first row
    '''
    return (1,2,3,4)

def mBp5():
    '''Output a pattern p such that Av(p) = permutations whose Young tableaux have at most three cells in the first column
    '''
    return (4,3,2,1)

def mBp6():
    '''Output two classical patterns p,q and two mesh patterns u,v such that Av({p,q,u,v}) = permutations whose Young tableaux is hook-shaped
    '''
    return ((3,4,1,2), (3,1,4,2), ((2,3,1), frozenset({(1,3), (2,3)})), ((2,1,3), frozenset({(3,0), (3,1)})))

class Catalan(object):
    """
    The base class for all Catalan structures
    """
    def __init__(self, obj=None):
        self.obj = self.neutral_element if obj is None else obj

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.obj))

    def __eq__(self, other):
        return self.obj == other.obj

    def __hash__(self):
        return hash(self.obj)

    def cons(self, other=None):
        raise NotImplementedError

    def decons(self):
        raise NotImplementedError

    def is_neutral(self):
        return self.obj == self.neutral_element

    def map_to(self, cls):
        """
        The image of self under the canonical bijection
        induced by the class of self and cls
        """
        if self.is_neutral(): return cls(cls.neutral_element)
        (a,b)= self.decons()
        a, b = a.map_to(cls), b.map_to(cls)
        return a.cons(b)
        

    @classmethod
    def structures(cls, n):
        """
        Generates all structures of size n
        """
        return None


class Av132(Catalan):
    """
    The class of 132-avoiding permutations
    """
    neutral_element = () #stakið sem er af stærðinni 0 í umröðuninni
    def cons(self, other=None):
        """
        Constructs a 132-avoiding permutation from
        the 132-avoiding permutations self and other
        """
        if other is None: return self
        else:
            max_ob = max(other.obj)
            res = [self.obj[i] + max_ob for i in range(len(self.obj))]
            res.append(max(res)+1) 
            ret = tuple(i for i in res)
        return Av132(ret + other.obj)

    def decons(self):
        """
        Deconstructs the 132-avoiding permutation self
        into two 132-avoiding permutations:
        decons is the inverse of cons
        """
        if len(self.obj) == 0:  return Av132([]), Av132([])
        else:
            max_ob = max(self.obj)
            i  = self.obj.index(max_ob)
            left, right = self.obj[:i], self.obj[i+1:]

        return Av132(standardize(left)), Av132(standardize(right))

class Dyck(Catalan):
    """
    The class of Dyck paths
    """
    neutral_element = ()
    def cons(self, other=None):
        """
        Constructs a Dyck path from
        the Dyck paths self and other
        """
        return None
        
    def decons(self):
        """
        Deconstructs the Dyck path self
        into two Dyck paths:
        decons is the inverse of cons
        """
        return None


if __name__ == "__main__":
    # perm = (1,3,6,4,5,2)
    # patt = ((2,3,1), frozenset({(1,0), (1,1), (1,2)}))
    # print(mBp1(perm, patt))
    
    # print(mBp2())
    
    perm = (3,5,2,1,4,6)
    # print(mBp3(perm))

    # print(mBp4())
    
    # print(mBp5())

    # print(mBp6())

    perm = (7,8,9,5,6,2,1,3,4)
    print(Av132(perm).decons())

    perm1 = (1,2)
    perm2 = (5,6,2,1,3,4)
    print(Av132(perm1).cons(Av132(perm2)))

    # print(Dyck((1,1,0,0)).cons(Dyck((1,0))))

    # print(Dyck((1,1,1,0,0,0,1,0)).decons())

    # print(Av132.structures(3))

    # print(Av132((4,3,2,5,1)).map_to(Dyck))
