# Name: Jeffrey Xiao


def numToBaseB (N, B):
    ans = ""
    while N != 0:
        ans += (str(N % B))
        N /= B
    return ans[::-1]
def baseBToNum (S, B):
    ans = 0
    power = 1
    S = S[::-1]
    for x in S:
        ans += power * (ord(x) - ord("0"))
        power *= B
    return ans

def baseToBase(B1, B2, S):
    return numToBaseB(baseBToNum(S, B1), B2)

def add (S, T):
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def addB (S, T):
    ans = []
    carry = 0
    S = "0"*(max(len(T) - len(S), 0)) + S
    T = "0"*(max(len(S) - len(T), 0)) + T
    S = S[::-1]
    T = T[::-1]
    N = min(len(S), len(T))
    for x in range(N):
        sum = carry + ord(S[x]) - ord('0') + ord(T[x]) - ord('0')
        ans.append(sum % 2)
        carry = sum/2
    if carry == 1:
        ans.append(1)
    ans.reverse()
    return "".join(str(x) for x in ans)

def compress (I):
    cnt = 1
    ans = ""
    for x in range(1, len(I)):
        if I[x] != I[x-1]:
            ans += I[x-1]
            pad = numToBaseB(cnt, 2)
            ans += "0"*(7-len(pad)) + pad
            cnt = 1
        else:
            cnt += 1
    pad = numToBaseB(cnt, 2)
    ans += I[len(I)-1] +  "0"*(7-len(pad)) + str(pad)
    return ans
def uncompress (I):
    ans = ""
    for i in xrange(0, len(I), 8):
        ans += I[i]*(baseBToNum(I[i+1:i+8], 2))
    return ans
    
    
    