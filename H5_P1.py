# Name: Jeffrey Xiao

def isOdd (n):
    return n % 2 == 1
def numToBinary (n):
    ans = ""
    while n != 0:
        ans += str(n % 2)
        n /= 2
    return ans[::-1]
def binaryToNum (S):
    S = S[::-1]
    ans = 0
    power = 1
    for x in S:
        ans += power if x == "1" else 0
        power *= 2
    return ans
def increment (S):
    ans = binaryToNum(S)
    ans += 1
    if ans == 256:
        ans = 0
    ans = numToBinary(ans)
    return '0'*(8-len(ans)) + ans
def count (S, n):
    for x in range(n+1):
        print S
        S = increment(S)
        
def numToTernary (n):
    ans = ""
    while n != 0:
        ans += str(n % 3)
        n /= 3
    return ans[::-1]
def ternaryToNum (S):
    S = S[::-1]
    ans = 0
    power = 1
    for x in S:
        ans += power * (ord(x) - ord("0"))
        power *= 3
    return ans

def numToBalancedTernary (n):
    ans = []
    while n != 0:
        ans.append(n % 3)
        n /= 3
    for x in range(len(ans)):
        if (ans[x] >= 2):
            ans[x] -= 3
            if x == len(ans)-1:
                ans.append(1)
            else:
                ans[x+1]+=1
    ans.reverse()
    res = ""
    for x in ans:
        if x == -1:
            res += "-"
        elif x == 0:
            res += "0"
        else:
            res += "+"
    return res
def balancedTernaryToNum (S):
    S = S[::-1]
    ans = 0
    power = 1
    for x in S:
        if x == "+":
            ans += power
        elif x == "-":
            ans -= power
        power *= 3
    return ans
    