from Extended_Eculid import *

p = int(input("p = "))

q = int(input("q = "))

e = int(input("e = "))

c = int(input("c = "))

g, d, k = extended_eculid(e,(p-1)*(q-1))

if d < 0:

    d = (q-1)*(p-1)+d

m = pow(c,d) % (p*q)

print("Result:\n\n"+str(m))

