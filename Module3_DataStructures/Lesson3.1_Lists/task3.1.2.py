'''программа добавляет элементы в лист до тех пор пока не будет введен пустой элемент'''

items = []
while True:
    item = input('Ввод: ')
    if item != '':
        items.append(item)
    else:
        break

print(items)
