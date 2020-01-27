import turtle
import os

class Player(turtle):
    player = turtle.Turtle()
    player_speed = 15

    def __init__(self):
        self.player.color("blue")
        self.player.shape("triangle")
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0, -250)
        self.player.setheading(90)