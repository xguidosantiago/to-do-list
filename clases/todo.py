import os
from .tarea import tarea
from .nota import nota

class todo:
    def __init__(self):
        self.lstTareas = []
        self.idTarea = 1

    def getLstTareas(self):
        return self.lstTareas
    
    def setTareas(self,tarea):
        self.lstTareas.append(tarea)

    def imprimirTareas(self):
        os.system("cls")
        print("Listado De Tareas: \n")
        print("{0:^5}|{1:<22}|{2:<40}|{3:<20}".format("ID", "Fecha y Hora", "Titulo", "Estado"))
        print("-"*90)
        for pTarea in self.lstTareas:
            pId = pTarea.getId()
            pFecha = pTarea.getFecha()
            pTitulo = pTarea.getTitulo()
            pEstado = pTarea.getEstado()

            print("{0:^5}|{1:<22}|{2:<40}|{3:<20}".format(pId,pFecha,pTitulo,pEstado))
        print()

    def crearTarea(self, titulo):
        pTarea = tarea(self.idTarea, titulo)
        self.setTareas(pTarea)
        self.idTarea +=1
        print("tarea creada exitosamente")
        input("ingrese enter para continuar...")

    def getTarea(self, id):
        return self.getLstTareas()[id-1]


