from random import *
from parse import *
from bus import *
from formatSol import *


def bestBus(list_Bus_Disponible,trajet,num):
    seed(1)
    if(len(list_Bus_Disponible) == 1):
        return list_Bus_Disponible[0]

    for b in list_Bus_Disponible:
        if(b.planning[-1].tArrivee == trajet.tDepart) :
            return b

    distmin = 99999999999
    for b in list_Bus_Disponible:
        dist = MatriceDT().getDistance(b.planning[-1].tArrivee,trajet.tDepart)
        if( int(dist) < distmin):
            distmin = dist
            best = b
    p = float(dist)/35
    if(random() < p) :
        return Bus(num,trajet.hDepart,trajet.tDepart)
    else  :
        return best

def generate(interlignage):
    if(interlignage):
        return interligne_generate()
    else:
        return no_interligne_generate()


def interligne_generate():

    (list_Trajet,sol) = parse("horaires.csv")
    print len(list_Trajet)

    list_Bus = []

    initMat = MatriceDT()
    initMat.initD('dist_terminus.csv')

    cptt = 0
    for l in list_Trajet:
        list_Bus_Disponible = []
        for b in list_Bus:
            if( b.dispo(l.hDepart,l.tDepart)) : list_Bus_Disponible.append(b)

        dispo = len(list_Bus_Disponible)
        if( dispo == 0) :
            numBus = len(list_Bus) + 1
            nouveau_Bus = Bus(numBus,l.hDepart,l.tDepart)
            nouveau_Bus.addTrajet(l)
            sol.addToSolution(l,numBus)
            cptt += 1
            list_Bus.append(nouveau_Bus)
        else:
            best = bestBus(list_Bus_Disponible,l,len(list_Bus) + 1)
            best.addTrajet(l)
            cptt += 1
            sol.addToSolution(l,best.num)

    for b in list_Bus:
        b.retourDepot()
    print len(list_Bus)

    cpt = 0
    '''
    for b in list_Bus:
      cpt += len(b.planning)
      print b
      print " \n"

    print cpt
    print cptt
    print len(list_Bus)
    print sol.lignes
    '''
    return list_Bus,sol

def no_interligne_generate():
    (list_Trajet,sol) = parse("horaires.csv",False)

    print len(list_Trajet)

    list_Bus = []


    initMat = MatriceDT()
    initMat.initD('dist_terminus.csv')

    ligneMemo = "l0000"

    for l in list_Trajet:
        if(l.ligne != ligneMemo):
            ligneMemo = l.ligne
            list_Bus_ligne = []

        list_Bus_Disponible = []
        for b in list_Bus_ligne:
            if( b.dispo(l.hDepart,l.tDepart)) : list_Bus_Disponible.append(b)

        dispo = len(list_Bus_Disponible)
        if( dispo == 0) :
            nouveau_Bus = Bus(len(list_Bus) + 1,l.hDepart,l.tDepart)
            nouveau_Bus.addTrajet(l)
            sol.addToSolution(l,nouveau_Bus.num)
            list_Bus_ligne.append(nouveau_Bus)
            list_Bus.append(nouveau_Bus)
        else:
            best = bestBus(list_Bus_Disponible,l,len(list_Bus) + 1)
            sol.addToSolution(l,best.num)
            best.addTrajet(l)

    print len(list_Bus)

    cpt = 0
    '''
    for b in list_Bus:
      cpt += len(b.planning)
      print b
      print " \n"
    print cpt
    '''

    return list_Bus,sol

