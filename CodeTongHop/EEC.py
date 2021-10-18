from Extended_Eculid import *

p=int(input("Nhap p = "))

x1=int(input("Nhap x1 = "))

y1=int(input("Nhap y1 = "))

x2=int(input("Nhap x2 = "))

y2=int(input("Nhap y2 = "))

if x1==x2 and y1==y2:

    k1=(3*x1*x1+1)

    k2=(2*y1)

    if k2<0:

        k2=-k2

        k1=-k1

    if k1%k2==0:

        k=(k1/k2)%p

    else:

        g,a,b = extended_eculid(k2, p)

        k=(k1*a)%p

else:

    k1=(y2-y1)

    k2=(x2-x1)

    if k2<0:

        k2=-k2

        k1=-k1 

    if k1%k2==0:

        k=(k1/k2)%p

    else:

        g,a,b = extended_eculid(k2, p)

        k=(k1*a)%p

x=(k*k-x1-x2)%p

y=(k*(x1-x)-y1)%p

print("x =",x,"\ty =",y)











