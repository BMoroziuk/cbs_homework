# чтобы не копировать два таска сделал в одном, из второго только импортнул кусочек кода
class Book:
    # task2
    fb = []
    feetback = ''

    def addfb(self, fb):
        self.fb.append(fb)

    # task2

    def __init__(self, author, tittle, year, genre):
        self.author = author
        self.tittle = tittle
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        if self.author == other.author and self.tittle == other.tittle and self.year == other.year and self.genre == other.genre:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.author != other.author or self.tittle != other.tittle or self.year != other.year or self.genre != other.genre:
            return True
        else:
            return False

    def __repr__(self):
        return "This is instance of class Book"

    def __str__(self):
        # task2
        for fbo in self.fb:
            self.feetback += fbo.fb + ', '
        if len(self.feetback) > 0:
            self.feetback = self.feetback[0:-2]
        # task2
        return f"{self.author}, {self.tittle}, {self.year}, {self.genre} , {self.feetback}"


book1 = Book('Daniel Defoe', 'Robinson Crusoe', 1719, 'Adventure')
book2 = Book('Mayne Reid', 'The Headless Horseman', 1866, 'Fiction')
book3 = Book('Daniel Defoe', 'Robinson Crusoe', 1719, 'Adventure')

print(book1 == book2)
print(book1 == book3)
print(book1 != book2)
print(book1 != book3)

# task 2 - импортил может неправильно, как нагуглил)
fb = __import__('task2').Feetback('Very good book!', True)
book1.addfb(fb)
fb = __import__('task2').Feetback('Very bad book!', False)
book1.addfb(fb)
# task 2

print(book1.__repr__())
print(book1)
