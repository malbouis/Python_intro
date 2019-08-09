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
    tere.fd(10)
    tere.left(90)
    tere.fd(10)
    tere.right(90)

n=0
while tammy.pos()[0]!=target.pos()[0] or tammy.pos()[1]!=target.pos()[1]:
    tammy.fd(10)
    tammy.left(90)
    tammy.fd(10)
    tammy.right(90)
    n+=1
    if n > 100:
        print(n)
        break

while  tom.pos()[0]!=target.pos()[0]:
    tom.fd(10)

tom.left(90)

while  tom.pos()[1]!=target.pos()[1]:
    tom.fd(10)
