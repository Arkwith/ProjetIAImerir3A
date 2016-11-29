from solution import *

def scoresUnitaires(listeBus):
	dureeTot = timeDelta(seconds=0)
	distanceTot = 0
	nbBus = listeBus.length()

	for bus in listeBus:
		for trajet in bus.planning:
			dureeTot += trajet.duree
			distanceTot += trajet.dist

	return (nbBus,dureeTot,distanceTot)

def scoreSolution(listeBus):
	poidBus = 50 			# Un bus coute 220.000€
	poidTemps = 10
	poidDistance = 10

	nbBus,dureeTot,distanceTot =	scoresUnitaires(listeBus)

	res = (poidBus * nbBus) + (poidTemps * dureeTot) + (poidDistance * distanceTot) 
	return res