N = input()
new = ""
cycle = 0

if len(N) < 2:
    N = "0" + N

new = N
tmp = str(int(new[0]) + int(new[1]))
if len(tmp) < 2:
    tmp = "0" + tmp
new = new[1] + tmp[1]
cycle += 1

while N != new:
    tmp = list(str(int(new[0]) + int(new[1])))
    if len(tmp) < 2:
        tmp.insert(0, "0")
    new = new[1] + tmp[1]
    cycle += 1

print(cycle)
