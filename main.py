import os
import keyboard
from time import sleep
from threading import Thread

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
            if multipleChoice(tempArr) == tempArr[0]:
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
    atb = attributes()
    with open(f'{name}.txt', 'w') as create:
        create.write(f'health:{atb.health}\n')
        create.write(f'strength:{atb.strength}\n')
        create.write(f'agility:{atb.agility}\n')
        create.write(f'inteligence:{atb.inteligence}\n')
        create.write(f'luck:{atb.luck}')
    os.chdir('../')
    os.system('CLS')
    typing(f'Your name is {name}, and you are verry weak.', '\033[1;37m')
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

#All the different choices from tavern
def fight():
    while True:
        os.system('CLS')
        fightArr = ['Fight', 'Info', 'Back to tavern']
        choice = multipleChoice(fightArr)
        if choice == fightArr[0]:
            print('Fight')
        elif choice == fightArr[1]:
            print('Info')
        elif choice == fightArr[2]:
            break


#The game
def game(newOrOld):
    os.system('CLS')
    if newOrOld=='new':
        newGame()
    atb = attributes()
    while True:
        os.system('CLS')
        print('\033[1;37mWelcome to the tavern. Choose your activity')
        activity = ['Fight', 'Train', 'Settings', 'Save', 'Exit']
        selected = multipleChoice(activity)
        if selected == activity[0]:
            fight()
        elif selected == activity[1]:
            print('Train')
        elif selected == activity[2]:
            print('Settings')
        elif selected == activity[3]:
            print('Save')
        elif selected == activity[4]:
            os.system('CLS')
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
    while True:
        print('Choose your save')
        temp = multipleChoice(savesArr)
        print('\033[1A', end='\x1b[2K')
        loadGame(temp)
        atb = attributes()
        print(f'You chose {temp}, this is the stats:')
        print('\033[1;32mHealth: ', atb.health)
        print('\033[1;31mStrength: ', atb.strength)
        print('\033[1;34mAgility: ', atb.agility)
        print('\033[1;36mInteligence: ', atb.inteligence)
        print('\033[1;35mLuck: ', atb.luck)
        print('\033[1;37m')
        conf = multipleChoice(['Confirm', 'Re select'])
        if conf == conf[0]:
            break
        else:
            for i in range(7):
                print('\033[1A', end='\x1b[2K')
    os.chdir('../')
    game('old')


#Checking if new game or continue game
startAr = ['New game', 'Continue']
startGame = multipleChoice(startAr)
if startGame == startAr[1]:
    findSave()
elif startGame == startAr[0]:
    game('new')
