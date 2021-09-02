s = input().split("-")
tmp = 0
res = 0

for i in s[0].split("+"):
    res += int(i)

for i in s[1:]:
    for j in i.split("+"):
        tmp += int(j)
    res -= tmp
    tmp = 0

print(res)
