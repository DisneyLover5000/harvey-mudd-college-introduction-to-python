# Name: Jeffrey Xiao

def unique (L) :
    if len(L) == 0:
        return True
    if L[0] in L[1:] :
        return False
    return unique(L[1:])
print unique([2, 42, 3, 42])