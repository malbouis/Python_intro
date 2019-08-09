import turtle

tammy = turtle.Turtle()
tammy.color("green")
tom = turtle.Turtle()
tom.color("blue")
tere = turtle.Turtle()
tere.color("yellow")

fimx = 200
fimy = 250

target = turtle.Turtle()
target.shape("turtle")
target.color("red","red")
target.pu()
target.setpos(fimx,fimy)
target.stamp()


while  tom.pos()[0]!=target.pos()[0]:
    tom.fd(10)

tom.left(90)

while  tom.pos()[1]!=target.pos()[1]:
    tom.fd(10)

while tere.pos()[0]!=target.pos()[0] and tere.pos()[1]!=target.pos()[1]:
    tere.fd(50)
    tere.left(90)
    tere.fd(50)
    tere.right(90)
tere.fd(30)
if tere.pos()!=target.pos():
    tere.goto(target.pos())


if (tammy.pos()[1]-target.pos()[1])>0:
    tammy.seth(270)
    tammy.fd(tammy.pos()[1]-target.pos()[1])
elif(tammy.pos()[1]-target.pos()[1])<0:
    tammy.seth(90)
    tammy.fd(target.pos()[1]-tammy.pos()[1])
if (tammy.pos()[0]-target.pos()[0])>0:
    tammy.seth(180)
    tammy.fd(tammy.pos()[0]-target.pos()[0])
elif(tammy.pos()[0]-target.pos()[0])<0:
    tammy.seth(0)
    tammy.fd(target.pos()[0]-tammy.pos()[0])
