from matriceDT import *
from generator import *
from formatSol import *
from parse import *





x,y = generate(True)
cpt = 0
for b in x:
	for t in b.planning:
		if(t.ligne[0] == 'l'):
			cpt += 1
print cpt
print y.lignes
format(x,True)
