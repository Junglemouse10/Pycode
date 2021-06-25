#turt2.py
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
#turtle.tracer(0,0)

dist = -150
for i in range(599):        #TIME
    t.fd(dist)
    t.pencolor('#FFFFFF')
    t.speed(9999999999999)
    t.rt(229)
    turtle.bgcolor('#000000')
    dist += 2000# dist = 2000 dist + 2000
    print(dist)
    
    dist = 444
for i in range(144):
    t.fd(dist)
    t.pencolor('#FFFFFF')
    t.speed(2000)
    t.rt(499)
    turtle.bgcolor('#000000')
    dist +=  10# dist = 10 dist + 10
    print(dist)
   
#turtle.update()
screen.exitonclick() 


