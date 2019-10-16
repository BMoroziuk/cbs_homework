def polindrom(text, s=0):
    if text[s] == text[-1 - s] and s != int(len(text) / 2) - 1:
        return polindrom(text, s + 1)
    if text[s] == text[-1 - s] and s == int(len(text) / 2) - 1:
        return 'Yes'
    if text[s] != text[-1 - s]:
        return 'No'

print(polindrom('lol'))