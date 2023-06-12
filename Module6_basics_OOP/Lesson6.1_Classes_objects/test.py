import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('Какой-то текст или URL-адрес')
qr.make(fit=True)

img = qr.make_image(fill_color=(237, 28, 36), back_color=(55, 95, 35))
img.save("some_file.png")