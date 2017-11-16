numbers = [7, 5, 2, 6, 9, 6, 8, 2, 3, 6, 1, 5, 2, 7]
print("number = ", numbers)
x = int(input("Enter a number? "))
dem = 0
for a, b in enumerate(numbers):
    if x == b:
        dem = dem + 1
print("{0} appears {1} times in my list".format(x, dem))
