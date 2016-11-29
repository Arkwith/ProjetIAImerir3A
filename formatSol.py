from bus import *
from evaluation import *

def format(list_Bus,inter):
	f = open("output","w")
	text = "# Alex Pujolas, Matthieu Drouaire, Ahmed El Moden, Julien Pozzera, Bastien Philippe\n"
	if(inter):
		n,t,k = scoresUnitaires(list_Bus)
		text += str(n) + "," + str(t) + "," + str(k) + "\n"
		for b in list_Bus:
			text += "bus" + str(b.num) + "," + b.planning[0].tDepart
			for t in b.planning:
				if(t.ligne[0] == 'l'):
					text += "," + t.ligne + ":" + t.sens + ":v" + str(t.index)
			text += "\n"
	else:
		list_ligne =[]
		ligneMemo = 'l00000000'
		for b in list_Bus:
			if(b.planning[1].ligne != ligneMemo):
				ligneMemo = b.planning[1].ligne
				if(len(list_ligne) > 0):
					n,t,k = scoresUnitaires(list_ligne)
					text += str(n) + "," + str(t) + "," + str(k) + "\n"
					for bl in list_ligne:
						text += "bus" + str(bl.num) + "," + bl.planning[0].tDepart
						for t in bl.planning:
							if(t.ligne[0] == 'l'):
								text += "," + t.ligne + ":" + t.sens + ":v" + str(t.index)
						text += "\n"

				list_ligne =[]
			list_ligne.append(b)
		n,t,k = scoresUnitaires(list_ligne)
		text += str(n) + "," + str(t) + "," + str(k) + "\n"
		for bl in list_ligne:
			text += "bus" + str(bl.num) + "," + bl.planning[0].tDepart
			for t in bl.planning:
				if(t.ligne[0] == 'l'):
					text += "," + t.ligne + ":" + t.sens + ":v" + str(t.index)
			text += "\n"

		

	f.write(text)