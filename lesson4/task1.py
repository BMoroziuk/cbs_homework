a= None
while True:
    if not a or not a.isnumeric():
        a = input('Enter a as natural number: ')
        if not a.isnumeric():
            continue
    b = input('Enter b as natural number (b must be greater than a): ')
    if b.isnumeric() and int(a) < int(b):
        break
summ = 0
for i in range(int(a), int(b) + 1):
    summ += i
print(f"The sum of all natural numbers from {a} to {b} is {summ}")