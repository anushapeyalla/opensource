N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    left, right = sum(A[:i]), sum(A[i+1:])
    print(abs(left - right), end=" ")
