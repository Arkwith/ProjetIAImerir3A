from generator import *
from random import randint
from utils import *
from evaluation import *

initMat = MatriceDT()
initMat.initD('dist_terminus.csv')
(listTrajet, s) = parse("horaires.csv", "none")
print len(listTrajet)
'''for t in listTrajet:
    print "{}-{}-{}-{}".format(t.hDepart, t.hArrivee, t.ligne, t.index)

sol1 = generate("horaires.csv", True)
print sol1.lignes
#(s1, s2, seg) = croisementRandom(sol1, sol2)
(errorArray1, etatBus1) = verifSolution(sol1, listTrajet)
print len(errorArray1)

pass'''

for i in range(0, 10):
    sol1 = generate("horaires.csv", True)
    sol2 = generate("horaires.csv", True)
    print sol1.lignes
    print ""
    print sol1.listeBus

    print "------------------------"

    print sol2.lignes
    print ""
    print sol2.listeBus
    print ""
    (s1, s2, seg) = croisementRandom(sol1, sol2)
    (errorArray1, etatBus1) = verifSolution(sol1, listTrajet)
    (errorArray2, etatBus2) = verifSolution(s2, listTrajet)
    #print len(errorArray1)
    #print len(errorArray2)
    if len(errorArray1) == 0:
        
        (s1, s2) = swapTrajet(s1, s2, seg)
        '''print "After swap"
        print s1.lignes[seg]
        print s2.lignes[seg]
        print ""'''
    if len(errorArray2) == 0:
        
        (s1, s2) = swapTrajet(s1, s2, seg)
        '''print "After swap"
        print s1.lignes[seg]
        print s2.lignes[seg]
        print ""'''


def bidouilleSolution(sol, listBus):
    print sol.lignesNum
    lignesNumIndex = randint(0, len(sol.lignesNum)-1)
    ligne = sol.lignesNum[lignesNumIndex]
    print ligne
    busIndex = randint(0, sol.sizeLignes[int(ligne)]-1)

    rSens = randint(0, 1)
    if rSens == 0:
        sens = "a"
    else:
        sens = "r"
    print "rd: ", sol.sizeLignes[int(ligne)]-1
    print str(ligne), ":", str(sens), "-", busIndex
    print sol.sizeLignes
    currentLigneBus = sol.lignes[str(ligne) + ":" + str(sens)][busIndex]
    newRandomBus = randint(1, len(listBus))
    while newRandomBus == currentLigneBus:
        newRandomBus = randint(1, len(listBus))

    sol.lignes[str(ligne) + ":" + str(sens)][busIndex] = newRandomBus

    return sol

# On bidouille la solution 3 fois
# for i in range(0, 3):
#     sol = bidouilleSolution(sol, listBus)
# sol.lignes["4:a"][0] = 10

# (errorArray, etatBus) = verifSolution(sol, listTrajet, listBus)
# print len(errorArray), " -- ", etatBus

# print sol.lignes["15:a"]
# print sol.lignes["15:r"]
# (y,x) = getIndexLignes(15, sol.sizeLignes)
# print y, x, sol.lignes[y][x]
# (y,x) = getIndexLignes(44, sol.sizeLignes)
# print y
# print sol.lignes[y]
# print y, x, sol.lignes[y][x]

# print sol.lignes
# print sol.lignes["1:r"]
