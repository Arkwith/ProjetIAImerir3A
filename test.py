from matriceDT import *
from generator import *
from formatSol import *
from parse import *




initMat = MatriceDT()
'''
initMat.initRATP('matrice_dist_terminus_ratp.csv')
x,y = generate("horaires_ratp.csv",True)

initMat.initD('dist_terminus.csv')
x,y = generate("horaires.csv",True)
'''


'''
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
'''
initMat.initD('dist_terminus.csv')
score = 999999999999999
res = None
for i in range(1):
	x,y = generate("horaires.csv",True)
	if(scoreSolution(x) < score):
		score = scoreSolution(x)
		res = x,y

print y.lignes
print(score)
print len(x)
format(x,True)