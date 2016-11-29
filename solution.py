from parse import *


class Solution:
        lignes = None
        indexLignes = []
	def __init__(self, lignes, indexLignes):
		self.matBus = []
                self.lignes = lignes
                self.indexLignes = indexLignes

        def initNbLignes(self, nb):
            lignes = [] *  nb

        def addToSolution(self,trajet,numBus):
		    index = trajet.ligne[1:] +":" + trajet.sens
		    self.lignes[index][int(trajet.index)-1] = numBus




