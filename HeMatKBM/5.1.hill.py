import re


def inversion(p, a):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = v//u
        r = v-q*u
        x = x2-q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p


def encrypt(plainText, B):
    subString = re.findall('\w{2}', plainText)
    ct = []
    for i in subString:
        x = [ord(i[0])-ord('a'), ord(i[1])-ord('a')]
        result = [chr((x[0]*B[0][0]+x[1]*B[1][0]) %
                      26+ord('a')), chr((x[0]*B[0][1]+x[1]*B[1][1]) % 26+ord('a'))]
        ct.append(''.join(result))
    return str(''.join(ct))


def decrypt(cipherText, B):
    subString = re.findall('\w{2}', cipherText)
    ct = []
    for i in subString:
        x = [ord(i[0])-ord('a'), ord(i[1])-ord('a')]
        result = [chr((x[0]*B[0][0]+x[1]*B[1][0]) %
                      26+ord('a')), chr((x[0]*B[0][1]+x[1]*B[1][1]) % 26+ord('a'))]
        ct.append(''.join(result))
    return str(''.join(ct))


if __name__ == '__main__':
    plainText = 'july'

    B = [[11, 8],
         [3, 7]]

    detA = B[0][0]*B[1][1]-B[0][1]*B[1][0]  # detA = 53
    detA1 = inversion(26, detA)  # detA ^ -1

    B1 = [[(B[1][1]*detA1) % 26, (-B[0][1]*detA1) % 26],
          [(-B[1][0]*detA1) % 26, (B[0][0]*detA1) % 26]]

    print(encrypt(plainText, B))
    cipherText = encrypt(plainText, B)
    print(decrypt(cipherText, B1))
    