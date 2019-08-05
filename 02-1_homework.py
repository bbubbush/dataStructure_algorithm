# 정렬된 리스트에 원소삽입
def solution(L, x):
    halfLength = len(L)//2

    if halfLength == 1:
        if x <= L[0]:
            L.insert(0, x)
        elif x >= L[1]:
            L.append(x)
        else:
            L.insert(1, x)
        return L    

    if x < L[halfLength]:
        result = solution(L[:halfLength+1], x)
        result += L[halfLength+1:]
    elif x >= L[halfLength]:
        result = L[:halfLength+1]
        result += solution(L[halfLength+1:], x)

    return result

print solution([20, 37, 58, 72, 91], 58)