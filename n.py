import math

print("The sum is = 1")
print("Convert Celsius to Fahrenheit = 2")
print("Convert Fahrenheit to Celsius = 3")
print("Area and perimeter of the rectangle = 4")
print("Perimeter and area of the circle = 5")

a = (input("Please enter the desired option: "))

if a == "1":
    b = int(input(' No. 1: '))
    c = int(input(' No. 2: '))
    print("Result of Sum: ", c + b)

elif a == "2":
    d = int(input(' Celsius: '))
    e = d * 9 / 5 + 32
    print(d , 'Celsius = Fahrenheit: ', e)

elif a == "3":
    f = int(input(' Fahrenheit: '))
    g = (f - 32)/ 9 * 5
    print(f , 'Fahrenheit = Celsius: ', g)

elif a == "4":
    h = int(input('the length: '))
    i = int(input(' Width: '))
    j = h * i 
    k = 2 * (h + i)
    print ( j , "= Area and", k , "= perimeter")

elif a == "5":
    l = int(input(' Radius: '))
    m = l ** 2 * math.pi
    n = l * 2 * math.pi
    print( m , "= Area and", n , "= perimeter")