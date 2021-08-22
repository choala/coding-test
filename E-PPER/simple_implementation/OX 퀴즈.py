def solution(user_input):
    user_input = list(user_input)
    prev = ""
    seriesCnt = 1
    total_score = 0

    for c in user_input:
        if c == "O":
            if prev == "O":
                seriesCnt += 1
                total_score += seriesCnt
                prev = "O"
            else:
                total_score += seriesCnt
                prev = "O"
        else:
            seriesCnt = 1
            prev = "X"

    return total_score


if __name__ == '__main__':
    user_input = input()
    if len(user_input) > 1000:
        print('입력 범위를 초과하였습니다.\n')
        exit(1)
    print(solution(user_input))