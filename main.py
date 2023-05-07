import qrcode

qr=qrcode.QRCode(version=1,box_size=10,border=5)
data="Código QR gerado!!!"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="#fbff00")
img.save("qrcode_1.png")