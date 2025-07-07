import qrcode as qr

new=("https://www.youtube.com/watch?v=FOGRHBp6lvM")
img=qr.make(new)
img.save("Simple1.png")