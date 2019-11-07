class Revers():
    def __init__(self, arr):
        self.arr = arr
        self.len = len(self.arr)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.index) >= self.len:
            raise StopIteration
        else:
            self.index -= 1
        return self.arr.__getitem__(self.index)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = Revers(arr)

print(next(a))
print(next(a))
print(next(a))

print()

for i in Iter(arr):
    print(i)
