print('Привет! Готов(а) играть ?')
print('Сначала давай немного расскажешь о себе')
name = input('Как тебя зовут? ')
print('Отлично! Приятно познакомиться ', name)
age = int(input('Теперь, сколько тебе лет? '))

if age >= 15:
    print('придумай шутку {0}'.format(name), 'продолжи шутку')
elif age <= 13:
    print('придумай шутку {0}'.format(name), 'продолжи шутку')
else:
    print('придумай шутку {0}'.format(name))


print('Хорошо, давай посмотрим сцену для игры.\n'
      'Ты гуляешь по лесу, как вдруг появляется медведь!')

myChoice = input('Что ты будешь делать? Бежать или драться ')
if myChoice == 'бежать':
    print('Хороший выбор ......')
elif myChoice == 'драться':
    print('Это было глупо! Ты выбываешь!')
else:
    print('Можешь попробовать снова!')
    myChoice == input('Что ты будешь делать? Бежать или драться ')
    if myChoice == 'бежать':
        print('Хороший выбор ......')
    elif myChoice == 'драться':
        print('Это было глупо! Ты выбываешь!')