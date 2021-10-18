def gen_key_Merkle_Hellman(n,M,W,daysieutang,hoanvi):
      arr = ['']*n
      for i in range(n):
         arr[i] = daysieutang[hoanvi[i] - 1]
      for i in range(n):
         arr[i] = arr[i]*W%M
      ke = arr
      kd = hoanvi,M,W,daysieutang
      return ke,kd

def encrypt_Merkle_Hellman(ke,m):
    c = 0
    for i in range(len(m)):
       if m[i] == "1":
         c += ke[i]
    return c

def decrypt_Merkle_Hellman(kd,c):
   hoanvi, M, W, daysieutang = kd
   d = c*pow(W,-1,M)%M
   S = d
   arr = []
   for i in range(len(daysieutang)):
     if S >= daysieutang[i]:
       arr.append('1')
       S = S-daysieutang[i]
     else:
        arr.append('0')
   a = ['']*len(arr)
   for i in range(len(arr)):
     a[i] = arr[hoanvi[i]-1]
   return ''.join(a)

M = 737
W = 635  
daysieutang = [12,17,33,74,157,316]
hoanvi = [3,6,1,2,5,4]
n = 6

ke,kd = gen_key_Merkle_Hellman(n,M,W,daysieutang,hoanvi)
print(f'Khoá công khai : {ke}')
print(f'Khoá bí mật : {kd}')

m = "101101"

c = encrypt_Merkle_Hellman(ke,m)
print(f'bản mã : {c}(10)')

m = decrypt_Merkle_Hellman(kd,c)
print(f'bản rõ : {m}(2)')
