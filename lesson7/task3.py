arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(arr)

newarr = []

for i in arr:
    yes = True
    for j in range(2, i):
        if i % j == 0:
            yes = False
    if yes and i != 1:
        newarr.append(i)

print(newarr)

while True:
    operator = input('What shell i do (* or +)? >>>')
    if operator != '*' and operator != '+':
        continue
    elif operator == '+':
        result = 0
        for i in newarr:
            result += i
        print(result)
        break
    else:
        result = 1
        for i in newarr:
            result *= i
        print(result)
        break