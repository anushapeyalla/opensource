m = int(input())
seasons = ["Winter", "Spring", "Summer", "Autumn", "Winter"]
print(seasons[m // 3] if 1 <= m <= 12 else "Invalid")
