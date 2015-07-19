# Name: Jeffrey Xiao


def rot (c, n):
    if 'a' <= c <= 'z':
        c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    if 'A' <= c <= 'Z':
        c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    return c
def list_to_str( L ):
    """ L must be a list of characters; then,
        this returns a single string from them
      """
    if len(L) == 0: return ''
    return L[0] + list_to_str( L[1:] )
def encipher (S, n):
    return list_to_str([rot(x, n) for x in S])

def letProb( c ):
    """ if c is the space character or an alphabetic character,
        we return its monogram probability (for english),
        otherwise we return 1.0 We ignore capitalization.
        Adapted from
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0
def toString (S):
    if len(S) == 0:
        return ""
    return S[0] + toString(S[1:])
def decipher (S):
    if (len(S) == 0):
        return ""
    LoL = [x for x in [encipher(S, y) for y in range(26)]]
    minDiff = 1 << 30
    index = 0
    for x in range(len(LoL)):
        freq = [0]*26
        for y in LoL[x]:
            if 'a' <= y <= 'z':
                freq[ord(y) - ord('a')] += 1.0
            elif 'A' <= y <= 'Z':
                freq[ord(y) - ord('A')] += 1.0
        currDiff = 0
        for y in range(26):
            currDiff += abs(freq[y]/len(LoL[x]) - letProb(chr(y+ord('a'))))**3
        #print currDiff, " ", toString(LoL[x])
        if currDiff < minDiff:
            minDiff = currDiff
            index = x
        #print(LoL[x]) 
    return toString(LoL[index])
#print decipher("iyebo tyusxq Wb. Poixwkx!")
def blsort (L):
    count = 0
    for x in L:
        if x == 0:
            count+=1
    LC = [(0 if count > x else 1) for x in range(len(L))]
    return LC
def gensort (L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L
def jscore (S, T):
    cnt = 0;
    found = [False] * len(T)
    for x in S:
        for y in range(len(T)):
            if x == T[y] and found[y] == False:
                found[y] = True
                cnt += 1
                break;
    return cnt

def exact_change (target_amount, L):
    if target_amount < 0:
        return False
    canMake = [False]*(target_amount+1)
    canMake[0] = True
    for y in L:
        for x in range(target_amount, -1, -1):
            if canMake[x] and x + y <= target_amount:
                canMake[x+y] = True
    return canMake[target_amount]

def LCS (S, T):
    cnt = [[0 for i in xrange(len(S)+1)] for j in xrange(len(T)+1)]

    for x in range(len(T)):
        for y in range(len(S)):
            if T[x] == S[y]:
                cnt[x+1][y+1] = max(1+cnt[x][y], max(cnt[x][y+1], cnt[x+1][y]))
            else:
                cnt[x+1][y+1] = max(cnt[x][y+1], cnt[x+1][y])
    y = len(S)
    x = len(T)
    ans = ""
    while x != 0 and y != 0:
        if cnt[x][y] == cnt[x-1][y-1]+1 and S[y-1] == T[x-1]:
            ans += S[y-1]
            x-=1;
            y-=1;
        elif cnt[x][y] == cnt[x-1][y]:
            x-=1
        else:
            y-=1
    return ans[::-1]
            