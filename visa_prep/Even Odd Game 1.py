number = input().strip()
sum_of_digits = sum(int(digit) for digit in number)
if sum_of_digits % 2 == 0:
    print("Vignesh")
else:
    print("Charan")
