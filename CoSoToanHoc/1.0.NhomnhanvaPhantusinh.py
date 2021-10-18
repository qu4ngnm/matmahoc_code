from random import randint
from math import sqrt
def findR_S(n):
    dem = 0
    n = n-1
    while n % 2 == 0:
        dem += 1
        n /= 2
    return dem, int(n)


def modular_pow(a, k, n):
    if k == 0:
        return 1
    b = 1
    A = a
    if k & 1 == 1:
        b = a
    for i in range(1, len(bin(k)[2:])):
        A = (A**2) % n
        if (k >> i) & 1 == 1:
            b = A*b % n
    return b


def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def miller_rabin(n, t=5):
    s, r = findR_S(n)
    arrRand = []
    for i in range(1, t+1):
        a = randint(2, n-2)
        while a in arrRand:
            a = randint(2, n-2)
        arrRand.append(a)
        if gcd(a, n) != 1:
            return False
        else:
            y = modular_pow(a, r, n)
            if y != 1 and y != n-1:
                j = 1
                while j <= s-1 and y != n-1:
                    y = (y**2) % n
                    if y == 1:
                        return False
                    j += 1
                if y != n-1:
                    return False
            return True


def pollard_rho(n, c=5):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5
    elif n % 7 == 0:
        return 7
    elif miller_rabin(n):
        return n
    a = 2
    b = 2
    while True:
        a = (a**2+c) % n
        b = (b**2+c) % n
        b = (b**2+c) % n
        d = gcd(abs(a-b), n)
        if 1 < d and d < n and miller_rabin(d):
            return d
        if d == n:
            # a = 2
            # b = 2
            # c -= 1
            return pollard_rho(n, c-1)


def analyze(n):
    coSo = list()
    soMu = list()

    while n != 1:

        dem = 0
        i = pollard_rho(n)
        while n % i == 0 and i != 1:
            dem += 1
            n //= i
        if dem > 0:
            coSo.append(i)
            soMu.append(dem)
    return coSo, soMu
def Phiole(n):
    if miller_rabin(n):
        return n-1
    cs,sm = analyze(n)
    s = 1
    for i in range(len(cs)):
        x = (1-(1/cs[i]))
        s = s*x
    return s*n
def GCD(a,b):
    while b > 0:
        tmp = a%b
        a = b
        b = tmp
    return a
def nhomnhan(n):
    arr = []
    for i in range(n):
        if(GCD(i,n) == 1):
            arr.append(i)
    return arr
def UocCuaPhiOle(n):
    arrp = []
    for i in range(1,n+1):
        if(n % i == 0):
            arrp.append(i)
    return arrp
def capcuaphantu(arr,arrp,n):
    ord = []
    for i in range(len(arr)):
        for j in range(len(arrp)):
            if ((arr[i] ** arrp[j])%n == 1):
                ord.append(arrp[j])
                break
    return ord
def tapi(phi,n):
    arrs = []
    phi = int(Phiole(n))
    for i in range(1,phi+1):
        if(GCD(phi,i) == 1):
            arrs.append(i)
    return arrs
def timPTS(n):
    phi = int(Phiole(n))
    p = n-1
    coso, somu = analyze(p)
    arrB = coso
    for i in range(2,n):
        flag=1
        for j in range(len(arrB)):
            if(i**(int(phi/arrB[j])) % n == 1) :                  
                flag = 0
        if flag==1:
            return i
        

def TapPTS(a,arrs,n):
    arrA = []
    for i in range(len(arrs)):
        x = (a**arrs[i]) % n
        arrA.append(x)
    return sorted(set(arrA))


if __name__ == '__main__':
    n = 25
    # Nếu a là phần tử sinh cho sẵn thì thay luôn a vào
    a = timPTS(n)
    print('Số a thỏa mãn là {}'.format(a))
    arr = nhomnhan(n)
    phi = int(Phiole(n))
    arrp = UocCuaPhiOle(phi)
    ord = capcuaphantu(arr,arrp,20)
    arrs = tapi(phi,n)
    arrA = TapPTS(a,arrs,n)
    print("Các ước của PhiOle {} la \n {}".format(phi,arrp))
    # in ra nhóm nhân Z*n của n
    print("Nhóm nhân Z*n của {} là \n {} ".format(n,arr))
    # in ra cấp của các phần tử trong Z*n 
    # có chu kì lặp lại 
    print("Cấp của các phần tử là \n {} ".format(ord))
    print('Tập i là \n {}'.format(arrs))
    print('Tập các phần tử sinh là \n {}'.format(arrA))




