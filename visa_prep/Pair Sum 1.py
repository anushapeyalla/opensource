def find_pair(arr, k):
    seen = set()
    for num in arr:
        if k - num in seen:
            print("true")
            return
        seen.add(num)
    print("false")
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
find_pair(arr, k)
