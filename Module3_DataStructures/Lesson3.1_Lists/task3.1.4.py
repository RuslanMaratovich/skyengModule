'''Перебор элементов листа'''

authors = ['Chekhov', 'Dostoevski', 'Tolstoy', 'Nekrasov', 'Bulgakov', 'Pushkin', 'Esenin', 'Blok']

for i in range(len(authors)):
    print(f'{i+1}. {authors[i]}')

for i in authors:
    print(i)