# matriceDT.py

import csv
import random

class MatriceDT:
    class __MatriceDT:
        def __init__(self):
            self.matrice = [] #On a le tableau de base
            self.maxDistance = 0

        def initD(self, distanceFichier):
            print("init matrice 1 fichier")

            f = open(distanceFichier, 'rb')
            try:
                reader = csv.reader(f, delimiter = ",")
                for row in reader:
                    line = []
                    for item in row:
                        if (item != ""):
                            if (item[0] != "T"):
                                if int(item) > self.maxDistance:
                                    self.maxDistance = int(item)
                                value = [item, str(int(item) * 60 / 25)]
                                line.append(value)
                            else:
                                line.append(item)
                    self.matrice.append(line)
            finally:
                f.close()

    def initDT(self, distanceFichier, tempsFichier):
        print("init matrice 2 fichiers")

        f = open(distanceFichier, 'rb')
        g = open(tempsFichier, 'rb')

        try:
            readerDistance = csv.reader(f, delimiter = ",")
            readerDuree = csv.reader(g, delimiter = ",")
            for row in readerDistance:
                line = []
                for item in row:
                    if (item != ""):
                        if ("T" not in item):
                            if int(item) > self.maxDistance:
                                self.maxDistance = int(item)
                            value = [item, 0]
                            line.append(value)
                        else:
                            line.append(item)
                self.matrice.append(line)

            i = 0
            for row in readerDuree:
                j = 0
                for item in row:
                    if (item != ""):
                        if ("T" not in item):
                            self.matrice[i][j][1] = item
                    j = j+1
                i = i+1
        finally:
            f.close()
            g.close()

    def initRATP(self, distanceFichier):
        print("init matrice RATP")

        f = open(distanceFichier, 'rb')
        try:
            reader = csv.reader(f, delimiter = ",")
            i = 0
            for row in reader:
                line = []
                j = 0
                for item in row:
                    if (item != ""):
                        if (j != 0 and i != 0):
                            dist = float(item)/1000
                            if dist > self.maxDistance:
                                self.maxDistance = dist
                            value = [str(dist), str(dist * 60 / 25)]
                            line.append(value)
                        else:
                            line.append(item)
                    elif (j == i):
                        line.append([0,0])
                    else:
                        line.append(self.matrice[j][i])


                    j+=1

                self.matrice.append(line)
                i+=1
        finally:
            print self.maxDistance
            f.close()


    def getDepots(self):
        if(self.matrice[0][0] == 'T0'):
            return ['T0']
        else:
            return ['1','2','3','4','5']

    def getDistance(self, ligne, colonne):
        if ligne[0] == 'T':
            i = int(ligne[1:])
            j = int(colonne[1:])
        #print(i,j)
            return self.matrice[i+1][j+1][0]
        else:
            lin = 0
            col = 0
            for i in range(0,len(self.matrice[0])):
                if self.matrice[0][i] == ligne:
                    lin = i
                if self.matrice[i][0] == colonne:
                    col = i
            return self.matrice[lin][col][0]


    def getDuree(self, ligne, colonne):
        if ligne[0] == 'T':
            i = int(ligne[1:])
            j = int(colonne[1:])
            return self.matrice[i+1][j+1][1]
        else:
            lin = 0
            col = 0
            for i in range(0,len(self.matrice[0])):
                if self.matrice[0][i] == ligne:
                    lin = i
                if self.matrice[i][0] == colonne:
                    col = i
            return self.matrice[lin][col][1]


    instance = None

    def __init__(self):
        if not MatriceDT.instance:
            MatriceDT.instance = MatriceDT.__MatriceDT()

    def __getattr__(self, name):
        return getattr(self.instance, name)
