a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / 2 * a
x2 = (-b - d ** 0.5) / 2 * a
print('x1 = ', x1, '; x2 = ', x2, sep = '')
