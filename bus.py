from matriceDT import *
from parse import *
from datetime import timedelta

class Bus:
    def __init__(self, num, hDep, tDep):

        mat = MatriceDT()
        trajet = Trajet(hDep - timedelta(minutes=int(mat.getDuree("T0", tDep))) , 
                            hDep, 
                            'T0', 
                            tDep, 
                            mat.getDistance("T0", tDep), 
                            "DEP", 
                            "  ", 
                            "  ", 
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
            lastTrajet.hArrivee + tmps - timedelta(minutes=int(dure)),  
            lastTrajet.tArrivee, 
            lastTrajet.tArrivee, 
            0, 
            "ATT", 
            "  ", 
            "  ", 
            int(tmps.seconds/60) - int(dure))

        trajetTerminus = Trajet(trajetWait.hArrivee, 
            trajet.hDepart, 
            lastTrajet.tArrivee, 
            trajet.tDepart, 
            mat.getDistance(lastTrajet.tArrivee, trajet.tDepart), 
            "TAV", 
            "  ", 
            "  ", 
            dure)

        if(int(tmps.seconds/60) != dure and len(self.planning) > 1):
            self.planning.append(trajetWait)

        if(lastTrajet.tArrivee != trajet.tDepart):
            self.planning.append(trajetTerminus)


        self.planning.append(trajet)

    def __str__(self):
        lignes = []
        ban = ["ATT","DEP","TAV"]
        for t in self.planning :
            if((t.ligne not in lignes) and t.ligne not in ban) : lignes.append(t.ligne)
        text = "Bus n" + str(self.num)+  "\n"
        text += ",".join(lignes) +"\n"

        for t in self.planning :
            text += "   " + str(t) +"\n"

        return text