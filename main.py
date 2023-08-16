import math

def do_f_x(x, n):
    sum_result = 1

    if x >= -0.0001 and x <= 0.0001:
        return 1
    for i in range(0, n + 1):
        sum_result = sum_result * (math.sin(x / (2 * i + 1)) / (x / (2 * i + 1)))
    return sum_result

def abs(n):
    if n < 0:
        n = n * -1
    return n

# Midpoint technique_______________________________

def midpoint(n):
    h = 0.5
    f = 0

    for x in range(0, 5000):
        f = f + (h * do_f_x((x + 0.5) + 0.25, n))
        f = f + (h * do_f_x(x + 0.25, n))
    print("\nMidpoint:\nI{0:d} = {1:.10f}\ndiff = {2:.10f}\n\n".format(n, f, abs(f - (3.14159265358979323846 / 2))))
    return
#__________________________________________________

# Trapeze technique________________________________

def trapeze(n):
    h = 0.5
    f = 0

    for i in range(0, 5000):
        f = f + (h * ((do_f_x(i + 0.5, n) + do_f_x(i + h + 0.5, n)) / 2))
        f = f + (h * ((do_f_x(i, n) + do_f_x(i + h, n)) / 2))
    print("Trapezoidal:\nI{0:d} = {1:.10f}\ndiff = {2:.10f}\n\n".format(n, f, abs(f - (3.14159265358979323846 / 2))))
    return
#__________________________________________________

# Simpson technique________________________________

def add_two(n):
    sum_result = 0

    for i in range(0, 10000):
        sum_result = sum_result + do_f_x(i * 0.5 + 0.25, n)
    return sum_result

def add_one(n):
    sum_result = 0

    for i in range(1, 10000):
        sum_result = sum_result + do_f_x(i * 0.5, n)
    return sum_result

def simpson(n):
    f = (1/12) * (do_f_x(0, n) + do_f_x(5000, n) + (2 * add_one(n)) + (4 * add_two(n)))

    print("Simpson:\nI{0:d} = {1:.10f}\ndiff = {2:.10f}\n\n".format(n, f, abs(f - (3.14159265358979323846 / 2))))
    return
#___________________________________________________

user_input = int(input("Enter n : "))

midpoint(user_input)
trapeze(user_input)
simpson(user_input)
