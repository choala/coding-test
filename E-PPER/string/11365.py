s = input()

while s != "END":
    s = "".join(reversed(s))
    print(s)
    s = input()