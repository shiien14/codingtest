def solution(board, moves):
    space=[]
    result=0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if len(space)!=0 and space[-1]==board[i][m-1]:
                    space.pop()
                    result+=2
                else:
                    space.append(board[i][m-1])
                board[i][m-1]=0
                break
        
    return result