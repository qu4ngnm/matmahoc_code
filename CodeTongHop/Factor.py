def phanTichSoNguyen(n):
    i = 2
    listNumbers = []
    while (n > 1):
        if (n % i == 0):
            n /= i
            listNumbers.append(i)
        else:
            i+= 1
    if (len(listNumbers) == 0):
        listNumbers.append(n)
    return listNumbers


print(phanTichSoNguyen(24)) 