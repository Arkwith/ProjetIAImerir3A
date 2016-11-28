from random import random
from parse import *
from bus import *


list_Trajet = parse("horaires.csv")

print len(list_Trajet)

list_Bus = []

initMat = MatriceDT()
initMat.initD('dist_terminus.csv')

for l in list_Trajet:
    list_Bus_Disponible = []
    for b in list_Bus:
        if( b.dispo(l.hDepart,l.tDepart)) : list_Bus_Disponible.append(b)

    dispo = len(list_Bus_Disponible)
    if( dispo == 0) :
        nouveau_Bus = Bus(len(list_Bus) + 1,l.hDepart,l.tDepart)
        nouveau_Bus.addTrajet(l)
        list_Bus.append(nouveau_Bus)
    else:
        index = int(dispo * random()) + 1  # un nombre alea entre 0 et le nb de bus dispo
        if( index == dispo) :
            nouveau_Bus = Bus(len(list_Bus) + 1,l.hDepart,l.tDepart)
            nouveau_Bus.addTrajet(l)
            list_Bus.append(nouveau_Bus)
        else :
            list_Bus_Disponible[index].addTrajet(l)

print len(list_Bus)

cpt = 0

for b in list_Bus:
  cpt += len(b.planning)
  print b
  print " \n"
print cpt

