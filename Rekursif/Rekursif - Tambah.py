def tambah(m,n):
    x = 0
    if n == 0:
        x = m
    else:
        x = tambah(m,n-1)+1
    return x

m,n = list(map(int,input('Masukkan dua bilangan: ').split()))
print(tambah(m,n))