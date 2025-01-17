# -*- coding: utf-8 -*- 

'''
객관식 4. N 개의 수가 입력으로 주어진다고 할 때, 모든 원소들 사이의 대소 관계를 비교하여 N X N 행렬로 나타내고자 합니다. 
이 문제를 풀기 위하여 모든 원소의 쌍에 대하여 대소 관계를 비교하여 그것을 행렬에 채우는 방법을 택한다고 할 때, 
이 알고리즘의 복잡도를 big-O 점근 표기법으로 표기한 다음 중 알맞은 것을 선택하세요.

선택한 정답 : 2. O(N)
실제 정답 : 4. O(N^2)
선택한 이유 : N개의 수를 N X N 행렬에 입력한다면 N이 부족하지 않나 싶어 문제를 잘못낸줄 알았다. N = 5일때, 5 X 5 행렬은 25개의 수가 필요하니깐...
'''
'''
객관식 5.N 행 N 열의 정사각행렬 A 와 B 가 주어진다고 할 때, 이 두 행렬의 곱 (product) 인 N X N 행렬 C 를 계산하기 위하여 다음과 같은 방법을 쓸 수 있습니다.
for i in range(N):
    for j in range(N):
        C[i][j] = 0
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]
이러한 알고리즘을 이용하여 행렬의 곱셈을 행할 때, 이 행렬 곱셈 (matrix multiplicaiton) 알고리즘의 복잡도를 big-O 점근 표기법으로 
알맞게 표기한 것을 아래 보기에서 선택하세요.

선택한 정답 : 4. O(N^2)
실제 정답 : 5. O(N^3)
선택한 이유 : 직관적으로 보면 삼중 for문이기 때문에 5번을 선택하려고 했지만 두 행렬의 곱 이기 때문에 N X N으로 생각하여 4번을 선택했다.
'''