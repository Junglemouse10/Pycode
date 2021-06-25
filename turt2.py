import turtle
screen = turtle.Screen()
t = turtle.Turtle()
#turtle.tracer(0, 0)

dist = 2
for i in range(9999999999999999):
    t.fd(dist)
    t.pencolor('#00FFFF')
    t.rt(190)
    t.speed(50)
    turtle.bgcolor('#0000FF')
    dist += 10 # dist = 10 dist + 10
    print(dist)
#turtle.update()
screen.exitonclick()    
