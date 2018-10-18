import turtle

#função para desenhar uma flor. Os parametros por defeito sao 6 petalas, cor vermelha, e tamanho 40 (radio da petala)
def flor(npetalas=6,cor="red",tamanho=40):
       turtle.seth(0)
       turtle.color(cor,"green")
       turtle.pd()
       angle=360/npetalas
       for i in range(npetalas):
          turtle.left(angle)
          turtle.circle(tamanho)
       turtle.pu()

def talo(comprimento=120,cor="green", offset=80):
    turtle.color(cor,"black")
    turtle.seth(270)
    turtle.fd(offset)
    turtle.pd()
    turtle.fd(comprimento)
    turtle.pu()

def folha_direita(comprimento=20,cor="green",v_offset=120):
    turtle.color(cor)
    turtle.pu()
    turtle.seth(270)
    turtle.bk(v_offset)
    turtle.seth(0)
    turtle.pd()
    tpos = turtle.pos()
    paso = comprimento/20
    for i in range(10):
        turtle.right(5)
        turtle.fd(paso)
    for i in range(10):
        turtle.left(5)
        turtle.fd(paso)
    turtle.setpos(tpos)
    turtle.pu()

  
def folha_esquerda(comprimento=20,cor="green",v_offset=120):
    turtle.color(cor)
    turtle.pu()
    turtle.seth(270)
    turtle.bk(v_offset)
    turtle.seth(180)
    turtle.pd()
    tpos = turtle.pos()
    paso = comprimento/20
    for i in range(10):
        turtle.right(5)
        turtle.fd(paso)
    for i in range(10):
        turtle.left(5)
        turtle.fd(paso)
    turtle.setpos(tpos)
    turtle.pu()
  


def rosinha(cor="pink"):
    flor(cor=cor)
    talo()
    folha_direita(v_offset=60)
    folha_esquerda(v_offset=0)

turtle.seth(90)
turtle.pu()

turtle.fd(200)
rosinha("magenta")

turtle.fd(200)
rosinha("red")

turtle.fd(-400)
rosinha("purple")

#Para salvar o desenho da tela num arquivo .ps   
tc= turtle.Screen().getcanvas()
tc.postscript(file="flores.ps")


