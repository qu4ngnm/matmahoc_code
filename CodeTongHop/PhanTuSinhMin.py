from Factor import *



p = int(input("p = "))

factor_n = phanTichSoNguyen(p-1)

factor_n.append(1)

nghiem = []

for i in range(0, len(factor_n)-1):

    if (factor_n[i] != factor_n[i+1]):

        nghiem.append(factor_n[i])

k = []

for i in range(0, len(nghiem)):

    k.append((p-1)/(nghiem[i]))

a = int(input("A = "))

b = int(input("B = ")) 

c = int(input("C = "))

d = int(input("D = "))



print("Result :\n")



count = 0

for i in range(0,len(k)):

    if pow(a,k[i])%p!=1:

        count += 1

if count == len(k):

    print("A. "+str(a)+" True")



count = 0

for i in range(0,len(k)):

    if pow(b,k[i])%p!=1:

        count += 1

if count == len(k):

    print("B. "+str(b)+" True")



count = 0

for i in range(0,len(k)):

    if pow(c,k[i])%p!=1:

        count += 1

if count == len(k):

    print("C. "+str(c)+" True")



count = 0

for i in range(0,len(k)):

    if pow(d,k[i])%p!=1:

        count += 1

if count == len(k):

    print("D. "+str(d)+" True")









