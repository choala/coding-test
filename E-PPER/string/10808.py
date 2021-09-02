s = input()
alpha = [0 for i in range(26)]
for c in s:
    index = ord(c) - 97
    alpha[index] += 1

for i in alpha:
    print(i, end=" ")