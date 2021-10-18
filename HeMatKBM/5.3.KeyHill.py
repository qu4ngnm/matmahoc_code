import numpy as np


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


A = [[25, 8], [16, 21]]
B = [[5, 17], [8, 3]]
detA = (B[0][0]*B[1][1]-B[0][1]*B[1][0]) % 26  # detA = 53
detA1 = inversion(26, detA)  # detA ^ -1

B1 = [[(B[1][1]*detA1) % 26, (-B[0][1]*detA1) % 26],
      [(-B[1][0]*detA1) % 26, (B[0][0]*detA1) % 26]]


x = np.array(A)
y = np.array(B1)
z = np.array(np.remainder(x.dot(y), 26))
print(z)