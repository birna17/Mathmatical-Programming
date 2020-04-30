# -*- coding: UTF-8 -*-
from sympy import *
from math import gcd
from functools import lru_cache

def miller_rabin(testee, witness):
    n, a = testee, witness
    if n % 2 == 0 or 1 < gcd(a, n) < n:
        return True
    q = n - 1
    k = 0
    while q % 2 == 0:
        q //= 2
        k += 1
    a = pow(a, q, n)
    if a == 1:
        return False
    for i in range(0, k):
        if a == n - 1:
            return False
        a = (a * a) % n
    return True

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    witnesses = [2, 3]
    return not any(miller_rabin(n, w) for w in witnesses)

def primes_upto(N):
    mx = (N-3) >> 1
    sq = 0
    v = 0
    i = -1
    primes = []
    prime = [True] * (mx + 1)
    if N >= 2:
        primes.append(2)
    while True:
        i += 1
        if i > mx:
            break
        if prime[i]:
            v = (i << 1) + 3
            primes.append(v)
            sq = i * ((i << 1) + 6) + 3
            if sq > mx:
                break
            for j in range(sq, mx+1, v):
                prime[j] = False
    while True:
        i += 1
        if i > mx:
            break
        if prime[i]:
            primes.append((i << 1) + 3)
    return primes

# Problems 

def m2p1(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number, using recursion.
    '''
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return m2p1(n-1) + m2p1(n-2) + m2p1(n-3)

memo = {0:0, 1:0, 2:1}
def m2p2(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number, using recursion and memoization.
    '''
    if n < 0: 
        return 0
    if n in memo:
        return memo[n]
    else:
        new_value = memo[n] = m2p2(n-1) + m2p2(n-2) + m2p2(n-3)
        memo[n] = new_value
        return new_value
        

def m2p3(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number using memoization with a list, and without using recursion
    '''
    T = [0,0,1] + [0]*(n-2)

    for i in range(3, n+1):
        T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]

def m2p4(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number, without using recursion and only storing three values.
    '''
    if n <= 1:
        return 0
    t3, t2, t1 = 1, 0, 0
    for _ in range(3, n+1):
        t3, t2 ,t1 = t1+t2+t3 ,t3 ,t2
    return t3

def m2p5(n,L):
    '''Project Euler Problem 31.
The input n is a positive integer and the input L is a list of coin values.
The returned value is the number of ways n can be split using the coin values in the list L.
    '''
    ways = [1] + [0]*n
    for i in L:
        for j in range(i, n+1):
            ways[j] += ways[j-i]
        
    return ways[n]  

def m2p6(k):
    '''Project Euler Problem 76.
The input k should be a positive integer. The returned value is the number of
different ways k can be written as a sum of at least two positive integers.
    '''
    ways = [0] *(k+1)
    ways[0] = 1 #only 1 way to get sum 1
    #ways for sums involving numbers in [1, k]
    for i in range(1, k):
        for j in range(i, k+1):
            ways[j] += ways[j-i]
    return ways[k]

    # ways = [1] + [0]*k
    # for num in range(1,k):
    #     for i in range(num, k+1):
    #         ways[i] += ways[i-k]
    # return ways[k]
    # return (binomial_coefficients_list(k))

def m2p7(k):
    '''Project Euler Problem 77.
The input k should be a positive integer. The returned value is the smallest positive
integer n such that the number of ways to write n as a sum of primes exceeds k
    '''
    #nota coins gaurinn m2p5, n=k og primes = L
    primes = [i for i in primerange(1, k+1)]
    for p in primes:
        n = m2p5(k,primes)
        nm = npartitions(prim)
    return nm
    
    # if k < 0: return 0
    # if k == 0: return 2




    # primes = [i for i in primerange(0,k+1)]
    # for j in range(k):
    #     binomial(k,primes[j])
    #     return m2p5(k,primes)
    

def m2p8(k):
    '''Project Euler Problem 78.
The input k should be a positive integer. The returned value is the smallest positive
integer n such that number of ways n coins can be separated into piles is divisible by k.
    '''
    return -1

def m2p9(M):
    '''Project Euler Problem 81.
The input M should be an n x n matrix containing integers, given as a list of lists.
The output is the minimal path sum, as defined on Project Euler.
    '''
    for i in range(len(M)-2, -1, -1): #sny fylkinu við
        M[len(M)-1][i] += M[len(M)-1][i+1]
        M[i][len(M)-1] += M[i+1][len(M)-1]

    for i in range((len(M))-2, -1, -1): #byrja neðst til hægri og leita upp 
        for j in range((len(M))-2, -1, -1):
            M[i][j] += min(M[i+1][j], M[i][j+1])
    
    return M[0][0] #skila vinstra efsta

if __name__ == "__main__":
    # print(m2p1(8))
    # print(m2p2(8))
    print(m2p3(1000000))
    # print(m2p4(10000))
    # print(m2p5(20,[1,2,5]))
    # print(m2p6(5))
    # print(m2p7(4))
    # print(m2p8(7))
    # print(m2p9([[1,1,9],[9,1,1],[9,9,1]]))
