l, p = map(int, input().split())
num = list(map(int, input().split()))

for n in num:
    print(n - l * p, end=" ")