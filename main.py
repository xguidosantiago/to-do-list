from datetime import datetime
from clases.nota import nota
from clases.tarea import tarea
from clases.todo import todo
import os
            
# programa
def main ():
    os.system("cls")
    pTodo = todo()
    pTodo.imprimirTareas()

    def listarOpciones():
        print("1. Nueva tarea")
        print("2. Ver tarea")
        print("3. Modificar Tarea")
        print("4. Eliminar Tarea")
        opcion = int(input("ingrese opcion > "))
        return opcion

    def abmTareas(opc):
        if opc == 1:
            pTitulo = input("ingrese el titulo de la tarea \n> ")
            pTodo.crearTarea(pTitulo)
        elif opc == 2:
            idTarea = int(input("ingrese id a visualizar > "))
            pTarea = pTodo.getTarea(idTarea)
            pTitulo =  pTarea.getTitulo()
            pFecha = pTarea.getFecha()
            pNotas = pTarea.getNotas()
            print(f"fecha: {pFecha}, titulo: {pTitulo}")



    while True:
        pTodo.imprimirTareas()
        resultado = listarOpciones() 
        abmTareas(resultado)

if __name__ == "__main__":
    main()






    


