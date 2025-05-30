import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(pos):
    visited[pos] = True
    for next_pos in (pos + arr[pos], pos - arr[pos]):
        if 0 <= next_pos < n and not visited[next_pos]:
            dfs(next_pos)

n = int(input())
arr = list(map(int, input().split()))
start = int(input()) - 1  

visited = [False] * n
dfs(start)

print(sum(visited))