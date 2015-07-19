'''
Created on Jun 13, 2015

@author: Jeffrey
'''


def swapBits (S) :
    if len(S) == 0 :
        return ""
    return ("1" if S[0] == "0" else "0") + swapBits(S[1:])

def numDivisors (N) :
    res = 0
    for i in range(1, N+1) :
        if N % i == 0 :
            res += 1
    return res

def cycle (S, N) :
    ans = ""
    sz = len(S)
    for x in range(sz) :
        ans += S[((x-N)%sz + sz)%sz]
    return ans

def indexNearest42 (L) :
    index = -1
    minV = 1 << 30
    for i in xrange(len(L)) :
        diff = L[i] - 42
        if diff < 0 :
            diff = -diff
        if diff < minV :
            minV = diff
            index = i
    return index

def longestDNA (s) :
    res = ""
    for i in xrange(len(s)) :
        for j in xrange(i, len(s)) :
            if s[j] in 'ACGT' and j - i + 1 > len(res) :
                res = s[i:j+1]
            elif not s[j] in 'ACGT' :
                break
    return res
""" HMMM
Add numbers until 0 is inputed. Then print the sum and average of the numbers.
00 setn r1 0
01 setn r3 0
02 read r2
03 jeqzn r2 07
04 add r1 r1 r2
05 addn r3 1
06 jumpn 02
07 write r1
08 div r1 r1 r3
09 write r1
10 halt
"""
