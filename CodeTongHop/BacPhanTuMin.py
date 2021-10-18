a = int(input("A = "))
b = int(input("B = ")) 
c = int(input("C = "))
d = int(input("D = "))

p = int(input("P = "))

print("Result :\n ")

for i in range(1,p):
    if pow(a,i)%p==1:
        print("A. "+str(i))
        break
for i in range(1,20):
    if pow(b,i)%p==1:
        print("B. "+str(i))
        break
for i in range(1,20):
    if pow(c,i)%p==1:
        print("C. "+str(i))
        break

for i in range(1,20):
    if pow(d,i)%p==1:
        print("D. "+str(i))
        break
        