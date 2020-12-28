from basicFunctions import *
from textCharacterization import * 
import sys
import numpy as np 


# Introducimos texto (ya sea a mano o en formato epub)
print sys.argv[1]
# Caracterizamos dicho texto
textFromBook = getTextFromChaps(epub2text(sys.argv[1]))
# Leemos nuestro fichero JSON con las caracteriscas de los autores de nuestra bbdd
currentText = {}
currentText["cincuentaPalabrasFrecuentes"] = fiftyMostUsedWords(textFromBook)

# Igualamos el autor mejor candidato al primero que aparezca en el JSON
frequencies = punctuationFreq(textFromBook)
auxVector = [lengthFreqDis(textFromBook), frequencies[0], frequencies[1], sentenceLength(textFromBook)]
textVector = np.array(auxVector)

# A medida que leemos el fichero vamos actualizando el autor mejor candidato 

# Devolvemos el autor final