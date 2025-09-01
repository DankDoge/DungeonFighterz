# importing libraries
import random as r
from time import sleep as s
import sys
import winsound

# defining lists that each character has
playerinv = []

# creating classes

# character class for character stats
class character:
    def __init__(self, name, hp, inv):
        self.name = name
        self.hp = hp
        self.inv = inv

# item class for item stats
class item:
    def __init__(self, name, durab, id):
        self.name = name
        self.durab = durab
        self.id = id

# defining the player
player = character("", 100, playerinv)

def typeWriter(message):
    y=0
    for x in message:
        print(x, end='', flush=True)
        sys.stdout.flush()
        timeSleep = r.randint(3,10)/100
        s(timeSleep)
    print("\n", end="")

typeWriter("Hello Player")
typeWriter("What is your name?")
player.name = input()
typeWriter(player.name + "?")
typeWriter("what a stupid name")
typeWriter("Anyways")
typeWriter("Let's begin with the actual story")
typeWriter("Uh lemme get my notes really quick")
typeWriter("Why don't I just hand you it?")