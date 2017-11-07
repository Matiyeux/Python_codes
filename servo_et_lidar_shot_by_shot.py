import RPi.GPIO as GPIO
import time
import smbus

bus_pi=smbus.SMBus(1)
addr=0x48

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

choix = input("1 : test a la main // 2 : auto\n")

if choix == 1:
	pwm=GPIO.PWM(17,100)
  pwm.start(5)
  j=1
  while j==1:
  	angle = input("Entrez l'angle souhaite (0 a 180) :\n")
  	angle=float(angle)
  	pwm.ChangeDutyCycle(4+angle/180*20)
  	tt=4+angle/180*20
  	print("Wait 3 seconds please\n")
  	print(tt)
  	time.sleep(1)
  	print("ok\n")
		rep = input("Voulez vous recommencez ? (oui : 1) \n")
		if rep==1:
			j=1
		else : j=0
  		
elif choix==2:
  pwm=GPIO.PWM(17,100)
  pwm.start(5)
 	j=1
 	while j==1:
 		pas=input("Nombre de pas ?")
 		for i in range(4,25,20/pas):
 			pwm.ChangeDutyCycle(i)
 			time.sleep(0.5)
      xlsb=bus_pi.read_word_data(0x08,0xa9)
      xmsb=bus_pi.read_word_data(0x08,0xa8)
      x=((xmsb&0x00ff)<<8)|(xlsb&0x00ff)
      print("pas "+str(i)+" donne "+str(x)+"mm")
 		for i in range(24,3,-20/pas):
 			pwm.ChangeDutyCycle(i)
 			time.sleep(0.5)	
      xlsb=bus_pi.read_word_data(0x08,0xa9)
      xmsb=bus_pi.read_word_data(0x08,0xa8)
      x=((xmsb&0x00ff)<<8)|(xlsb&0x00ff)
      print("pas "+str(i)+" donne "+str(x)+"mm")
 		rep = input("Voulez vous recommencez ? (oui : 1) \n")
  		if rep==1:
  			j=1
  		else : j=0	

GPIO.cleanup()
print("END")