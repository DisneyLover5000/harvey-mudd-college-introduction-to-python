# python 2
#
# Homework 3, Problem 2
#
# Name: Jeffrey Xiao
#

import random  

def rs():
    """ rs chooses a random step and returns it 
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos (start, nsteps):
    print "CURRENT POSITION", start
    if nsteps == 0:
        return start
    return rwpos(start + rs(), nsteps-1)

def rwsteps (start, low, hi):
    print "-"*(start-low) + "S" + "-" * (hi - start)
    if start == low or start == hi:
        return 0;
    return 1 + rwsteps(start + rs(), low, hi)
def rwposPlain (start, nsteps):
    if nsteps == 0:
        return start
    return rwposPlain(start + rs(), nsteps-1)
def ave_signed_displacement (numtrials):
    sum = 0;
    for x in range(numtrials):
        sum += rwposPlain(0, 100)
    return float(sum) / numtrials
def ave_squared_displacement (numtrials):
    sum = 0;
    for x in range(numtrials):
        sum += rwposPlain(0, 100)**2
    return float(sum) / numtrials
# print ave_signed_displacement(10000)
# print ave_squared_displacement(10000)
"""
    In order to compute the average signed displacement for
    a random walker after 100 random steps, I created a function
    rwpos that simulated the path of the random walk and returned
    the position after the N steps
    
    Using that function, I was able to compute the average of
    N trials (in this case my averages were the result fo 10,000
    trials)
    
    average signed displacement = 0.0428
    average squared displacement = 100.2336
"""