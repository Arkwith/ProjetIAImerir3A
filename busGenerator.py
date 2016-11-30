from random import *
from parse import *
from bus import *
from formatSol import *

def bestTrajet(bus,list_Trajet):
	if(len(bus.planning)==0):
		lDep = 'T0'
		lHorr = timedelta()
		#print "new bus baby"
	else:
		last_Trajet = bus.planning[-1]
		lDep = last_Trajet.tArrivee
		lHorr = last_Trajet.hArrivee

	list_poids = []
	cptPoids = 0

	for t in list_Trajet:

		if(bus.dispo(t.hDepart,t.tDepart)):

			dist = MatriceDT().getDistance(lDep,t.tDepart)
			time = t.hDepart - lHorr
			poids = 100/(1+float(dist)*4) + (100/(1+(time.seconds/60)))
			poids = poids*poids*poids*poids*poids
			cptPoids += poids

		else:
			poids = 0

		list_poids.append(poids)
		if(len(list_poids) > 1) : list_poids[-1] += list_poids[-2]

	rnd =  cptPoids * random.random()
	#print list_poids
	#print rnd
	#print cptPoids
	for p in list_poids :
		if(p >= rnd):
			#print list_poids.index(p)
			#print "\n"
			return ((cptPoids !=0),list_Trajet[list_poids.index(p)])

def busGenerate(filename):
	(list_Trajet,sol) = parse(filename, "all")

	list_Bus =[]

	while len(list_Trajet) > 0:

		nouveauBus = Bus(0,timedelta(minutes=600),'T2')
		nouveauBus.planning = []
		print "BUS !!!!!!!!!!!!!!!!!!!!!"
		out = True
		while(out and (len(list_Trajet) > 0)):
			#print len(list_Trajet)
			out,t = bestTrajet(nouveauBus,list_Trajet)
			#print "here"
			#print out
			print t
			if(len(nouveauBus.planning) == 0):
				nouveauBus = Bus(len(list_Bus)+1,t.hDepart,t.tDepart)
			if(out):
				nouveauBus.addTrajet(t)
				#print(list_Trajet.index(t))
				list_Trajet.pop(list_Trajet.index(t))
		list_Bus.append(nouveauBus)
	return list_Bus