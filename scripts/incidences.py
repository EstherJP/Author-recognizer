# Comunicador de incidencias
def writeIncidences(name, email, so, incidenceBody):
  file = open("incidences.txt", "a")
  identification = "Name: " + name + "\n"
  file.write(identification)
  contact = "Contact: " + email + "\n"
  file.write(contact)
  so = "Operative System: " + so + "\n"
  file.write(so)
  text = "Incidence: " + incidenceBody + "\n"
  file.write(text)
  separator = "--------------------\n"
  file.write(separator)
