k = int(input("k ="))

a = int(input("A = "))
b = int(input("B = ")) 
c = int(input("C = "))
d = int(input("D = "))

p = int(input("P = "))


print("Result :\n")

for i in range(1, p):
    if pow(k,i)%p==a:
        print("A. "+str(i))
        
for i in range(1, p):
    if pow(k,i)%p==b:
        print("B. "+str(i))

for i in range(1, p):
    if pow(k,i)%p==c:
        print("C. "+str(i))

for i in range(1, p):
    if pow(k,i)%p==d:
        print("D. "+str(i))
