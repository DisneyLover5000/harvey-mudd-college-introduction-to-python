# Name: Jeffrey Xiao

import random
import math

def dartThrow ():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
        return True;
    return False;

def forPi (N):
    numhits = 0.0
    for i in range(N):
        numhits += 1.0 if dartThrow() else 0.0
        print numhits," out of ", i+1, " throws so pi is ", numhits/(i+1)*4
    return numhits / N * 4

def whilePi (maxError):
    numthrows = 0.0
    numhits = 0.0
    while numthrows == 0 or abs(numhits/numthrows*4 - math.pi) > maxError:
        numhits += 1.0 if dartThrow() else 0.0
        numthrows += 1
        print numhits," out of ", numthrows, " throws so pi is ", numhits/(numthrows)*4
    return numthrows