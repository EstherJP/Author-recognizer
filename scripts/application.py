############## ENSAMBLADO DE LA APLICACION CON TODAS SUS FUNCIONALIDADES
from tkinter import *
from tkinter import filedialog
from searchAuthor import *
from userTraining import *
from incidences import *
from tkinter import ttk
from tkinter import messagebox

bookPath = ''

# Funcion que abre el buscador de archivo para seleccionar el fichero en formato epub que desees
def openBook(fileExplorer):
  global bookPath
  auxPath = filedialog.askopenfilename(initialdir="C:/Users/", title="Select file", filetypes=(("Text Files", "*.epub"), ))
  if auxPath != '':
    filteredPath = auxPath.split('/')
    showPath = filteredPath[-2] + '/' + filteredPath[-1] 
    fileExplorer.configure(text=showPath)
    bookPath = auxPath
  else:
    filteredPath = bookPath.split('/')
    showPath = filteredPath[-2] + '/' + filteredPath[-1]
    fileExplorer.configure(text=showPath) 
  
# Funcion que busca los tres mejores autores
def callSearchAuthor():
  if len(bookPath) > 0:
    authors = informationRetrieval(bookPath)
    authorsTitleLabel = Label(tabSearch, text="Three authors with most probability")
    authorsTitleLabel.place(x=5, y=100)
    textAuthors = ""
    for i in range(3):
      textAuthors += str(i + 1) + ".- " + authors[i][1] + " "
      textAuthors += "with a similarity percentage of" + str(authors[i][0]) + "%\n"
      
    authorsLabel = Label(tabSearch, text=textAuthors)
    authorsLabel.place(x=5, y=130)
  else:
    messagebox.showwarning('SEARCH','Must select a book')

# Funcion que crea las incidencias
def callIncidences(name, email, so, incidenceText):
  userName = name.get("1.0", "end-1c")
  userEmail = email.get("1.0", "end-1c")
  userSO = so.get("1.0", "end-1c")
  userIncidence = incidenceText.get("1.0", "end-1c")

  writeIncidences(userName, userEmail, userSO, userIncidence)
  messagebox.showinfo('INCIDENCES', 'Your incidence was sent with succes.')

# Funcion que permite al usuario agrandar la base de datos
def callUserTrain(authorName):
  if len(bookPath) > 0 and len(authorName.get("1.0", "end-1c")) > 0:
    authorBook = authorName.get("1.0", "end-1c")
    retrainIA(bookPath, authorBook)
    messagebox.showinfo('TRAIN', 'Training done correctly')
  elif len(bookPath) <= 0 and len(authorName.get("1.0", "end-1c")) > 0: 
    messagebox.showwarning('TRAIN','Must select a book')
  elif len(bookPath) > 0 and len(authorName.get("1.0", "end-1c")) <= 0: 
    messagebox.showwarning('TRAIN','Must select an author')
  else:
    messagebox.showwarning('TRAIN','Must select a book and an author')

