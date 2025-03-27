# код Савелия Жердеева
# приведение кода к PEP8 Савелия Жердеева
import csv
import time
def SetNewScore(name: str, score: int):
    '''
    Функция которая добавляет новый рекорд
    '''
    with open ('leaderboard.csv', 'a', newline = '', encoding = 'utf-16') as file:
        fields = ['score', 'name']
        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writerow({'score' : score, 'name' : name})
        file.close()
    with open ('leaderboard.csv', 'r', encoding = 'utf-16') as file:
        reader = csv.reader(file)
        reader = sorted(reader, key = lambda row: int(row[0]), reverse = True)
        file.close()
        
    with open ('leaderboard.csv', 'w', newline = '', encoding = 'utf-16') as file:
        csvwriter = csv.writer(file)
        for i in reader:
            csvwriter.writerow(i)
        file.close()
def GetScores():
    '''
    Функция которая возвращает все рекорды в формате [рекорд,имя]
    '''
    with open ('leaderboard.csv', 'r', encoding = 'utf-16') as file:
        scorelist = []
        reader = csv.reader(file)
        for i in reader:
            scorelist.append(i)
        return scorelist
