import math
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
def timp(p,q,e):
    phin = (1-p)*(1-q)
    d = inverse(e,phin)
    return d
def encryptRSA(m,e,n):
    c = nhanbinhphuongcolap(m,e,n)
    return c

def decryptRSA(c,d,n):
    m = nhanbinhphuongcolap(c,d,n)
    return m

if __name__ == '__main__':
    p = 17
    q = 13
    n = p*q
    # số e được chọn sao cho gcd(e,phi(n)) = 1
    e = 35
    # d là khóa bí mật sao cho e.d = 1 mod phi(n)
    d = 11
    # m bản đã mã hóa
    m = 78 
    # c bản rõ
    c = 65
    print(timp(p,q,e))
    print(encryptRSA(m,e,n))
    print(decryptRSA(c,d,n))