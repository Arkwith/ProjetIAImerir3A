class Solution:
        '''
        Structure du tableau
            Exemple pour la ligne 10 retour
            '10:r' = [v1, v2, v3, v4]

            Access a partir du code : lignes['15:r'][indexDuVoyage]
        '''
        lignes = None
        indexLignes = []
        sizeLignes = []
        lignesNum = []
        listeBus = []
	def __init__(self, lignes, indexLignes, sizeLignes, lignesNum, listeBus):
		self.matBus = []
                self.lignes = lignes
                self.indexLignes = indexLignes
                self.sizeLignes = sizeLignes
                self.lignesNum = lignesNum
                self.listeBus = listeBus

        def initNbLignes(self, nb):
            lignes = [] *  nb

        def addToSolution(self,trajet,numBus):
                index = trajet.ligne[1:] +":" + trajet.sens
                self.lignes[index][int(trajet.index)-1] = numBus




