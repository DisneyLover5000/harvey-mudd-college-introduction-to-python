# Name: Jeffrey Xiao

def isPrime (n) :
    for x in range(2, n) :
        if n % x == 0 :
            return False
    return True

def addPrimes (L) :
    ans = 0
    for x in L :
        if isPrime(x) :
            ans += x
    return ans

def uniquify (L) :
    if len(L) == 0 :
        return []
    if not L[0] in L[1:] :
        return [L[0]] + uniquify(L[1:])
    return uniquify(L[1:])
    
def median (L) :
    L.sort()
    N = len(L)
    if N % 2 == 0 :
        return (L[N/2] + L[(N-1)/2])/2.0
    return L[N/2]

def symmetric (S) :
    N = len(S)
    for i in range(N) :
        for j in range(N) :
            if S[i][j] != S[j][i] :
                return False
    return True
class Matrix:
    def __init__(self, nr, nc):
        self.NRows = nr
        self.NCols = nc
        self.data = [ [0]*self.NCols for r in range(self.NRows) ]
    def max (self, m2) :
        N = min(self.NRows, m2.NRows)
        M = min(self.NCols, m2.NCols)
        res = Matrix(N, M)
        for i in range(N) :
            for j in range(M) :
                res.data[i][j] = max(self.data[i][j], m2.data[i][j])
        return res
print Matrix(5, 5).max(Matrix(3, 6)).data