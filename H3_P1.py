from turtle import *
def chai(size):
    """ our chai function! """
    if (size<9): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai(size/2)
        right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return
def spiral (initialLength, angle, multiplier):
  if initialLength < 1 or initialLength > 500:
    return
  forward(initialLength)
  left(angle)
  spiral(initialLength * multiplier, angle, multiplier);



def svtree (trunkLength, levels):
  if levels == 0:
    return
  forward(trunkLength)
  left(20)
  svtree(trunkLength/2, levels-1)
  right(20)
  right(20)
  svtree(trunkLength/2, levels-1)
  left(20)
  backward(trunkLength)

def flakeside (sidelength, levels):
  if levels == 0:
    forward(sidelength)
    return;
  flakeside(sidelength/3, levels-1)
  right(60)
  flakeside(sidelength/3, levels-1)
  left(120)
  flakeside(sidelength/3, levels-1)
  right(60)
  flakeside(sidelength/3, levels-1)

def snowflake (sidelength, levels):
  flakeside(sidelength, levels)
  left(120)
  flakeside(sidelength, levels)
  left(120)
  flakeside(sidelength, levels)
  left(120)




'''
Created on Jun 11, 2015

@author: Jeffrey
'''
