# -*- coding: utf-8 -*- 

# 이진탐색
def solution(L, x):
    # 직접해보다 망함 ㅋ
    # if len(L) == 1 and L[0] != x:
    #     return -1
    
    # halfLength = len(L)//2  # 중앙값 인덱스
    # if x < L[halfLength]:
    #     return solution(L[:halfLength], x)
    # elif x > L[halfLength]:
    #     result = solution(L[halfLength+1:], x)
    #     if result == -1:
    #         return -1
    #     else:
    #         return  result + halfLength + 1
    # elif x == L[halfLength]:
    #     return halfLength
    # return -1

    # 강의 따라서 작성
    lower = 0
    upper = len(L) -1
    idx = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] > x:
            upper = middle - 1

        elif L[middle] < x:
            lower = middle + 1
    
    return -1


#  Test case
print solution([2, 3, 5, 6, 9, 11, 15], 2)
print solution([2, 5, 7, 9, 11], 4)