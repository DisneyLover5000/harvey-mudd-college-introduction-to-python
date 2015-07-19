# python 2
#
# Homework 3, Problem 3
# List comprehensions!
#
# Name: Jeffrey Xiao
#

# this gives us functions like sin and cos
from math import *

# two more functions (not in the math library above)
def dbl(x):
    """ doubler!  input: x, a number """
    return 2*x

def sq(x):
    """ squarer!  input: x, a number """
    return x**2

# examples for getting used to list comprehensions
def lc_mult( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each multiplied by 2**
    """
    return [ 2*x for x in range(N) ]

def lc_idiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        WARNING: this is INTEGER division...!
    """
    return [ x/2 for x in range(N) ]

def lc_fdiv( N ):
    """ this example takes in an int N
        and returns a list of integers
        from 0 to N-1, **each divided by 2**
        NOTE: this is floating-point division...!
    """
    return [ float(x)/N for x in range(N) ]


# Here is where your functions start for the homework:

# Step 1, part 1
def unitfracs( N ):
    """ Returns a list of evenly-spaced left-hand endpoints 
        in the unit interval of [0, 1)
    """
    return lc_fdiv(N);

def scaledfracs (lo, hi, N):
    """ Returns a list of N left endpoints uniformly through
        the interval of [low, hi)
    """
    return [(hi - lo) * x + lo for x in unitfracs(N)]
def sqfracs (lo, hi, N):
    """ Returns a list of N squared left endpoints uniformly 
        through the interval of [lo, hi)
    """
    return [x**2 for x in scaledfracs(lo, hi, N)]

def f_of_fracs (f, low, hi, N):
    """ Returns a list of N left endpoints uniformly through
        the interval of [lo, hi) that has function f applied
        to it
    """
    return [f(x) for x in scaledfracs(low, hi, N)];

def integrate (f, low, hi, N):
    """ integrate returns an estimate of the definite integral
        of the function f (the first input)
        with lower limit low (the second input)
        and upper limit hi (the third input)
        where N steps are taken (the fourth input)

        integrate simply returns the sum of the areas of rectangles
        under f, drawn at the left endpoints of N uniform steps
        from low to hi
      """
    return sum(f_of_fracs(f, low, hi, N)) * (hi - low)/N

def c (x):
    return (4-x**2)**0.5

"""
Q1.

Integrate will always underestimate the correct value of this
integral because no matter how small the rectangles you use
to partition the area under y = 2x, there will be small part
of the area unaccounted for.

Q2.
It converges to pi. The area of a circle with radius 2
is 4pi. Thus 1/4 of that area is pi.
"""

