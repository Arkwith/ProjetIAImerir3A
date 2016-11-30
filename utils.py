from error import *
from datetime import timedelta


def verifSolution(solution, listTrajets,  listBus):
    print solution.lignes
    print len(listBus)
    for b in listBus:
        print b.num
    t5 = timedelta(days=0, seconds=300) # 5 mins
    errorArray = []
    etatBus = {}
    for b in listBus:
        etatBus[b.num] = 0

    for i in range(0, len(listTrajets)):
        (y, x) = getIndexLignes(i, solution.sizeLignes)
        trajetReference = listTrajets[i]
        busReference = solution.lignes[y][x]

        etatBus[busReference] += 1
        j = i + 1
        while j < len(listTrajets):
            (y2, x2)  = getIndexLignes(j, solution.sizeLignes)
            print "j, Y2, X2: ", j, " ",  y2, " ", x2
            bus = solution.lignes[y2][x2]
            trajet = listTrajets[j]
            print "Trajet: ", trajet.ligne, ":", trajet.sens, " ", trajet.index
            if bus == busReference:
                # print "match"
                # print bus, "-", busReference
                if trajetReference.hDepart < trajet.hDepart:
                    # print "a"
                    if ((trajet.hDepart > trajetReference.hArrivee) and (trajet.hDepart - trajetReference.hArrivee) < t5) or (trajet.hDepart < trajetReference.hArrivee):
                        print "i: ", i, " j: ", j
                        print "TrajetReference: ", trajetReference.ligne, ":", trajetReference.sens, trajetReference.index, "-", "Trajet: ",trajet.ligne,":", trajet.sens, trajet.index
                        print "Arrivee a: ", trajetReference.hArrivee," Prochain Depart: ", trajet.hDepart,  "-", trajet.hDepart - trajetReference.hArrivee
                        print bus
                        print solution.lignes[trajetReference.ligne[1:]+ ":"+ trajetReference.sens]
                        print solution.lignes[trajet.ligne[1:]+ ":"+ trajet.sens]
                        print solution.sizeLignes
                        error = Error(trajetReference, busReference, i, bus, trajet, j)
                        errorArray.append(error)
                elif trajetReference.hDepart > trajet.hDepart:
                    print "b"
                    if ((trajet.hArrivee < trajetReference.hDepart) and (trajetReference.hDepart - trajet.hArrivee) < t5) or (trajetReference.hDepart < trajet.hArrivee):
                        # print "LigneReference: ", trajetReference.ligne, ":", trajetReference.sens, trajetReference.index, "-", "Trajet: ",trajet.ligne,":", trajet.sens, trajet.index
                        # print "Arrivee a: ", trajetReference.hArrivee," Prochain Depart: ", trajet.hDepart,  "-", trajet.hDepart - trajetReference.hArrivee
                        # print bus
                        # print solution.lignes[trajetReference.ligne[1:]+ ":"+ trajetReference.sens]
                        # print solution.lignes[trajet.ligne[1:]+ ":"+ trajet.sens]
                        # print solution.sizeLignes
                        error = Error(trajetReference, busReference, i, bus, trajet, j)
                        errorArray.append(error)
                else:
                    print "c"
                    error = Error(trajetReference, busReference, i, bus, trajet, j)
                    errorArray.append(error)
            j += 1

    return (errorArray, etatBus)


def getIndexLignes(i, sizeLignes):
    id = 0
    y = None
    x = 0
    z = 0
    for j in range(0, len(sizeLignes)):
        if j % 2 == 0:
            z += 1
        # print "BEFORE ID : ", id, " IndexListTrajet: ", i, " TailleLigne: ", sizeLignes[j]
        # print "id+sizeLignes[j]:", id+sizeLignes[j]
        if id+sizeLignes[j] <= i :
            id += sizeLignes[j]
            # print "here ", id
            # print "IDi : ", id, " ", sizeLignes[j]
        else:
            # print "aaaa"
            if z>=8:
                z+=1
            sens = "a" if (j % 2) == 0 else "r"
            y = str(z) + ":" +  sens
            x = i - id
            # print "yx : ", y, "-", x
            break
        # print "AFTER ID : ", id, " IndexListTrajet: ", i, " TailleLigne: ", sizeLignes[j]
    return (y, x)
