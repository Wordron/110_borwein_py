import other_function

def add_two(n):
    sum_result = 0

    for i in range(0, 10000):
        sum_result = sum_result + other_function.do_f_x(i * 0.5 + 0.25, n)
    return sum_result

def add_one(n):
    sum_result = 0

    for i in range(1, 10000):
        sum_result = sum_result + other_function.do_f_x(i * 0.5, n)
    return sum_result

def simpson(n):
    f = (1/12) * (other_function.do_f_x(0, n) + other_function.do_f_x(5000, n) + (2 * add_one(n)) + (4 * add_two(n)))

    print("Simpson:\nI{0:d} = {1:.10f}\ndiff = {2:.10f}".format(n, f, other_function.abs(f - (3.14159265358979323846 / 2))))
    return
