# class Class_name:
#     ....

class Car:
    wheels = 4
    engine = 1
    color = 'white'

#print(Car)
moskvich = Car()
volga = Car()
niva = Car()

print(Car.color)
print(moskvich.color)
print(volga.color)
print(niva.color)

moskvich.color= 'red'
niva.color = 'blue'

print(moskvich.color)
print(volga.color)
print(niva.color)