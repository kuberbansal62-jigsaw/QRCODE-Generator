import sys
import subprocess

# This forces the active interpreter to install the library
subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode", "pillow"])

import qrcode
data=input("Enter the URL/LINK : ")
# Generate the data

img = qrcode.make(data)

# Save the image
img.save("QR.png")
print("QR Code generated successfully!")




