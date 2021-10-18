import math
def log(a,j,n):
    arr = []
    for i in range(j):
        x = a**i % n
        arr.append(x)
    return arr

def bangi(b,a,j,n):
    arr = []
    for i in range(j):
        x = (b*(a**i))%n
        arr.append(x)
    return arr

def ktr(a,b):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == b[j]:
                return j,i

def nhanbinhphuongcolap(a,k,n):
    b = 1
    if k == 0:
        return b
    A = a
    if k&1 == 1:
        b = a 
    for i in range (1, len(bin(k))-2):    
        A = (A**2)%n 
        if (k >> i)&1 == 1:
            b = (A*b) % n 
    return b 

def inverse(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = math.floor(v/u)
        r = v - u*q
        x = x2 - x1*q
        v = u
        u = r
        x2 = x1
        x1 = x
    return (x1%p)  

def tinhc(a,n,j):
    x = inverse(a,n)
    y = nhanbinhphuongcolap(x,j,n)
    return y

if __name__ == "__main__":
    # cơ số dưới của log
    a = 2
    # cơ số trên
    b = 22
    # trường p
    n = 83
    # căn của ord
    j = math.ceil(math.sqrt(n-1))
    # print(j) 
    # giá trị của a^-j mod p
    c = tinhc(a,n,j)
    an = log(a,j,n)
    bn = bangi(b,c,j,n)
    # print(bn)
    x,y = ktr(an,bn)
    # print(ktr(an,bn))
    print(j*x+y)