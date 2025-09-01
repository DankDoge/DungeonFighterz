# importing libraries - tpeWriter is used for making text seem like it's been typed
import random as r
from time import sleep as s
import sys
import winsound

# variables/lists defined before any of the code
enemyNameList = []
x=1

# typeWriter function - makes the text look like it's being typed. Speed can be set by the function's 2nd parameter. Default speed is an integer between 2 and 5 as defined by the typSpeed variable
typSpeed = r.randint(2,5)/100
def typeWriter(message, speed=0):
    for x in message:
        print(x, end='', flush=True)
        sys.stdout.flush()
        s(speed)
    print("\n", end="")

# def objects

"""
def fighter class
hp = hitpoints (how much health the fighter has)
at = attack (how much damage the fighter does)
dg = dodge (chance to dodge attack) [dodge chance = dg%]
id is used for fighter calss's number which is used for lists
"""
class fighter:
    fighterCount = 1
    def __init__(self, type, hp, at, dg):
        self.type = type
        self.hp = hp
        self.at = at
        self.dg = dg
        self.id = fighter.fighterCount
        fighter.fighterCount += 1

"""
used to define both the player and enemy

"""
class character(fighter):
    def __init__(self, name):
        self.name = name

class move:
    def __init__(self, char, choice):
        self.char = char
        self.choice = choice

# setting up the player and enemy classes
player = character("")
enemy = character("")

# list of all the fighterTypes with their stats
fighterTypes = [
fighter("Knight", 200, 30, 5),
fighter("Barbarian", 100, 50, 10),
fighter("Archer", 75, 40, 20),
fighter("Ranger", 50, 60, 10)
#Classes: ranger, paladin, wizard, berserker, wandering trader, Warden, Cataphract, Imperial Legionary, auxillarey
]

# exposition
typeWriter("Hello, I am the king")
typeWriter("And I need you to fight someone, cuz I'm bored")
typeWriter("First, what is your name fighter?")
playerName = input()
typeWriter(f"{playerName}? How interesting")
typeWriter("I suppose you should pick your fighter type now")
typeWriter(f"You have {len(fighterTypes)} options right now")

# used to list all the options for the player to pick. It's made so that all I have to do is just add a new fighter to the FighterType list and the amount listed changes
for fighters in fighterTypes:
    if fighters.id == x:
        message = f"{x}. {fighters.type}"
        typeWriter(message) 
    x+=1

# sets the player and enemy fightertypes
typeWriter("Select your class by typing either 1,2,etc.")
player = enemy = fighterTypes[int(input())-1]
while enemy.type == player.type:
    enemy = fighterTypes[r.randint(0,len(fighterTypes)-1)]
player.name = playerName
enemy.name = "Enemy"
typeWriter(f'Wow the {player.type} class!')
typeWriter("Why don't we focus on your enemy now?")
typeWriter(f"Well for starters their name is '{enemy.name}'")
typeWriter(f"Their class will also be {enemy.type}")
typeWriter(f"why don't we start the battle?")

# copy of the ininital player and enemy data to be used to show change in stats
playerP = player
EnemyE = enemy

# the game itself pretty much, everything before was just setup lolz
while player.hp or enemy.hp != 0:
    typeWriter(  f"""
{player.name}'s Health: {player.hp}/{playerP.hp}
{enemy.name}'s Health: {enemy.hp}/{EnemyE.hp}

1. Attack
          """)
    Pchoice = input()