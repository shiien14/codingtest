import sys

input = sys.stdin.readline

base=input().strip()
sentence = set()

for i in range(len(base)):
    for j in range(len(base)-i+1):
        sentence.add(base[j:j+i])

print(len(sentence))