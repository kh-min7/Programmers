def solution(park, routes):
    answer = []
    start_x, start_y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start_x, start_y = i, j
                break

    for i in range(len(routes)):
        if routes[i][0] == "E":
            if start_y + int(routes[i][2]) < len(park[0]):
                for j in range(1, int(routes[i][2]) + 1):
                    if park[start_x][start_y + j] == "X":
                        break
                    if j == int(routes[i][2]):
                        start_y += int(routes[i][2])

        elif routes[i][0] == "S":
            if start_x + int(routes[i][2]) < len(park):
                for j in range(1, int(routes[i][2]) + 1):
                    if park[start_x + j][start_y] == "X":
                        break
                    if j == int(routes[i][2]):
                        start_x += int(routes[i][2])

        elif routes[i][0] == "W":
            if start_y - int(routes[i][2]) >= 0:
                for j in range(1, int(routes[i][2]) + 1):
                    if park[start_x][start_y - j] == "X":
                        break
                    if j == int(routes[i][2]):
                        start_y -= int(routes[i][2])      
                        
        elif routes[i][0] == "N":
            if start_x - int(routes[i][2]) >= 0:
                for j in range(1, int(routes[i][2]) + 1):
                    if park[start_x - j][start_y] == "X":
                        break
                    if j == int(routes[i][2]):
                        start_x -= int(routes[i][2])         
                        
    answer.append(start_x)
    answer.append(start_y)
    return answer
