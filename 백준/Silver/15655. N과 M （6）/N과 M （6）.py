import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums= list(map(int, input().split()))
nums.sort()

result = []

def back(k):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(k,n):
        if nums[i] not in result:
            result.append(nums[i])
            back(i+1)
            result.pop()

back(0)
