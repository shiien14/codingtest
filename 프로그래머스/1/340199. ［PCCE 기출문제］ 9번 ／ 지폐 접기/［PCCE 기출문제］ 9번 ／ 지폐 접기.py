def solution(wallet, bill):
    answer = 0
    while True:
        wallet.sort(reverse=True)
        bill.sort(reverse=True)
        if wallet[0]>=bill[0] and wallet[1]>=bill[1]:
            return answer
        else:
            bill[0]=bill[0]//2
            answer+=1
    return answer