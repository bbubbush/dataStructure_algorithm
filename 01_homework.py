# 리스트에서 첫번째와 마지막 값 구하기
def solution(x):
    if len(x) < 2 :
        return 0
    return x[0] + x[-1]

print solution([5])