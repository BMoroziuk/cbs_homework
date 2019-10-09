while True:
    print('n must be a natural number')
    n = input('n = ')
    if n.isnumeric():
        break
factorial = 0
for i in range(int(n) + 1):
    factorial += i
print(f"Factorial of {n} is {factorial}")
