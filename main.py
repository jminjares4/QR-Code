# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
# Import the os module
import os

currentDir  = os.getcwd()
print(currentDir)

# String which represents the QR code 
linkedIn = 'https://www.linkedin.com/in/jesus-minjares-157a21195/'
gitHub = 'https://github.com/jminjares4'
links = 'https://linktr.ee/JesusMinjares'

# Generate QR code 
linkedIn_url = pyqrcode.create(linkedIn)
gitHub_url = pyqrcode.create(gitHub)
links_url = pyqrcode.create(links)


os.chdir(currentDir + '/LinkedIn')
# Create and save the svg and png files
linkedIn_url.svg('linkedIn.svg', scale = 8)
linkedIn_url.png('linkedIn.png', scale = 6)

os.chdir(currentDir + '/Link')
# Create and save the svg and png files
links_url.svg('links.svg', scale = 8)
links_url.png('links.png', scale = 6)

os.chdir(currentDir + '/GitHub')
# Create and save the svg and png files
gitHub_url.svg('gitHub.svg', scale = 8)
gitHub_url.png('gitHub.png', scale = 6)

os.chdir(currentDir)

print("QR-Code are store in their corresponding directories!")


