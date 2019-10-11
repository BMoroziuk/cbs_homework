def calc(a, b, op):
    if op == '+':
        return sum(a, b)
    elif op == '-':
        return min(a, b)
    elif op == '*':
        return umn(a, b)
    elif op == '/':
        if b > 0:
            return div(a, b)
        else:
            return 'Zero division!'


def sum(a, b):
    return a + b


def min(a, b):
    return a - b


def umn(a, b):
    return a * b


def div(a, b):
    return a / b


while True:
    a = input('>')
    op = input('>')
    b = input('>')
    if a.isnumeric() and b.isnumeric() and (op == '+' or op == '-' or op == '*' or op == '/'):
        print(f'{a} {op} {b} =', calc(int(a), int(b), op))
    else:
        print('Error!')
    if a == 'Stop' or b == 'Stop' or op == 'Stop':
        break