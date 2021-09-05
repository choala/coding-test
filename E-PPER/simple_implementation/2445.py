n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end="")

    for k in range(2 * n - 2, 2 * i, -1):
        print(" ", end="")

    for q in range(i + 1):
        print("*", end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")

    for k in range(2 * i, 2 * n):
        print(" ", end="")

    for j in range(i, 0, -1):
        print("*", end="")

    print()