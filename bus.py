from matriceDT import *
from parse import *
from datetime import timedelta

class Bus:
    def __init__(self, num, hDep, tDep):

        mat = MatriceDT()
        trajet = Trajet(0, 
                            hDep, 
                            'T0', 
                            tDep, 
                            mat.getDistance("T0", tDep), 
                            0, 
                            "", 
                            "", 
                            mat.getDuree("T0", tDep))
        self.num = num
        self.hSor = trajet.duree
        self.hRet = -1
        self.planning = []
        self.planning.append(trajet)

    def dispo(self,heure, terminus):
        mat = MatriceDT()
        lastTrajet = self.planning[-1]
        if(lastTrajet.hArrivee > heure):
            res = False
        else:
            dure = mat.getDuree(lastTrajet.tArrivee, terminus)
            dure_time = timedelta(seconds = 60 * int(dure))
            if(int(dure) < 5):
                if(timedelta(seconds=300) + lastTrajet.hArrivee < heure):
                    res = True
                else:
                    res = False
            else:
                if(dure_time + lastTrajet.hArrivee < heure):
                    res = True
                else:
                    res = False
                
        return res

    def addTrajet(self,trajet):
        mat = MatriceDT()
        lastTrajet = self.planning[-1]
        tmps = trajet.hDepart - lastTrajet.hArrivee
        dure = mat.getDuree(lastTrajet.tArrivee, trajet.tDepart)

        trajetWait = Trajet(lastTrajet.hArrivee, 
            lastTrajet.hArrivee + timedelta(seconds=((int(tmps.seconds/60) - int(dure)*60))), 
            lastTrajet.tArrivee, 
            lastTrajet.tArrivee, 
            0, 
            0, 
            "", 
            "", 
            int(tmps.seconds/60) - int(dure))

        trajetTerminus = Trajet(lastTrajet.hArrivee, 
            trajet.hDepart, 
            lastTrajet.tArrivee, 
            trajet.tDepart, 
            mat.getDistance(lastTrajet.tArrivee, trajet.tDepart), 
            0, 
            "", 
            "", 
            dure)

        if(int(tmps.seconds/60) != dure):
            self.planning.append(trajetWait)

        if(lastTrajet.tArrivee != trajet.tDepart):
            self.planning.append(trajetTerminus)


        self.planning.append(trajet)

    def __str__(self):
        text = "Bus n" + str(self.num) + "\n"

        for t in self.planning :
            text += "   " + str(t) +"\n"

        return text