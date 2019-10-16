def nechet(stroka=input('Enter your number >>> ')):
    if stroka[0] == '0':
        return
    if int(stroka[0]) % 2 == 1:
        print(stroka[0], end = '')
        nechet(stroka[1:])
    else:
        nechet(stroka[1:])


nechet()
