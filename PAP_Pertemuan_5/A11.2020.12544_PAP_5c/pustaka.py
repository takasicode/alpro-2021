def InsertionSort(A):
    n = len(A)
    temp = 0    
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j >= 0 and temp < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp

def InputData(Id, nama, harga, n) :
    for i in range(n) :
        Id[i] = int(input("Masukkan ID : "))
        nama[i] = input("Masukkan Nama Produk : ")
        harga[i] = int(input("Masukkan Harga : "))

def LihatData(Id, nama, produk, n) :
    print("ID, Nama Produk, Harga")
    for i in range(n) :
        print(Id[i], ",", nama[i], ",", produk[i])

def LihatDataTerurut(Id, nama, produk, n) :
    print("ID, Nama Produk, Harga")
    InsertionSort(Id)
    for i in range(n) :
        print(Id[i], ",", nama[i], ",", produk[i])