import qrcode

data = 'Hello, world'

# img = qrcode.make(data) #сохраняет qrcode в переменную
qr = qrcode.QRCode(version=5, box_size=15, border=10)
# записываем параметры QRCode: version - версия от 1 до 40, box_size - размер QRCode, border - размер белых рамок

qr.add_data(data)
# записываем данные в QR
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="black")
#конвектируем данные qr в картинку

img.save('test.png')
#сохраняем картинку img в файл test.png
