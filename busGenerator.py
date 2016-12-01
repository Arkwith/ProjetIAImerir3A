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
	maxPoids = -1

	for t in list_Trajet:

		if(bus.dispo(t.hDepart,t.tDepart)):

			dist = MatriceDT().getDistance(lDep,t.tDepart)
			time = t.hDepart -lHorr
			pDist = 1/(1+float(dist)*float(dist)*float(dist))
			pTime = 100000.0/(1+(time.seconds/60)*(time.seconds/60)*(time.seconds/60))
			poids = pDist + pTime
			cptPoids += poids

		else:

			poids = 0

		if(poids > maxPoids) : 
			maxPoids = poids
			bt = t

		'''if(len(list_poids) < 10 ) :
			list_poids.append(poids)
		else :
			if(min(list_poids) < poids):
				list_poids[list_poids.index(min(list_poids))] = poids'''
		list_poids.append(poids)
		if(len(list_poids) > 1) : list_poids[-1] += list_poids[-2]

	'''list_cumul = []
	for p in list_poids :
		cptPoids += p
		list_cumul.append(p)
		if(len(list_cumul) > 1) :
			list_cumul[-1] += list_cumul[-2]'''

	if(random.random() > 0) :
		#print "no random"
		return ((cptPoids!=0),bt)
	
	#print "random"
	rnd =  cptPoids * random.random()
	#print list_poids
	#print rnd
	#print cptPoids
	maxPoids = -1

	for p in list_poids :
	
		if(p >= rnd):
			#print list_poids.index(p)
			#print "\n"
			return ((cptPoids !=0),list_Trajet[list_poids.index(p)])
	

def busGenerate(list_Trajet_input):
	
	list_Trajet = list(list_Trajet_input)

	list_Bus =[]

	while len(list_Trajet) > 0:

		nouveauBus = Bus(0,timedelta(minutes=600),'T2')
		nouveauBus.planning = []
		#print "BUS !!!!!!!!!!!!!!!!!!!!!"
		out = True
		while(out and (len(list_Trajet) > 0)):
			#print len(list_Trajet)
			out,t = bestTrajet(nouveauBus,list_Trajet)
			#print "here"
			#print out
			#print t
			if(len(nouveauBus.planning) == 0):
				nouveauBus = Bus(len(list_Bus)+1,t.hDepart,t.tDepart)
			if(out):
				nouveauBus.addTrajet(t)
				#print(list_Trajet.index(t))
				list_Trajet.pop(list_Trajet.index(t))
		list_Bus.append(nouveauBus)
		nouveauBus.retourDepot()


	return list_Bus