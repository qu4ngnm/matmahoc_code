from Extended_Eculid import *

a = int(input("p = "))
b = int(input("q = "))
g, x, y = extended_eculid(a, b)
print("GCD = ", g, "\ta = ", x, "\tb = ", y)
