import csv
import time

score=input("score")
username=input("name")

with open ("protleader.txt", "a", newline='') as file:
    fields=['score', 'name']
    writer=csv.DictWriter(file, fieldnames=fields)
    writer.writerow({'score' : score, 'name' : username})

with open ("protleader.txt", "r") as file:
    sortlist=[]
    reader=csv.reader(file)
    for i in reader:
        sortlist.append(i)

for i in range(len(sortlist)):
    if i != 0:
        sortlist[i][0]=int(sortlist[i][int(0)])