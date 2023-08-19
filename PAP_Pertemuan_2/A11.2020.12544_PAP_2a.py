def getSmaller(num1, num2):
    smaller = num1
    if num1 > num2:
        smaller = num2

    return smaller

num1 = 10
num2 = 20
print("Bilangan terkecil diantara " + str(num1) + " dan " + str(num2) + " adalah : " + str(getSmaller(num1, num2)))