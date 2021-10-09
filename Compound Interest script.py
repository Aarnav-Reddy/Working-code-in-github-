import math
a = num =float(input("Enter the principal:"))
b = num =float(input("Enter the rate of interest:"))
c = num =float(input("Enter the time:"))
d = a*(1+b/100)**c
z = str(input(("calculate amount?"'y''n:')))
e = 'y'
f = 'n'
if e: print("This is the amount:", d)
else: print("This is the compound interest:", d-a)