class Bus:
    def __init__(self, num, hDep, tDep):
        trajet = new Trajet(0, 
                            hDep, 
                            'T0', 
                            tDep, 
                            distance("T0", tDep), 
                            0, 
                            "", 
                            "", 
                            duree("T0", tDep))
        self.num = num
        self.hSor = trajet.duree
        self.hRet = -1
        self.planning = []
        self.planning.append(trajet)

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
        lastTrajet = self.planning[-1]
        dure = duree(lastTrajet.tArrivee, trajet.tArrivee)
        trajetTerminus = new Trajet(lastTrajet.hArrivee, 
                            trajet.hDepart, 
                            lastTrajet.tArrivee, 
                            trajet.tDepart, 
                            distance(lastTrajet.tArrivee, trajet.tDepart), 
                            0, 
                            "", 
                            "", 
                            duree(lastTrajet.tArrivee, trajet.tDepart))
        
        if(dure < 5):
            trajetWait = new Trajet(lastTrajet.hArrivee, 
                                    lastTrajet.hArrivee + (trajet.hDepart - lastTrajet.hArrivee), 
                                    lastTrajet.tArrivee, 
                                    lastTrajet.tArrivee, 
                                    0, 
                                    0, 
                                    "", 
                                    "", 
                                    trajet.hDepart - lastTrajet.hArrivee)
            self.planning.append(trajetWait)
            self.planning.append(trajetTerminus)
        else if(dure >= 5):
            self.planning.append(trajetTerminus)


        self.planning.append(trajet)