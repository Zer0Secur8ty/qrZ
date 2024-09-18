#!/usr/bin/python3
import optparse 
import qrcode
from PIL import Image

#Author : ZeroSecurity
#Date create : 09/02/2024
#Date modified : 09/02/2024
#this code Generate QRCODE by enter any URL ...>


#the data you want to encode in the QR code
data = input("Enter the URL : ")

#Generate the QR CODE
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#Create an image from the QR code
image = qr.make_image(fill="black", back_color="white")

#Save the image
image.save("qr_code.png")

#this line to open the generated QRCODE 
#if you want to run this line remove the hash ...

#image.open("qr_code.png")





