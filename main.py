import csv

depart = "SAINT-MALO"
end = "AJACCIO"
voiture = 55 #CO2 en g / passager/km
bus = 68
moto = 72
train = 14
avion = 285
nombrePassager = 157

liste = []
master = []
calcul = []
resultat = []


def calculCarbon(km, moyen):
    if moyen == 'ROUTIER':
        bilan = km * voiture * nombrePassager
    elif moyen == 'AERIEN':
        bilan = km * avion * nombrePassager
    elif moyen == 'FERRE':
        bilan = km * train * nombrePassager
    return bilan


def openCsv():
    with open('reseaux.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            liste.append([row[0], row[1], row[2], row[3]])


def rechercheDepart(depart):
    for i in range(0, len(liste)):
        listTmp = list(liste[i])
        if depart in listTmp:
            if depart == listTmp[1]:
                listTmp[1] = listTmp[0]
                listTmp[0] = depart
            listTmp.append([depart])
            master.append(listTmp)
            master[-1][3] = calculCarbon(int(master[-1][3]), master[-1][2])


def rechercheVille2(ville, tab, history, carbon,transport):
    for i in range(0, len(liste)):
        listTmp = list(liste[i])
        historyTmp = list(history)
        historyTmp.append(ville)
        if ville in listTmp and historyTmp[0] not in tab:
            if ville == listTmp[1]:
                listTmp[1] = listTmp[0]
                listTmp[0] = ville
            listTmp.append(historyTmp)
            listTmp.append([transport,listTmp[2]])
            tab.append(listTmp)
            tab[-1][3] = calculCarbon(int(tab[-1][3]), tab[-1][2]) + int(carbon)


def rechercheVille3(ville, tab, history, carbon, transport):
    for i in range(0, len(liste)):
        bool = True
        listTmp = list(liste[i])
        historyTmp = list(history)
        historyTmp.append(ville)
        transportTmp = list(transport)
        if ville in listTmp:
            for j in range(len(historyTmp) - 1):
                if historyTmp[j] in listTmp:
                    bool = False
                    break
            if not bool:
                continue
            if ville == listTmp[1]:
                listTmp[1] = str(listTmp[0])
                listTmp[0] = str(ville)
            listTmp.append(historyTmp)
            transportTmp.append(listTmp[2])
            listTmp.append(transportTmp)
            tab.append(listTmp)
            tab[-1][3] = calculCarbon(int(tab[-1][3]), tab[-1][2]) + int(carbon)


def main():
    rechercheDepart(depart)
    tmp = []
    for i in range(len(master)):
        rechercheVille2(master[i][1], tmp, master[i][4], master[i][3], master[i][2])
    masterEnd = [list(master), list(tmp)]
    while True:
        tmp = []
        for i in range(len(masterEnd[len(masterEnd) - 1])):
            if masterEnd[len(masterEnd)-1][i][1] != end:
                rechercheVille3(masterEnd[len(masterEnd)-1][i][1], tmp, masterEnd[len(masterEnd)-1][i][4], masterEnd[len(masterEnd)-1][i][3], masterEnd[-1][i][5])
            else:
                resultat.append(masterEnd[len(masterEnd)-1][i])
        if tmp:
            masterEnd.append(tmp)
        else:
            break
    return masterEnd


openCsv()

masterEnd = main()

temp = resultat[0][3]
sauv = []
transportfinal = []

for line in resultat:
    if line[3] < temp:
        temp = line[3]
        sauv = list(line[4])
        transportfinal = list(line[5])
        sauv.append(end)

print("\nLe trajet passe par le villes suviantes : " + str(sauv) + " avec une consomation de "
      + str(temp) + "g de CO2 en utilisant" + str(transportfinal))


