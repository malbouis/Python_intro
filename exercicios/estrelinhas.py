import turtle

#####################################################################################################################
def estrela(npontas = 5,cor="red",tamanho=100,pos=(0,0)):
    '''
    FUNÇÃO QUE DESENHA UMA ESTRELA. 
    VALORES POR DEFAULT: 
    5 PONTAS, 
    COR VERMELHA, 
    TAMANHO 100, 
    POSIÇÃO AO COMEÇAR: ORIGEM
    '''
    tina = turtle.Turtle()
    tina.color(cor)
    tina.penup()
    tina.setpos(pos)
    alpha = 0.0
    if npontas % 2  ==0:
        # para um numero par de pontas da estrela
        alpha = 180.0 - (360.0/npontas)
        if npontas %4 !=0:
            # para numeros pares mas não divisiveis por 4 (2* algum impar)
            # o angulo alpha é o mesmo de uma estrela de pontas impares
            print("Atenção!: será desenhada uma estrela de n = ", int(npontas/2), "pontas, 2 vezes")
    else :
        # numero impar
        alpha = 180.0 - (360.0/(2*npontas))

    #o bloco do desenho, abaixo a caneta
    tina.pendown()
    for i in range(npontas):
        tina.forward(tamanho)
        tina.left(alpha)
    #acabou o desenho, levanto a caneta
    tina.penup()
    #para não aparecer o triangulinho da tartaruga ao acabar o desenho
    tina.hideturtle()
    return
#################################################################################################################

# Programa principal 
def main():
    print("Bem-vindos ao programa que desenha estrelinhas no ceu azul")
    tela = turtle.Screen()
    tela.bgcolor("darkblue")
    estrela(7) 
    estrela(5,"yellow",150,(-150,-150))
    estrela(8,"white",50,(150,150))
    estrela(36,"orange",pos=(-200,100)) 
    return tela.getcanvas()

salvatela = main()

###############################################################################
### APOS EXECUÇÃO, COM -i,  PODEM ADICIONAR MAIS ESTRELINHAS A PARTIR DO PROMPT
#%$   python3 -i estrelinhas.py
#% >>> estrela(14,"green",120,(200,-200))
#
###
### Depois de adicionar mais estrelas pode salvar com
#
#% >>> salvatela.postscript(file="desenhoestrelas.ps")
#
### Mas isto só salva o desenho das estrelas, não a cor de fundo
################################################################################

