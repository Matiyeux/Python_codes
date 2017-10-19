import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import smbus

#I2C
bus_pi=smbus.SMBus(1)
addr=0X48
#SPI
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=30)
disp.clear()
disp.display()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

print("Voulez vous lancer l'acquisition ?")
ask=raw_input()

if ask=="1":
	ask=True
else: ask=False

while ask:
	xlsb=bus_pi.read_word_data(0x08,0xa9)
	xmsb=bus_pi.read_word_data(0x08,0xa8)
	x=((xmsb&0x00ff)<<8)|(xlsb&0x00ff)
	draw.text((8,30), x, font=font)
	disp.image(image)
	disp.display()
