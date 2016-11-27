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
                        else:
                            line.append(item)
                self.matrice.append(line)
        finally:
            f.close()

    def initDT(self, distanceFichier, tempsFichier):
        f = open(distanceFichier, 'rb')
        g = open(tempsFichier, 'rb')

        try:
            readerf = csv.reader(f, delimiter = ";")
            readerg = csv.reader(g, delimiter = ",")
            for row in readerf:
                line = []
                for item in row:
                    if (item != ""):
                        if (item[0] != "T"):
                            value = [item, "empty"]
                            line.append(value)
                        else:
                            line.append(item)
                self.matrice.append(line)

            i = 0
            for row in readerg:
                j = -1
                for item in row:
                    if (item != ""):
                        if (item[0] != "T"):
                            if(i != 0):
                                print(item, j, i)
                                #self.matrice[i][j][1] = item
                            
                    j = j+1
                i = i+1
        finally:
            f.close()
            g.close()



mat = matriceDT()
mat.initD("dist_terminus.csv")#, "terminus.csv")
print(mat.matrice)

#g = open("terminus.csv", 'rb')
#try:
#    reader = csv.reader(g, delimiter = ",")
#    for row in reader:
#        print row.value
#finally:
#    g.close()