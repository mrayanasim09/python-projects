#This code is made by MRayan Asim
#packages needed:
#pip install pyshorteners
#pip install requests
#pip install qrcode
import pyshorteners
import requests
import qrcode
import time

print("This Url code is made by MRayan Asim hope you will like this! 😊")
time.sleep(3)

def shorten_url(url):
    # Initialize the URL shortener
    shortener = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = shortener.tinyurl.short(url)
    
    return shortened_url

def is_valid_url(url):
    # Send a HEAD request to check if the URL exists
    try:
        response = requests.head(url)
        return response.status_code == requests.codes.ok
    except requests.exceptions.RequestException:
        return False

# Prompt the user to enter a URL
url = input("Enter a URL: ")

# Check if the URL is valid
if is_valid_url(url):
    # Shorten the URL
    shortened_url = shorten_url(url)
    print("Shortened URL:", shortened_url)
else:
    print("Invalid URL")


# Data to encode
data = url

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
					back_color = 'white')
print("the qr code image is saved to your device by the name of the : 'QRCode.png'")
img.save('QRCode.png')
