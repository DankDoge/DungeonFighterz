import random as r # rng component
from time import sleep as s # stops program from running for a set time
import sys # gimmick stuff idrk what the library does specifically
import winsound # sound, not yet implemented

enemyNameList = []
num=1
Repeat = True

# typeWriter function - makes the text look like it's being typed. Speed can be set by the function's 2nd parameter. Default speed is an integer between 2 and 5 as defined by the typSpeed variable
typSpeed = r.randint(2,5)/100
def typeWriter(message, speed=0):
    for char in message:
        print(char, end='', flush=True)
        sys.stdout.flush()
        s(speed)
    print("\n", end="")

# def objects

"""
def fighter class
hp = hitpoints (how much health the fighter has)
oghp = permanent hitpoints (how much health the fighter had before the fight)
at = attack (how much damage the fighter does)
dg = dodge (chance to dodge attack) [dodge chance = dg / 100 * 100%]
acc = accuracy (chance to miss attack) [miss chance = (1 - acc / 100) * 100%]
ma = magic affinity (how effective heal is) [heal * ma/100]
arm = armor (extra hp that won't be healed)
id is used for fighter class's number which is used for lists

IDEAS:
crt = critical hit (would be a 1.25x, 1.5x, or 2x multiplier to dmg, some classes would specialize in this -- like barbarian!)
mn = mana (for more mystical fightertypes like wizard or elf. Would have this to deliever unique spells and tricks. 
Might also turn into an energy system which could help with balancing)
"""
class fighter:
    fighterCount = 1
    def __init__(self, type, hp, arm, at, dg, acc, ma):
        self.type = type
        self.hp = round(hp)
        self.oghp = self.hp
        self.arm = arm
        self.ogarm = self.arm
        self.at = at
        self.dg = dg
        self.acc = acc
        self.ma = ma
        self.id = fighter.fighterCount
        fighter.fighterCount += 1

    # used to determine the winner and loser (which lets be for real, YOU are the loser hahahaha)
    def place(self):
        if self.hp != 0:
            typeWriter(f"{self.name} won!")
        else:
            lossNum += 1
            if lossNum == 2:
                extraLoss = " as well"
            typeWriter(f"{self.name} lost" + extraLoss + "!")
    

"""
def moves (currently represents attacks, but will at some point affect health and defence and other stats)
the max and min represent the range of damage

class move:
    def __init__(self,name,max,min):
        self.name = name
        self.max = max
        self.min = min
"""




# list of different possible moves
moveList = [
"Attack",
"Heal"
]

# writes the actual move list during the game, iterates through the list so all the dev needs to do is add the attack name :)
moveStr = ''
moveCount = 0
while moveCount != len(moveList):
    moveStr += str(moveCount+1) + '. ' + moveList[moveCount] + '\n'
    moveCount += 1

"""
move system of the game, the pokemon part pretty much. 
Includes an error check to see make sure the user's input is an integer and within the number of choices
Attacking (move 1):
- first takes into account the dodge chance and sets variable of dodge to either true or false based on rng. 
  If rng is less than or equal to dodge, dodge will be true and vice versa
- since the integer value of true is 1 and false is 0. The damage will get mutliplied by 0 when the dodge is True 
  and mutliplied by 1 when dodge is false
- The target will take damage, or succesfuly dodge where the respective message will be displayed

Healing (move 2):
- Simple heal that heals by percentage based on rng
"""

def move(choice, attacker, target):
    try:
        int_Choice = int(choice)
    except:
        print("that is not a Repeat move try again\n")
    else:        
        global Repeat
        Repeat = False
        if int_Choice == 1:
            noDodged = target.dg < r.randint(1,100) # equals 0 if target dodged, and 1 if target didn't dodge
            noMissed = attacker.acc >= r.randint(1,100) # equals 0 if attacker missed, and 1 if attacker didn't miss

            dmg = attacker.at * int(noDodged) * int(noMissed) 
            target.hp -= dmg

            finalMessageList = [
            f"{attacker.name} dealt {dmg} damage to {target.name}",
            f"{target.name} dodged {attacker.name}'s attack!",
            f"{attacker.name} missed!",
            f"{target.name} dodged, but {attacker.name} still hit them and dealt {dmg} damage!"
            ]

            return finalMessageList[int(not noDodged) + 2 * int(not noMissed)]  
        elif int_Choice == 2:
            heal_pcent = r.randrange(10,50, 5)
            plus_heal = attacker.oghp * heal_pcent / 100 * attacker.ma / 100
            attacker.hp += plus_heal
            finalMessageList[
            f"{attacker.name} healed {heal_pcent}% or {plus_heal} hp!"
            ]
            return finalMessageList[0]
        elif int_Choice > len(moveList):
            print('Make sure to pick a value between 1 and', len(moveList))
            Repeat = True
        else:
            pass

"""
used to define both the player and enemy

"""
class character(fighter):
    def __init__(self, name, id):
        self.name = name
        self.id = id

# setting up the player and enemy classes
player = character("", 0)
enemy = character("", 1)

# list of all the fighterTypes with their stats (name, hp, arm, at, dg, acc, ma)
fighterTypes = [
fighter("Knight", 170, 50, 30, 5, 95, 70),
fighter("Barbarian", 110, 20, 60, 10, 80, 110),
fighter("Archer", 75, 25, 50, 20, 60, 125),
fighter("Wizard", 70, 10, 60, 15, 50, 140),
fighter("God", 999, 999, 999, 100, 100, 999)
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
    if fighters.id == num:
        message = f"{num}. {fighters.type}"
        typeWriter(message) 
    num+=1

# sets the player and enemy fightertypes
typeWriter("Select your class by typing either 1,2,etc.")

# sets player and enemy to the same class initially, however repeats the process of selecting a class until both player and enemy have diff classes, possibly change depending on how I feel lolz
player = enemy = fighterTypes[int(input())-1]
while enemy.type == player.type or enemy.type == "God":
    enemy = fighterTypes[r.randint(0,len(fighterTypes)-1)]

# setting up the name of the player again... along with the enemy as well! Will add list of possible enemy names... maybe enemy names based on class idk
player.name = f"{player.type} {playerName}"
enemy.name = f"{enemy.type} Enemy"

typeWriter(f'Wow the {player.type} class!')
typeWriter("Why don't we focus on your enemy now?")
typeWriter(f"Well for starters their name is '{enemy.name}'")
typeWriter(f"Their class will also be {enemy.type}")
typeWriter(f"why don't we start the battle?")

# the game itself pretty much, everything before was just setup lolz
while player.hp > 0 and enemy.hp > 0:
    typeWriter(  f"""
{player.name} 
Armor: {player.arm}/{player.ogarm} Health: {player.hp}/{player.oghp} 

{enemy.name} 
Armor: {enemy.arm}/{enemy.ogarm} Health: {enemy.hp}/{enemy.oghp} 
          """)
    typeWriter(moveStr)
    while Repeat:
        Pchoice = input("Your move: ")
        Pmove = move(Pchoice, player, enemy)
    typeWriter("\n" + Pmove)
    Emove = move(r.randint(1,1), enemy, player)
    typeWriter(Emove + "\n")
    Repeat = True
    
    player.hp = 0
    enemy.hp = 0
    # player.hp = max(0, player.hp)
    # enemy.hp = max(0, enemy.hp)

# we're in the endgame now, time to see by how much you lost!
player.place()
enemy.place()





    

