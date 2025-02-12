import qrcode

data = input("Enter URL or text: ").strip()
fileName = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10,border=5)
qr.add_data(data)
image = qr.make_image(fill_color = 'black', back_color = 'white')
image.save(fileName)

print(f'QR is save as {fileName}')
