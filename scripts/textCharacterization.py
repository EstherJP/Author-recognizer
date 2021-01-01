import nltk
from nltk.corpus import stopwords  
import string
from basicFunctions import *
from collections import Counter

############ Ver si podemos generalizar la tokenizacion
################3 ¿Por que estan globales?
stopWords = [] # Array que contendrá las palabras vacías del inglés
quotes = ["’", '“', '”', "'", '"'] # Array que contiene las comillas de citas

# Función que obtiene la frecuencia de la distribución según la longitud de las 
# palabras por letra
def lengthFreqDis(text):
  # Eliminamos los elementos de puntuación, los números y las comillas
  toRemove = string.punctuation
  toRemove += string.digits
  for elem in quotes:
    toRemove += elem
  tokens = nltk.word_tokenize(text)
  for item in toRemove:
    if item in tokens:
      tokens = remove_values_from_list(tokens, item)

  # Calculamos la longitud de las palabras que se almacenará en un hash cuya clave
  # será la longitud y el valor el número de apariciones
  numberOfTokens = len(tokens)
  tokensLengths = [len(token) for token in tokens]
  freqDist = nltk.FreqDist(tokensLengths)
  filtFreqDist = {}
  for key in freqDist:
    if key < 15:
      filtFreqDist[key] = round((freqDist[key] / numberOfTokens), 6)

  filtFreqDist = sorted(filtFreqDist.items())
  
  return ([filtFreqDist, len(tokens)])

# Función que obtiene la frecuencia media de los puntos y comas cada mil palabras
def punctuationFreq(text):
  comma = ","
  dot = "."
  # Eliminamos todas las palabras dejando un array con todos los puntos y comas del
  # texto
  toRemove = string.punctuation
  toRemove += string.digits
  toRemove = toRemove.replace(comma, "")
  toRemove = toRemove.replace(dot, "")
  for elem in quotes:
    toRemove += elem
  tokens = nltk.word_tokenize(text)
  for item in toRemove:
    if item in tokens:
      tokens = remove_values_from_list(tokens, item)
  
  # Dividimos el texto en packs de mil palbras
  numberOfPack = len(text) / 1000
  dotAcc = 0
  commaAcc = 0
  # Contamos el número de comas y el número de puntos
  for i in text:
    if i == dot:
      dotAcc += 1
    if i == comma:
      commaAcc += 1
  # Hacemos la media del número de comas y puntos cada mil palabras
  averageComma = commaAcc / numberOfPack
  averageDot = dotAcc / numberOfPack
  # Devolvemos un array en donde en la primera posición se encuentra la frecuencia
  # de comas y en el segundo la frecuencia de puntos
  return ([round(averageComma, 6), round(averageDot, 6), len(tokens)])

# Función que obtiene el número medio de la longitud de frases del texto
def sentenceLength(text):
  # Procesamos el texto
  dot = "."
  toRemove = string.punctuation
  toRemove = toRemove.replace(dot, "")
  for elem in quotes:
    toRemove += elem
  tokens = nltk.word_tokenize(text)
  for item in toRemove:
    if item in tokens:
      tokens = remove_values_from_list(tokens, item)

  # Contamos el número de palabras de cada oración 
  sentenceSizes = []
  numberOfSentences = 0
  totalLength = 0 
  for word in tokens:
    if word == dot:
      numberOfSentences += 1
    else:
      totalLength += 1
      
  # Devolvemos la media del tamaño de las oraciones del texto
  return ([round((totalLength / numberOfSentences), 6), len(tokens)])

# Función que obtiene las 50 palabras más frecuentes del texto
def fiftyMostUsedWords(text):
  # Pasamos todas las palabras a minúscila para tratarlas por igual
  text = text.lower()
  # Procesamos el texto eliminamos los caracteres que no nos interesan incluido
  # las palabras vacías
  stop_words = set(stopwords.words('english'))
  toRemove = string.punctuation
  toRemove += string.digits
  for elem in quotes:
    toRemove += elem
  tokens = nltk.word_tokenize(text)
  filtered_sentence = [w for w in tokens if not w in stop_words]  
  for item in toRemove:
    if item in tokens:
      filtered_sentence = remove_values_from_list(filtered_sentence, item)

  # Almacenamos un hash como clave la palabra y como valor su frecuencia
  wordsFrequency = Counter(filtered_sentence)
  # Devolvemos un array de arrays con primer valor la palabra y segundo valor su frecuencia
  return([wordsFrequency.most_common(50), len(tokens)])

def rareWords(text):
  # Pasamos todas las palabras a minúscila para tratarlas por igual
  text = text.lower()
  # Procesamos el texto eliminamos los caracteres que no nos interesan incluido
  # las palabras vacías
  stop_words = set(stopwords.words('english'))
  toRemove = string.punctuation
  toRemove += string.digits
  for elem in quotes:
    toRemove += elem
  tokens = nltk.word_tokenize(text)
  filtered_sentence = [w for w in tokens if not w in stop_words]  
  for item in toRemove:
    if item in tokens:
      filtered_sentence = remove_values_from_list(filtered_sentence, item)

  wordsFrequency = Counter(filtered_sentence)
  count = 0
  for x in wordsFrequency.keys():
    if wordsFrequency[x] <= 2:
      count += 1

  return ([count / len(wordsFrequency), len(filtered_sentence)])