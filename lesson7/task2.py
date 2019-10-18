def step(n):
    if n > 1:
        arr = [1, 2]
        for i in range(n - 2):
            arr.append(arr[i] + arr[i + 1])
        return arr[-1]
    elif n == 1:
        return 1
    else:
        return 'Steps <= 0!'


print(step(10))
