# Name: Jeffrey Xiao
import math

def makeList(numString):
    numString = numString.replace('[', '')
    numString = numString.replace(']', '')
    numList = numString.split(',')
    L = []
    for x in numList:
        L.append(float(x.strip()))
    return L

def main ():
    isQuit = False
    L = []
    while isQuit == False:
        print "(0) Input a new list"
        print "(1) Print the current list"
        print "(2) Find the average price"
        print "(3) Find the standard deviation"
        print "(4) Find the min and its day"
        print "(5) Find the max and its day"
        print "(6) Your TT investment plan"
        print "(9) Quit"
        print 
        choice = int(raw_input("Enter your choice: "));
        if choice == 9:
            isQuit = True
        elif choice == 0:
            numString = raw_input("Enter a new list: ")
            L = makeList(numString)
        elif choice == 1:
            printList(L)
        elif choice == 2:
            print "The average price is", averagePrice(L)
        elif choice == 3:
            print "The st. deviation is", standardDev(L)
        elif choice == 4:
            ans = minDay(L)
            print "The min is", ans[0], "on day", ans[1]
        elif choice == 5:
            ans = maxDay(L)
            print "The max is", ans[0], "on day", ans[1]
        elif choice == 6:
            ans = TTPlan(L)
            print "Your TTS investment strategy is to"
            print 
            print " Buy on day", ans[0], "at price", L[ans[0]]
            print " Sell on day", ans[1], "at price", L[ans[1]]
            print " For a total profit of", ans[2]
        else:
            print "The choice", choice, "is not an option."
            print "Try again"
        print
    print "See you yesterday!"
def TTPlan (L):
    maxV = -(1 << 30)
    ans = []
    for x in xrange(len(L)):
        for y in xrange(1, len(L)):
            if L[y] - L[x] > maxV:
                maxV = L[y] - L[x]
                ans = [x, y, maxV]
    return ans
def maxDay (L):
    maxV = -(1 << 30)
    index = 0
    for x in xrange(len(L)):
        if L[x] > maxV:
            maxV = L[x]
            index = x
    return [maxV, index]
def minDay (L):
    minV = 1 << 30
    index = 0
    for x in xrange(len(L)):
        if L[x] < minV:
            minV = L[x]
            index = x
    return [minV, index]
def standardDev (L):
    ave = averagePrice(L)
    s = 0.0
    for x in L:
        s += (x - ave)**2
    return math.sqrt(s / len(L))
def averagePrice (L):
    s = 0.0
    for x in L:
        s += x
    return s / len(L)
def printList (L):
    print
    print "Day  Price"
    print "---  -----"
    for x in xrange(len(L)):
        print ("%3d %5.2f" %(x, L[x]))
    print
    
main()