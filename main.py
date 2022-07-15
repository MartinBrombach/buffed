import os
import keyboard
from time import sleep

#Clearing the terminal to make it look better
os.system('CLS')

#Welcome screen
print('\033[1;37mWelcome to Grinding simulator')
print('Do you want to continue on character or creat a new character')
print('')
print('\033[1;32mWhen a list like this appears use arrow up and down to pick and press arrow right to select\033[1;37m')

#Temp variable
temp = 0

#Player attributes
class attributes():
    health = 100
    strength = 5
    agility = 1
    inteligence = 0
    luck = 0

def typing(text, color):
    for char in text:
        sleep(0.01)
        print(color+char, end='', flush=True)
    print()

#Code for multiple choice
def multipleChoice(ar):
    for i in ar:
        print(i)
    print('---------------------')
    print(ar[0])
    temp=0
    sleep(1)
    while True:
        sleep(.1)
        if keyboard.is_pressed('up'):
            if temp==0:
                jjk=0
            else:
                temp-=1
                print('\033[1A', end='\x1b[2K')
                print(ar[temp])
        elif keyboard.is_pressed('down'):
            if temp==(len(ar)-1):
                jjk=0
            else:
                temp+=1
                print('\033[1A', end='\x1b[2K')
                print(ar[temp])
        elif keyboard.is_pressed('right'):
            for removes in range(len(ar)+2):
                print('\033[1A', end='\x1b[2K')
            print('You chose '+ar[temp])
            return ar[temp]
            break

def newGame():
    typing('Welcome to the beautiful world of Bufania.', '\033[1;37m')
    sleep(1.5)
    typing('This game is a text based mix between Super Life RPG, Sword and Sandals and Pokèmon.', '\033[1;37m')
    sleep(3)
    typing('The goal of this game is to defeat all the champions and become the strongest.', '\033[1;37m')
    sleep(2)
    print('')
    typing('Now type the name of your character: ', '\033[1;33m')
    os.chdir('saves')
    counting=0
    while True:
        name = input('\033[A\033[37C\033[1;32m')
        saveGames = os.listdir()
        savesArr=[]
        for saves in saveGames:
            saves = saves.replace('.txt', '')
            savesArr.append(saves)
        if name not in savesArr:
            print('\033[1A', end='\x1b[2K')
            print('\033[1A', end='\x1b[2K')
            print('')
            print(f'\033[1;33mNow type the name of your character: \033[1;32m{name}')
            print('')
            print(f'\033[1;37mAre you sure you want to name your character {name}?')
            tempArr=['Yes', 'No']
            if multipleChoice(tempArr) == 'Yes':
                os.chdir('../')
                break
            else:
                for i in range(4):
                    print('\033[1A', end='\x1b[2K')
                print(f'\033[1;33mNow type the name of your character: ')
        else:
            counting+=1
            if counting >=1:
                print('\033[1A', end='\x1b[2K')
            print('\033[1A', end='\x1b[2K')
            print('\033[1;31mThat name is allready taken, try again.')
            print('\033[1;33mNow type the name of your character: ')
    # Add creating of savefile HERE
    # Add creating of savefile HERE
    # Add creating of savefile HERE
    # Add creating of savefile HERE
    # Add creating of savefile HERE
    # Add creating of savefile HERE
    os.system('CLS')
    typing(f'Your name is {name}, and you are verry weak.', '\033[1;37m')
    atb = attributes()
    sleep(1)
    print()
    typing('This is your stats:', '\033[1;37m')
    sleep(1)
    print('\033[1;32mHealth: ', atb.health)
    print('\033[1;31mStrength: ', atb.strength)
    print('\033[1;34mAgility: ', atb.agility)
    print('\033[1;36mInteligence: ', atb.inteligence)
    print('\033[1;35mLuck: ', atb.luck)
    print('\033[1;37m')
    sleep(3)
    typing('There is not currently a tutorial at this time... ', '\033[1;37m')
    sleep(2)
    typing('You will now appear at the tavern. GLHF', '\033[1;37m')
    sleep(1)
    typing('PSA: The game will only autosave after returning to tavern.', '\033[1;31m')
    sleep(1)
    typing('Press arrow right to continue...', '\033[1;30m')
    while True:
        sleep(.05)
        if keyboard.is_pressed('right'):
            break

#The game
def game(newOrOld):
    os.system('CLS')
    if newOrOld=='new':
        newGame()
    atb = attributes()
    os.system('CLS')
    print('\033[1;37mGame start')

#If continue is chosen this loads the save
def loadGame(saveGame):
    with open(saveGame+'.txt', 'r') as save:
        obj = attributes()
        stats = save.readlines()
        for stat in stats:
            stat = stat.strip('\n').split(':')
            setattr(obj, stat[0], int(stat[1]))


def findSave():
    os.chdir('saves')
    saveGames = os.listdir()
    savesArr=[]
    for saves in saveGames:
        saves = saves.replace('.txt', '')
        savesArr.append(saves)
    sleep(.5)
    print('')
    while True:
        print('Choose your save')
        temp = multipleChoice(savesArr)
        loadGame(temp)
        atb = attributes()
        print('')
        print('\033[1;32mHealth: ', atb.health)
        print('\033[1;31mStrength: ', atb.strength)
        print('\033[1;34mAgility: ', atb.agility)
        print('\033[1;36mInteligence: ', atb.inteligence)
        print('\033[1;35mLuck: ', atb.luck)
        print('\033[1;37m')
        conf = multipleChoice(['Confirm', 'Re select'])
        if conf=='Confirm':
            break
        else:
            for i in range(11):
                print('\033[1A', end='\x1b[2K')
            print('')
    os.chdir('../')
    game('old')


#Checking if new game or continue game
startAr = ['New game', 'Continue']
startGame = multipleChoice(startAr)
if startGame == 'Continue':
    findSave()
elif startGame == 'New game':
    game('new')