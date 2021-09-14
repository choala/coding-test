n = int(input())
flag = 0
alpha = [0 for _ in range(26)]

for i in range(n):
    s = input()
    index = ord(s[0]) - 97
    alpha[index] += 1

for i in range(26):
    if alpha[i] > 4:
        print(chr(i + 97), end="")
        flag = 1

if flag == 0:
    print("PREDAJA")