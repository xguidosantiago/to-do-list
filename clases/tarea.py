from datetime import datetime
from .nota import nota

class tarea:
    def __init__(self, id, titulo):
        self.idTarea = id
        self.titulo = titulo
        self.lstNotas = []
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.estado = False

    def agregarNota(self, mensaje):
        pNota = nota()
        pNota.setMensaje(mensaje)
        self.lstNotas.append(pNota)
        print("nota añadida exitosamente")
    
    def getId(self):
        return self.idTarea
    
    def getTitulo(self):
        return self.titulo
    
    def getFecha(self):
        return self.fecha
    
    def getEstado(self):
        if self.estado == True:
            return "Finalizado"
        else:
            return "Pendiente"
    
    def getNotas(self):
        return self.lstNotas