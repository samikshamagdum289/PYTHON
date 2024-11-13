def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def floordivision(num1, num2):
    return num1 // num2

def modulus(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2

print("**ENTER HERE TWO VALUES**")
num1 = int(input("Enter the First Value: "))
num2 = int(input("Enter the Second Value: "))

add=addition(num1,num2)
print("Addition:",add)

sub=subtraction(num1,num2)
print("Subtraction:",sub)

mul=multiplication(num1,num2)
print("Multiplication:",mul)

div=division(num1,num2)
print("Division:",div)

floor_division=floordivision(num1,num2)
print("Floor Division is:",floor_division)

mod=modulus(num1,num2)
print("Modulus:",mod)

expo=exponent(num1,num2)
print("Exponent:",expo)

#OUTPUT:
# **ENTER HERE TWO VALUES**
# Enter the First Value: 22
# Enter the Second Value: 3
# Addition: 25
# Subtraction: 19
# Multiplication: 66
# Division: 7.333333333333333
# Floor Division is: 7
# Modulus: 1
# Exponent: 10648
