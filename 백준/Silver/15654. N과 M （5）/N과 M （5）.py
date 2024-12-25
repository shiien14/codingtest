import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums= list(map(int, input().split()))
nums.sort()

result = []

def back():
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(n):
        if nums[i] not in result:
            result.append(nums[i])
            back()
            result.pop()

back()