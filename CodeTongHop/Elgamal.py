# giải mã vì mã hóa bấm máy còn nhanh hơn 
p = int(input("p = ")) 
a = int(input("a = ")) 
y1 = int(input("y1 = ")) 
y2 = int(input("y2 = ")) 

x = (pow(y1, (p-1-a), p)*y2) % p
print(f'x = {x}')
