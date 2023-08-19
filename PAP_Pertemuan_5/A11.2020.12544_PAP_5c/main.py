import pustaka

def main() :
    n = int(input("Masukkan kapasitas barang : "))
    print("Kapasitas Barang :",n,"\n")

    Id = [int]*n
    Nama_Produk = [str]*n
    Harga = [int]*n

    while True :
        print("Pilih Menu :\n1.InputData \n2.LihatData \n3.LihatDataTerurut \n0.Keluar \n")
        menu = int(input("Pilih Angka : "))

        if menu == 1 :
            pustaka.InputData(Id, Nama_Produk, Harga, n)
        elif menu == 2 :
            pustaka.LihatData(Id, Nama_Produk, Harga, n)
        elif menu == 3 :
            pustaka.LihatDataTerurut(Id, Nama_Produk, Harga, n)
        elif menu == 0 :
            break
        else :
            print("Eror, harap masukkan angka 1/2/3 atau 0 untuk keluar.")

if __name__ == '__main__' :
    main()