import  turtle
import time
wn=turtle.Screen()
wn.title("chut")
wn.bgcolor("black")
wn.register_shape("jar.gif")
wn.register_shape("vi.gif")
player=turtle.Turtle()
player.shape("jar.gif")
def player_animation():
    if player.shape()=="jar.gif":
        player.shape("vi.gif")
    elif player.shape()=="vi.gif":
        player.shape("jar.gif")

    wn.ontimer(player_animation(),50000)
