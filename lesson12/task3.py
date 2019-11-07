text = input('Enter a text: ')
for i in sorted(text.split(), key=str.lower):
    print(i, end=' ')
