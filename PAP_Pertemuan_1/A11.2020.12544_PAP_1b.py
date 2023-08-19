x=input("Masukkan Nama : ")
y=int(input("Masukkan berat badan : "))

if y <= 70 and y >= 51 :
    print("Hai," + x)
    print("Berat badanmu" ,int(y), "Kg termasuk Kurus")
elif y < 70 :
    print("Hai," + x)
    print("Berat badanmu" ,int(y), "Kg termasuk Normal")
else :
    print("Hai," + x)
    print("Berat badanmu" ,int(y), "Kg termasuk Gemuk")