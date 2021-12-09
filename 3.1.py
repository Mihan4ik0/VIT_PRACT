class University_employer():

    def __init__(self):
        self.code = 0
        self.surname = 0
        self.name = 0
        self.midlename = 0
        self.rank = 0
        self.start = 0
        self.money = 00.00

    def info(self):
        return self.code, self.surname, self.name, self.midlename, self.rank, self.start, self.money


Stepa = University_employer()
Stepa.code = 1
Stepa.surname = 'Ivanov'
Stepa.name = 'Stepa'
Stepa.midlename = 'Aleksandrovich'
Stepa.rank = 3
Stepa.start = '21.03.2019'
Stepa.money = 20000

Vanya = University_employer()
Vanya.code = 2
Vanya.surname = 'Putin'
Vanya.name = 'Vanya'
Vanya.midlename = 'Aleksandrovich'
Vanya.rank = 1
Vanya.start = '19.03.2020'
Vanya.money = 10000

print(Stepa.info())
print(Vanya.info())

