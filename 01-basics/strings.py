# Ex01: Concatena duas strings e escreve o resultado invertido usando um loop.
nome = "Leonardo"
apelido = "Luís"

resultado = nome + apelido
output = ""
for char in resultado:
    output = char + output

print(output)


# Ex02: Pede ao utilizador uma frase e conta quantos espaços tem.
frase = input("Digita uma frase: ")
space_count = 0
for char in frase:
    if char == " ":
       space_count += 1

print(f"A frase tem {space_count} espaços.")


# Ex03: Transforma uma string em maiúsculas, depois só a primeira letra em maiúscula.

string = "gato preto"

print(string.upper()) 

capitalized_string = ""

for char in range(len(string)):
    if char == 0:
        capitalized_string += string[char].upper()
    else:
        capitalized_string += string[char]

print(capitalized_string) 



