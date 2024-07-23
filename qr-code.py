import qrcode

image = qrcode.make("https://www.linkedin.com/in/rishabh-tiwari-55b948146/")

image.save('qr.png')

