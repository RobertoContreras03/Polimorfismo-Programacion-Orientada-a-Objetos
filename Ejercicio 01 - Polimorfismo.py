
#EJERCICIO 01

class Libro:
    def __init__(self,nombre):
        self.nombre = nombre
persona1 = Libro("Aftermath: Empire ends")
persona2 = Libro("The Man in the High Castle")

class Critico(Libro):
    pass
    def OpinionLibro():
        return "El libro {} fue de su agrado".format(persona1.nombre)

class Lector(Libro):
     pass
     def OpinionLibro():
         return "El libro {} tambien fue de su agrado".format(persona2.nombre)

critico = Critico
lector = Lector
print(critico.OpinionLibro())
print(lector.OpinionLibro())
