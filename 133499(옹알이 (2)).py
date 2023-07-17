def solution(babbling):
    answer = 0
    double_words = ["ayaaya", "yeye", "woowoo", "mama"]
    words = ["aya", "ye", "woo", "ma"]

    for x in babbling:
        for word in double_words:
            x = x.replace(word, "X")
        for word in words:
            x = x.replace(word, "O")

        flag = 1
        for c in x:
            if c != "O":
                flag = 0
                break

        if flag:
            answer += 1
    
    return answer