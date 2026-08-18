# This code is made by MRayan Asim
# packages needed:
# pip install pyshorteners
# pip install requests
# pip install qrcode
import re
import time

import pyshorteners
import qrcode
import requests

# Default timeout for HTTP requests (seconds)
DEFAULT_TIMEOUT = 10


def validate_url(url):
    """Validate URL format using regular expression."""
    # Regular expression pattern for URL validation
    pattern = re.compile(
        r"^https?://"  # http:// or https://
        r"([A-Za-z0-9.-]+)"  # domain
        r"(:\d+)?"  # optional port number
        r"(/[A-Za-z0-9_\.-]*)*?$"  # optional path
    )
    return bool(re.match(pattern, url))


def analyze_url(url):
    """Analyze and validate a URL."""
    if validate_url(url):
        print("URL is valid.")
        # Perform further analysis or processing here
    else:
        print("Invalid URL.")


def shorten_url(url):
    """Shorten a URL using pyshorteners."""
    # Initialize the URL shortener
    shortener = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = shortener.tinyurl.short(url)

    return shortened_url


def is_valid_url(url, timeout=DEFAULT_TIMEOUT):
    """
    Check if a URL exists and is accessible.

    Args:
        url: The URL to check
        timeout: Request timeout in seconds (default: 10)
    """
    # Send a HEAD request to check if the URL exists
    try:
        # Use timeout to prevent hanging
        response = requests.head(url, timeout=timeout)
        return response.status_code == requests.codes.ok
    except requests.Timeout:
        return False
    except requests.exceptions.RequestException:
        return False


print("This URL code is made by MRayan Asim. Hope you will like this! \ud83d\ude0a")
time.sleep(3)

# Prompt the user to enter a URL
url = input("Enter a URL: ")

# Check if the URL is valid
if is_valid_url(url):
    # Shorten the URL
    try:
        shortened_url = shorten_url(url)
        print("Shortened URL:", shortened_url)
    except Exception as e:
        print(f"Error shortening URL: {e}")
        shortened_url = url
else:
    print("Invalid URL")

# Analyze the URL
analyze_url(url)

# Data to encode
data = url

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
print("The QR code image is saved to your device with the name 'QRCode.png'")
img.save("QRCode.png")
