import nltk
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import string
from glob2 import glob
from pylab import *
from basicFunctions import *
from textCharacterization import * 
import json

# Recorremos nuestra base de datos y concatenamos los libros po autor
separator = " "
authors = glob("./books/*")
booksText = []
for author in authors:
  books = glob(author + "/*.epub")
  bookText = []
  for book in books:
    rawBook = epub.read_epub(book)
    authors.append(rawBook.get_metadata('DC', 'creator')[0][0])
    bookText.append(getTextFromChaps(epub2text(book)))
  booksText.append(separator.join(bookText))

# Función que escribe en un texto de tipo JSON las características del autor
def dataToJSON():
  data = []

  # Creamos el hash con los datos para cada autor
  for authorCorpus in booksText:
    aux = {}
    aux["Nombre"] = authors[i]
    aux["longitudPalabras"] = lengthFreqDis(authorCorpus)
    frequencies = punctuationFreq(authorCorpus)
    aux["frecuenciaComas"] = frequencies[0]
    aux["frecuenciaPuntos"] = frequencies[1]
    aux["longitudSentenciaMedia"] = sentenceLength(authorCorpus)
    aux["cincuentaPalabrasFrecuentes"] = fiftyMostUsedWords(authorCorpus)

    data.append(aux)
    i += 1

  # Escribimos en el fichero
  with open('info.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent = 2)
  
# dataToJSON()