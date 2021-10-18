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
def p3mode4(a,p):
    y = (p+1)//4
    x = nhanbinhphuongcolap(a,y,p)
    return x,(-x%p)
if __name__=="__main__":
    a  = 184
    p = 211
    print(p3mode4(a,p))