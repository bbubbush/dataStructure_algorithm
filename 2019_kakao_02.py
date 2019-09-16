def solution(N, stages):
    answer = {}
    totalStage = [0 for i in range(N + 2)]
    for currentStage in stages:
        totalStage[currentStage] = totalStage[currentStage] + 1
    
    for i in range(1, N + 1):
        sumValue = sum(totalStage[i:])
        if sumValue == 0:
            answer[i] = 0
        else:
            answer[i] = totalStage[i] / sumValue
        
    return [i[0] for i in sorted(answer.items(), key = lambda x: x[1], reverse=True)]


# print(solution(6, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4]))
print(solution(3, [2,2,2,1,1]))