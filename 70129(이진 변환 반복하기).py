def solution(s):
    zero_cnt = 0
    binary_cnt = 0

    while len(s) > 1:
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        binary = ""

        len_s = len(s)
        while len_s:
            binary += str(len_s % 2)
            len_s //= 2

        binary_cnt += 1
        s = binary[::-1]

    return [binary_cnt, zero_cnt]