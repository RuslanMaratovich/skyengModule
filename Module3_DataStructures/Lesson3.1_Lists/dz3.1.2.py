white_list = []
answers = []

while True:
    white_request = input('Разрешенный запрос:')
    if white_request == '':
        break
    white_list.append(white_request)

while True:
    request = input('Запрос: ')
    if request == '':
        break
    if request in white_list:
        answers.append(request)

for answer in answers:
    print(answer)