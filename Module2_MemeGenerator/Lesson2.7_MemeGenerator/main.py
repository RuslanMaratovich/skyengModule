import requests
import urllib

username = 'g_user_105375711440410450936'
password = 'GhV-YjQ-55q-NkR'

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name': image['name'], 'url': image['url'], 'id': image['id']} for image in data]

print('лист доступных мемов:')

ctr = 1
for img in images:
    print(ctr, img['name'])
    ctr += 1

id = int(input('введите номер картинки '))
text0 = input('введите первый текст ')
text1 = input('введите второй текст ')

URL = 'https://api.imgflip.com/caption_image'

params = {
    'username': username,
    'password': password,
    'template_id': images[id - 1]['id'],
    'text0': text0,
    'text1': text1
}

response = requests.request('POST', URL, params=params).json()
print(response)

opener = urllib.request.URLopener()

opener.addheader('User-Agent', userAgent)

filename, headers = opener.retrieve(response['data']['url'], images[id - 1]['name'] + '.jpg')
