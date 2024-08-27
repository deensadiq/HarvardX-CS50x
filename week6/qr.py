import qrcode

img = qrcode.make("https://youtube.be/xvFZjo5PgG0")
img.save("qr.png", "PNG")