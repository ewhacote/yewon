# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

global ok 
ok = list()

def is_prime_number(n):
    # tuple -> list -> str -> int
    nums = list(n)
    string = ''.join(s for s in nums)
    num = int(string)
    # 소수 판별
    if num == 1 or num == 0 :
        return False
    for i in range(2,num):
        if (num % i == 0):
            return False
    ok.append(num)
    cnt = ok.count(num)
    if (cnt >= 2):
        return False
    return True

def solution(numbers):
    answer = 0
    length = len(numbers)
    for i in range(1,length+1):
        for j in permutations(numbers,i):
            result = is_prime_number(j)
            if (result == True):
                answer+=1
    return answer
