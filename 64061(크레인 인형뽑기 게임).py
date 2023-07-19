def solution(board, moves):
    answer = 0
    bucket = []
    for i in range(len(moves)):
        for row in range(len(board)):

            if board[row][moves[i]-1] > 0:
                doll = board[row][moves[i]-1]
                board[row][moves[i]-1] = 0

                if len(bucket) > 0 and bucket[-1] == doll:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(doll)
                break 

    
    return answer