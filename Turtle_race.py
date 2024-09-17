from turtle import Turtle,Screen
from random import randint


screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="Make your bet",prompt="Which turtle wl win the race? Enter a color from rainbow: ")

colors=["red","orange","yellow","green","blue","purple"]
y_position=[80,50,20,-20,-50,-80]
turtles=[]
for i in range(6) :
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    turtles.append(new_turtle)

if bet:
    race_on=True

while race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            race_on=False
            winning=turtle.pencolor()
            if winning==bet:
                print(f"You have won the race. The {winning} is the winner!!!")
            else:
                print(f"You have lost the race. The {winning} is the winner!!!")
        else:
            turtle.forward(randint(0, 10))


screen.exitonclick()