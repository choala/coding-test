s = input()
answer = ""
for c in s:
    if c.islower():
        answer += c.upper()
    else:
        answer += c.lower()

print(answer)