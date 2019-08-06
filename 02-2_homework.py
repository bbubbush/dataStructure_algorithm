# 리스트에서 원소 찾아내기

'''
 개발 방법: 
 배열 중 x와 같은 데이터의 인덱스를 따로 뽑아두고, 해당 결과값이 0개면 [-1]을, 아니면 결과값을 리턴한다
'''
def solution(L, x):
    result = [idx for idx, value in enumerate(L) if x == value]
    return len(result) == 0 and [-1] or result 

# 테스트 케이스
print solution([20, 37, 58, 72, 91], 11)