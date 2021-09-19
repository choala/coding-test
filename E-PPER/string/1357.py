x, y = input().split()
reversed_x = "".join(reversed(x))
reversed_y = "".join(reversed(y))
reversed_sum = int(reversed_x) + int(reversed_y)

print(int("".join(reversed(str(reversed_sum)))))