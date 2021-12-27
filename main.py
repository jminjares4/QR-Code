# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
# Import the os module
import os

# Generate QR Code and store into custom folder
def generateQRCode(link, folder='', name='default', png_scale=8, svg_scale=6):
    dir = os.getcwd()
    url = pyqrcode.create(link)

    path = dir + '/' + folder
 
    if os.path.isdir(path) is True:
        os.chdir(path)
        url.svg(name+'.svg', scale=svg_scale)
        url.png(name + ".png", scale=png_scale)
        os.chdir(dir)
    else:
        os.mkdir(path)
        os.chdir(path)
        url.svg(name+'.svg', scale=svg_scale)
        url.png(name + ".png", scale=png_scale)
        os.chdir(dir)

    return "QR code stored in " + dir + "/" + folder

if __name__ == '__main__':
    linkedIn = 'https://www.linkedin.com/in/jesus-minjares-157a21195/'
    gitHub = 'https://github.com/jminjares4'
    linktree = 'https://linktr.ee/JesusMinjares'

    print(generateQRCode(link=linkedIn, folder="LinkedIn",
                name="linkedIn", png_scale=8, svg_scale=6))
    print(generateQRCode(link=gitHub, folder="GitHub",
                name="gitHub", png_scale=8, svg_scale=6))
    print(generateQRCode(link=linktree, folder="Linktree",
                name="linktree", png_scale=8, svg_scale=6))
    print("QR-Code are store in their corresponding directories!")

    generateQRCode(link='https://google.com')