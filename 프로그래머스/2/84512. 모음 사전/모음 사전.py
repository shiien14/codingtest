from itertools import product

def solution(word):
    result = []
    for i in range(1, 6):
        result += list(map(''.join, product('AEIOU', repeat = i)))
    result.sort()
    return result.index(word) + 1