from matriceDT import *
from generator import *
from formatSol import *
from parse import *


a = timedelta(minutes=0.15)
print a



initMat = MatriceDT()
initMat.initD('dist_terminus.csv')
x,y = generate("horaires.csv",True)
cpt = 0
for b in x:
	for t in b.planning:
		if(t.ligne[0] == 'l'):
			cpt += 1
print cpt
print y.lignes
format(x,True)
