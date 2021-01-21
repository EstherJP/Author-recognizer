import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
# Fichero que contiene funciones básicas

# Función que nos permite eliminar un elemento de la lista
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

# Conjunto de función que nos permiten pasar de epub a texto manejable en python
blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]

# Función que pasa de formato epub a fformato html
def epub2thtml(path):
  book = epub.read_epub(path)
  chapters = []
  for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
  return chapters

# Función que transforma un capítulo en formato html a texto
def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output

# Función que
def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

# Función que transforma un texto en formato epub a un texto en un formato
# con el que se pueda trabajar des de el código
def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext

# Función que une todos los elementos (capítulos) de una lista
def getTextFromChaps(chapters):
  separator = " "
  text = separator.join(chapters)
  return text