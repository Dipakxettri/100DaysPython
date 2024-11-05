# Operators in Python

# 1. Arithmetic Operators
# Used to perform mathematical operations.
# +  : Addition
# -  : Subtraction
# *  : Multiplication
# /  : Division (returns float)
# // : Floor Division (returns integer)
# %  : Modulus (returns the remainder)
# ** : Exponentiation (power)

# Example:
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation

# 2. Comparison Operators
# Used to compare two values.
# == : Equal
# != : Not Equal
# >  : Greater than
# <  : Less than
# >= : Greater than or Equal to
# <= : Less than or Equal to

# Example:
print("\nComparison Operators:")
print("a == b:", a == b)  # Equal
print("a != b:", a != b)  # Not Equal
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or Equal to
print("a <= b:", a <= b)  # Less than or Equal to

# 3. Assignment Operators
# Used to assign values to variables.
# =    : Assign
# +=   : Add and assign
# -=   : Subtract and assign
# *=   : Multiply and assign
# /=   : Divide and assign
# //=  : Floor Divide and assign
# %=   : Modulus and assign
# **=  : Exponentiate and assign

# Example:
print("\nAssignment Operators:")
c = 5
print("Initial value of c:", c)
c += 2  # Add and assign
print("c += 2 =>", c)
c *= 3  # Multiply and assign
print("c *= 3 =>", c)

# 4. Logical Operators
# Used to combine conditional statements.
# and : Returns True if both statements are true
# or  : Returns True if at least one statement is true
# not  : Returns True if the statement is false

# Example:
print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT

# 5. Bitwise Operators
# Used to perform bit-level operations.
# &  : Bitwise AND
# |  : Bitwise OR
# ^  : Bitwise XOR
# ~  : Bitwise NOT
# << : Bitwise Left Shift
# >> : Bitwise Right Shift

# Example:
print("\nBitwise Operators:")
x = 10  # 1010 in binary
y = 4   # 0100 in binary
print("x & y =", x & y)  # Bitwise AND
print("x | y =", x | y)  # Bitwise OR
print("x ^ y =", x ^ y)  # Bitwise XOR
print("~x =", ~x)        # Bitwise NOT
print("x << 1 =", x << 1)  # Left Shift
print("x >> 1 =", x >> 1)  # Right Shift

# 6. Identity Operators
# Used to check if two variables point to the same object.
# is  : Returns True if both variables are the same object
# is not : Returns True if both variables are not the same object

# Example:
print("\nIdentity Operators:")
a = [1, 2, 3]
b = a
c = a.copy()
print("a is b:", a is b)      # True
print("a is c:", a is c)      # False
print("a is not c:", a is not c)  # True

# 7. Membership Operators
# Used to test if a value is found in a sequence (like a list, tuple, or string).
# in    : Returns True if a value is found in the sequence
# not in: Returns True if a value is not found in the sequence

# Example:
print("\nMembership Operators:")
my_list = [1, 2, 3, 4, 5]
print("2 in my_list:", 2 in my_list)       # True
print("6 not in my_list:", 6 not in my_list)  # True