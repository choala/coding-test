s = input()

if len(s) % 2 == 0:
    pre_s = s[0:len(s) // 2]
    post_s = s[len(s) // 2:]
else:
    pre_s = s[0:len(s) // 2]
    post_s = s[len(s) // 2 + 1:]

reversed_post_s = "".join(reversed(post_s))
if pre_s == reversed_post_s:
    print("1")
else:
    print("0")
