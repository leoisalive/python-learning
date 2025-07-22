# author: Leonardo Luís
# date: 2025-07-22
# goal: Pratice while loops in Python

# 1. Password prompt
# Keep asking user to enter the password until they type "python123"

password="python123"

user_password = input("Please type your password:")

while user_password != password:
    user_password = input("The password you typed is wrong, please try again:")
else:
    print("The password you typed is correct!")


# 2. ATM pin checker with 3 attempts
# Pin is 4321. Block access after 3 incorrect tries.

pin = 4321
tries = 3

while tries > 0:
    user_pin = int(input("Please insert your ATM PIN:"))
    if user_pin == pin:
        print("The PIN you inserted is correct!")
        break
    else:
        tries -= 1
        if tries == 0:
            print("You have reached the limit of tries!")
        else:
            print(f"The PIN you inserted is wrong, please try again. You have {tries} more tries left.")




# 3. Ask user for numbers until total sum reaches at least 100

total = 0

while total < 100:
    number = int(input("Por favor digite um número:"))
    total += number
else:
    print(f"Os números que inseriu dão um total de {total}")


# 4. Guess the number (between 1 and 10)
# Hardcode a number, and ask user to guess until they get it right

import random

number = random.randint(1, 10)

guess_number=0

while guess_number != number:
    guess_number=int(input("Tente adivinhar o número de 1 a 10:"))
else:
    print(f"Adivinhou o número! {guess_number}")

