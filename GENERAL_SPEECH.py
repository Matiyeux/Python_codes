import pyaudio
import wave
import sys
import pygame
from gtts import gTTS
import time
import speech_recognition as sr
from time import gmtime, strftime, localtime
import requests
import json


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "apt.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

print ("* Recording audio...")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	frames.append(data)

print ("* done\n" )

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

wavefile = 'apt.wav'
r = sr.Recognizer()
with sr.WavFile(wavefile) as source:
    audio = r.record(source)
    try:
        print('Transcription GOOGLE: ' + r.recognize_google(
            audio, language='fr-FR', show_all=False))
    except LookupError:
        print('Cannot understand audio!')
 
response=r.recognize_google(audio, language='fr-FR', show_all=False)


print(response)
if ("météo" in response):
	r=requests.get("https://www.prevision-meteo.ch/services/json/manosque")
	data=r.json()
	hour=data['current_condition']['hour']
	lieu=data['city_info']['name']
	temp=data['current_condition']['tmp']
	cond=data['current_condition']['condition']
	rep= "A " + lieu + " " + "à " + hour + ", il faisait " +  str(temp) + " degrés celsius. Les conditions sont définies comme étant " + cond
	tts=gTTS(text=rep,lang='fr',slow=False)
	#tts=gTTS(text="J'ai une tête de miss météo ? ... batard !?",lang='fr',slow=False)
	tts.save("test.mp3")
	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
if ("chante" in response) and ("chanson" in response):
	tts=gTTS(text="Boumbo, boumbo, petite automobile bile, boumbo, boumbo, tu parais si fragile gile. Sous ton drole de capot, bouboubouboumbo",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
if ("dessine" in response) and ("mouton" in response):
	tts=gTTS(text="hé ducon, tu m'as pris pour saint exupéry ??",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
if "heure" in response:
	rep="Achète toi une montre connard ... sinon il est ..."+ strftime("%H heures %M minute et %S secondes", localtime())
	tts=gTTS(text=rep,lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
if "date" in response:
	if strftime("%w")=="0":
		jour="dimanche"
	elif strftime("%w")=="1":
		jour="lundi"
	elif strftime("%w")=="2":
		jour="mardi"
	elif strftime("%w")=="3":
		jour="mercredi"
	elif strftime("%w")=="4":
		jour="jeudi"
	elif strftime("%w")=="5":
		jour="vendredi"
	elif strftime("%w")=="6":
		jour="samedi"

	if strftime("%m")=="01":
		mois="janvier"
	elif strftime("%m")=="02":
		mois="février"
	elif strftime("%m")=="03":
		mois="mars"
	elif strftime("%m")=="04":
		mois="avril"
	elif strftime("%m")=="05":
		mois="mai"
	elif strftime("%m")=="06":
		mois="juin"
	elif strftime("%m")=="07":
		mois="juillet"
	elif strftime("%m")=="08":
		mois="aout"
	elif strftime("%m")=="09":
		mois="septembre"
	elif strftime("%m")=="10":
		mois="octobre"
	elif strftime("%m")=="11":
		mois="novembre"
	elif strftime("%m")=="12":
		mois="décembre"

	rep="C'est mon anniversaire, achète moi une batterie batard. C'est le " + jour + " " + strftime("%d", localtime()) + " " + mois + " " + strftime("%Y", localtime())
	tts=gTTS(text=rep,lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
if ("connard" in response) or ("con" in response):
	tts=gTTS(text="Je te prie de rester correct, sale con",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
if "citation" in response:
	tts=gTTS(text="Bien sur, voici la citation ... c'est la marque d'un esprit cultivé que d'être capable de nourrir la pensée d'autrui sans pour autant la cautionner. Aristote je vous prie",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif "Maxime" in response :
	tts=gTTS(text="C'est le plus grand des traitres",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif "David" in response :
	tts=gTTS(text="Je ne dirai qu'une chose... lassagne",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif ("monsieur billet" in response) or ("Monsieur billet" in response) :
	tts=gTTS(text="tu parles de tchoutchou ?",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif "Stéphane" in response :
	tts=gTTS(text="C'est un vaurien",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif "Matthieu" in response :
	tts=gTTS(text="Lui, c'est un bon",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif "Antoine" in response :
	tts=gTTS(text="Je doute de lui ... ah ...ah ...ah",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif "Régis" in response :
	tts=gTTS(text="Non, je ne parlerai pas de Régis... Il me fait peur",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
elif (("comment" in response) or ("ça" in response)) and (("vas" in response) or ("va" in response)) :
	tts=gTTS(text="ça roule ma poule... Et toi ?",lang='fr',slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()==True:
		continue
# else : 
# 	tts=gTTS(text="Je ne comprend pas ta demande",lang='fr',slow=False)
# 	tts.save("test.mp3")

# 	pygame.mixer.init()
# 	pygame.mixer.music.load('C:\\Users\\matthieu.hauck\\Desktop\\Python\\test.mp3')
# 	pygame.mixer.music.set_volume(1)
# 	pygame.mixer.music.play()
# 	time.sleep(7)