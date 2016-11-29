from matriceDT import *
from generator import *
from formatSol import *
from parse import *


li,so = parse("horaires.csv",True)
print len(li)

'''
x,y = generate(False)
cpt = 0
for b in x:
	for t in b.planning:
		if(t.ligne[0] == 'l'):
			cpt += 1
print cpt
print y.lignes
format(x,False)
'''