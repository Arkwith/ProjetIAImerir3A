from generator import *
from random import randint
from utils import *

(listBus, sol) = generate(True)
# format(listBus, True)
(listTrajet, s) = parse("horaires.csv", False, False)

def bidouilleSolution(sol, listBus):
    r = randint(1, 15)
    while r == 8:
        r = randint(1, 15)

    rSens = randint(0, 1)
    if rSens == 0:
        sens = "a"
    else:
        sens = "r"

    currentLigneBus = sol.lignes[str(r) + ":" + str(sens)]
    newRandomBus = randint(1, len(listBus))
    while newRandomBus == currentLigneBus:
        newRandomBus = randint(1, len(listBus))

    sol.lignes[str(r) + ":" + str(sens)] = newRandomBus

    return sol

# On bidouille la solution 3 fois
# for i in range(0, 3):
#     sol = bidouilleSolution(sol, listBus)

(errorArray, etatBus) = verifSolution(sol, listTrajet, listBus)
print len(errorArray), " -- ", etatBus

# print sol.lignes["15:a"]
# print sol.lignes["15:r"]
# (y,x) = getIndexLignes(536, sol.sizeLignes)
# print y, x, sol.lignes[y][x]
# (y,x) = getIndexLignes(15, sol.sizeLignes)
# print y, x, sol.lignes[y][x]
# (y,x) = getIndexLignes(44, sol.sizeLignes)
# print y
# print sol.lignes[y]
# print y, x, sol.lignes[y][x]

# print sol.lignes
# print sol.lignes["1:r"]
