N = int(input())
M = int(input())
if N & (1 << (M - 1)):
    print("true")
else:
    print("false")
