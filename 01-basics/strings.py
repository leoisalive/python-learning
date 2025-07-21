# author: Leonardo Luís
# date: 2025-07-21
# goal: Pratice strings in Python


# Ex01: Concatenate two strings and print the reversed result using a loop.
nome = "Leonardo"
apelido = "Luís"

resultado = nome + apelido
output = ""
for char in resultado:
    output = char + output

print(output)


# Ex02: Asks the user for a sentence and counts how many spaces it has.
frase = input("Digita uma frase: ")
space_count = 0
for char in frase:
    if char == " ":
       space_count += 1

print(f"A frase tem {space_count} espaços.")


# Ex03: Converts a string to uppercase, then only the first letter to uppercase.

string = "gato preto"

print(string.upper()) 

capitalized_string = ""

for char in range(len(string)):
    if char == 0:
        capitalized_string += string[char].upper()
    else:
        capitalized_string += string[char]

print(capitalized_string) 



