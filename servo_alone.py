import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

choix = input("Voulez vous démarrez ? (oui : 1)\n")

if choix == 1:
	pwm=GPIO.PWM(17,100)
    pwm.start(5)
    j=1
    while j==1:
    	angle = input("Entrez l'angle souhaite (0 à 180) :\n")
    	pwm.ChangeDutyCycle(0.1+angle/180*0.1)
    	print("Wait 3 seconds please\n")
    	time.sleep(3)
    	print("ok\n")
  		rep = input("Voulez vous recommencez ? (oui : 1) \n")
  		if rep==1:
  			j=1
  		elif : j=0
  		
