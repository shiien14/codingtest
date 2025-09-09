def solution(prices):
    n = len(prices)
    answer = [0] * n
    st = []

    for i, p in enumerate(prices):
        while st and prices[st[-1]] > p:
            j = st.pop()
            answer[j] = i - j
        st.append(i)

    while st:
        j = st.pop()
        answer[j] = n - 1 - j

    return answer