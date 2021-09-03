n = int(input())
num = 0
fib_num = []

for i in range(n + 1):
    if i == 0:
        num = 0
    elif i == 1:
        num = 1
    else:
        num = fib_num[-1] + fib_num[-2]
    fib_num.append(num)

print(fib_num[-1])

