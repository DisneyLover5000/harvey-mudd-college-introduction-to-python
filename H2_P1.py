# python 2
# 
# Name: Jeffrey Xiao
#
# Homework 2, Problem 1
# slicing and indexing challenges
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]   
answer1 = e[1:];  
answer2 = [pi[5]] +2*[e[2]]
answer3 = pi[1:]
answer4 = e[::-2] + pi[::2]
print answer0
print answer1
print answer2
print answer3
print answer4

h = "harvey"
m = "mudd"
c = "college"
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5
answer6 = c[0:4] + m[1:3] + c[4]
print answer6
answer7 = h[1: 6] + m[1: 4]
print answer7
answer8 = h[0:3] + m[2] + c[4] + 3*h[0:3]
print answer8
answer9 = c[3:6] + c[1] + m[0] + h[5] + c[4:6] + c[1]
print answer9
answer10 = c[0] + c[3:5] + h[1:3]+c[0]+h[1]+c[2:4]
print answer10