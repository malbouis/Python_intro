from musica import *


cancao = [ (Do,0.3),(Re,1)]

for nota,tempo in cancao:
      nota.toca(tempo)


nova = Nota("FaChar",0.2)
nova.toca(5)


def novizia_rebelde():
    notas= [Do,Re,Mi,Do,Mi,Do, Mi,
            Re, Mi, Fa,  Fa , Mi, Re, Fa ]
    duracao = [300,200,300,200,300,300,500,
               300,200,200,200,200,200,1000]
    for i,nota in enumerate(notas):
        tempo=duracao[i]/1000
        nota.toca(tempo)

novizia_rebelde()
