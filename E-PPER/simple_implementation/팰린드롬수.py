def solution(input_num):
    num = str(input_num)
    num_length = len(num)
    middle_index = num_length // 2
    pre_num = num[0:middle_index]
    if num_length % 2 == 0:
        post_num = num[num_length-1:middle_index-1:-1]
    else:
        post_num = num[num_length-1:middle_index:-1]

    if pre_num == post_num:
        print("yes")
    else:
        print("no")

    return 0


input_num = int(input())
while input_num != 0:
    solution(input_num)
    input_num = int(input())
