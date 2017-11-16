bacteria = int(input("How many B bacterias are there? "))
tg1 = int(input("How much time in minutes will we have wait?"))
tg2 = tg1
if tg1 % 2 == 0:
    tg2 = tg2/2
else:
    tg2 = (tg2 - 1)/2
n = bacteria * (2 ** tg2)
print("After {0} minutes, we would have {1} bacterias".format(tg1, n))
