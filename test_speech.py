import speech_recognition as sr
 
def decodeSpeech(wavefile):
    r = sr.Recognizer()
    with sr.WavFile(wavefile) as source:
        audio = r.record(source)
        try:
            print('Transcription GOOGLE: ' + r.recognize_google(
                audio, language='fr-FR', show_all=False))
        except LookupError:
            print('Cannot understand audio!')
 
 
WAVFILE = 'Sans titre.wav'
decodeSpeech(WAVFILE)