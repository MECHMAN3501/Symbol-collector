import keyboard
import time
import os
import random
hp=3
score=0
player_leight=3
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
symlist=[['dollar','$'],['rubl','₽'],['plus','+'],['minus','-'],['bomb','*'],['extra_life','=']]
class Symbol():
    '''
    Класс символа который создаёт, рисует и оперирует символ.
    '''
    def __init__(self, symbol: str):
        '''
        Функция которая инициализирует переменные
        self.symbol = symbol
        self.x = 0
        self.y = 0
        self.generated = 0
        '''
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
    def catch(self):

        self.generated=False
        screen[self.y][self.x]=' '
    def miss(self):
        if self.y==len(screen):
            self.generated=False

run=True
plx=7
for i in symlist:
    i[0]=Symbol(i[1])
#dollar.generate()
while run:
    for i in range(0,15):
        screen[-1][i]=' '
    if keyboard.is_pressed('a'):
        plx-=1
    if keyboard.is_pressed('d'):
        plx+=1
    for i in range(-(player_leight//2),player_leight-1):
        screen[-1][plx+i]='='
    
    #screen[-1][plx]='='
    #screen[-1][plx+1]='='
    #screen[-1][plx-1]='='
    print('score:',score, 'leight:', player_leight)
    print('== '*hp)
    print('---------------')
    for i in screen:
        screenstr=''
        for j in i:
            screenstr+=j
        print(screenstr)
    print('---------------')
    newsym=random.randint(0,18)
    if newsym<6 and symlist[newsym][0].generated==False:
        symlist[newsym][0].y=0
        symlist[newsym][0].generated=True
        symlist[newsym][0].generate()
        
    for i in symlist:
        if i[0].y==len(screen)-1:
            i[0].generated=False
            screen[i[0].y][i[0].x]=' '
        if i[0].y==8 and screen[9][i[0].x]=='=':
            i[0].generated=False
            screen[i[0].y][i[0].x]=' '
            if i[1]=='=':
                if hp!=5:
                    hp+=1
            elif i[1]=='$':
                score+=25
            elif i[1]=='₽':
                score+=10
            elif i[1]=='+':
                if player_leight!=5:
                    player_leight+=2
            elif i[1]=='-':
                player_leight-=2
            elif i[1]=='*':
                hp-=1
        if i[0].generated:
            i[0].fall()
    
    time.sleep(0.5)
    os.system('cls')
