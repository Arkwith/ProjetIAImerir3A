from bus import *
from datetime import timedelta

def scoresUnitaires(listeBus):
	dureeTot = 0
	distanceTot = 0
	nbBus = len(listeBus)

	for bus in listeBus:
		for trajet in bus.planning:
			dureeTot += int(trajet.duree.seconds / 60)
			distanceTot += int(trajet.dist)

	return (nbBus,dureeTot,distanceTot)

def scoreSolution(listeBus):
	poidBus = 50 
	poidTemps = 10
	poidDistance = 10

	nbBus,dureeTot,distanceTot =	scoresUnitaires(listeBus)

	res = (poidBus * nbBus) + (poidTemps * dureeTot) + (poidDistance * distanceTot) 
	return res