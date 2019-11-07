def avg(*args):
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)


print(avg(1, 2))

print(avg(*tuple(range(10))))
