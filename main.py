import csv
import json

voiture = 55 #CO2 en g / passager/km
bus = 68
moto = 72
train = 14
avion = 285
nombrePassager = 157
depart = "SAINT-MALO"
end = "PARIS"
liste = []
master = []


def rechercheDepart(depart):
        for i in range(0, len(liste)):
            listTmp = list(liste[i])
            if depart in listTmp:
                if depart == listTmp[1]:
                    listTmp[1] = listTmp[0]
                    listTmp[0] = depart
                listTmp.append([depart])
                print(listTmp)
                master.append(listTmp)


def rechercheVille2(depart, tab, history):
    for i in range(0, len(liste)):
        listTmp = list(liste[i])
        historyTmp = list(history)
        if depart in listTmp and historyTmp not in tab:
            if depart == listTmp:
                listTmp[1] = listTmp[0]
                listTmp[0] = depart
            listTmp.append(historyTmp.append(depart))
            print(historyTmp)
            print(tab)
            tab.append(listTmp)


def rechercheVille3(depart, tab, history):
    for i in range(0, len(liste)):
        if depart in liste[i] and tab != history:
            if depart == liste[i][1]:
                liste[i][1] = liste[i][0]
                liste[i][0] = depart
            liste[i].append(history[4].append(depart))
            tab.append(liste[i])


def openCsv():
    with open('reseaux.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            liste.append([row[0], row[1], row[2], row[3]])


def main():
    rechercheDepart(depart)
    tmp = []
    for i in range(len(master)):
        rechercheVille2(master[i][1], tmp, master[i][4])
    masterEnd = [list(master), list(tmp)]
    fin = 0
  #  while True:
   #     tmp = []
    #    for i in range(len(master[len(master) - 1])):
     #       rechercheVille3(master[len(master)-1][i][1], tmp, master[len(master)-1][i])
      #  master.append(tmp)
       # fin += 1
        #if fin == 4 :
         #   break
    return masterEnd
openCsv()

masterEnd = main()

for i in range(len(masterEnd)):
    print(masterEnd[i])
