def solution(dirs):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = []
    start_x, start_y = 0, 0
    answer = 0
    for x in dirs:
        print(x)
        if x == 'U' and start_x + dx[0] >= -5 and start_x + dx[0] <= 5 and start_y + dy[0] >= -5 and start_y + dy[0] <= 5:
            if (start_x, start_y, start_x + dx[0], start_y + dy[0]) not in visited:
                visited.append((start_x, start_y, start_x + dx[0], start_y + dy[0]))
                visited.append((start_x + dx[0], start_y + dy[0], start_x, start_y))
                start_x, start_y = start_x + dx[0], start_y + dy[0]
                answer += 1
            else:
                start_x, start_y = start_x + dx[0], start_y + dy[0]

        elif x == 'D' and start_x + dx[1] >= -5 and start_x + dx[1] <= 5 and start_y + dy[1] >= -5 and start_y + dy[1] <= 5:
            if (start_x, start_y, start_x + dx[1], start_y + dy[1]) not in visited:
                visited.append((start_x, start_y, start_x + dx[1], start_y + dy[1]))
                visited.append((start_x + dx[1], start_y + dy[1], start_x, start_y))
                start_x, start_y = start_x + dx[1], start_y + dy[1]
                answer += 1
            else:
                start_x, start_y = start_x + dx[1], start_y + dy[1]

        elif x == 'L' and start_x + dx[2] >= -5 and start_x + dx[2] <= 5 and start_y + dy[2] >= -5 and start_y + dy[2] <= 5:
            if (start_x, start_y, start_x + dx[2], start_y + dy[2]) not in visited:
                visited.append((start_x, start_y, start_x + dx[2], start_y + dy[2]))
                visited.append((start_x + dx[2], start_y + dy[2], start_x, start_y))
                start_x, start_y = start_x + dx[2], start_y + dy[2]
                answer += 1
            else:
                start_x, start_y = start_x + dx[2], start_y + dy[2]


        elif x == 'R'  and start_x + dx[3] >= -5 and start_x + dx[3] <= 5 and start_y + dy[3] >= -5 and start_y + dy[3] <= 5:
            if (start_x, start_y, start_x + dx[3], start_y + dy[3]) not in visited:
                visited.append((start_x, start_y, start_x + dx[3], start_y + dy[3]))
                visited.append((start_x + dx[3], start_y + dy[3], start_x, start_y))
                start_x, start_y = start_x + dx[3], start_y + dy[3]
                answer += 1
            else:
                start_x, start_y = start_x + dx[3], start_y + dy[3]

    return answer

dirs = "ULURRDLLU"
print(solution(dirs))