n=int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0  # 해당 단어 안에서 그룹단어로 충족되지 않는 알파벳 종류의 갯수
    
    # 입력받은 단어에서 i번째 알파벳과 i+1번째 알파벳이 다르면...
    # i+1 번째 알파벳부터 끝까지를 new_word로 정의하고 i 번째 알파벳과 동일한 알파벳의 유무를 파악한다.
    # 만약 있다면 그룹단어의 조건을 충족하지 못하기에 error의 값을 +1 해준다.
    # 그리고 error = 0 이면 그룹단어의 조건을 충족한 것이기에 group_word의 값을 +1해준다.
    
    # 그룹 단어의 조건 충족여부 확인        
    for i in range(len(word)-1):
        if word[i] != word[i+1]: 
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                error += 1
    
    # 그룹 단어의 조건을 충족(error = 0)하면 그룹단어의 갯수 +1            
    if error == 0:
        group_word += 1
print(group_word)