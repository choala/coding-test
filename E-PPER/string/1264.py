s = input().lower()
sum = 0

while s != "#":
    sum += s.count("a")
    sum += s.count("e")
    sum += s.count("i")
    sum += s.count("o")
    sum += s.count("u")
    print(sum)

    sum = 0
    s = input().lower()
