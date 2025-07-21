# author: Leonardo Luís
# date: 2025-07-21
# goal: Pratice loops in Python



# Ex01: Print even numbers between 1 and 100.
# % 2 == 0 checks if the number is even.
for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)

        

# Ex02: Ask the user for a number and print its multiplication table up to 10.

#Input has to be converted to int to perform mathematical operations
tabuada = int(input("Insira um número:"))
resultado = 0

for i in range(1, 11):
    resultado = tabuada * i
    print(resultado)


# Ex03: Simulates 10 dice rolls (1 to 6) and counts how many times each number appears.
#you can use `random.randint(1,6)` with `import random`

import random
lancamentos = [random.randint(1, 6) for _ in range(10)]

print("Contagem de lançamentos:")

#range(1, 7) generates numbers from 1 to 6
for i in range(1, 7):
    # .count() counts how many times the number appears in the list
    print(f"O número {i} saiu {lancamentos.count(i)} vezes") 


# Ex04: Prints the numbers from 1 to 50, but replaces multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".


for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Just need to check if the number is a multiple of 3 because we already checked if it is a multiple of both above.
    elif i % 3 == 0:
        print("Fizz")
    #just need to check if the number is a multiple of 5 because we already checked if it is a multiple of both above.
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 




