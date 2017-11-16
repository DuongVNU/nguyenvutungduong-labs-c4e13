n1 = 1
n2 = 0
tong = 0
month = int(input("Enter the number of month: "))
for i in range(month + 1):
    tong = n1 + n2
    n1 = tong
    n2 = n1
    print("Month {0}: {1} pair(s) of rabbit.".format(i, tong))
