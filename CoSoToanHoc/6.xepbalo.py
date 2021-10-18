def xepbalo(arr,s,n):
    v = []
    for i in range(n-1,-1,-1):
            if(s>= arr[i]):              
                a = 1
                v.append(a)
                s = s - arr[i]
            else:
                a = 0
                v.append(a)    
    return list(reversed(v))
arr = [61,106,253,555,1728,3680,8658,24205]
s = 36857
n = len(arr)
print(xepbalo(arr,s,n))