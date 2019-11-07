arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = iter([i for i in arr[-1::-1]])

print(next(a))
print(next(a))
print(next(a))

print()

for i in iter([i for i in arr[-1::-1]]):
    print(i)