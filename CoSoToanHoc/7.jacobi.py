
a = int(input('Nhap a: '))
n = int(input('Nhap n le : '))
x = (a, n)
dauTru = 0

print(f'(a/n) = ', x)
if a % n == 0:
    print('KQ = 0')
elif n % 2 == 0:
    print('n nhap vao phai la so le!')
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
    print('KQ: '+(' ', '-')[dauTru % 2 == 1], '1')
