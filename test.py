from matriceDT import *
from generator import *
from formatSol import *
from parse import *
from utils import *


a = timedelta(minutes=0.15)
print a



initMat = MatriceDT()
'''
initMat.initRATP('matrice_dist_terminus_ratp.csv')
x,y = generate("horaires_ratp.csv",True)

initMat.initD('dist_terminus.csv')
x,y = generate("horaires.csv",True)
'''
initMat.initRATP('matrice_dist_terminus_ratp.csv')
(listBus,sol) = generate("horaires_ratp.csv",True)
(listTrajet, s) = parse("horaires_ratp.csv", "none")
(errorArray, etatBus) = verifSolution(sol, listTrajet, listBus)
print len(errorArray), " -- ", etatBus
cpt = 0
# for b in x:
# 	for t in b.planning:
# 		if(t.ligne[0] == 'l'):
# 			cpt += 1
# print cpt
# print y.lignes
# format(x,True)
