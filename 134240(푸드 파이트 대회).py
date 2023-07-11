def solution(food):
    answer = ""
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            answer += str(i)
    r_answer = "".join(reversed(answer))
    answer += "0"
    answer += (r_answer)

    return answer