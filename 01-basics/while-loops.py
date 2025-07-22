# author: Leonardo Luís
# date: 2025-07-22
# goal: Pratice while loops in Python

# 1. Count from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1



# 2. Sum from 1 to N (input from user)
# Ask the user for a number and sum from 1 to that number
# Example: If user inputs 5, output should be 15
# You can test with: n = int(input("Enter a number: "))

n = int(input("Enter a number: "))
i = 1
product=0

while i <= n:
    product+=i
    i += 1

print(product)
    

# 3. Countdown from N
# Ask user for a number and count down to 0
# Example: If input is 3, output: 3, 2, 1, 0

num = int(input("Enter a number: "))


while num > 0:
    print(num)
    num-=1

# 4. Ask numbers until user enters an even number
# Keep asking for a number and stop only when it's even

even = int(input("Insert an even number:"))

while even % 2 != 0:
    even = int(input(f"{even} is an odd number, please insert an even number:"))
else:
    print(even , "is an even number!")


