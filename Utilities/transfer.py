# This code is made by MRayan Asim
# Packages needed :
# pip install pygame
import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

# Set the directory path to the desired location
directory_path = r""  # enter the path of file for qr code

# Change the current working directory to the desired location
os.chdir(directory_path)

PORT = 8010

Handler = http.server.SimpleHTTPRequestHandler

# Get the hostname of the system
hostname = socket.gethostname()

# Get the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# Generate the QR code
url = pyqrcode.create(link)
# Save the QR code image as SVG
url.svg("myqr.svg", scale=8)
# Open the QR code image in the default web browser
webbrowser.open("myqr.svg")

# Start the HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your browser:", IP)
    print("Or use the QR Code")
    httpd.serve_forever()
