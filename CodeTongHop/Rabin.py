from Extended_Eculid import*



p = int(input("p = "))

q = int(input("q = "))

x = int(input("x = "))



print("Result :\n")

y = x*x % (p*q)

print("y = "+str(y))

g, a, b = extended_eculid(p, q)

print("a = "+str(a)+"\tb = "+str(b))

r = pow(y,(p+1)/4) % p

s = pow(y,(q+1)/4) % q

print("r = "+str(r)+"\ns = "+str(s))

x1 = (a*p*s + b*q*r) % (p*q)

y1 = (a*p*s - b*q*r) % (p*q)

x2 = (p*q) - x1

y2 = (p*q) - y1

print(str(x1)+"\t"+str(y1)+"\t"+str(x2)+"\t"+str(y2))

