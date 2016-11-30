from matriceDT import *
from parse import *
from datetime import timedelta

class Bus:


    def __init__(self, num, hDep, tDep):

        mat = MatriceDT()
<<<<<<< HEAD
        trajet = Trajet(hDep - timedelta(minutes=int(mat.getDuree("T0", tDep))) ,
                            hDep,
                            'T0',
                            tDep,
                            mat.getDistance("T0", tDep),
                            "DEP",
                            "  ",
                            "  ",
                            timedelta(minutes=int(mat.getDuree("T0", tDep))))
=======
        list_depots = mat.getDepots()
        distDep = -1

        for d in list_depots:
            distTmp = mat.getDistance(d,tDep);
            #print distTmp
            #print distDep
            if(float(distTmp) < float(distDep) or distDep == -1):
                distDep = distTmp
                self.depot = d

        trajet = Trajet(hDep - timedelta(minutes=float(mat.getDuree(d, tDep))) ,
                            hDep,
                            self.depot,
                            tDep,
                            distDep,
                            "DEP",
                            "  ",
                            "  ",
                            timedelta(minutes=float(mat.getDuree(d, tDep))))
>>>>>>> fba354a58663fa2b95da64917560766d152962ec
        self.num = num
        self.hSor = trajet.duree
        self.hRet = -1
        self.planning = []
        self.planning.append(trajet)
    
    def dispo(self,heure, terminus):
        if(len(self.planning) == 0):
            return True
        mat = MatriceDT()
        lastTrajet = self.planning[-1]
        if(lastTrajet.hArrivee > heure):
            res = False
        else:
            dure = mat.getDuree(lastTrajet.tArrivee, terminus)
            dure_time = timedelta(seconds = 60 * float(dure))
            if(float(dure) < 5):
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

    def retourDepot(self):
        mat = MatriceDT()
        lastTrajet = self.planning[-1]
<<<<<<< HEAD
        dure = mat.getDuree(lastTrajet.tArrivee,"T0")
        trajetDep = Trajet(lastTrajet.hArrivee,
            lastTrajet.hArrivee +  timedelta(minutes=int(dure)),
            lastTrajet.tArrivee,
            "T0",
=======
        dure = mat.getDuree(lastTrajet.tArrivee,self.depot)
        trajetDep = Trajet(lastTrajet.hArrivee,
            lastTrajet.hArrivee +  timedelta(minutes=float(dure)),
            lastTrajet.tArrivee,
            self.depot,
>>>>>>> fba354a58663fa2b95da64917560766d152962ec
            0,
            "DEP",
            "  ",
            "  ",
<<<<<<< HEAD
            timedelta(minutes=int(dure)))
=======
            timedelta(minutes=float(dure)))
>>>>>>> fba354a58663fa2b95da64917560766d152962ec
        self.planning.append(trajetDep)


    def addTrajet(self,trajet):
        mat = MatriceDT()
        lastTrajet = self.planning[-1]
        tmps = trajet.hDepart - lastTrajet.hArrivee
        dure = mat.getDuree(lastTrajet.tArrivee, trajet.tDepart)

        trajetWait = Trajet(lastTrajet.hArrivee,
<<<<<<< HEAD
            lastTrajet.hArrivee + tmps - timedelta(minutes=int(dure)),
=======
            lastTrajet.hArrivee + tmps - timedelta(minutes=float(dure)),
>>>>>>> fba354a58663fa2b95da64917560766d152962ec
            lastTrajet.tArrivee,
            lastTrajet.tArrivee,
            0,
            "ATT",
            "  ",
            "  ",
<<<<<<< HEAD
            timedelta(minutes=int(tmps.seconds/60) - int(dure)))
=======
            timedelta(minutes=float(tmps.seconds/60) - float(dure)))
>>>>>>> fba354a58663fa2b95da64917560766d152962ec

        trajetTerminus = Trajet(trajetWait.hArrivee,
            trajet.hDepart,
            lastTrajet.tArrivee,
            trajet.tDepart,
            mat.getDistance(lastTrajet.tArrivee, trajet.tDepart),
            "TAV",
            "  ",
            "  ",
<<<<<<< HEAD
            timedelta(minutes=int(dure)))
=======
            timedelta(minutes=float(dure)))
>>>>>>> fba354a58663fa2b95da64917560766d152962ec

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
