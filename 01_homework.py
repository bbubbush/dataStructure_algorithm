def solution(x):
    # firstValue = x[0]
    # lastValue = x[len(x)-1]
    # answer = firstValue + lastValue

    if len(x) < 2 :
        return 0
    return x[0] + x[-1]

print solution([5])