# код Соловьева Владимира
# приведение кода к PEP8 Савелия Жердеева
import keyboard
import time
import os
import random
import leaderboard

wide_time = 0
hp = 3
score = 0
player_length = 3
tps = 15

screen = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
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

symlist = [['dollar','$'],['rubl','₽'],['plus','+'],['minus','-'],['bomb','ð'],['extra_life','=']]
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
        self.symbol = symbol
        self.y = 0
        self.x = 0
        self.generated = False
    
    
    def generate(self):
        '''
        Функция которая генерирует символ
        '''
        global screen
        self.x = random.randint(2,12)
        screen[0][self.x] = self.symbol
        self.generated = True
    
    
    def fall(self):
        '''
        Функция которая двигает символ вниз
        '''
        global screen
        screen[self.y][self.x] = ' '
        self.y += 1
        screen[self.y][self.x] = self.symbol
    
    
    def catch(self):
        '''
        Функция которая обрабатывает ловлю символа платформой
        '''
        self.generated = False
        screen[self.y][self.x] = ' '
    
    
    def miss(self):
        '''
        Функция которая обрабатывает попадание символа на пол
        '''
        if self.y == len(screen):
            self.generated = False


def IsOnRightBorder():
    '''
    Функция которая возвращает True если платформа в правом углу
    '''
    if plx + 1 == 14 and player_length == 3:
        return True
    elif plx + 2 == 14 and player_length == 5:
        return True
    else:
        return False
    
    
def IsOnLeftBorder():
    
    '''
    Функция которая возвращает True если платформа в левом углу
    '''
    global plx, player_length
    if plx - 1 == 0 and player_length == 3:
        return True
    elif plx - 2 == 0 and player_length == 5:
        return True
    else:
        return False


run = True
plx = 7
for i in symlist:
    i[0] = Symbol(i[1])
print('  ╒═══════════════╕')
print('  │ SYMBOL        │')
print('  │     COLLECTOR │')
print('  │  =        ð   │')
print('  │             + │')
print('  │     $         │')
print('  │   ===         │')
print('  ╘═══════════════╛')
print('Press Enter for >START<')
just_for_delay = input()
os.system('cls')
print('Controls:')
print(' left arrow - move left')
print(' right arrow - move right')
print(' Esc - exit')
print('Info:')
print('You are: ===')
print('$ - gives 25 points')
print('₽ - gives 10 points')
print('+ - increase platform up to 5 blocks for 10 seconds')
print('- - decrease platform back to 3 blocks')
print('= - gives an extra life')
print('ð - decrease your life by one')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('Score as much as you can!')
print('Lost all lives = Game over')
time.sleep(3)
print('Ready...')
time.sleep(3)
print('Steady...')
time.sleep(2)
print('GO!!!')
time.sleep(0.3)
os.system('cls')

while run:
    for i in range(0,15):
        screen[-1][i] = ' '
    if keyboard.is_pressed('left arrow') and not IsOnLeftBorder():
        plx -= 1
    if keyboard.is_pressed('right arrow') and not IsOnRightBorder():
        plx += 1
    if keyboard.is_pressed('escape'):
        break
    
    if player_length == 5:
        if plx == 1:
            plx == 2
        if plx == 13:
            plx == 12
    if player_length == 3:
        for i in range(-1,2):
            screen[-1][plx+i] = '='
    if player_length == 5:
        for i in range(-2,3):
            screen[-1][plx+i] = '='
    
    print('Score:',score, 'Length:', player_length)
    print('== '*hp)
    
    print('╒═══════════════╕')
    for i in screen:
        screenstr = ''
        for j in i:
            screenstr += j
        print('│' + screenstr + '│')
    print('╘═══════════════╛')
    
    newsym=random.randint(0, 18)
    if newsym > 6:
        newsym = 4
    if newsym < 6 and symlist[newsym][0].generated == False:
        symlist[newsym][0].y = 0
        symlist[newsym][0].generated = True
        symlist[newsym][0].generate()
        
    for i in symlist:
        if i[0].y == len(screen)-1:# если символ упал на пол, то пропадает
            i[0].generated=False
            screen[i[0].y][i[0].x] = ' '
        if i[0].y == 8 and screen[9][i[0].x] == '=':# если упал на игрока
            i[0].generated = False
            screen[i[0].y][i[0].x] = ' '
            i[0].y = 0
            if i[1] == '=':  # добавляет жизнь
                if hp != 5:
                    hp += 1
            elif i[1] == '$':  # добавляет 25 очков
                score += 25
            elif i[1] == '₽':  # добавляет 10 очков
                score += 10
            elif i[1] == '+':  # расширяет игрока на 5 секунд
                if IsOnLeftBorder():
                    plx += 1
                elif IsOnRightBorder():
                    plx -= 1
                if player_length != 5:
                    player_length += 2
                wide_time = tps * 5
            elif i[1] == '-':  # принудительно сужает игрока
                if player_length == 5:
                    player_length -= 2
            elif i[1] == 'ð':  # отнимает жизнь
                hp -= 1
        if i[0].generated:
            i[0].fall()
    if wide_time == 0:
        player_length == 3
    if hp == 0:
        print('╒═══════════════╕')
        print('│   Game over   │')
        print('╘═══════════════╛')
        time.sleep(2)
        print('Your score:', score)
        while True:
            name = input('Enter your name:')
            if name == '':
                print('Name cannot be empty')
                continue
            if len(name) > 10:
                print('Please shorter name, no more 10 char')
                continue
            else:
                break
        leaderboard.SetNewScore(name, score)
        run = False
        time.sleep(1)
    wide_time -= 1
    time.sleep(tps / 100)
    os.system('cls')
ldb = leaderboard.GetScores()
print('        ╔════════╗')
print('════════╣ TOP 10 ╠════════')
print('  name  ╚═══╤╤═══╝  score ')
if len(ldb) < 10:
    topsize = len(ldb)
else:
    topsize = 10

for i in range(0, topsize):
    if len(ldb[i][1]) < 10:
        print(' ' + str(ldb[i][1]) + ' ' * (9-len(ldb[i][1])) + '  ││       ' + ldb[i][0])
