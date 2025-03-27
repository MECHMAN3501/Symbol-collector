# код Савелия Жердеева
import csv
import time
def SetNewScore(name: str, score: int):

    with open ('leaderboard.csv', 'a', newline='', encoding='utf-16') as file:
        fields=['score', 'name']
        writer=csv.DictWriter(file, fieldnames=fields)
        writer.writerow({'score' : score, 'name' : name})
        file.close()
    with open ('leaderboard.csv', 'r', encoding='utf-16') as file:
        reader=csv.reader(file)
        reader = sorted(reader, key=lambda row: int(row[0]), reverse=True)
        file.close()
        
    with open ('leaderboard.csv', 'w', newline='', encoding='utf-16') as file:
        csvwriter=csv.writer(file)
        for i in reader:
            csvwriter.writerow(i)
        file.close()
def GetScores():
    with open ('leaderboard.csv', 'r', encoding='utf-16') as file:
        scorelist=[]
        reader=csv.reader(file)
        for i in reader:
            scorelist.append(i)
        return scorelist
