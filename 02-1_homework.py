
def solution(L, x):
    halfLength = len(L)//2  
    if len(L) == 1:
        if x <= L[0]:
            L.insert(0, x)
        elif x > L[0]:
            L.append(x)
        
        return L    
    
    if x < L[halfLength]:
        result = solution(L[:halfLength+1], x)
        result += L[halfLength+1:]
    elif x >= L[halfLength]:
        result = L[:halfLength+1]
        result += solution(L[halfLength+1:], x)

    return result


print solution([20, 37, 58, 72, 91, 100, 121], 58)