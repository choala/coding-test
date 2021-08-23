import math
N = int(input())
count = 0

A = list(map(int, input().split()))
B, C = map(int, input().split())

for i in A:
    for_c = i - B
    if for_c <= 0:
        for_c = 0
    count += (1 + math.ceil(for_c / C))

print(count)
