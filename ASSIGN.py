import csv

with open("Starfish_Data.csv") as data_file:
    data = csv.reader(data_file)
    distances=[]
    total=0
    numerater=0
    for row in data:
        if row[2]!='Prob':
            total = total + int(row[2])
            distance = (10**(0.2*(int(float(row[0]))+(2.5*int(float(row[1])))+0.17)))
            numerater = numerater + distance*int(row[2])
    wavg = numerater/total
    print(wavg)
