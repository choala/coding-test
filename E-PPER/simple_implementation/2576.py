odd = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        odd.append(n)

if sum(odd) == 0:
    print("-1")
else:
    print(sum(odd))
    print(min(odd))