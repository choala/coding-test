N = int(input())
flag = 0
five_count, remain_sugar = divmod(N, 5)
three_count = 0

if remain_sugar % 3 == 0:
    three_count = remain_sugar // 3
    print(five_count + three_count)
    flag = 1
else:
    while five_count > 0:
        five_count -= 1
        remain_sugar += 5
        if remain_sugar % 3 == 0:
            three_count = remain_sugar // 3
            print(five_count + three_count)
            flag = 1
            break

if flag == 0:
    print("-1")
