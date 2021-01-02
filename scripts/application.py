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
    authors = informationRetrieval(bookPath)
  
    authorsTitleLabel = Label(root, text="Three authors with most probability(?)", bg="alice blue")
    authorsTitleLabel.place(x=5, y=100)
    textAuthors = ""
    for i in range(3):
      textAuthors += str(i + 1) + ".- " + authors[i][1] + " "
      textAuthors += "con un porcentaje de similitud de " + str(authors[i][0]) + "%\n"
      
    authorsLabel = Label(root, text=textAuthors, bg="alice blue")
    authorsLabel.place(x=5, y=130)
  else:
    messagebox.showinfo('ERROR','Must select a book')
    
def application():
  global root
  root = Tk()
  root.title("Author-recognizer")
  root.geometry("750x500")
  root.configure(background='alice blue')

  # Control de ventanas
  tabControl = ttk.Notebook(root)
  tabSearch = Frame(tabControl)
  tabTrain = Frame(tabControl)
  tabIncident = Frame(tabControl)

  # tabSearch.pack(fill="both", expand=1)
  # tabTrain.pack(fill="both", expand=1)
  # tabIncident.pack(fill="both", expand=1)

  tabControl.add(tabSearch, text="Search")
  tabControl.add(tabTrain, text="Train")
  tabControl.add(tabIncident, text="Incident")

  searchTitle = Label(tabSearch, text="Application to find the name of the author of a book", bg="alice blue")
  # searchTitle.grid(column=1, row=0)
  # searchTitle.pack()
  searchTitle.place(x=35, y=5)

  global fileExplorer
  fileExplorer = Label(tabSearch, text = "File explorer", bd=4, bg="ghost white", width=75, relief=RIDGE) 
  # fileExplorer.grid(column=1, row=1)
  fileExplorer.place(x=15, y=30)
  # fileExplorer.pack()

  openButton = Button(tabSearch, text="Select file", command=openBook, bg="lavender", width=11, height=1)
  # openButton.grid(column=0, row=1)
  openButton.place(x=480, y=30)

  # openButton.pack()

  searchButton = Button(tabSearch, text="Search author", command=searchAuthor, bg="lavender", width=11, height=1)
  # searchButton.grid(column=0, row=2)
  searchButton.place(x=580, y=30)
  # searchButton.pack()

  tabControl.pack(expand=1, fill='both')

  root.mainloop()

application()