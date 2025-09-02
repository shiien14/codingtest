def change(number, n):
    changedNumber = ''

    while number >0:
        number, mod = divmod(number, n)
        changedNumber += str(mod)

    return changedNumber[::-1]

def solution(n, k):
    answer = 0
    for num in change(n,k).split('0'):
        if num == '1' or num == '':
            continue
        for i in range(2,int(int(num)**0.5)+1):
            if int(num)%i == 0:
                break
        else:
            answer += 1
    return answer