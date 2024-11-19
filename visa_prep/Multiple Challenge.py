def count_multiples(N):
    count_3 = N // 3
    count_5 = N // 5
    count_15 = N // 15
    result = count_3 + count_5 - count_15
    return result
N = int(input().strip())
print(count_multiples(N))
