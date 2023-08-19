def getSmaller(num1, num2):
    smaller = num1
    if num1 > num2:
        smaller = num2

    return smaller

num1 = 5
num2 = 10
num3 = 15
print("Bilangan terkecil diantara " + str(num1) + ", " + str(num2) + ", dan " + str(num3) + " adalah : " + str(getSmaller(getSmaller(num1, num2), num3)))