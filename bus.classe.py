class Bus:
    def __init__(self, num, hDep, tDep):
        trajet = new Trajet(0, hDep, 'T0', tDep)
        self.num = num
        self.hSor = trajet.duree
        self.hRet = -1
        self.planning = []

    def dispo(heure, terminus):
        lastTrajet = self.planning[-1]
        if(lastTrajet.hArrivee > heure):
            res = false
        else:
            dure = duree(lastTrajet.tArrivee, terminus)
            if(dure < 5):
                if(5 + lastTrajet.hArrivee < heure):
                    res = true
                else:
                    res = false
            else:
                if(dure + lastTrajet.hArrivee < heure):
                    res = true
                else:
                    res = false
                
        return res

    def addTrajet(trajet):
        #TODO