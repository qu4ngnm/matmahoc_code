from random import randint
import re
import math
def jacobi(a,p,dauTru):
    x= (a,p)
    # print(f'(a/p) = ', x)
    if a % p == 0:
        print('KQ = 0')
    elif p % 2 == 0:
        print('p nhap vao phai la so le!')
    else:
        while x[0] != 1 and x[1] % 2 == 1:
            if x[0] > x[1] :
                x = (x[0] % x[1], x[1])
            elif x[0] < x[1] and x[0] % 2 == 1:
                if x[0] % 4 == 3 and x[1] % 4 == 3:
                    dauTru += 1
                x = (x[1], x[0])
            elif x[0] % 2 == 0 :
                if x[1] % 8 == 3 or x[1] % 8 == 5:
                    dauTru += 1
                x = (x[0] // 2, x[1])
            # print('= ' + (' ', '-')[dauTru % 2 == 1], x)
        arr = (' ', '-')[dauTru % 2 == 1], '1'
        if(arr[0] == ' '):
            return 1
        return -1
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

def timRvaS(n):
    dem = 0
    n = n-1
    while n % 2 == 0:
        dem += 1
        n /= 2
    return dem, int(n)
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
def pnguyento(a,p,dauTru):
    if(jacobi(a,p,dauTru)== -1):
        print("a không có căn bậc hai theo mod p")
    b = randint(1,p-1) 
    if (jacobi(b,p,dauTru) == 1):
        b = randint(1,p-1)
    an = p-1
    s,t = timRvaS(an)
    n = inverse(a,p)
    c = nhanbinhphuongcolap(b,t,p)
    r = nhanbinhphuongcolap(a,((t+1)//2),p)
    for i in range(s):
        dr = ((r*r)**(2**(s-i-1)))%p
        dn = (n**(2**(s-i-1)))%p
        d = dr*dn
        if (d==-1):
            r = (r*c)%p
        c = c*c%p
    return r,-r

    

        
if __name__=='__main__':
    a = int(input('Nhap a: '))
    p = int(input('Nhap n le : '))   
    dauTru = 0
    print(pnguyento(a,p,dauTru))
    