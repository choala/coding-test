answer = ""
s = list(input())
map(int, s)
s.sort(reverse=True)

for i in range(len(s)):
    answer += s[i]

print(answer)