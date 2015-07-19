# python 2
#
# Homework 9, Problem 2
#
# Name: Jeffrey Xiao
#

# here is a function for printing 2d arrays
# (lists-of-lists) of data

def print2d( A ):
    """ print2d prints a 2d array, A
        as rows and columns
        input: A, a 2d list of lists
        output: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR):
        for c in range(NC): 
            print A[r][c],
        print

    return None


# create a 2d array from a 1d string
def createA( NR, NC, s ):
    """ returns a 2d array with
        NR rows (numrows) and
        NC cols (numcols)
        using the data from s: across the
        first row, then the second, etc.
        We'll only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [ s[0] ]
            s = s[1:] 
        A += [newrow]
    return A

def inarow_3east (ch, r_start, c_start, A):
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start >= h or c_start < 0 or c_start+2 >= w:
        return False
    for i in range(3):
        if A[r_start][c_start+i] != ch:
            return False
    return True
def inarow_3south (ch, r_start, c_start, A):
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+2 >= h or c_start < 0 or c_start >= w:
        return False
    for i in range(3):
        if A[r_start+i][c_start] != ch:
            return False
    return True
def inarow_3se (ch, r_start, c_start, A):
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+2 >= h or c_start < 0 or c_start+2 >= w:
        return False
    for i in range(3):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True
def inarow_3ne (ch, r_start, c_start, A):
    h = len(A)
    w = len(A[0])
    if r_start-1 < 0 or r_start >= h or c_start < 0 or c_start+2 >= w:
        return False
    for i in range(3):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True

def inarow_Neast (ch, r_start, c_start, A, N):
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start >= h or c_start < 0 or c_start+N-1 >= w:
        return False
    for i in range(N):
        if A[r_start][c_start+i] != ch:
            return False
    return True
def inarow_Nsouth (ch, r_start, c_start, A, N):
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+N-1 >= h or c_start < 0 or c_start >= w:
        return False
    for i in range(N):
        if A[r_start+i][c_start] != ch:
            return False
    return True
def inarow_Nse (ch, r_start, c_start, A, N):
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+N-1 >= h or c_start < 0 or c_start+N-1 >= w:
        return False
    for i in range(N):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True
def inarow_Nne (ch, r_start, c_start, A, N):
    h = len(A)
    w = len(A[0])
    if r_start-N+1 < 0 or r_start >= h or c_start < 0 or c_start+N-1 >= w:
        return False
    for i in range(N):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True
