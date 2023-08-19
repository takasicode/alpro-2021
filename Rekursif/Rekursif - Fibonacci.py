'''Deret Fibonacci: 1,1,2,3,5,8,13,21,34,55,89,144... '''

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

x = int(input('Ingin mencari nilai fibonacci di baris keberapa? (dimulai dari 0) : '))
print(fib(x))

