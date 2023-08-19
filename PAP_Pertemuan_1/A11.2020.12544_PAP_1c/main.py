from pustaka import *

def main():
    n = int(input("Masukkan angka: "))
    print("Luas persegi adalah: ", str(luas_persegi(n)))
    print("Factorial n: ", str(fact(n)))
    print("Bilangan terbesar adalah: ", str(is_besar(n)))
    print("Bilangan terkecil adalah: ", str(is_kecil(n)))
    print("Apakah n bilangan ganjil: ", str(is_ganjil(n)))
    print("Apakah n bilangan genap: ", str(is_genap(n)))
    print("Bilangan integer positif: ", str(to_positive(n)))
    print("Bilangan integer negatif: ", str(to_negative(n)))
    print("Jumlah bilangan n: ", str(sum_n(n)))
    print("Rata-rata n: ", str(avg_n(n)))

if __name__ == "__main__":
    main()