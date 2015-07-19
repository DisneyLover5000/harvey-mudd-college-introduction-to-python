# python 2
#
# Homework 4, Problem 1
# "Lights On!"
#
# Name: Jeffrey Xiao
#
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.

def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def mutate1 (i, oldL):
    return oldL[i]**2

def mutate2 (i, oldL):
    return oldL[(i+int(len(oldL))-1)%len(oldL)]
def mutate3 (i, oldL):
    return choice([0, 1])

def mutate4(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        new_ith_element = 1 
    else:
        new_ith_element = oldL[i]
    return new_ith_element

def mutate5(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        new_ith_element = (oldL[i]+1)%2 
    else:
        new_ith_element = oldL[i]
    return new_ith_element
def mutate6(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if abs(i-user) <= 1:
        new_ith_element = (oldL[i]+1)%2
    else:
        new_ith_element = oldL[i]
    return new_ith_element
def allOnes (l):
    for x in l:
        if x != 1:
            return False;
    return True;
def randBL (N):
    """ Returns a random binarylist
    """
    return [choice([0,1]) for x in range(N)]
def evolve(oldL, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print oldL,                    # print the old list, L
    print "  (gen: " + str(curgen) + ")"  # and its gen.
    #time.sleep(0.1)
    if allOnes(oldL):
        return curgen;
    #user = input("Index? ")
    user = choice(range(len(oldL))) # simulating computer
    newL = [ mutate6(i,oldL,user) for i in range(len(oldL)) ]
    return evolve(newL, curgen + 1)
"""
I believe that it should take approximately 32 times
to randomly generate all 1s for 5 lights
"""
#print evolve([1,0,0,1])
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)