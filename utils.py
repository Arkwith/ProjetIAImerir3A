from error import *
from datetime import timedelta
from random import randint

def croisementRandom(solution1, solution2):
    sens = ""
    seg = solution1.indexLignes[randint(0,len(solution1.indexLignes)-1)]
    # print("modif : ", seg)

    while solution1.lignes[seg] == solution2.lignes[seg]:
        seg = solution1.indexLignes[randint(0,len(solution1.indexLignes)-1)]

    tampon = solution1.lignes[seg]
    solution1.lignes[seg] = solution2.lignes[seg]
    solution2.lignes[seg] = tampon


    
    return (solution1, solution2, seg)

def swapTrajet(solution1, solution2, seg):
    print "swapping en cours"
    copieSeg1 = solution1.lignes[seg]
    copieSeg2 = solution2.lignes[seg]

    tamponT1 = None
    positionT1 = None
    positionJ = None

    for i in range(len(copieSeg1)):
        if copieSeg1[i] != copieSeg2[i]:
            print seg
            print len(solution1.lignes[seg])
            print solution1.lignes[seg]
            print solution2.lignes[seg]
            numBus1 = copieSeg1[i]
            numBus2 = copieSeg2[i]

            for j in range(len(solution1.listeBus)):
                bus = solution1.listeBus[j]
                if numBus1 == bus.num:
            #        print bus.planning
                    for t in bus.planning:
                        if isinstance(t.index, int):
                            print "{}, {}-{}-{}-{}".format(i, t.hDepart, t.hArrivee, t.ligne, t.index)
                    for t in range(len(bus.planning)):
            #            print "index: ", bus.planning[t].index
                        trajet = bus.planning[t]
                        #if isinstance(trajet.index, int):
                            #print "ICI: ", trajet.index, "-", i
                        if trajet.index == i+1:
                            tamponT1 = trajet
                            positionT1 = t
                            positionJ = j
            #                print t, "-", j
                            break


            for j in range(len(solution2.listeBus)):
                bus = solution2.listeBus[j]
                if numBus1 == bus.num:
                    for t in range(len(bus.planning)):
                        if bus.planning[t].index == i+1:
                            print(positionJ, positionT1, t)
                            solution1.listeBus[positionJ].planning[positionT1] = bus.planning[t] # On met le trajet de sol2 dans sol1
                            bus.planning[t] = tamponT1
                            break
    return (solution1, solution2)

def verifSolution(solution, listTrajets):
    listBus = solution.listeBus
    t5 = timedelta(days=0, seconds=300) # 5 mins
    errorArray = []
    etatBus = {}
    for b in listBus:
        etatBus[b.num] = 0

    #print solution.lignes
    for i in range(0, len(listTrajets)):
        (y, x) = getIndexLignes(i, solution)
        trajetReference = listTrajets[i]
        busReference = solution.lignes[y][x]

        if busReference in etatBus:
            etatBus[busReference] += 1
        j = i + 1
        while j < len(listTrajets):
            (y2, x2)  = getIndexLignes(j, solution)
            bus = solution.lignes[y2][x2]
            trajet = listTrajets[j]

            if bus == busReference:
                if trajetReference.hDepart < trajet.hDepart:
                    if ((trajet.hDepart > trajetReference.hArrivee) and (trajet.hDepart - trajetReference.hArrivee) < t5) or (trajet.hDepart < trajetReference.hArrivee):
                        # print "i: ", i, " j: ", j
                        #print "TrajetReference: ", trajetReference.ligne, ":", trajetReference.sens, trajetReference.index, "-", "Trajet: ",trajet.ligne,":", trajet.sens, trajet.index
                        #print "Arrivee a: ", trajetReference.hArrivee," Prochain Depart: ", trajet.hDepart,  "-", trajet.hDepart - trajetReference.hArrivee
                        # print bus
                        # print solution.lignes
                        # print solution.lignes[trajetReference.ligne[1:]+ ":"+ trajetReference.sens]
                        # print solution.lignes[trajet.ligne[1:]+ ":"+ trajet.sens]
                        # print solution.sizeLignes
                        error = Error(trajetReference, busReference, i, bus, trajet, j)
                        errorArray.append(error)
                elif trajetReference.hDepart > trajet.hDepart:
                    # print "b"
                    if ((trajet.hArrivee < trajetReference.hDepart) and (trajetReference.hDepart - trajet.hArrivee) < t5) or (trajetReference.hDepart < trajet.hArrivee):
                        error = Error(trajetReference, busReference, i, bus, trajet, j)
                        errorArray.append(error)
                else:
                    # print "c"
                    error = Error(trajetReference, busReference, i, bus, trajet, j)
                    errorArray.append(error)
            j += 1

    return (errorArray, etatBus)


def getIndexLignes(i, solution):
    sizeLignes = solution.sizeLignes
    id = 0
    y = None
    x = 0
    z = 0
    for j in range(0, len(sizeLignes)):
        # print "BEFORE ID : ", id, " IndexListTrajet: ", i, " TailleLigne: ", sizeLignes[j]
        # print "id+sizeLignes[j]:", id+sizeLignes[j]
        if id+sizeLignes[j] <= i :
            id += sizeLignes[j]
            # print "here ", id
            # print "IDi : ", id, " ", sizeLignes[j]
        else:
            # print "aaaa"
            sens = "a" if (j % 2) == 0 else "r"
            y = solution.lignesNum[z] + ":" +  sens
            x = i - id
            # print "yx : ", y, "-", x
            break
        # print "AFTER ID : ", id, " IndexListTrajet: ", i, " TailleLigne: ", sizeLignes[j]
        z += 1
    return (y, x)
