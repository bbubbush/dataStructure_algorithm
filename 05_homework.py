# -*- coding: utf-8 -*- 

# 재귀적 이진탐색
def solution(L, x, l, u):
    if l > u:   # 종료조건
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)

#  Test case
print solution([2, 3, 5, 6, 9, 11, 15], 6, 0, 6)
print solution([2, 5, 7, 9, 11], 4, 0, 4)