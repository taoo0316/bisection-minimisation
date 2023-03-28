def bisection(f, a, b, l):
    n = 0
    while b - a > l:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) > 0:
            b = c
        else:
            a = c
        n += 1
        print((a + b)/2)
        print(f((a + b)/2))
    return (a + b) / 2, n

def f(x):
    return -3 + 2*x - 5/(x**2)

a = 1
b = 4
l = 0.0001

x, n = bisection(f, a, b, l)

print("The approximate minimal point of the function is x ≈ {:.4f}".format(x))
print("The bisection method took {} iterations.".format(n))
