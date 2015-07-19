# python 2
#
# Homework 2, Problem 2
#
# Name: Jeffrey
# Date: June 11th
#

def tpl (x):
    return 3*x
def sq(x):
    return x*x
def interp (lo, hi, fraction):
    return float(hi-lo)*fraction + lo
def checkends (s):
    return s[0] == s[len(s)-1]
def flipside (s):
    return s[len(s)/2:] + s[:len(s)/2]
def convertFromSeconds (s):
    days = s / (24*60*60)
    s %= (24*60*60)
    hours = s/(60*60)
    s %= (60*60)
    minutes = s/60
    s %= 60
    return [days, hours, minutes, s]
def front3(s):
    return 3*s[:3]
#print convertFromSeconds(int(raw_input()))
#print interp(float(raw_input()), float(raw_input()), float(raw_input()))
