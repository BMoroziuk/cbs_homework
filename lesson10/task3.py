class Worker:
    def __init__(self, name, surname, department, year):
        self.name = name
        self.surname = surname
        self.department = department
        self.setyear(year)

    def setyear(self, year):
        if not year.isnumeric():
            del self
            raise ValueError('Year must be a number')
        else:
            self.year = year


running = True
workers = []
while running == True:
    try:
        workers.append(Worker(input('Name: '), input('Surname: '), input('Department: '), input('Year of start: ')))
        c = input('Would you like to continue (y/n)? ')  # тут не обрабатывал возможность ввода чего либо кроме n
        if c == 'n':
            running = False
    except ValueError as e:
        print(e)

y = input('Enter year to sort: ')  # тут не обрабатывал возможность ввода не числа
for i in workers:
    if int(i.year) > int(y):
        print(i.department + ', ')
        print(i.surname + ', ')
        print(i.name)
        print()