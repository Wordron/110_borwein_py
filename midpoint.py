import other_function

def midpoint(n):
    h = 0.5
    f = 0

    for x in range(0, 5000):
        f = f + (h * other_function.do_f_x((x + 0.5) + 0.25, n))
        f = f + (h * other_function.do_f_x(x + 0.25, n))
    print("\nMidpoint:\nI{0:d} = {1:.10f}\ndiff = {2:.10f}\n\n".format(n, f, other_function.abs(f - (3.14159265358979323846 / 2))))
    return
