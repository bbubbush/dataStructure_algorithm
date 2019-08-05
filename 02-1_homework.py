# 정렬된 리스트에 원소삽입

'''
 개발 방법: 
 문제에 "정렬된" 배열이 들어온다면 x값을 앞에서부터 비교하지 말고 배열의 전체 길이 중 
 가운데부터 비교하여 이보다 x가 크다면 우측을 기준으로 다시 절반을 비교하였다. (이진탐색의 원리)
'''
def solution(L, x):
    halfLength = len(L)//2  # 중앙값 인덱스

    # 종료조건
    if halfLength == 1:
        if x <= L[0]:
            L.insert(0, x)
        elif x >= L[1]:
            L.append(x)
        else:
            L.insert(1, x)
        return L    
    
    # 배열의 중앙값과 x의 값을 비교하여 입력된 배열을 잘라 재귀적으로 탐색
    if x < L[halfLength]:
        result = solution(L[:halfLength+1], x)
        result += L[halfLength+1:]
    elif x >= L[halfLength]:
        result = L[:halfLength+1]
        result += solution(L[halfLength+1:], x)

    return result

# 테스트케이스
print solution([20, 37, 58, 72, 91], 58)