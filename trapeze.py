import other_function

def trapeze(n):
    h = 0.5
    f = 0

    for i in range(0, 5000):
        f = f + (h * ((other_function.do_f_x(i + 0.5, n) + other_function.do_f_x(i + h + 0.5, n)) / 2))
        f = f + (h * ((other_function.do_f_x(i, n) + other_function.do_f_x(i + h, n)) / 2))
    print("Trapezoidal:\nI{0:d} = {1:.10f}\ndiff = {2:.10f}\n\n".format(n, f, other_function.abs(f - (3.14159265358979323846 / 2))))
    return
