# -*- coding: utf-8 -*- 

# 피보나치수열
def solution(x):
    if x == 0 or x == 1:
        return x
    else:
        return solution(x-1) + solution(x-2)

#  Test case
print solution(2)
print solution(5)
print solution(7)