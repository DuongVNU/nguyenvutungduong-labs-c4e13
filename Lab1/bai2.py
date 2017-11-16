n = int(input("Enter a number: "))
dem = 0
for i in range(2, n - 1):
    if n % i == 0:
        dem += 1;
if dem ==0:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
