from error import *
from datetime import timedelta
from random import randint

def croisementRandom(solution1, solution2):
    sens = ""
    seg = solution1.indexLignes[randint(0,len(solution1.indexLignes)-1)]
    # print("modif : ", seg)

    tampon = solution1.lignes[seg]
    solution2.lignes[seg] = solution1.lignes[seg]
    solution1.lignes[seg] = solution2.lignes[seg]

    return (solution1, solution2)

def verifSolution(solution, listTrajets,  listBus):
    # print solution.lignes
    # print len(listBus)
    # for b in listBus:
    #     print b.num
    t5 = timedelta(days=0, seconds=300) # 5 mins
    errorArray = []
    etatBus = {}
    for b in listBus:
        etatBus[b.num] = 0

    for i in range(0, len(listTrajets)):
        (y, x) = getIndexLignes(i, solution)
        trajetReference = listTrajets[i]
        busReference = solution.lignes[y][x]

        etatBus[busReference] += 1
        j = i + 1
        while j < len(listTrajets):
            (y2, x2)  = getIndexLignes(j, solution)
            # print(y2, x2)
            # print solution.sizeLignes
            # print solution.lignes
            # print solution.lignesNum
            bus = solution.lignes[y2][x2]
            trajet = listTrajets[j]
            if bus == busReference:
                if trajetReference.hDepart < trajet.hDepart:
                    if ((trajet.hDepart > trajetReference.hArrivee) and (trajet.hDepart - trajetReference.hArrivee) < t5) or (trajet.hDepart < trajetReference.hArrivee):
                        # print "i: ", i, " j: ", j
                        # print "TrajetReference: ", trajetReference.ligne, ":", trajetReference.sens, trajetReference.index, "-", "Trajet: ",trajet.ligne,":", trajet.sens, trajet.index
                        # print "Arrivee a: ", trajetReference.hArrivee," Prochain Depart: ", trajet.hDepart,  "-", trajet.hDepart - trajetReference.hArrivee
                        # print bus
                        # print solution.lignes
                        # # print solution.lignes[trajetReference.ligne[1:]+ ":"+ trajetReference.sens]
                        # # print solution.lignes[trajet.ligne[1:]+ ":"+ trajet.sens]
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
            x = i - id - 1
            # print "yx : ", y, "-", x
            break
        # print "AFTER ID : ", id, " IndexListTrajet: ", i, " TailleLigne: ", sizeLignes[j]
        z += 1
    return (y, x)
