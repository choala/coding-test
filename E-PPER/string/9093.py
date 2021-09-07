n = int(input())

for i in range(n):
    s = input().split()

    for j in s:
        print("".join(reversed(j)), end=" ")
    print()