# author: Leonardo Luís
# date: 2025-07-24
# goal: Pratice nested loops in Python

# 1️⃣ Print a 5x5 grid of "*"
# Output example:
# *****
# *****
# *****
# *****
# *****
for i in range(5):
    char = ""
    for j in range(5):
        char += "*"
    print(char)


# 2️⃣ Multiplication table from 1 to 10
# Output example:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 10 x 10 = 100

for i in range (1, 11):
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")


# 3️⃣ Print all coordinate pairs in a 3x3 grid
# Output example:
# (0, 0)
# (0, 1)
# ...
# (2, 2)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"({i},{j})")

# 4️⃣ Count how many times each letter appears in a list of words
# Example list: ["hi", "hello"]
# Output example:
# h: 2
# i: 1
# e: 1
# l: 2
# o: 1



# 5️⃣ Flatten a nested list (e.g. [[1, 2], [3, 4], [5]])
# Result should be [1, 2, 3, 4, 5]

# 6️⃣ Build a pattern like this (use numbers):
# 1
# 12
# 123
# 1234
# 12345
