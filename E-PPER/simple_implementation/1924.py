day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

x, y = map(int, input().split())

for i in range(1, x):
    day += month_list[i - 1]


print(day_list[(day + y) % 7 - 1])
