import math

def func_value(x):
    return x^3 - 3.125 * x^2 - 3.5 * x + 2.458

a = float(input())
b = float(input())
n = 0
e = 0.01

print(str(a) + " ")
print(str(b) + " ")

x = (a + b) / 2

while abs(a - b) > e and func_value(x) > e:
    x = (a + b) / 2
    print(str(x) + " " + str(func_value(a)) + " " + str(func_value(b)) + " " + str(func_value(x)) + str(abs(a - b)) + "\n")
    if func_value(a) * func_value(x) > 0:
        a = x
    else:
        b = x
    n += 1

x = (a + b) / 2
