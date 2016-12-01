from random import *
from parse import *
from bus import *
from formatSol import *



def bestBus(list_Bus_Disponible,trajet):
    maxdist = 33
    '''
    if(len(list_Bus_Disponible) == 1):
        return list_Bus_Disponible[0]
    '''
    for b in list_Bus_Disponible:
        if(b.planning[-1].tArrivee == trajet.tDepart) :
            return b

    distmin = 99999999999
    for b in list_Bus_Disponible:
        dist = MatriceDT().getDistance(b.planning[-1].tArrivee,trajet.tDepart)
        if( float(dist) < distmin):
            distmin = dist
            best = b

    p = float(dist)*float(dist) / (33*33*2)
    if(random.random() < p) :
        return None
    else  :
        return best



def generate(filename,interlignage):
    if(interlignage):
        return interligne_generate(filename)
    else:
        return no_interligne_generate(filename)


def interligne_generate(filename):

    (list_Trajet,sol) = parse(filename, "all")
    # print len(list_Trajet)

    list_Bus = []

    initMat = MatriceDT()


    cptt = 0
    loop = 0
    #print len(list_Trajet)
    for l in list_Trajet:
        loop += 1
        # print  loop
        list_Bus_Disponible = []
        for b in list_Bus:
            if( b.dispo(l.hDepart,l.tDepart)) : list_Bus_Disponible.append(b)

        dispo = len(list_Bus_Disponible)
        if( dispo == 0) :
            numBus = len(list_Bus) + 1
            #if l.ligne == "l9" and l.sens == "a":
                #print "numBus: ", numBus, "-", l.index
            nouveau_Bus = Bus(numBus,l.hDepart,l.tDepart)
            nouveau_Bus.addTrajet(l)
            sol.addToSolution(l,numBus)
            cptt += 1
            list_Bus.append(nouveau_Bus)
        else:
            best = bestBus(list_Bus_Disponible,l)
            if not best:
                best = Bus(len(list_Bus) + 1,l.hDepart,l.tDepart)
                list_Bus.append(best)

            best.addTrajet(l)
            cptt += 1
            sol.addToSolution(l,best.num)
            #if l.ligne == "l9" and l.sens == "a":
                #print "best.num: ", best.num, "-", l.index


    for b in list_Bus:
        b.retourDepot()
    # print len(list_Bus)

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
    sol.listeBus = list_Bus
    return sol

def no_interligne_generate(filename):
    (list_Trajet,sol) = parse(filename, "byline")

    # print len(list_Trajet)

    list_Bus = []


    initMat = MatriceDT()


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
            best = bestBus(list_Bus_Disponible,l)
            if not best:
                best = Bus(len(list_Bus) + 1,l.hDepart,l.tDepart)
                list_Bus.append(best)
                list_Bus_ligne.append(best)
            best.addTrajet(l)
            sol.addToSolution(l,best.num)

    # print len(list_Bus)

    cpt = 0
    '''
    for b in list_Bus:
      cpt += len(b.planning)
      print b
      print " \n"
    print cpt
    '''
    sol.listeBus = list_Bus

    return sol

