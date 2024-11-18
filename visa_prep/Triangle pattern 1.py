N = int(input())
counter = 1
for row in range(1, N + 1):
    for _ in range(row):
        print(counter, end=" ")
        counter += 1
    print()
