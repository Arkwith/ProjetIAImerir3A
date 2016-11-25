# matriceDT.py

import csv

class matriceDT:
    def __init__(self):
        self.matrice = [] #On a le tableau de base
    def initD(self, distanceFichier):

        f = open(distanceFichier, 'rb')
        try:
            reader = csv.reader(f, delimiter = ";")
            for row in reader:
                line = []
                for item in row:
                    if (item != ""):
                        if (item[0] != "T"):
                            value = [item, str(int(item) * 60 / 25)]
                            line.append(value)
                self.matrice.append(line)
        finally:
            f.close()

    def initDT(self, distanceFichier, tempsFichier):
        f = open(distanceFichier, 'rb')
        g = open(tempsFichier, 'rb')

        try:
            readerf = csv.reader(f, delimiter = ";")
            readerg = csv.reader(g, delimiter = ",")
            for row in 



mat = matriceDT()
mat.initD("dist_terminus.csv")
print(mat.matrice)

#g = open("terminus.csv", 'rb')
#try:
#    reader = csv.reader(g, delimiter = ",")
#    for row in reader:
#        print row.value
#finally:
#    g.close()