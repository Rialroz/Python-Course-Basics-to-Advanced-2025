# PYTHON DATA HANDLING CHALLENGE
# Aritmetic & Assigment

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")

# Comparison & Logical operations
a = float(input("Enter first comparison number: "))
b = float(input("Enter second comparison number: "))
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a >= b}")
print((a > b) and (b < a))

# Bitwise, Iddentity, and Membership operations

# Bitwise operations
print(f"BITWISE OPERATIONS")
x = 5
y = 3
print(f"Bitwise AND: {x} & {y} = {x & y}")
print(f"Bitwise OR: {x} | {y} = {x | y}")
print(f"Bitwise XOR: {x} ^ {y} = {x ^ y}")
print(f"Left Shift Operation: {x} << 1 = {x << 1}")

# Identity operations
print("IDENTITY OPERATIONS")
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
print(f"Are list1 and list2 the same object? {list1 is list2}")
print(f"Are list1 and list2 not the same object? {list1 is not list2}")

# Membership operations
print("MEMBERSHIP OPERATIONS")
print(f"2 in list1 {2 in list1}")
print(f"4 not in list2 {4 not in list2}")

# OPERATOR PRECEDENCE AND ASSOCIATIVITY
print("OPERATOR PRECEDENCE AND ASSOCIATIVITY")

exp1 = 5 + 2 * 3
print(f"Expression 5 + 2 * 3 = {exp1} (Multiplication has higher precedence than addition)")

exp2 = (4 + 2) * 6
print(f"Expression (4 + 2) * 6 = {exp2} (Parentheses change the order of operations)")