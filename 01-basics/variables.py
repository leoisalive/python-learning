# author: Leonardo Luís
# date: 2025-07-21
# goal: Pratice variables in Python

# Ex01: Store the result of 2+3*4 in a variable and print the result.
# Confirm if Python follows the correct order of operations.

resultado = 2 + 3 * 4
print(resultado)


# Ex02: Calculate the perimeter of a rectangle using the variables base and height.

base = 5
altura = 10
perimetro = 2 * (base + altura)
print(perimetro)

# Ex03: Calculate how much you will have in a savings account after 12 months, with simple interest.
# Use values such as: initial_deposit = 1000, monthly_interest = 0.01

deposito_inicial = 1000
juros_mensal = 0.01

# ** is exponentiation in Python

total = deposito_inicial * (1 + juros_mensal) ** 12
print(total)


# Ex04: Convert a temperature from Celsius to Fahrenheit.
# Use the formula: F = C * 9/5 + 32

celsius = 25
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)


# Ex05: Calculate the area of a circle with radius 7.
# Use the formula: A = π * r²

import math 
raio = 7
area = math.pi * raio ** 2
print(area)

