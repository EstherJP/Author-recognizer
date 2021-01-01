from basicFunctions import *
from textCharacterization import * 
# from searchAuthor import * 

import sys
import numpy as np 
import json
import math
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

# ((resultado anterior * total anterior de tokens) + (resultado nuevo * total nuevo de tokens)) / total absoluto de tokens
# Resultado anterior total por total tokens + resultado nuevo por sus tokens 
# todo esto entre el total
def calculateNewResult(author, charac, numTokens):
  oldResult = author.get(charac) * author['NumeroTokens'].get(numTokens)
  newResult = data.get(charac) * data['NumeroTokens'].get(numTokens)
  totalTokens = author['NumeroTokens'].get(numTokens) + data['NumeroTokens'].get(numTokens)
  newResult = (oldResult + newResult) / totalTokens
  return newResult;

# El usuario introduce un libro en formato epub y el nombre del autor sin espacios
pathBook = sys.argv[1]
authorBook = sys.argv[2]
print(pathBook, authorBook)

bookText = getTextFromChaps(epub2text(pathBook))

# Caracterizamos el texto como en el json
data = {}
distribution = lengthFreqDis(bookText)
auxSentenceLength = sentenceLength(bookText)
fiftyWords = fiftyMostUsedWords(bookText)
auxRareWords = rareWords(bookText)

data['ProporcionLongitudPalabras'] = distribution[0]
frequencies = punctuationFreq(bookText)
data['frecuenciaComas'] = frequencies[0]
data['frecuenciaPuntos'] = frequencies[1]
data['longitudSentenciaMedia'] = auxSentenceLength[0]
data['cincuentaPalabrasFrecuentes'] = fiftyWords[0]
data['palabrasRaras'] = auxRareWords[0]

auxTokens = {}
auxTokens["NumLongitudPalabras"] = distribution[1]
auxTokens["NumFrecuenciaPuntos"] = frequencies[2]
auxTokens["NumLongitudSentenciaMedia"] = auxSentenceLength[1]
auxTokens["NumCincuentaPalabras"] = fiftyWords[1]
auxTokens["NumPalabrasRaras"] = auxRareWords[1]
data["NumeroTokens"] = auxTokens

# Comprobamos si el usuario existe en nuestra base de datos recorriendo los nombres
# de nuestras carpetas o recorriendo los nombre en el json 

with open('authors.json') as json_file:
  authorsCharacs = json.load(json_file)

authorExists = False;
for author in authorsCharacs:
  # Si no existe -> hacemos un append al author.json con ese autor
  if author['Nombre'].lower().count(authorBook.lower()) != 0:
    # data['Nombre'] = author['Nombre']
    # Longitud de palabra
    author['ProporcionLongitudPalabras'] = calculateNewResult(author, "ProporcionLongitudPalabras", "NumLongitudPalabras")
    # Frecuencia comas
    author['frecuenciaComas'] = calculateNewResult(author, "frecuenciaComas", "NumFrecuenciaPuntos")
    # Frecuencia puntos
    author['frecuenciaPuntos'] = calculateNewResult(author, "frecuenciaPuntos", "NumFrecuenciaPuntos")
    # Longitud media de frase
    author['longitudSentenciaMedia'] = calculateNewResult(author, "longitudSentenciaMedia", "NumCincuentaPalabras")
    # Longitud media de frase
    author['palabrasRaras'] = calculateNewResult(author, "palabrasRaras", "NumPalabrasRaras")

    # Cincuenta palabras ordenar
    



    authorExists = True;
    break

aux = authorsCharacs
# Si existe -> buscar autor en el json y equilibrar la estadistica de caracterizacion
if authorExists == False:
  # hacemos un append
  aux.append(data)


# print(json.dumps(aux, indent=2, sort_keys=True))



  


