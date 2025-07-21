# author: Leonardo Luís
# date: 2025-07-21
# goal: Pratice conditions in Python

# Ex01: Ask the user for their age and tell them if they can vote or not.

idade = int(input("Por favor insira a sua idade:"))

if idade < 18:
    print("Ainda não tem idade para votar")
else:
    print("Já atingiu a idade necessária para votar!")

# Ex02: Ask the user for a number and tell them if it is positive, negative or zero.

numero = int(input("Por favor insira um numero"))

if numero > 0:
    print("O número que insiriu é positivo!")
elif numero < 0:
    print("O número que insiriu é negativo!")
else:
    print("Insiriu o número 0")

# Ex03: Simulate a login system with if/else.
# username = "leonardo", password = "1234"
# Verifies if the user input is correct.

username = "leonardo"
password = "1234"

input_username = input("Insira o seu nome de utilizador:")

input_password = input("Insira a sua password:")

if input_username == username and input_password == password:
    print("Os seus dados estão corretos!")
elif input_username == username:
    print("A palavra passe que introduziu está errada!")
else:
    print("Os dados que inseriu estão errados!")

