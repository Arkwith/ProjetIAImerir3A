from matriceDT import *
from generator import *


x,y = generate(True)

print y.lignes


x,y = generate(False)

print y.lignes
cpt = 0
for k in y.lignes:
	print k +"\t"+ str(len(y.lignes[k]))
	cpt += len(y.lignes[k])
print cpt
cpt = 0
for b in x:
	for t in b.planning:
		if(t.ligne[0] == 'l') : cpt += 1
print cpt