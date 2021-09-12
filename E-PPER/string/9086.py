n = int(input())

for i in range(n):
    answer = ""
    s = input()

    answer += s[0]
    answer += s[len(s) - 1]

    print(answer)