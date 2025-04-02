# Project 3: QR code encoder or decoder Python Project
# ✔ Encoder: Normal text ya data ko QR code me convert karna.
# ✔ Decoder: QR code ko scan karke original text ya data wapas lana.


# for design QRCODE image:
import qrcode 

# QR ENCODE CODE:
data = "If you scanned this QR code, now you owe me a treat!😆🍕" 

img = qrcode.make(data)
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)
qr.make(fit = True) # This line ensures that the QR code's size and the data fit properly.

img = qr.make_image(fill_color = 'green', back_color = 'white' )

img.save('D:/practicing/assign_1/qrcode1.png')
#---------------------------------------------------------------------

# QRcode scan and decode
import cv2

 # Creates an object that helps in detecting and decoding QR codes from an image
detector = cv2.QRCodeDetector()

# QR code image load
img = cv2.imread('D:/practicing/assign_1/qrcode1.png')

# Scans the QR code from the image and stores the decoded text in 'data', ignores the other returned values
data, _, _ = detector.detectAndDecode(img)

if data:
    print("QR Code Data:", data)
else:
    print("QR Code not detected!")








