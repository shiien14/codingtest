import sys
from collections import defaultdict

input = sys.stdin.readline

n,m = map(int,input().split())
words=defaultdict(int)

for _ in range(n):
    w=input().rstrip()
    words[w]+=1

word = list(set(words))
new=[]

for i in range(len(word)):
    if len(word[i])>=m:
        new.append([word[i], words[word[i]], len(word[i])])

new.sort(key= lambda x: (-x[1],-x[2],x[0]))

for n in new:
    print(n[0])