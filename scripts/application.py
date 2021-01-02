############## ENSAMBLADO DE LA APLICACION CON TODAS SUS FUNCIONALIDADES
from tkinter import *
from tkinter import filedialog
from searchAuthor import *
from tkinter import ttk
from tkinter import messagebox

bookPath = ''

def openBook():
  global bookPath
  auxPath = filedialog.askopenfilename(initialdir="C:/Users/eduar/Documents/ULL/4º/SI/Proyecto_final/Author-recognizer/books", title="Seleccionar fichero", filetypes=(("Text Files", "*.epub"), ))
  if auxPath != '':
    filteredPath = auxPath.split('/')
    showPath = filteredPath[-2] + '/' + filteredPath[-1] 
    fileExplorer.configure(text=showPath)
    bookPath = auxPath
  else:
    filteredPath = bookPath.split('/')
    showPath = filteredPath[-2] + '/' + filteredPath[-1]
    fileExplorer.configure(text=showPath)

def searchAuthor():
  if len(bookPath) > 0:
    print(informationRetrieval(bookPath))
  else:
    messagebox.showinfo('ERROR','Must select a book')
    
def application():
  root = Tk()
  root.title("Author-recognizer")
  root.geometry("750x500")
  root.configure(background='alice blue')

  # Control de ventanas
  # tabControl = ttk.Notebook(root)
  # tabSearch = Frame(tabControl)
  # tabTrain = Frame(tabControl)
  # tabIncident = Frame(tabControl)

  # tabSearch.pack(fill="both", expand=1)
  # tabTrain.pack(fill="both", expand=1)
  # tabIncident.pack(fill="both", expand=1)

  # tabControl.add(tabSearch, text="Search")
  # tabControl.add(tabTrain, text="Train")
  # tabControl.add(tabIncident, text="Incident")

  searchTitle = Label(root, text="Application to find the name of the author of a book", bg="alice blue")
  searchTitle.grid(column=1, row=0)
  # searchTitle.pack()

  global fileExplorer
  fileExplorer = Label(root, text = "File explorer", bd=4, bg="ghost white", width="75", relief=RIDGE) 
  fileExplorer.grid(column=1, row=1)
  # fileExplorer.pack()

  openButton = Button(root, text="Select file", command=openBook, bg="lavender")
  openButton.grid(column=0, row=1)
  # openButton.pack()

  searchButton = Button(root, text="Search author", command=searchAuthor, bg="lavender")
  searchButton.grid(column=0, row=2)
  # searchButton.pack()

  root.mainloop()

application()