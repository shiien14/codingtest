import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
goals = list(map(int, input().split()))

goals_re = goals[::-1]

# 문자열 변환
nums_str = ' '.join(map(str, nums))
goals_str = ' '.join(map(str, goals * 2))
goals_re_str = ' '.join(map(str, goals_re * 2))

if nums_str in goals_str or nums_str in goals_re_str:
    print("good puzzle")
else:
    print("bad puzzle")