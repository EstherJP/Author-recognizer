from basicFunctions import *
from textCharacterization import * 
# from searchAuthor import * 
# import sys
# import numpy as np 
import os
import json
# import math
# from numpy import (array, dot, arccos, clip)
# from numpy.linalg import norm

# Función auxiliar para obtener el segundo elemento de un array
def takeSecond(elem):
  return elem[1]

# Funcion que calcula los nuevos valores de la base de datos
def calculateNewResult(author, data, charac, numTokens):
  oldResult = author.get(charac) * author['NumTokens'].get(numTokens)
  newResult = data.get(charac) * data['NumTokens'].get(numTokens)
  totalTokens = author['NumTokens'].get(numTokens) + data['NumTokens'].get(numTokens)
  newResult = (oldResult + newResult) / totalTokens
  return newResult;

# Fusiona los dos arrays de las 50 palabras mas usadas
def topWordsMoreUsed(authorWords, dataWords):
  # Actualizamos los contadores
  numberWords = 75;
  for i in range(numberWords):
    for authorWord in authorWords:
      if dataWords[i][0] == authorWord[0]:
        # print('palabra', dataWords[i][0], 'author', authorWord[0])
        authorWord[1] += dataWords[i][1]
  # Reordenamos el conjunto
  authorWords.sort(key=takeSecond, reverse=True)
  return authorWords


# El usuario introduce un libro en formato epub y el nombre del autor sin espacios
# pathBook = sys.argv[1]
# authorBook = sys.argv[2]
# print(pathBook, authorBook)

def retrainIA(pathBook, authorBook):
  bookText = getTextFromChaps(epub2text(pathBook))

  # Caracterizamos el texto como en el json
  data = {}
  distribution = lengthFreqDis(bookText)
  auxSentenceLength = sentenceLength(bookText)
  auxRareWords = rareWords(bookText)

  data['ProporcionLongitudPalabras'] = distribution[0]
  frequencies = punctuationFreq(bookText)
  data['frecuenciaComas'] = frequencies[0]
  data['frecuenciaPuntos'] = frequencies[1]
  data['longitudSentenciaMedia'] = auxSentenceLength[0]
  data['palabrasFrecuentes'] = most75UsedWords(bookText)
  data['palabrasRaras'] = auxRareWords[0]

  auxTokens = {}
  auxTokens["NumLongitudPalabras"] = distribution[1]
  auxTokens["NumFrecuenciaPuntos"] = frequencies[2]
  auxTokens["NumLongitudSentenciaMedia"] = auxSentenceLength[1]
  auxTokens["NumPalabrasRaras"] = auxRareWords[1]
  data["NumTokens"] = auxTokens

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
      # AJUSTAMOS LA ESTADISTICA DE LOS VALORES DEL JSON DEL AUTOR EXISTINTE
      auxLongPal = []
      rangeIter = len(author['ProporcionLongitudPalabras']) if len(author['ProporcionLongitudPalabras']) < len(data['ProporcionLongitudPalabras']) else len(data['ProporcionLongitudPalabras'])
      for i in range(rangeIter):
        aux = [i + 1]
        oldResult = author['ProporcionLongitudPalabras'][i][1] * author['NumTokens']['NumLongitudPalabras']
        newResult = data['ProporcionLongitudPalabras'][i][1] * data['NumTokens']['NumLongitudPalabras']
        totalTokens = author['NumTokens']['NumLongitudPalabras'] + data['NumTokens']['NumLongitudPalabras']
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
      author['frecuenciaComas'] = calculateNewResult(author, data, "frecuenciaComas", "NumFrecuenciaPuntos")
      # Frecuencia puntos
      author['frecuenciaPuntos'] = calculateNewResult(author, data, "frecuenciaPuntos", "NumFrecuenciaPuntos")
      # Longitud media de frase
      author['longitudSentenciaMedia'] = calculateNewResult(author, data, "longitudSentenciaMedia", "NumLongitudSentenciaMedia")
      # Longitud media de frase
      author['palabrasRaras'] = calculateNewResult(author, data, "palabrasRaras", "NumPalabrasRaras")

      # Actualizacion de numero de tokens
      author['NumTokens']["NumLongitudPalabras"] += data['NumTokens']["NumLongitudPalabras"]
      author['NumTokens']["NumFrecuenciaPuntos"] += data['NumTokens']["NumFrecuenciaPuntos"]
      author['NumTokens']["NumLongitudSentenciaMedia"] += data['NumTokens']["NumLongitudSentenciaMedia"]
      author['NumTokens']["NumPalabrasRaras"] += data['NumTokens']["NumPalabrasRaras"]

      # ORDENAMOS LAS 75 PALABRAS MAS FRECUENTES
      author['palabrasFrecuentes'] = topWordsMoreUsed(author['palabrasFrecuentes'], data['palabrasFrecuentes'])

      authorExists = True;
      break

  aux = authorsCharacs
  # Si existe -> buscar autor en el json y equilibrar la estadistica de caracterizacion
  if authorExists == False:
    # hacemos un append
    data['Nombre'] = authorBook
    authorsCharacs.append(data)

  # HAY QUE ESCRIBIR LA ACTUALIZACION DEL JSON
  # print(json.dumps(authorsCharacs, indent=2, sort_keys=True))
  os.remove('authors.json')
  with open('authors.json', 'w') as outputFile:
      json.dump(authorsCharacs, outputFile, indent=4)




  


