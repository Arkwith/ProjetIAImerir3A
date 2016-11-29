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

    def __str__(self):
        text = "ligne : " + str(self.ligne) + "  sens : " + self.sens + "  index : " + str(self.index)
        text += "  dep : " + str(self.tDepart) + " " + str(self.hDepart)
        text += "  arr : " + str(self.tArrivee) + " " + str(self.hArrivee)
        return text

