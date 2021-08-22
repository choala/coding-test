def solution(r, c, zr, zc, words):
    answer = []

    for i in range(r):
        input_row = list(words[i])
        tmp_row = ""
        for j in input_row:
            for k in range(zc):
                tmp_row += j

        for q in range(zr):
            answer.append(tmp_row)

    return answer


r, c, zr, zc = input().split()
r = int(r)
c = int(c)
zr = int(zr)
zc = int(zc)

words = []

for i in range(r):
    temp = input()
    if (len(temp) > c):
        print("입력 범위를 초과하였습니다.\n")
        exit(1)
    words.append(temp)

answer = solution(r, c, zr, zc, words);

for i in range(r * zr):
    print(answer[i])