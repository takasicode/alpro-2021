def luas_persegi(n):
    return n * n

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def is_besar(n):
    bilangan = []
    cetak = ""
    for i in range(1, n+1):
        cetak += str(i) + " "
        bilangan.append(i)
        
    print(cetak)
    return bilangan[n-1]

def is_kecil(n):
    bilangan = []
    cetak = ""
    for i in range(1, n+1):
        cetak += str(i) + " "
        bilangan.append(i)

    print(cetak)
    return bilangan[0]

def is_ganjil(n):
    if n % 2 != 0:
        return True
    else:
        return False

def is_genap(n):
    if n % 2 == 0:
        return True
    else:
        return False

def to_positive(n):
    if n < 0:
        n *= -1
    return n

def to_negative(n):
    if n > 0:
        n *= -1
    return n

def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i    
    return total

def avg_n(n):
    return sum_n(n) / n

print(to_positive(-10))