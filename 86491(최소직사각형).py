def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_x = 0
    max_y = 0
    for x, y in sizes:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
            
    return max_x * max_y