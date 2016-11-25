#!/usr/bin/python

import time, sys, getopt
import csv
from datetime import timedelta


def parse(horaireFile):
    with open(horaireFile, 'r') as f:
        csvFile = csv.reader(f, delimiter=',')
        numLigne = ""
        rowList = []
        distLigne = None
        noRow = False
        sens = "r"
        # Parcours de ligne
        for row in csvFile:
            # Parcours de colonne
            for iCol in range(0, len(row)):
                col = row[iCol]
                if "ligne" in col:
                    sens = "a" if "r" else "a"
                    numLigne = col[5:]
                    noRow = True
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
                print "RowList : ", len(rowList)

                for x in range(1, maxTrajetRowSize):
                    firstTime = None
                    lastTime = None
                    tDepart = None
                    tArrivee = None
                    dist = distLigne[x]
                    for y in range(0, len(rowList)):
                        try:
                            time = rowList[y][x]
                            if firstTime == None and time != "":
                                firstTime = time
                                tDepart = rowList[y][0]
                                print firstTime, lastTime, time
                            elif firstTime != None and time != "":
                                lastTime = time
                                tArrivee = rowList[y][0]
                                print firstTime, lastTime, time
                        except IndexError:
                            print "Index Error"
                            continue
                    if firstTime != None and lastTime != None:
                        hDepart = timedelta(int(firstTime.split(":")[0]), int(firstTime.split(":")[1]))
                        hArrivee = timedelta(int(lastTime.split(":")[0]), int(lastTime.split(":")[1]))
                        Trajet(hDepart, hArrivee, tDepart, tArrivee, dist, "l"+numLigne, sens, x, hArrivee - hDepart)
                        print(firstTime, lastTime, tDepart, tArrivee, dist, "l"+numLigne, sens, x, hArrivee - hDepart)

                noRow = False
                rowList = []

def getMaxTrajetRowSize(rowList):
    maxRowSize = 0
    for y in range(0, len(rowList)):
        if len(rowList[y]) > maxRowSize:
            maxRowSize = len(rowList[y])

    return maxRowSize

class Trajet:
    hDepart = None
    hArrivee = None
    tDepart = None
    tArrivee = None
    dist = None
    ligne = None
    sens = None
    index = None
    duree = None

    def __init__(self, hDepart, hArrivee, tDepart, tArrivee, dist, ligne, sens, index, duree):
        self.hDepart = hDepart
        self.hArrivee = hArrivee
        self.tDepart = tDepart
        self.tArrivee = tArrivee
        self.dist = dist
        self.ligne = ligne
        self.sens = sens
        self.index = index
        self.duree = duree



horaireFile = ""
try:
    opts, args = getopt.getopt(sys.argv[1:],"h:")
except getopt.GetoptError:
   print 'parse.py -h horaires'
   sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        horaireFile = arg

parse(horaireFile)
