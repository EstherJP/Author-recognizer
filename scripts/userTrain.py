from basicFunctions import *
from textCharacterization import * 
# from searchAuthor import * 

import sys
import numpy as np 
import json
import math
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

# El usuario introduce un libro en formato epub y el nombre del autor sin espacios
pathBook = sys.argv[1]
authorBook = sys.argv[2]
print(pathBook, authorBook)

bookText = getTextFromChaps(epub2text(pathBook))

# Caracterizamos el texto como en el json
data = {}
data['ProporcionLongitudPalabras'] = lengthFreqDis(bookText)
frequencies = punctuationFreq(bookText)
data['frecuenciaComas'] = frequencies[0]
data['frecuenciaPuntos'] = frequencies[1]
data['longitudSentenciaMedia'] = sentenceLength(bookText)
data['cincuentaPalabrasFrecuentes'] = fiftyMostUsedWords(bookText)
data['palabrasRaras'] = rareWords(bookText)

# Comprobamos si el usuario existe en nuestra base de datos recorriendo los nombres
# de nuestras carpetas o recorriendo los nombre en el json 

with open('authors.json') as json_file:
  authorsCharacs = json.load(json_file)

authorExists = False;
for author in authorsCharacs:
  # Si no existe -> hacemos un append al author.json con ese autor
  # if author['Nombre'] == authorBook:
  if author['Nombre'].lower().count(authorBook.lower()) != 0:
    data['Nombre'] = author['Nombre']
    print("Codigo equilibrar la estadistica")
    authorExists = True;
    break

aux = authorsCharacs
# Si existe -> buscar autor en el json y equilibrar la estadistica de caracterizacion
if authorExists == False:
  # hacemos un append
  aux.append(data)

# print(json.dumps(aux, indent=2, sort_keys=True))



  


