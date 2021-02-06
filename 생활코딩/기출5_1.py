import math
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
x = (c - 20 * b) / (a - 2 * b)
y = (c - a * x) / b
print(x, y)
