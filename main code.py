import keyboard
import time

import random
hp=3
screen=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ]

class Symbol():
    def __init__(self, symbol=str):
        self.symbol=symbol
        self.y=0
        self.x=0
        self.generated=False
    def generate(self):
        global screen
        self.x=random.randint(0,14)
        screen[0][self.x]=self.symbol
        self.generated=True
    def fall(self):
        global screen
        screen[self.y][self.x]=' '
        self.y+=1
        screen[self.y][self.x]=self.symbol
run=True
plx=7
dollar=Symbol('$')
rubl=Symbol('₽')
bomb=Symbol('*')
plus=Symbol('+')
minus=Symbol('-')
extra_life=Symbol('=')
dollar.generate()
while run:
    screen[-1][plx]=' '
    screen[-1][plx+1]=' '
    screen[-1][plx-1]=' '
    if keyboard.is_pressed('a'):
        plx-=1
    if keyboard.is_pressed('d'):
        plx+=1
    screen[-1][plx]='='
    screen[-1][plx+1]='='
    screen[-1][plx-1]='='
    print('---------------')
    for i in screen:
        screenstr=''
        for j in i:
            screenstr+=j
        print(screenstr)
    print('---------------')
    newsym=random.randint(0,6)
    if newsym==0 and not dollar.generated:
        dollar.generate()
    elif newsym==1 and not rubl.generated:
        rubl.generate()
    elif newsym==2 and not bomb.generated:
        bomb.generate()
    elif newsym==3 and not plus.generated:
        plus.generate()
    elif newsym==4 and not minus.generated:
        minus.generate()
    elif newsym==5 and not extra_life.generated:
        extra_life.generate()
    dollar.fall()
    rubl.fall()
    bomb.fall()
    plus.fall()
    minus.fall()
    extra_life.fall()
    time.sleep(0.5)
