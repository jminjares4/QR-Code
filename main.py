# Author:   Jesus Minjares
#           Master of Science in Computer Engineering
# Date:     12-27-2021
# Purpose:  Generate QR-Codes for different urls using Python packages

# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
# Import the os module
import os

# Generate QR Code and store into custom folder

def generateQRCode(link, folder='', name='default', png_scale=8, svg_scale=6):
    dir = os.getcwd()  # get current working directory
    url = pyqrcode.create(link)  # create qrcode

    # path to store the qrcode
    path = dir + '/' + folder
    # check if the path exist
    if os.path.isdir(path) is True:
        pass  # skip
    else:
        os.mkdir(path)  # create directory if it does not exist
    os.chdir(path)  # change the directory to store the qrcode
    # store in svg and png format
    url.svg(name+'.svg', scale=svg_scale)
    url.png(name + ".png", scale=png_scale)
    # change to original directory
    os.chdir(dir)
    # return a QR code location
    return "QR code stored in " + dir + "/" + folder


if __name__ == "__main__":
    # get current directory
    dir = os.getcwd()
    # Directory to store generate QR codes
    qr_code_path = 'QR-Code Test'
    # check if the directory exist
    if os.path.isdir(qr_code_path) is True:
        pass  # skip
    else:
        os.mkdir(qr_code_path)  # create directory
    os.chdir(qr_code_path)  # change the directory

    # Different url to generate QR-Code
    linkedIn = 'https://www.linkedin.com/in/jesus-minjares-157a21195/'
    gitHub = 'https://github.com/jminjares4'
    linktree = 'https://linktr.ee/JesusMinjares'

    # Call generateQRCode
    print(generateQRCode(link=linkedIn, folder="LinkedIn",
                         name="linkedIn", png_scale=8, svg_scale=6))
    print(generateQRCode(link=gitHub, folder="GitHub",
                         name="gitHub", png_scale=8, svg_scale=6))
    print(generateQRCode(link=linktree, folder="Linktree",
                         name="linktree", png_scale=8, svg_scale=6))
    # Print message
    print("QR-Code are store in their corresponding directories!")
