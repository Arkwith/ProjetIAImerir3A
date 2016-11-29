# util.py

def croisementRandom(solution1, solution2):
    sens = ""
    seg = solution1.indexLignes[randint(0,len(solution1.indexLignes)-1)]
    print("modif : ", seg)

    tampon = solution1.lignes[seg]
    solution2.lignes[seg] = solution1.lignes[seg]
    solution1.lignes[seg] = solution2.lignes[seg]
    
    return (solution1, solution2)
