from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

game_over = False

while not game_over:
    screen.bgcolor('black')
    user_choice = screen.textinput(title="Turtle Race",
                                   prompt="Choose a winner (red, purple, blue, green, yellow, orange): ").lower()
    colors = ["red", "purple", "blue", "green", "yellow", "orange"]
    all_turtles = []

    race_on = True

    for _ in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[_])
        new_turtle.goto(x=-230, y=(90 - (_ * 30)))
        all_turtles.append(new_turtle)

    while race_on:
        for turtle in all_turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() > 230:
                race_on = False
                winner = turtle.pencolor()

    if winner == user_choice:
        play_again = screen.textinput(title="You win!", prompt="Would you like to play again? (Type 'yes' or 'no'): ")
        if play_again == 'no':
            game_over = True
    else:
        play_again = screen.textinput(title=f"You lose! The {winner} turtle finished first",
                                      prompt="Would you like to play again? (Type 'yes' or 'no'): ")
        if play_again == 'no':
            game_over = True
    screen.clearscreen()

screen.exitonclick()
