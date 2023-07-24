def solution(today, terms, privacies):
    answer = []

    today_list = list(map(int, today.split(".")))

    terms_list = {}
    for x in terms:
        terms_list[x[0]] = int(x[2:])

    privacies_list = []
    for x in privacies:
        tmp = list(map(int, x[:-1].split(".")))
        tmp.append(x[-1])
        privacies_list.append(tmp)

    for i in range(len(privacies)):
        privacies_list[i][1] += terms_list[privacies_list[i][3]]
        while privacies_list[i][1] > 12:
            privacies_list[i][0] += 1
            privacies_list[i][1] = privacies_list[i][1] - 12

        if privacies_list[i][0] < today_list[0]:
            answer.append(i + 1)
        elif privacies_list[i][0] == today_list[0] and privacies_list[i][1] < today_list[1]:
            answer.append(i+1)
        elif privacies_list[i][0] == today_list[0] and privacies_list[i][1] == today_list[1] and privacies_list[i][2] <= today_list[2]:
            answer.append(i+1)
             
    return answer