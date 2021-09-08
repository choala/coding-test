def solution(n, times):
    answer = 9999999999999
    times.sort()
    start = 1
    end = n * times[len(times) - 1]
    temp = 0

    while start <= end:
        mid = (start + end) // 2
        temp = 0

        for i in range(len(times)):
            temp += mid // times[i]

        if temp >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer