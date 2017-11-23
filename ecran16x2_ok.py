import time 
from RPLCD.gpio import CharLCD

lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD)

while True: 	
	lcd.clear()
	lcd.cursor_pos = (0, 5)
	lcd.write_string('Bravo!')
	time.sleep(3)  
	lcd.clear()
	lcd.cursor_pos = (0, 1)
	lcd.write_string('Je fonctionne')
	lcd.cursor_pos = (1, 2)
	lcd.write_string('parfaitement')
time.sleep(3) 