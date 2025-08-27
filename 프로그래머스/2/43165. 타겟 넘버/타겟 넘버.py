def solution(numbers, target):
    def dfs(c_s, cnt):
        if cnt == len(numbers):
            if c_s == target:
                return 1
            else:
                return 0
        else:
            return dfs(c_s+numbers[cnt], cnt+1) + dfs(c_s-numbers[cnt],cnt+1)
            
    return dfs(0,0)