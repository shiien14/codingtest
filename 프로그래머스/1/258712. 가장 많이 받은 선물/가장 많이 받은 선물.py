from typing import List
from itertools import combinations

def solution(friends: List[str], gifts: List[str]) -> int:
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}

    sent = [[0] * n for _ in range(n)]
    gift_index = [0] * n

    for g in gifts:
        a, b = g.split()
        i, j = idx[a], idx[b]
        sent[i][j] += 1
        gift_index[i] += 1
        gift_index[j] -= 1

    received_next = [0] * n

    for i, j in combinations(range(n), 2):
        if sent[i][j] > sent[j][i]:
            received_next[i] += 1
        elif sent[i][j] < sent[j][i]:
            received_next[j] += 1
        else:
            if gift_index[i] > gift_index[j]:
                received_next[i] += 1
            elif gift_index[i] < gift_index[j]:
                received_next[j] += 1

    return max(received_next) if received_next else 0
