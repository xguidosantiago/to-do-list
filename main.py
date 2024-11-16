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

            print(f"\n fecha: {pFecha}, \ntitulo: {pTitulo} \n notas: ")
            if len(pNotas) > 0:
                for pnota in pNotas:
                    print(f"{pnota.getFecha()}: '{pnota.getMensaje()}'")
            print("\n1. Agregar Nota")
            print("2. Cambiar Estado")
            print("3. Eliminar")
            opcion = int(input("Ingrese opcion > "))

            if opcion == 1:
                msj = input("ingrese nota: ")
                pTarea.agregarNota(msj)
                input("nota añadida exitosamente")
            elif opcion == 2:
                pTarea.setEstado()
                input(f"se modificó estado a {pTarea.getEstado()}")
            elif opcion == 3:
                idEliminar = int(input("Ingrese id a eliminar: "))
                pTodo.eliminarTarea(idEliminar)
                input(f"se eliminó la tarea con id {idEliminar}")

    while True:
        pTodo.imprimirTareas()
        resultado = listarOpciones() 
        abmTareas(resultado)

if __name__ == "__main__":
    main()








    


