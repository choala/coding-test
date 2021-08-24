def solution(input):
    string = list(input)
    prev_c = ""
    answer = ""
    count = 0

    for c in string:
        if prev_c == c:
            count += 1
        else:
            if prev_c == "":
                if c == "1":
                    answer += "1"
                prev_c = c
                count += 1
            else:
                answer += chr(count + 64)
                count = 1
                prev_c = c
    answer += chr(count + 64)
    return answer


user_input = input()
print(solution(user_input))