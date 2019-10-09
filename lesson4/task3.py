while True:
    n = input('Enter height of triangle (natural number): ')
    if n.isnumeric():
        n = int(n)
        break
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1:
            print('*')
        elif j == 1:
            print('*', end='')
        elif j == i:
            print('*')
        elif i == n:
            print('*' * (i - 1))
            break
        else:
            print(' ', end='')
