def ones(stroka=input('Enter your number >>> '), n=0):
    if stroka[0] + stroka[1] == '00':
       return n
    if int(stroka[0]) == 1:
        n += 1
        return ones(stroka[1:], n)
    else:
        return ones(stroka[1:], n)


print(ones())
