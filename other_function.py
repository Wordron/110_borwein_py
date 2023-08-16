from math import sin

def do_f_x(x, n):
    sum_result = 1

    if x >= -0.0001 and x <= 0.0001:
        return 1
    for i in range(0, n + 1):
        sum_result = sum_result * (sin(x / (2 * i + 1)) / (x / (2 * i + 1)))
    return sum_result

def abs(n):
    if n < 0:
        n = n * -1
    return n
