import sys
input = sys.stdin.readline

N = int(input().strip())
budgets=list(map(int, input().split()))
total_budget = int(input().strip())

low, high = 0, max(budgets)
result = 0

while low <= high:
    mid = (low + high) // 2
    
    allocated = sum(min(b, mid) for b in budgets)
        
    if allocated <= total_budget:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)