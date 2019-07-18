from musica_piano import *
import random
import turtle
import math


def desenhar_circulo(t,centro,raio):
    t.pu()
    t.goto(centro[0],centro[1]-raio)
    t.pd()
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def desenhar_alvo(loc,raio):
    c=turtle.Turtle()
    c.color("red","white")
    c.pensize(raio/4)
    desenhar_circulo(c,loc,raio)
    desenhar_circulo(c,loc,raio/1.8)
    desenhar_circulo(c,loc,raio/8)
    c.hideturtle()
    
def distancia(t,loc):
    dist = math.sqrt( ( t.pos()[0] - loc[0] )**2 +  (t.pos()[1] - loc[1])**2 )
    return dist

def p1():
    do.toca(0.5)
    re.toca(0.5)
    mi.toca(0.5)    
    do.tocafade(0.5)
    sleep(0.5)
def p2():
    mi.toca(0.5)
    fa.toca(0.5)
    sol.tocafade(1)
    sleep(1)
def p3():
    sol.toca(0.25)
    la.toca(0.25)
    sol.toca(0.25)
    fa.toca(0.25)
    mi.toca(0.5)
    do.tocafade(0.5)
    sleep(0.5)
def p4():
    do.toca(0.5)
    sol3.toca(0.5)
    do.tocafade(1)
    sleep(1)
    
def toca_meu_sininho():
    p1()
    p1()
    p2()
    p2()
    p3()
    p3()
    p4()
    p4()

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(2)

centro=(100,150)
raio=100
desenhar_alvo(centro,raio)

def random_walk(t,paso,ang):
    while abs(t.pos()[0]) <300 and  abs(t.pos()[1])<300 :
        if round(distancia(t,centro),2) <= raio*9/8 :
            toca_meu_sininho()
            break
        else:
            t.fd(paso*random.random())
            t.left(random.random() * ang)

random_walk(t,20,45)
