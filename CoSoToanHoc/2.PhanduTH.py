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

def GCD(a,b):
    while b != 0:
        t = a%b
        a = b
        b = t
    return a

def tinhN(n):
    s = 1
    for i in range(len(n)):
        s = s*n[i]
    return s


def tinhNi(s,n):
    ni = []
    for i in range(len(n)):
        x = s //n[i]
        ni.append(x)
    return ni


def tinhM(ni,n):
    m = []
    for i in range(len(n)):
        x = inverse(ni[i],n[i])
        m.append(x)
    return m


def phanduTH(a,s,ni,m):
    sum = 0
    for i in range(len(n)):
        sum += a[i]*ni[i]*m[i]
    return sum%s,s

if __name__=='__main__':
    a = [7,4,15]
    n = [9,10,23]
    # print(tinhN(n))
    s = tinhN(n)
    # print(tinhNi(s,n))
    ni = tinhNi(s,n)
    # print(tinhM(ni,n))
    m = tinhM(ni,n)
    a,b = phanduTH(a,s,ni,m)
    print('x = {} mod {}'.format(a,b))
    # print(a%b)