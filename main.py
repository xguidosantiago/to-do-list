from datetime import datetime
from clases.nota import nota
from clases.tarea import tarea
from clases.todo import todo
import os

            
# programa

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
        pass

print("1. Listar Tareas")
print("2. Crear Tarea")
opcion = int(input("Ingrese una opcion: "))
   

while True:
    pTodo.imprimirTareas()
    resultado = listarOpciones() 
    abmTareas(resultado)






    


