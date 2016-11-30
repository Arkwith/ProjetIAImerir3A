from matriceDT import *
from generator import *
from formatSol import *
from parse import *
from busGenerator import *

initMat = MatriceDT()
initMat.initD('dist_terminus.csv')
x = busGenerate("horaires.csv")

format(x,True)



