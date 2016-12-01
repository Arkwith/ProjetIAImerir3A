from matriceDT import *
from generator import *
from formatSol import *
from parse import *
from busGenerator import *



POPULATION = 25
ITER = 25
MODIFICATION = 0.60


initMat = MatriceDT()
initMat.initD('dist_terminus.csv')
(list_Trajet,sol) = parse("horaires.csv", "all")
good_bus= []
score = 9999999999999
scgb = 9999999999999
for j in range(ITER):
	for i in range(POPULATION):
		if(len(good_bus) > 0):
			nb_mod_bus = int(len(x)*MODIFICATION)
			good_bus = random.sample(gb,nb_mod_bus)
			list_Trajet = []
			for b in gb :
				if(b not in good_bus) :
					for t in b.planning:
						if(t.ligne[0] == 'l'):
							list_Trajet.append(t)

		x = busGenerate(list_Trajet)
		tmpScore = scoreSolution(x)
		if(tmpScore < score) :
			score = tmpScore
			lb = x 
	print j
	

	lb += good_bus

	if( scoreSolution(lb) < scgb) :
		gb = lb
		scgb = scoreSolution(lb)

	print len(gb)
	
	
	#print good_bus
	
	#print len(list_Trajet)
	print "\n"

cpt = 0
cpbus = 0
for b in gb :
	cpbus += 1
	b.num = cpbus
	print b
	for t in b.planning :
		if(t.ligne[0] == 'l'):
			cpt += 1
print cpt
print len(gb)
print scoreSolution(gb)
format(gb,True)
