import nltk
# nltk.download('punkt')
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import string
from glob2 import glob
# %matplotlib inline
from pylab import *
from basicFunctions import *
import json

books = glob("./books/*.epub")
booksText = []
authors = []

for book in books:
  rawBook = epub.read_epub(book)
  authors.append(rawBook.get_metadata('DC', 'creator')[0][0])
  booksText.append(epub2text(book))

# Función que nos obtenga la distribución de longitud de palabras
def lengthFreqDis(text):
# Eliminamos los elementos de puntuación y los números
  toRemove = string.punctuation
  toRemove += string.digits
  tokens = nltk.word_tokenize(text)
  for item in toRemove:
    if (item in tokens):
      tokens = remove_values_from_list(tokens, item)
  # Calculamos la longitud de las palabras
  tokensLengths = [len(token) for token in tokens]
  freqDist = nltk.FreqDist(tokensLengths)
  return freqDist

def punctuationFreq(text):
  comma = ","
  dot = "."
  toRemove = string.punctuation
  toRemove = toRemove.replace(comma, "")
  toRemove = toRemove.replace(dot, "")
  tokens = nltk.word_tokenize(text)
  for item in toRemove:
    if (item in tokens):
      tokens = remove_values_from_list(tokens, item)
  
  numberOfPack = len(text) / 1000
  dotAcc = 0
  commaAcc = 0
  for i in text:
    if i == dot:
      dotAcc += 1
    if i == comma:
      commaAcc += 1
  averageComma = commaAcc / numberOfPack
  averageDot = dotAcc / numberOfPack
  return([averageComma, averageDot])

def sentenceLength(text):
  dot = "."
  toRemove = string.punctuation
  toRemove = toRemove.replace(dot, "")
  tokens = nltk.word_tokenize(text)
  
  for item in toRemove:
    if item in tokens:
      tokens = remove_values_from_list(tokens, item)
      
  sentenceSizes = []
  wordAcc = 0
  totalLength = 0
  for word in tokens:
    if word == dot:
      sentenceSizes.append(wordAcc)
      wordAcc = 0
    else:
      wordAcc += 1
      
  for element in sentenceSizes:
    totalLength += element
    
  return(totalLength / len(sentenceSizes))

def dataToJSON():
  data = []
  i = 0

  for chaps in booksText:
    aux = {}
    aux["Nombre"] = authors[i]
    aux["longitudPalabras"] = lengthFreqDis(getTextFromChaps(chaps))
    frequencies = punctuationFreq(getTextFromChaps(chaps))
    aux["frecuenciaComas"] = frequencies[0]
    aux["frecuenciaPuntos"] = frequencies[1]
    aux["longitudSentenciaMedia"] = sentenceLength(getTextFromChaps(chaps))

    data.append(aux)
    i += 1

  with open('info.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent = 2)
  
dataToJSON()