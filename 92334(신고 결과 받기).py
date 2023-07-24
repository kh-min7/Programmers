def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_list = []
    for x in report:
        tmp = list(map(str, x.split(" ")))
        report_list.append((tmp[0], tmp[1]))
    report_list = list(set(report_list))

    report_dict = {}
    for x in report_list:
        if x[1] not in report_dict:
            report_dict[x[1]] = 1
        else:
            report_dict[x[1]] += 1


    for i in range(len(report_list)):
        if report_dict[report_list[i][1]] >= k:
            answer[id_list.index(report_list[i][0])] += 1

    return answer