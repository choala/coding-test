i = 0
while i < 100:
    try:
        s = input()
        print(s)
    except EOFError:
        break

    i += 1
