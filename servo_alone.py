import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

choix = input("1 : test a la main // 2 : auto\n")

if choix == 1:
	pwm=GPIO.PWM(17,100)
    pwm.start(5)
    j=1
    while j==1:
    	angle = input("Entrez l'angle souhaite (0 à 180) :\n")
    	angle=float(angle)
    	pwm.ChangeDutyCycle(10+angle/180*10)
    	tt=10+angle/180*10
    	print("Wait 3 seconds please\n")
    	print(tt)
    	time.sleep(1)
    	print("ok\n")
  		rep = input("Voulez vous recommencez ? (oui : 1) \n")
  		if rep==1:
  			j=1
  		else : j=0
  		
 elif choix==2:
 	j=1
 	while j==1:
 		pas=input("Nombre de pas ?")
 		for i in range(4,24,20/pas):
 			pwm.ChangeDutyCycle(i)
 			time.sleep(0.5)
 		for i in range(24,4,-20/pas):
 			pwm.ChangeDutyCycle(i)
 			time.sleep(0.5)	
 		rep = input("Voulez vous recommencez ? (oui : 1) \n")
  		if rep==1:
  			j=1
  		else : j=0	

GPIO.cleanup()
pirnt("END")