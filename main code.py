import keyboard
import time

import random
hp=3
screen=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ',' ',' '],
        [' ','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ','-',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ','$',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ]

class symbol():
    def __init__(self, symbol=str):
        self.symbol=symbol
    def generate(self):
        global screen
        self.x=random.randint(0,15)
        screen[0][self.x]
        
run=True
plx=7

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
    time.sleep(0.5)
