# Ex01: Imprime os números pares entre 1 e 100.
# % 2 == 0 verifica se o número é par.
for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)

        

# Ex02: Pede ao utilizador um número e imprime a tabuada desse número até 10.

#input tem que ser convertido para int para poder fazer operações matemáticas
tabuada = int(input("Insira um número:"))
resultado = 0

for i in range(1, 11):
    resultado = tabuada * i
    print(resultado)


# Ex03: Simula 10 lançamentos de dados (1 a 6) e conta quantas vezes saiu cada número.
# (podes usar `random.randint(1,6)` com `import random`)

import random
lancamentos = [random.randint(1, 6) for _ in range(10)]

print("Contagem de lançamentos:")

#range(1, 7) gera números de 1 a 6
for i in range(1, 7):
    #  .count() conta quantas vezes o número aparece na lista
    print(f"O número {i} saiu {lancamentos.count(i)} vezes") 


# Ex04: Imprime os números de 1 a 50, mas substitui múltiplos de 3 por "Fizz", múltiplos de 5 por "Buzz" e múltiplos de ambos por "FizzBuzz".


for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # basta verificar se o número é múltiplo de 3 porque em cima já verificamos se é múltiplo de ambos
    elif i % 3 == 0:
        print("Fizz")
    # basta verificar se o número é múltiplo de 5 porque em cima já verificamos se é múltiplo de ambos
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 




