# python 2
#
# Homework 8, Problem 1
# Loops!
#
# Name: Jeffrey Xiao
#
import random

def power (b, p):
    ans = 1
    for i in xrange(p):
        ans *= b
    return ans

def summedOdds (L):
    ans = 0
    for i in xrange(len(L)):
        ans += L[i] if L[i] % 2 == 1 else 0
    return ans
def uniq( L ):
    """ returns whether all elements in L are unique
        input: L, a list of any elements
        output: True, if all elements in L are unique,
             or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return uniq( L[1:] ) # recursion is OK, too!
def untilARepeat (high):
    L = []
    cnt = 0
    while uniq(L):
        L.append(random.choice(range(0, high)))
        cnt += 1
    return cnt