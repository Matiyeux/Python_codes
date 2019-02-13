import pygame
import sys
from gtts import gTTS
import time

phrase=sys.argv[1]

tts=gTTS(text=phrase,lang='fr',slow=False)
tts.save("test.mp3")

pygame.mixer.init()
pygame.mixer.music.load('C:\\???\\test.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
time.sleep(7)
