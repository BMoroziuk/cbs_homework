class Romb:
    pass


class Top(Romb):
    pass


class Left(Top):
    pass


class Right(Top):
    pass


class Bottom(Left, Right):
    pass


print(Romb.__mro__)
print(Top.__mro__)
print(Left.__mro__)
print(Right.__mro__)
print(Bottom.__mro__)

print()
print('    o')
print('    ↑')
print('    o')
print('      ↖')
print('o → → → o')
print('  ↖')
print('    o')