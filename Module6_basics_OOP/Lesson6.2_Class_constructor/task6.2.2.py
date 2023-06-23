class Airplane:
    def __init__(self, engines, seats):
        # Конструктор класса
        # self определяет переданный оргумент для конкретного объкта класса
        self.engines = engines
        self.seats = seats

        print('Самолет собран!')


plane1 = Airplane(engines=2, seats=150)
plane2 = Airplane(engines=4, seats=200)
plane3 = Airplane(engines=5, seats=500)

print('Самолет 1:',plane1.engines, plane1.seats)
print('Самолет 2:',plane1.engines, plane1.seats)
print('Самолет 3:',plane1.engines, plane1.seats)

#engines - является атрибутом класса (свойство класса)