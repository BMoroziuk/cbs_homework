running = True
while running == True:
    emamp = input('Enter simple mthematical example eg. 2+2: ')
    try:
        arr = emamp.split('+')
        if len(arr) == 2:
            res = float(arr[0]) + float(arr[1])
        if len(arr) < 2:
            arr = emamp.split('-')
        if len(arr) == 2:
            res = float(arr[0]) - float(arr[1])
        if len(arr) < 2:
            arr = emamp.split('*')
        if len(arr) == 2:
            res = float(arr[0]) * float(arr[1])
        if len(arr) < 2:
            arr = emamp.split('/')
        if len(arr) == 2:
            res = float(arr[0]) / float(arr[1])
        if len(arr) < 2:
            arr = emamp.split('^')
        if len(arr) == 2:
            res = float(arr[0]) ** float(arr[1])
        if len(arr) > 2:
            raise ValueError('To difficult example')
        if len(arr) < 2:
            raise ValueError('Not mthematical example')
    except (ValueError, ZeroDivisionError) as e:
        print(e)
    else:
        print(res)
        running = False
