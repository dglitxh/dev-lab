import qrcode

site_link = input("Enter site link")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(site_link)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color="white")
img.save('myqr.png')