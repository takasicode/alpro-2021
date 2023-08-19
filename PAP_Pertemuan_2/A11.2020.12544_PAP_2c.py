from pustaka import *

def main():
    num1 = 20
    num2 = 5

    print("Angka : " + str(num1) + " dan " + str(num2))
    print("Hasil penjumlahan : " + str(add(num1, num2)))
    print("Hasil pengurangan : " + str(subtract(num1, num2)))
    print("Hasil perkalian : " + str(multiply(num1, num2)))
    print("Hasil pembagian : " + str(divide(num1, num2)))

if __name__ == "__main__":
    main()