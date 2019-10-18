lists = []
while True:
    n = input("Enter a natural number or command \"Stop\": ")
    if n.isnumeric():
        lists.append(n)
    elif n == 'Stop':
        break
    else:
        print(f"{n} is not natural number!")

print(f'Max value of list is {max(lists)}')
print(f'Min value of list is {min(lists)}')

summ = 0
for i in lists:
    summ += int(i)

print(f"Summ of list's elements is {summ}")
print(f"Avg value of list is {summ / len(lists)}")
