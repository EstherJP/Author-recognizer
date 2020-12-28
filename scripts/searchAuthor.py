from basicFunctions import *
from textCharacterization import * 
import sys
import numpy as np 
import json
import math
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

# Introducimos texto (ya sea a mano o en formato epub)
print(sys.argv[1])
# Caracterizamos dicho texto
textFromBook = getTextFromChaps(epub2text(sys.argv[1]))
# Leemos nuestro fichero JSON con las caracteriscas de los autores de nuestra bbdd
currentText = {}
currentText["cincuentaPalabrasFrecuentes"] = fiftyMostUsedWords(textFromBook)

auxVector = [];
# Igualamos el autor mejor candidato al primero que aparezca en el JSON
frequencies = punctuationFreq(textFromBook)
freqDist = lengthFreqDis(textFromBook)
for elem in freqDist:
  auxVector.append(elem[1])
auxVector.append(frequencies[0])
auxVector.append(frequencies[1])
auxVector.append(sentenceLength(textFromBook))
auxVector.append(rareWords(textFromBook))
textVector = np.array(auxVector)
textFiftyMostUsed = fiftyMostUsedWords(textFromBook)
# print(textVector)
# Leemos el fichero json y lo guardamos en un objeto
with open('authors.json') as json_file:
  authorsCharacs = json.load(json_file)

# Inicializamos el mejor angulo al valor mas bajo para coger el primer author como referencia
bestAngle = 90;
bestAuthor = 'nadie';
currentAngle = 0
percentageDict = {}
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
  authorFiftyMostUsed = author['cincuentaPalabrasFrecuentes']
  for textPairs in textFiftyMostUsed:
    for authorPairs in authorFiftyMostUsed:
      if textPairs[0] == authorPairs[0]:
        commonWords += 1

  # Calculamos el angulo 
  cosineAngle = dot(authorVector, textVector)/norm(authorVector)/norm(textVector) 
  currentAngle = math.degrees(arccos(clip(cosineAngle, -1, 1))) - (commonWords * 0.5)

  # percentage =  (round(100 - ((currentAngle * 100) / 90), 2) * 100) / 115
  percentage = round(100 - (((currentAngle + 25) * 100) / 115), 2)
  percentageDict[percentage] = author['Nombre']

percentageDict = sorted(percentageDict.items(), reverse = True)
# print(percentageDict)
print("El texto introducido probablemente sea de :")
for i in range(3):
  print(i + 1, ".", "Autor: ", percentageDict[i][1])
  print("Porcentaje: ", percentageDict[i][0])
