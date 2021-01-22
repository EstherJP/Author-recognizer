from basicFunctions import *
from textCharacterization import * 
import sys # podemos quitar este sys la verdad
import numpy as np 
import json
import math
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

# Introducimos texto (ya sea a mano o en formato epub)
# Caracterizamos dicho texto
def characterizeText(path):
  textFromBook = getTextFromChaps(epub2text(path))
  # Leemos nuestro fichero JSON con las caracteriscas de los autores de nuestra bbdd
  currentText = {}
  currentText["palabrasFrecuentes"] = most75UsedWords(textFromBook)

  auxVector = [];
  # Igualamos el autor mejor candidato al primero que aparezca en el JSON
  frequencies = punctuationFreq(textFromBook)
  freqDist = lengthFreqDis(textFromBook)[0]
  for elem in freqDist:
    auxVector.append(elem[1])
  auxVector.append(frequencies[0])
  auxVector.append(frequencies[1])
  auxVector.append(sentenceLength(textFromBook)[0])
  auxVector.append(rareWords(textFromBook)[0])
  textVector = np.array(auxVector)
  textWordsMostUsed = most75UsedWords(textFromBook)

  return [textVector, textWordsMostUsed]

# Busca y ordena los autores de más probable a menos
def informationRetrieval(path):
  # Leemos el fichero json y lo guardamos en un objeto
  with open('authors.json') as json_file:
    authorsCharacs = json.load(json_file)
  
  characterizedText = characterizeText(path)
  textVector = characterizedText[0]
  textWordsMostUsed = characterizedText[1]

  # Inicializamos los parámetros que vamos a usar
  currentAngle = 0
  percentageAuthors = {}
  # A medida que leemos los datos de cada autor, vamos actualizando el autor mejor candidato 
  for author in authorsCharacs:
    # Limpiamos los vectores
    auxVector = []
    authorVector = []

    # Vector caracteristico del autor conocido
    for elem in author['ProporcionLongitudPalabras']:
      auxVector.append(elem[1])
    auxVector.append(author['frecuenciaComas'])
    auxVector.append(author['frecuenciaPuntos'])
    auxVector.append(author['longitudSentenciaMedia'])
    auxVector.append(author['palabrasRaras'])
    authorVector = np.array(auxVector) # lo pasamos a numpy

    # Plabras comunes
    commonWords = 0
    authorWordsMostUsed = author['palabrasFrecuentes']
    for textPairs in range(50):
      for authorPairs in range(50):
        if textWordsMostUsed[textPairs][0] == authorWordsMostUsed[authorPairs][0]:
          commonWords += 1

    # Calculamos el angulo 
    cosineAngle = dot(authorVector, textVector)/norm(authorVector)/norm(textVector) 
    currentAngle = math.degrees(arccos(clip(cosineAngle, -1, 1))) - (commonWords * 0.5)

    percentage = round(100 - (((currentAngle + 25) * 100) / 115), 2)
    percentageAuthors[percentage] = author['Nombre']

  percentageAuthors = sorted(percentageAuthors.items(), reverse = True)

  return percentageAuthors

# Muestra los 3 primeros resultados por la terminal
def showResult():
  result = informationRetrieval(sys.argv[1])
  print("El texto introducido probablemente sea de :")
  for i in range(3):
    print(i + 1, ".", "Autor: ", result[i][1])
    print("Porcentaje: ", result[i][0])

# showResult()