#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "C:\\Users\\matthieu.hauck\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\pocketsphinx\\model"
DATADIR = "C:\\Users\\matthieu.hauck\\Desktop\\"#AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\pocketsphinx\\data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us\\'))
config.set_string('-lm', path.join(MODELDIR, 'en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'cmudict-en-us.dict'))
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, 'test.raw'), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])