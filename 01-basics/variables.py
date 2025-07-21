# Ex01: Guarda o resultado de 2+3*4 numa variável e imprime o resultado.
# Confirma se o Python segue a ordem correta de operações.

resultado = 2 + 3 * 4
print(resultado)


# Ex02: Calcula o perímetro de um retângulo com base em base e altura (usando variáveis).

base = 5
altura = 10
perimetro = 2 * (base + altura)
print(perimetro)

# Ex03: Calcula quanto vais ter numa conta poupança após 12 meses, com juros simples.
# Usa valores como: deposito_inicial = 1000, juros_mensal = 0.01

deposito_inicial = 1000
juros_mensal = 0.01

#** é exponenciação em Python

total = deposito_inicial * (1 + juros_mensal) ** 12
print(total)


# Ex04: Converte uma temperatura de Celsius para Fahrenheit.
# Usa a fórmula: F = C * 9/5 + 32

celsius = 25
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)


# Ex05: Calcula a área de um círculo com raio 7.
# Usa a fórmula: A = π * r²

import math 
raio = 7
area = math.pi * raio ** 2
print(area)

