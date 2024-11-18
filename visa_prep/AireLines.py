import math
current_planes, total_passengers = map(int, input().split())
print(max(0, math.ceil((total_passengers - current_planes * 100) / 100)))
