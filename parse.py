

import time, sys, getopt
import csv
import operator
from datetime import timedelta
from solution import *
from trajet import *


def initSolution(lignes, indexLignes):
    s = Solution(lignes, indexLignes)
    return s

def parse(horaireFile, sortedByHDepart=True):
    listTrajets, tempListTrajets, indexLignes, lignes = [], [], [], {}
    previousLigne, isLigneDifferent = None, False

    with open(horaireFile, 'r') as f:
        csvFile = csv.reader(f, delimiter=',')
        numLigne, rowList, distLigne, noRow, sens = "", [], None, False, "r"

        # Parcours de ligne
        for row in csvFile:
            # Parcours de colonne
            for iCol in range(0, len(row)):
                col = row[iCol]
                if "ligne" in col:
                    sens = "a" if sens == "r" else "r"
                    noRow = True
                    numLigne = col[6:]

                    if previousLigne != numLigne and previousLigne != None:
                        isLigneDifferent = True
                    else:
                        isLigneDifferent = False

                    previousLigne = numLigne
                    break
                elif iCol == 0 and "Dist" not in col:
                    rowList.append(row)
                    noRow = False
                    break
                elif "Dist" in col:
                    noRow = True
                    distLigne = row
                    break

            if len(rowList) != 0 and noRow == True:
                # Parse rows
                maxTrajetRowSize = getMaxTrajetRowSize(rowList)
                lignes[numLigne + ":" + sens] = [None for _ in range(maxTrajetRowSize)]
                indexLignes.append(numLigne + ":" + sens)

                for x in range(1, maxTrajetRowSize):
                    firstTime,  lastTime,  tDepart,  tArrivee, dist = None, None, None, None, distLigne[x]

                    for y in range(0, len(rowList)):
                        try:
                            time = rowList[y][x]
                            if firstTime == None and time != "":
                                firstTime = time
                                tDepart = rowList[y][0]
                            elif firstTime != None and time != "":
                                lastTime = time
                                tArrivee = rowList[y][0]
                        except IndexError:
                            continue

                    if firstTime != None and lastTime != None:
                        hDepart = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=int(firstTime.split(":")[1]), hours=int(firstTime.split(":")[0]))
                        hArrivee = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=int(lastTime.split(":")[1]), hours=int(lastTime.split(":")[0]))
                        t = Trajet(hDepart, hArrivee, tDepart, tArrivee, dist, "l"+numLigne, sens, x, hArrivee - hDepart)

                        tempListTrajets.append(t)


                        if sortedByHDepart == False:
                            isLigneDifferent, listTrajets, tempListTrajets = sortLignesByTime(isLigneDifferent, listTrajets, tempListTrajets, t)
                        else:
                            listTrajets.append(t)

                        # print(hDepart, hArrivee, tDepart, tArrivee, dist, "l"+numLigne, sens, x, hArrivee - hDepart)

                noRow = False
                rowList = []
            previousLigne = numLigne

    if sortedByHDepart == False:
        isLigneDifferent, listTrajets, tempListTrajets = sortLignesByTime(isLigneDifferent, listTrajets, tempListTrajets, t, True)

    s = initSolution(indexLignes, lignes)

    # i = 1
    # for index in indexLignes:
    #     print index + " " + str(lignes[index])

    #     if i % 2 == 0:
    #         print ""

    #     i += 1




    if sortedByHDepart == True:
        listTrajets = sorted(listTrajets, key=operator.attrgetter("hDepart"))

    s = initSolution(lignes, indexLignes)
    return (listTrajets, s)

def sortLignesByTime(isLigneDifferent, listTrajets, tempListTrajets, t, force=False):
    tempLastTrajet = tempListTrajets[-1]
    del tempListTrajets[-1]

    if isLigneDifferent == True or force == True:
        tempListTrajets = sorted(tempListTrajets, key=operator.attrgetter("hDepart"))
        listTrajets.extend(tempListTrajets)
        del tempListTrajets[:]
        tempListTrajets.append(tempLastTrajet)
        isLigneDifferent = False
    else:
        tempListTrajets.append(t)

    return (isLigneDifferent, listTrajets, tempListTrajets)

def getMaxTrajetRowSize(rowList):
    maxRowSize = 0
    for y in range(0, len(rowList)):
        if len(rowList[y]) > maxRowSize:
            maxRowSize = len(rowList[y]) - 1

    return maxRowSize


'''
horaireFile = ""
try:
    opts, args = getopt.getopt(sys.argv[1:],"h:")
except getopt.GetoptError:
   print 'parse.py -h horaires'
   sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        horaireFile = arg

parse(horaireFile, False)
'''
