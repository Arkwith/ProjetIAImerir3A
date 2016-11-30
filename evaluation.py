from bus import *
from datetime import timedelta

def scoresUnitaires(listeBus):
	dureeTot = 0
	distanceTot = 0
	nbBus = len(listeBus)

	for bus in listeBus:
		for trajet in bus.planning:
			dureeTot += float(trajet.duree.seconds / 60)
			distanceTot += float(trajet.dist)

	return (nbBus,dureeTot,distanceTot)

def scoreSolution(listeBus):
	poidBus = 875*150000
	poidTemps = 1
	poidDistance = 4

	nbBus,dureeTot,distanceTot =	scoresUnitaires(listeBus)

	res = (poidBus * nbBus) + (poidTemps * dureeTot) + (poidDistance * distanceTot) 
	return res