# Aplicacion    
def application():
  # Creamos la pestaña principal de nuestra aplicacion
  root = Tk()
  root.title("Author-recognizer")
  root.geometry("750x500")
  root.configure(background='alice blue')

  # Control de ventanas de las distintas funcionalidades de la aplicacion (buscar autor, entrenar IA y reportar incidencia)
  tabControl = ttk.Notebook(root)
  global tabSearch
  tabSearch = Frame(tabControl)
  tabTrain = Frame(tabControl)
  tabIncidence = Frame(tabControl)

  # Ponemos nombres a nuestras pestañas
  tabControl.add(tabSearch, text="Search")
  tabControl.add(tabTrain, text="Train")
  tabControl.add(tabIncidence, text="Incidences")

  tabControl.pack(expand=1, fill='both')

  # PESTAÑA DE BUSCAR AUTOR
  # Mostramos el titulo de la aplicacion
  searchTitle = Label(tabSearch, text="Application to find the name of the author of a book")
  searchTitle.place(x=15, y=5)

  # global fileExplorer
  # Muestra la ruta del libro seleccionado
  fileExplorerS = Label(tabSearch, text = "", bd=4, bg="ghost white", width=75, relief=RIDGE) 
  fileExplorerS.place(x=15, y=30)

  # Buscamos en nuestro explorador de archivos el libro en formato epub que queremos buscar
  openButtonS = Button(tabSearch, text="Select file", command=lambda: openBook(fileExplorerS), bg="lavender", width=11, height=1)
  openButtonS.place(x=485, y=30)

  waitLabel = Label(tabSearch, text="This could take a while...")
  waitLabel.place(x=15, y=65)
  # Una vez introducido el libro, seleccionamos buscar los autores mas posible y los mostramos
  searchButton = Button(tabSearch, text="Search author", command=callSearchAuthor, bg="lavender", width=11, height=1)
  searchButton.place(x=580, y=30)

  # PESTAÑA ENTRENAMIENTO
  # Muestra la ruta del libro seleccionado
  trainTitle = Label(tabTrain, text="Here you can introduce your .epub files to train and improve the IA!")
  trainTitle.place(x=15, y=10)

  fileExplorerT = Label(tabTrain, text = "", bd=4, bg="ghost white", width=75, relief=RIDGE) 
  fileExplorerT.place(x=15, y=30)

  # Buscamos en nuestro explorador de archivos el libro en formato epub que queremos buscar
  openButtonT = Button(tabTrain, text="Select file", command=lambda: openBook(fileExplorerT), bg="lavender", width=11, height=1)
  openButtonT.place(x=485, y=30)

  authorBook = Label(tabTrain, text = "Author's surname", width=20) 
  authorBook.place(x=15, y=60)
  insertAuthor = Text(tabTrain, height=1, width=25)
  insertAuthor.place(x=140, y=60)

  trainButton = Button(tabTrain, text="Train", command=lambda: callUserTrain(insertAuthor), bg="lavender", width=12, height=1)
  trainButton.place(x=250, y=100)

  # PESTAÑA DE INCIDENCIAS
  # Realizamos formulario de incidencias
  # Introducir el nombre del usuario
  title = Label(tabIncidence, text = "Here you can send your opinions and incidences. We will attend them as fast as possible.") 
  title.place(x=15, y=5)

  userName = Label(tabIncidence, text = "Name", bd=4, bg="ghost white", width=20, relief=RIDGE) 
  userName.place(x=15, y=30)
  insertName = Text(tabIncidence, height=1, width=25)
  insertName.place(x=160 , y=30)

  # Introducir el correo del usurio
  userEmail = Label(tabIncidence, text="Email", bd=4, bg="ghost white", width=20, relief=RIDGE)
  userEmail.place(x=15, y=60)
  insertEmail = Text(tabIncidence, height=1, width=25)
  insertEmail.place(x=160, y=60)

  # Introducir el sistema operativo en donde ocurrio el problema
  userSo = Label(tabIncidence, text="Operating System", bd=4, bg="ghost white", width=20, relief=RIDGE)
  userSo.place(x=15, y=90)
  insertSo = Text(tabIncidence, height=1, width=25)
  insertSo.place(x=160, y=90)

  # Descripcion de la incicendia
  userIncidence = Label(tabIncidence, text="Incidence", bd=4, bg="ghost white", width=20, relief=RIDGE)  
  userIncidence.place(x=15, y=120)
  insertIncidence = Text(tabIncidence, height=15, width=70)
  insertIncidence.place(x=160, y=120)
  
  incidenceButton = Button(tabIncidence, text="Send incidence", command=lambda: callIncidences(insertName, insertEmail, insertSo, insertIncidence), bg="lavender", width=12, height=1)
  incidenceButton.place(x=330, y=340)

  root.mainloop()

# Ejecutamos nuestra aplicacion
application()