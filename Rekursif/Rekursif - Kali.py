def kali(a,b):
    if b == 1:
        return a
    else :
        return a+kali(a,b-1)

m,n = list(map(int,input('Masukkan dua bilangan: ').split()))
print(kali(m,n))