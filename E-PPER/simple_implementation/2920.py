scale = list(map(int, input().split()))
prev_scale = scale[0]
gap = scale[0] - scale[1]
flag = 0

for i in range(1, len(scale)):
    if prev_scale - scale[i] != gap:
        print("mixed")
        flag = 1
        break
    prev_scale = scale[i]

if flag == 0:
    if gap > 0:
        print("descending")
    if gap < 0:
        print("ascending")