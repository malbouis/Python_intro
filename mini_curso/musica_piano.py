from time import sleep
import os
import pygame
from pygame.mixer import Sound, get_init, pre_init

class NotaPiano(Sound):
    def __init__(self,filename,volume=0.5):
        self.filename = filename
        pygame.mixer.Sound.__init__(self,filename)
        self.set_volume(volume)
    def toca(self,segs):
        self.play()
        sleep(segs)
        self.stop()
    def tocafade(self,secs):
        self.play()
        self.fadeout(int(1000*secs))



pre_init(44100, -16, 1, 1024)
pygame.init()

music_order = ['c','db','d','eb','e','f','gb','g','ab','a','bb','b']
note_sounds = [] # list of all the note filename
NotasPiano = {}
for octave in range(2,6):
    for idx, insidenote in enumerate(music_order):
        note = NotaPiano(os.path.join('pythonpiano_sounds','16_piano-med-'+insidenote+str(octave)+'.ogg'))
        note_sounds.append(note)
        NotasPiano[insidenote+str(octave)] = note

sol3 = NotasPiano["g3"]
la3  = NotasPiano["a3"]
si3  = NotasPiano["b3"]
do   = NotasPiano["c4"]
re   = NotasPiano["d4"]
mi   = NotasPiano["e4"]
fa   = NotasPiano["f4"]
sol  = NotasPiano["g4"]
la   = NotasPiano["a4"]
si   = NotasPiano["b4"]
do5  = NotasPiano["c5"]
re5  = NotasPiano["d5"]
mi5  = NotasPiano["e5"]


if __name__=="__main__":
    cancao = [do,re,mi, do, do, re, mi, do, mi, fa, sol, mi, fa, sol]
    dura = [1,1,1,1,1,1,1,1,1,1,2,1,1,2]
    for d,note in zip(dura,cancao):
        note.tocafade(d)
        sleep(d/2)
        
