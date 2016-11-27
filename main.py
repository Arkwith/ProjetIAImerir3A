from random import random


list_Trajet = Parse("chemin")
list_Bus = []

for l in list_Trajet:
    list_Bus_Disponible = []
    for b in list_Bus:
        if( b.dispo(l.Hdep,lTdep)) : list_Bus_Disponible.append(b)

    dispo = len(list_Bus_Disponible)
    if( dispo == 0) :
        nouveau_Bus = new Bus(l.Hdep,l.Tdep)
        nouveau_Bus.Planning.append(l)
        list_Bus.append(nouveau_Bus)
    else:
        index = int(dispo * random()) + 1  # un nombre aléa entre 0 et le nb de bus dispo
        if( index =  dispo) :
            nouveau_Bus = new Bus(l.Hdep,l.Tdep)
            nouveau_Bus.Planning.append(l)
            list_Bus.append(nouveau_Bus)
        else :
            list_Bus_Disponible[index].Planning.append(l)


            4 5 7 8 9 2 4 1 3
            2 1 5 7 9 3 1 4 1


          T0 T1 T2 T3 T4
      v1  
      v2
      v3
      v4
      v5
      v6 
