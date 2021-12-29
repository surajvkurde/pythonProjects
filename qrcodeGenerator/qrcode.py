import pyqrcode
import png 
from pyqrcode import QRCode


#define data to be converted to qrcode
data = "https://www.youtube.com"
#create qrcode
url = pyqrcode.create(data)
#save qrcode as png
url.png("text.png",scale=8)
#save qrcode as svg
url.svg("qrsvg.svg",scale=8)


