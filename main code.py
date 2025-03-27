# код Соловьева Владимира
import keyboard
import time
import os
import random
import leaderboard
wide_time=0
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
        self.x=random.randint(2,12)
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


def IsOnRightBorder():
    if plx+1==14 and player_leight==3:
        return True
    elif plx+2==14 and player_leight==5:
        return True
    else:
        return False
    
    
def IsOnLeftBorder():
    global plx, player_leight
    if plx-1==0 and player_leight==3:
        return True
    elif plx-2==0 and player_leight==5:
        return True
    else:
        return False
run=True
plx=7
for i in symlist:
    i[0]=Symbol(i[1])
print('  | SYMBOL        |')
print('  |     COLLECTOR |')
print('  |  =        *   |')
print('  |             + |')
print('  |     $         |')
print('  |   ===         |')
print('press enter for start')
just_for_delay=input()
os.system('cls')
print('controls:')
print(' left arrow - move left')
print(' right arrow - move right')
print('info:')
print('you are: ===')
print('$ - gives 25 points')
print('₽ - gives 10 points')
print('+ - increase platform to 5 blocks for 10 seconds')
print('- - decrease platform back to 3 blocks')
print('= - gives an extra life')
print('* - decrease your life by one')
print('----------------------------------')
print('grab as much points as you can!')
print('you have no life = game over')
time.sleep(7)
os.system('cls')
while run:
    for i in range(0,15):
        screen[-1][i]=' '
    if keyboard.is_pressed('left arrow') and not IsOnLeftBorder():
        plx-=1
    if keyboard.is_pressed('right arrow') and not IsOnRightBorder():
        plx+=1
    if player_leight==5:
        if plx==1:
            plx==2
        if plx==13:
            plx==12
    
    if player_leight==3:
        for i in range(-1,2):
            screen[-1][plx+i]='='
    if player_leight==5:
        for i in range(-2,3):
            screen[-1][plx+i]='='
    print('score:',score, 'leight:', player_leight)
    print('== '*hp)
    print('-----------------')
    for i in screen:
        screenstr=''
        for j in i:
            screenstr+=j
        print('|'+screenstr+'|')
    print('-----------------')
    newsym=random.randint(0,18)
    if newsym>6:
        newsym=4
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
            i[0].y=0
            if i[1]=='=':
                if hp!=5:
                    hp+=1
            elif i[1]=='$':
                score+=25
            elif i[1]=='₽':
                score+=10
            elif i[1]=='+':
                if IsOnLeftBorder():
                    plx+=1
                elif IsOnRightBorder():
                    plx-=1
                if player_leight!=5:
                    player_leight+=2
                wide_time=25
            elif i[1]=='-':
                if player_leight==5:
                    player_leight-=2
            elif i[1]=='*':
                hp-=1
        if i[0].generated:
            i[0].fall()
    if wide_time==0:
        player_leight==3
    if hp==0:
        print('===============')
        print('|  Game over  |')
        print('===============')
        print('your score:',score)
        name=input('enter your name:')
        leaderboard.SetNewScore(name, score)
        run=False
        time.sleep(1)
    wide_time-=1
    time.sleep(0.2)
    os.system('cls')
print('--------top 10--------')
file=open('leaderboard.txt', 'r')
for i in range(0,10):
    file.readline(i)
    print(file.readline(i))
