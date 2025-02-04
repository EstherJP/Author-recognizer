# import nltk
# import ebooklib
from ebooklib import epub
# from bs4 import BeautifulSoup
# import string
from glob2 import glob
from pylab import *
# from basicFunctions import *
from textCharacterization import * 
import json
import os

def getBooks():
  # Recorremos nuestra base de datos y concatenamos los libros por autor
  separator = " "
  authors = glob("./booksTrain/*")
  booksText = []
  for author in authors:
    books = glob(author + "/*.epub")
    bookText = []
    for book in books:
      # rawBook = epub.read_epub(book)
      # authors.append(rawBook.get_metadata('DC', 'creator')[0][0])
      bookText.append(getTextFromChaps(epub2text(book)))
    booksText.append(separator.join(bookText))

  return booksText, authors

# Función que escribe en un texto de tipo JSON las características del autor
def dataToJSON():
  data = []
  i = 0
  booksText, authors = getBooks()
  # Creamos el hash con los datos para cada autor
  for authorCorpus in booksText:
    aux = {}
    name = authors[i].split("/")
    distribution = lengthFreqDis(authorCorpus)
    frequencies = punctuationFreq(authorCorpus)
    auxSentenceLength = sentenceLength(authorCorpus)
    auxRareWords = rareWords(authorCorpus)

    aux["Nombre"] = name[2]
    aux["ProporcionLongitudPalabras"] = distribution[0]
    aux["frecuenciaComas"] = frequencies[0]
    aux["frecuenciaPuntos"] = frequencies[1]
    aux["longitudSentenciaMedia"] = auxSentenceLength[0]
    aux["palabrasFrecuentes"] = most75UsedWords(authorCorpus)
    aux["palabrasRaras"] = auxRareWords[0]

    auxTokens = {}
    auxTokens["NumLongitudPalabras"] = distribution[1]
    auxTokens["NumFrecuenciaPuntos"] = frequencies[2]
    auxTokens["NumLongitudSentenciaMedia"] = auxSentenceLength[1]
    auxTokens["NumPalabrasRaras"] = auxRareWords[1]
    aux["NumTokens"] = auxTokens

    data.append(aux)
    i += 1

  if os.path.exists("authors.json"):
    os.remove("authors.json")

  json_file = json.dumps(data, indent = 2)
  # Escribimos en el fichero
  with open('authors.json', 'w') as outputFile:
    outputFile.write(json_file)
  
dataToJSON()