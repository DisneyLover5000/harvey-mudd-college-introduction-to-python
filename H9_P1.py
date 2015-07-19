# python 2
#
# Homework 9, Problem 1
# Game of Life
#
# Name: Jeffrey Xiao
#

import random
import math
def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]  
    return A
def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line
    print
def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A
def innerCells(w, h):
    A = createBoard(w, h)

    for row in range(h):
        for col in range(w):
            if 0 < row < h-1 and 0 < col < w-1:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
def randomCells (w, h):
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            A[row][col] = random.choice([0, 1])
    return A
def copy (A):
    height = len(A)
    width = len(A[0])
    B = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            B[row][col] = A[row][col]
    return B
def innerReverse (A):
    for row in range(len(A)):
        for col in range(len(A[0])):
            if 0 < row < len(A)-1 and 0 < col < len(A[0])-1:
                A[row][col] = (A[row][col] + 1) % 2
            else:
                A[row][col] = 0
    return A

def countNeighbors (row, col, A):
    cnt = 0
    for x in xrange(-1, 2, 1):
        for y in xrange(-1, 2, 1):
            if abs(x) + abs(y) != 0:
                cnt += A[row+x][col+y]
    return cnt

def next_life_generation (A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
    w = len(A[0])
    h = len(A)
    B = createBoard(w, h)
    for i in xrange(h):
        for j in xrange(w):
            if 0 < i < h-1 and 0 < j < w-1:
                cnt = countNeighbors(i, j, A)
                if cnt < 2 or cnt > 3:
                    B[i][j] = 0
                elif cnt == 3:
                    B[i][j] = 1
                else:
                    B[i][j] = A[i][j]
            else:
                B[i][j] = 0
    return B
