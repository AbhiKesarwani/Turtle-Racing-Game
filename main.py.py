from turtle import Turtle, Screen
import random
import tkinter

screen = Screen()

#setting screen for race

screen.setup(width=500, height=400)
screen.bgcolor("black")

#setting result window
def window(winner, result):
    output_text = f"{winner}\n{result}"
    result_declaration = tkinter.Label(text=output_text, font=("Arial", 24, "italic"))
    result_declaration.pack()

#drawing starting and ending line

for line in range(2):
    x = [-210, 210]
    tom = Turtle()
    tom.speed("fast")
    tom.hideturtle()
    tom.goto(x[line], -140)
    tom.pendown()
    tom.pencolor("white")
    tom.pensize(10)
    tom.setheading(90)
    tom.fd(320)
    tom.penup()

#setting turtle's
colors = ["red", "yellow", "blue", "orange", "pink", "purple"]
objects = []
for turtle_object in range(6):
    tom = Turtle()
    tom.color(colors[turtle_object])
    tom.penup()
    tom.shape("turtle")
    tom.goto(x=-240, y=150 - 50 * turtle_object)
    objects.append(tom)

screen.title("Turtle's Race")
is_race_on = False
user_turtle = screen.textinput("Bet on Turtle", "Which color turtle will win?").lower()
if user_turtle:
    is_race_on = True

#moving turtle and deciding winner
if user_turtle in colors:
    while is_race_on:
        for turtle_object in objects:
            turtle_object.fd(random.randint(0, 10))
            if turtle_object.xcor()>200:
                is_race_on = False
                winner_turtle = colors[objects.index(turtle_object)]
                winner = f"The color of winner turtle is {winner_turtle}"
                if user_turtle == winner_turtle:
                    result = "Your turtle won the race."
                    window(winner, result)
                else:
                    result = "Your turtle lost the race."
                    window(winner, result)
                break
else:
    winner = "Invalid Turtle Colour Input."
    result = "Try Again."
    window(winner, result)

screen.exitonclick()