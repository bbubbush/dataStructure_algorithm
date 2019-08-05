# 리스트에서 원소 찾아내기
def solution(L, x):
    result = [idx for idx, value in enumerate(L) if x == value]
    return len(result) == 0 and [-1] or result 

print solution([20, 37, 58, 72, 91], 11)