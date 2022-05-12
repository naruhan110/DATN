import pyqrcode

qr = pyqrcode.create("Ve xe 1")

qr.png("qrcode.png", scale=6)