# -*- coding: UTF-8 -*-
from sympy import *

def factor(n):
    """
    Naive algorithm for prime factorization
    Input: A positive integer n
    Output: A list of all the prime factors of n with repetitions
    Time complexity: O(sqrt(n))
    """
    L = []
    i = 2
    while n % i == 0:
        n //= i
        L.append(i)
    i = 3
    while i*i <= n:
        while n % i == 0:
            L.append(i)
            n //= i
        i += 2
    if n > 1:
        L.append(n)
    return L

def m1p1(n):
    '''Project Euler Problem 1
Given a positive integer n calculate the sum of all multiples of 3 and 5 less than n.
    '''
    ans = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans

def m1p2(n):
    '''Project Euler Problem 2.
Given a positive integer n find the sum of the even valued Fibonacci numbers less than n.
'''
    fibs = [0, 1]
    count = 2 #check even 
    nextfib = 1
    summ = 0
    while nextfib <= n:
        if nextfib % 2 == 0:
            summ += nextfib
        fibs.append(nextfib)
        count += 1
        nextfib = fibs[count-1] + fibs[count-2]
        
    return summ

def m1p3(n):
    '''Project Euler Problem 3.
Given an positive integer n find the largest prime factor of n
    # '''
    # prime_list = [i for i in sieve.primerange(0,n+1)]
    num = primefactors(n)
    return max(num)
    #eða nota primorial(n) , sem skilar lista af ollum prime neðar en n.. 

def m1p4(n):
    '''Project Euler Problem 4.
Given a positive integer n. Find the largest palindrome made from the product of two n digit numbers
    '''
    upper_limit = 10**n
    lower_limit = 10*n//2
    pal_list = [i * j for i in reversed(range(lower_limit, upper_limit)) 
                for j in reversed(range(lower_limit, upper_limit))
                        if str(i*j) == str(i*j)[::-1]]
    return max(pal_list)


def m1p5(n):
    '''Project Euler Problem 5.
    Given a positive integer n. Find the smallest positive number evenly divisible by all numbers from 1 to n
    '''
    divs = range(1,n+1)
    return lcm(divs)
    # divs = [int(i) for i in range(n+1)]    
    # for j in range(1,n+1):
    #     if n <= 0: 
    #         return
    #     if n % j == 0:
    #         return m1p5(n)
        
    # num = r
    # num = factorint(n)
    # smallest = min(num.keys())
    # return smallest

def m1p6(n):
    '''Project Euler Problem 6.
Given a positive integer n. Find the difference between the square of the sum and the sum of the squares of the
first n natural numbers
    '''
    nums = range(1,n+1)
    sum_sq = sum(nums)**2
    sq_sum = sum(list(map(lambda x: x**2, nums)))
    return abs(sq_sum - sum_sq)

def m1p7(n):
    '''Project Euler Problem 7.
Given a positive integer n. Find the nth Prime.
    '''
    if n > 0:
        return prime(n)

def m1p8(n,k):
    '''Project Euler Problem 8.
Given positive integers n and k. Find the greatest product of k adjacent digits in n.
    '''
    #t.d. find the 4 adjecent digits in the 100 digits number, that have the greatest product.
    string = str(k)
    stringLength = len(str(string))
    result = 0

    for i in range(stringLength-n):
        subString = string[i:i+n]
        number = 1
        for j in range(len(subString)):
            number *= int(subString[j])
        
        if number > result:
            result = number
            resultIndex = i
    return result
    # n_str = str(n)
    # for i in range(len(n_str) - n):
    #     digits = n_str[i: i+n]
    #     greatest_prod = prod([int(j) for j in digits])
    #     return greatest_prod

def m1p9(n):
    '''Project Euler Problem 9.
Given a positive integer n. Find a Pythagorean triple such that a+b+c=n
    '''
    a, b, c = symbols('a b c')
    expr = Eq(c**2, a**2 + b**2)
    pprint(expr)
    # c = n // 2
    # for i in range(1,n):
    #     for j in range(1,n):
    #         if i**2 + j**2 == c:
    #             return (i,j,sqrt(c))

def m1p10(n):
    '''Project Euler Problem 10.
Given a positive integer n. Find the sum of all primes less than n.
    '''
    prime_list = primerange(0,n)
    return sum(prime_list)

def m1p11(M,k):
    '''Project Euler Problem 11.
Given a matrix m (as a list of lists) and integer k. Find the greatest product of k vertical, horizontal, or diagonal entries in m.
    '''
    return gcd(prod(n*m))

def m1p12(n):
    '''Project Euler Problem 12.
Given an integer n. Find the smallest triangular number with more than n divisors.
    '''
    if n == 1:
        return 3
    i = 2
    count = 0
    second = 1 
    first = 1
    while n >= count:
        if i % 2 == 0:
            first = divisor_count(i + 1)
            count = first*second
        else:
            second = divisor_count((int(i)+1)// 2)
            count = first*second
        i += 1
    return i * (i -1) // 2

def m1p13(L,k):
    '''Project Euler Problem 13.
Given a list L of integers and an integer k. Find the first k digits of the sum of the elements of L.
    '''
    return 0

def m1p14(n):
    '''Project Euler Problem 14.
Which starting number under n produces the longest Collatz chain.
    '''
    return 0

def m1p15(n,m):
    '''Project Euler Problem 14.
How many paths are there with only steps right and down through an n*m grid.
If you use a mathematical formula as a shortcut in your solution, then justify
why it can be used.
    ''' 
    #This is a classic combination example. To get from the top left corner to the bottom right corner of the m*n,
#it involves making exactly n moves right and then n moves down in some kind of order.
    # num = [bell(i) for i in range(m*n)]
    return factorial(m + n) // factorial(m) // factorial(n)

if __name__ == "__main__":
    # print('Sum of multiples: ' , m1p1(1000))

    print(m1p15(4,4))

    print('sum of Fibonacci less then n: ', m1p2(20))

    print('Largest prime factor: ', m1p3(100))

    # print('Largest palindrome: ', m1p4(2))

    print(m1p5(20))

    # print('Difference between sum_of_sq and sq_sum: ' , m1p6(3))

    # print('nth Prime: ' , m1p7(7))

    print(m1p9(50))
# 
    # print('sum of all primes less than n: ', m1p10(50))
    print('greatest product for adjacent blal: ', m1p8(4,12031203912038102938109283190283019283012))


