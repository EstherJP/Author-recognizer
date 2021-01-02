from basicFunctions import *
from textCharacterization import * 
import sys
import numpy as np 
import json
import math
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

print(sys.argv[1])
# Introducimos texto (ya sea a mano o en formato epub)
# Caracterizamos dicho texto
def characterizeText(path):
  textFromBook = getTextFromChaps(epub2text(path))
  # Leemos nuestro fichero JSON con las caracteriscas de los autores de nuestra bbdd
  currentText = {}
  currentText["cincuentaPalabrasFrecuentes"] = fiftyMostUsedWords(textFromBook)

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
  textFiftyMostUsed = fiftyMostUsedWords(textFromBook)

  return [textVector, textFiftyMostUsed]

def informationRetrieval(path):
  # Leemos el fichero json y lo guardamos en un objeto
  with open('authors.json') as json_file:
    authorsCharacs = json.load(json_file)
  
  characterizedText = characterizeText(path)
  textVector = characterizedText[0]
  textFiftyMostUsed = characterizedText[1]

  # Inicializamos el mejor angulo al valor mas bajo para coger el primer author como referencia
  bestAngle = 90;
  bestAuthor = 'nadie';
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
    authorFiftyMostUsed = author['cincuentaPalabrasFrecuentes']
    for textPairs in range(50):
      for authorPairs in range(50):
        if textFiftyMostUsed[textPairs][0] == authorFiftyMostUsed[authorPairs][0]:
          commonWords += 1

    # Calculamos el angulo 
    cosineAngle = dot(authorVector, textVector)/norm(authorVector)/norm(textVector) 
    currentAngle = math.degrees(arccos(clip(cosineAngle, -1, 1))) - (commonWords * 0.5)

    percentage = round(100 - (((currentAngle + 25) * 100) /
    
     115), 2)
    percentageAuthors[percentage] = author['Nombre']

  percentageAuthors = sorted(percentageAuthors.items(), reverse = True)

  return percentageAuthors

def mostrarResultado():
  result = informationRetrieval(sys.argv[1])
  print("El texto introducido probablemente sea de :")
  for i in range(3):
    print(i + 1, ".", "Autor: ", result[i][1])
    print("Porcentaje: ", result[i][0])

mostrarResultado()