def solution(n, arr1, arr2):
    result= []
    map1 = []
    map2 = []
    for num1 in arr1:
        num=bin(num1)[2:]
        if len(num) <n:
            num="0"*(n-len(num))+num
        map1.append(num)
    for num2 in arr2:
        num=bin(num2)[2:]
        if len(num) <n:
            num="0"*(n-len(num))+num
        map2.append(num)

    for i in range(n):
        answer=""
        for j in range(n):
            if map1[i][j] == "1" or map2[i][j] == "1":
                answer+="#"
            else:
                answer+=" "
        result.append(answer)
    return result