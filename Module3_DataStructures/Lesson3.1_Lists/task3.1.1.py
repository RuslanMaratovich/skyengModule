authors = ['Chekhov', 'Dostoevski', 'Tolstoy', 'Nekrasov', 'Bulgakov', 'Pushkin', 'Esenin', 'Blok']
print(authors[1])

list = [0] * 5
print(list)

print(authors[0:4:2]) #Срез
print(authors[-1:4:-1])
print(authors[::-1])

authors.append("Pasternak") #добавляет элемент в список
print(authors)

test = authors.pop(-2)
#вырезает элемент по индексу, без индекса вырезает последний элемент
#сохраняет вырезанный элемент в переменную
print(authors)
print(test)

index = authors.index('Dostoevski') #Получаем индекс элемента
print(index)

del authors[0] #удаляет элемент по индексу
print(authors)


