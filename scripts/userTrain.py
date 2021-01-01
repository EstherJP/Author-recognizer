from basicFunctions import *
from textCharacterization import * 
# from searchAuthor import * 
import os
import sys
import numpy as np 
import json
import math
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

def calculateNewResult(author, charac, numTokens):
  oldResult = author.get(charac) * author['NumeroTokens'].get(numTokens)
  newResult = data.get(charac) * data['NumeroTokens'].get(numTokens)
  totalTokens = author['NumeroTokens'].get(numTokens) + data['NumeroTokens'].get(numTokens)
  newResult = (oldResult + newResult) / totalTokens
  return newResult;

def takeSecond(elem):
  return elem[1]

def topFiftyWordsMoreUsed(authorWords, dataWords):
  newFiftyWords = []
  # Actualizamos los contadores
  for i in range(50):
    for authorWord in authorWords:
      if dataWords[i][0] == authorWord[0]:
        # print('palabra', dataWords[i][0], 'author', authorWord[0])
        authorWord[1] += dataWords[i][1]
  # Reordenamos el conjunto
  authorWords.sort(key=takeSecond, reverse=True)
  return authorWords

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
  json_file.close()

authorExists = False;
for author in authorsCharacs:
  # Si no existe -> hacemos un append al author.json con ese autor
  if author['Nombre'].lower().count(authorBook.lower()) != 0:
    # data['Nombre'] = author['Nombre']
    # Longitud de palabr
    auxLongPal = []
    rangeIter = len(author['ProporcionLongitudPalabras']) if len(author['ProporcionLongitudPalabras']) < len(data['ProporcionLongitudPalabras']) else len(data['ProporcionLongitudPalabras'])
    for i in range(rangeIter):
      aux = [i + 1]
      oldResult = author['ProporcionLongitudPalabras'][i][1] * author['NumeroTokens']['NumLongitudPalabras']
      newResult = data['ProporcionLongitudPalabras'][i][1] * data['NumeroTokens']['NumLongitudPalabras']
      totalTokens = author['NumeroTokens']['NumLongitudPalabras'] + data['NumeroTokens']['NumLongitudPalabras']
      newResult = (oldResult + newResult) / totalTokens
      aux.append(newResult)
      auxLongPal.append(aux)
      aux = []
    # Como los tamaños pueden ser diferentes, debemos rellenar con los datos del array más largo
    authorLen = len(author['ProporcionLongitudPalabras'])
    dataLen = len(data['ProporcionLongitudPalabras'])
    sizeDiff = authorLen - dataLen
    # Si dataLen > authorLen
    if (sizeDiff < 0):
      for i in range(sizeDiff):
        auxLongPal.append([authorLen + sizeDiff, data['ProporcionLongitudPalabras'][authorLen + sizeDiff]])
    # Si authorLen > dataLen
    elif (sizeDiff > 0):
      for i in range(sizeDiff):
        auxLongPal.append([dataLen + sizeDiff, author['ProporcionLongitudPalabras'][dataLen + sizeDiff]])

    author['ProporcionLongitudPalabras'] = auxLongPal
    # Frecuencia comas
    author['frecuenciaComas'] = calculateNewResult(author, "frecuenciaComas", "NumFrecuenciaPuntos")
    # Frecuencia puntos
    author['frecuenciaPuntos'] = calculateNewResult(author, "frecuenciaPuntos", "NumFrecuenciaPuntos")
    # Longitud media de frase
    author['longitudSentenciaMedia'] = calculateNewResult(author, "longitudSentenciaMedia", "NumCincuentaPalabras")
    # Longitud media de frase
    author['palabrasRaras'] = calculateNewResult(author, "palabrasRaras", "NumPalabrasRaras")

    # Actualizacion de numero de tokens
    author['NumeroTokens']["NumLongitudPalabras"] += data['NumeroTokens']["NumLongitudPalabras"]
    author['NumeroTokens']["NumFrecuenciaPuntos"] += data['NumeroTokens']["NumFrecuenciaPuntos"]
    author['NumeroTokens']["NumLongitudSentenciaMedia"] += data['NumeroTokens']["NumLongitudSentenciaMedia"]
    author['NumeroTokens']["NumCincuentaPalabras"] += data['NumeroTokens']["NumCincuentaPalabras"]
    author['NumeroTokens']["NumPalabrasRaras"] += data['NumeroTokens']["NumPalabrasRaras"]

    # Cincuenta palabras ordenar
    author['cincuentaPalabrasFrecuentes'] = topFiftyWordsMoreUsed(author['cincuentaPalabrasFrecuentes'], data['cincuentaPalabrasFrecuentes'])
    authorExists = True;
    break

# Si existe -> buscar autor en el json y equilibrar la estadistica de caracterizacion
if authorExists == False:
  # hacemos un append
  data['Nombre'] = authorBook
  authorsCharacs.append(data)

if os.path.exists("authors.json"):
  os.remove("authors.json")

json_file_out = json.dumps(authorsCharacs, indent = 2)
# Escribimos en el fichero
with open('authors.json', 'w') as outputFile:
  outputFile.write(json_file_out)



  


