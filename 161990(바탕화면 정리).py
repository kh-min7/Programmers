import math

def solution(wallpaper):
    answer = []
    left, up, right, down = -math.inf, -math.inf, math.inf, math.inf,
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                if left <= j:
                    left = j
                if up <= i:
                    up = i
                if right >= j:
                    right = j
                if down >= i:
                    down = i
    answer.append(down)
    answer.append(right)
    answer.append(up + 1)
    answer.append(left + 1)
        
    return answer

wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))

