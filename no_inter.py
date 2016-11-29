import random
from parse import *
from bus import *


def bestBus(list_Bus_Disponible,trajet):
    if(len(list_Bus_Disponible) == 1):
        return list_Bus_Disponible[0]

    for b in list_Bus_Disponible:
        if(b.planning[-1].tArrivee == trajet.tDepart) :
            return b

    distmin = 99999999999
    for b in list_Bus_Disponible:
        dist = MatriceDT().getDistance(b.planning[-1].tArrivee,trajet.tDepart)
        if( dist < distmin):
            distmin = dist
            best = b
    return best





list_Trajet = parse("horaires.csv")

print len(list_Trajet)

list_Bus = []


initMat = MatriceDT()
initMat.initD('dist_terminus.csv')

ligneMemo = "l0000"

for l in list_Trajet:
    if(l.ligne != ligneMemo):
        ligneMemo = l.ligne
        list_Bus_ligne = []
    else : 
        list_Bus_Disponible = []
        for b in list_Bus_ligne:
            if( b.dispo(l.hDepart,l.tDepart)) : list_Bus_Disponible.append(b)

        dispo = len(list_Bus_Disponible)
        if( dispo == 0) :
            nouveau_Bus = Bus(len(list_Bus) + 1,l.hDepart,l.tDepart)
            nouveau_Bus.addTrajet(l)
            list_Bus_ligne.append(nouveau_Bus)
            list_Bus.append(nouveau_Bus)
        else:
            bestBus(list_Bus_Disponible,l).addTrajet(l)

print len(list_Bus)

cpt = 0

for b in list_Bus:
  cpt += len(b.planning)
  print b
  print " \n"
print cpt

