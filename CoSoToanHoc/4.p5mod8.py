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
def p5mod8(a,p):
    y =(p-1)//4
    d = nhanbinhphuongcolap(a,y,p)
    r = 0
    if(d==1):
        x = (p+3)//8
        r = nhanbinhphuongcolap(a,x,p)
    elif(d == p-1):
        k =(p-5)//8
        g = nhanbinhphuongcolap(4*a,k,p)
        r = (2*a)*g
    return r%p,(-r%p)
if __name__=="__main__":
    a  = 40
    p = 53
    print(p5mod8(a,p))