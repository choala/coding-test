n = int(input())
num = 0
fib = []

for i in range(n + 1):
    if i == 0:
        num = 0
    elif i == 1:
        num = 1
    else:
        num = fib[i - 1] + fib[i - 2]
    fib.append(num)

print(fib[-1])
