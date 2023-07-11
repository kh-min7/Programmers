def solution(s):
    str_to_num = {"zero":'0', "one":'1', "two":'2', "three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    num = ["0","1","2","3","4","5","6","7","8","9"]
    
    answer = []
    tmp_s = 0
    tmp_e = -1

    for i in range(len(s)):
        if s[i] in num:
            tmp_s = i + 1
            answer.append(s[i])
 
        else:
            tmp_e = i
            if s[tmp_s:tmp_e + 1] in str_to_num:
                answer.append(str_to_num[s[tmp_s:tmp_e + 1]])
                tmp_s = i + 1

    answer = "".join(answer)

    return int(answer)