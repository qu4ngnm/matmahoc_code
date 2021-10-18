def xep_balo(m, s):
    i = len(m) - 1
    while i >= 0: 
        if s >= m[i]:
            v = 1
            s -= m[i]
        else:
           v = 0
        i -= 1
        print(s+m[i+1], "\t", m[i+1] ,"\t", v)
m = [2, 7, 11, 21, 42, 89, 180, 351]
s = 646
print("S\t Mi\t Vi")
xep_balo(m, s)
