import math

x = input('x = ')
if x.isnumeric():
    x = float(x)
    pi = math.pi
    if -pi <= x <= pi:
        y = math.cos(3 * x)
    else:
        y = x
    print('y =', y)
else:
    print('x must be anumber!')
