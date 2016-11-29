from bus import *

def format(list_Bus):
	#f = open("output","w")
	text = "# Alex Pujolas, Matthieu Drouaire, Ahmed El Moden, Julien Pozzera, Bastien Philippe\n"
	text += "n,t,k\n"
	for b in list_Bus:
		text += "bus" + str(b.num)
		for t in b.planning:
			text += " ," + t.ligne + ":" + t.sens + ":v" + str(t.index)
		text += "\n"
	print text