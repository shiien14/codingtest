import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

cards.sort()

def binary_search(array, target):
    left = 0
    right = N-1
    
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    return False 


for t in test:
    if binary_search(cards, t):
        print(1, end=" ")
    else:
        print(0, end=" ")