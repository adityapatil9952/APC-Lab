
# Data Types

x = 100
print(type(x))

x = "hello"
print(type(x))

x = 3.14
print(type(x))

x = ["apple", "banana", "fruit"]
print(type(x))

x = {"apple", "banana"}
print(type(x))

x = ("apple", "banana")
print(type(x))

x = {("banana", "apple")}
print(type(x))

x = frozenset(["apple", "banana"])
print(type(x))

# List Operations

x = ["10", "20", "30"]
x.append(40)
print(x)

print(x[2])

# Tuple

y = (21, 45, 88)
print(y)

x = ("apple", "banana")
print(x)

# Arithmetic Operators

print(1 + 6)
print(68 - 45)
print(45 / 5)
print(56 * 89)
print(89 % 7)
print(87 ** 5)
print(34 // 3)

# Assignment Operators

x = 97

x += 34
print(x)

x -= 90
print(x)

x /= 2
print(x)

x //= 3
print(x)

x %= 5
print(x)

x **= 2
print(x)

# Comparison Operators

x = 9
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)

# Logical Operators

x = 7
y = 8

print(x > y and x < y)
print(x > y or x < y)
print(not(x > y))

# Identity Operators

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x is not z)

# Membership Operators

x = ["apple", "banana", "mango"]

print("apple" in x)
print("grapes" in x)
print("banana" not in x)

# Bitwise Operators

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

