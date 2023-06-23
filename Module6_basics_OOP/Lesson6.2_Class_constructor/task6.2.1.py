class Airplane:
    def __init__(self):
        # Конструктор класса
        engines = int(input('Двигатели: '))
        seats = int(input('Посадочные места: '))

        print('Самолет собран!')


plane1 = Airplane()
plane2 = Airplane()
plane3 = Airplane()

print(plane1.engines)
print(plane2.engines)
print(plane3.engines)

#engines - является атрибутом класса (свойство класса)