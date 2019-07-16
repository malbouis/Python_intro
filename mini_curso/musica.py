import numpy

from array import array
from time import sleep

import pygame
from pygame.mixer import Sound, get_init, pre_init

class Nota(Sound):
    notasfreq={"do":523.25, "re": 587.33,  "mi":659.25,
               "fa":698.46, "sol":783.99,  "la":880, "si":987.77,
               # semitonos
               "dochar" :554.37 , "rechar": 622.25,
               "fachar":739.99, "solchar":830.61 , "lachar":932.33    }

    def __init__(self, frequency, volume=.5,option="harmonic"):
        if type(frequency)  == str :
            freqname = frequency.lower()
            try:
                frequency=self.notasfreq[freqname]
            except:
                print("no such note")
                return
        self.frequency = frequency
        if option.lower()=="midi":
            build = self.build_samples_square
        else : #opcao harmonica
            build = self.build_samples

        pygame.mixer.Sound.__init__(self, buffer=build())
        self.set_volume(volume)

    def build_samples_square(self): ## som tipo ATARI / antigo / MIDI
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples


    def build_samples(self): ## som mais harmonico
        sample_rate = pygame.mixer.get_init()[0]
        period = int(round(sample_rate / self.frequency))
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1

        def frame_value(i):
            return amplitude * numpy.sin(2.0 * numpy.pi * self.frequency * i / sample_rate)

        return numpy.array([frame_value(x) for x in range(0, period)]).astype(numpy.int16)


    def toca(self,secs):
        maxt=10000
        self.play(-1,maxt)
        sleep(secs)
        self.stop()

##Definir algumas notas
pre_init(44100, -16, 1, 1024)
pygame.init()
Fa4 = Nota(698.46/2.0)
Sol4= Nota(783.99/2.0)
La4 = Nota(440)
Si4 = Nota(493.88)
Do  = Nota(523.25)
Re  = Nota(587.33)
Mi  = Nota(659.25)
Fa  = Nota(698.46)
Sol = Nota(783.99)
La  = Nota(880)
Si  = Nota(987.77)
Do6 = Nota(2*523.25)
Re6 = Nota(2*587.33)
Mi6 = Nota(2*659.25)


if __name__ == "__main__":

    notas= [Do,Re,Mi,Do,Mi,Do, Mi,
            Re, Mi, Fa,  Fa , Mi, Re, Fa ]
    #[Do, Sol, Fa, Mi, Mi, Mi,
    #Do, Re, Mi, Fa]
    duracao = [300,200,300,200,300,300,500,
               300,200,200,200,200,200,1000]
    for i,nota in enumerate(notas):
        maxt=duracao[i]
        loops = 10000
        nota.play(loops,maxt,100)
        sleep(0.0015*maxt)

    for i,nota in enumerate(notas):
        tempo=duracao[i]/1000
        nota.toca(tempo)

    Fach = Nota("fachar")
    Fach.play(-1,1000)
    sleep(3)
    Fach.stop()
    n=Nota(261,0.8,"midi")
    n.play(1000,2000)
    sleep(5)
