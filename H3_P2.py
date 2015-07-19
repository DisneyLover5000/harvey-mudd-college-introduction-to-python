# python 2
#
# Homework 3, Problem 1.5
#
# Name: Jeffrey Xiao
#
# Date: June 11
# Overall comments:
#

#
# mylen example from class
#
def mult (n, m):
    if m < 0:
        n = -n
        m = -m
    if m == 0:
        return 0;
    return n + mult(n, m-1)

def dot (L, K):
    if len(L) != len(K):
        return 0.0
    if len(L) == 0:
        return 0.0
    return L[0]*K[0] + dot(L[1:], K[1:])

def ind (e, L):
    if len(L) == 0:
        return 0
    if L[0] == e:
        return 0
    return 1+ind(e, L[1:])

def letterScore (let):
    if let in "aeilnorsstu":
        return 1
    elif let in "dg":
        return 2
    elif let in "bcmp":
        return 3
    elif let in "fhvwy":
        return 4
    elif let in "k":
        return 5
    elif let in "jx":
        return 8
    elif let in "qz":
        return 10
    return 0;
def scrabbleScore (S):
    if len(S) == 0:
        return 0
    return letterScore(S[0]) + scrabbleScore(S[1:])
def one_dna_to_rna( c ):
    if c == 'A': return 'U'
    elif c == 'C': return 'G'
    elif c == 'G': return 'C'
    elif c == 'T': return 'A'
    return ''
def transcribe (S):
    if len(S) == 0:
        return "";
    return one_dna_to_rna(S[0]) + transcribe(S[1:])