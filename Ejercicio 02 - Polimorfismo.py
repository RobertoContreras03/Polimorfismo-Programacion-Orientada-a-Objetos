class Examen:
    def __init__(self,materia,):
        self.materia = materia

tematica = Examen("Analisis Númerico")
tematica2 = Examen("Base de datos")

class Estudiante(Examen):
    pass
    def Evaluacion():
        return "El resultado del examen de {} fue positivo".format(tematica.materia)

class Docente(Examen):
    pass
    def Evaluacion():
        return "La evaluacion del resultado del examen de {} fue positivo".format(tematica2.materia)

estudiante1 = Estudiante
estudiante2 = Docente
print(estudiante1.Evaluacion())
print(estudiante2.Evaluacion())
