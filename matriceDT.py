# matriceDT.py

import csv

class matriceDT:
    def __init__(self):
        self.matrice = [] #On a le tableau de base
    def initD(self, distanceFichier):

        f = open(distanceFichier, 'rb')
        try:
            reader = csv.reader(f, delimiter = ",")
            for row in reader:
                line = []
                for item in row:
                    if (item != ""):
                        if (item[0] != "T"):
                            value = [item, str(int(item) * 60 / 25)]
                            line.append(value)
                        else:
                            line.append(item)
                self.matrice.append(line)
        finally:
            f.close()

    def initDT(self, distanceFichier, tempsFichier):
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

    def getDistance(self, ligne, colonne):
        i = int(ligne[1:])
        j = int(colonne[1:])
        print(i,j)
        return self.matrice[i+1][j+1][0]

    def getDuree(self, ligne, colonne):
        i = int(ligne[1:])
        j = int(colonne[1:])
        return self.matrice[i+1][j+1][1]


mat = matriceDT()
mat.initDT("dist_terminus.csv", "terminus.csv")

print(mat.getDistance('T5','T12'), mat.getDuree('T5','T12'))

