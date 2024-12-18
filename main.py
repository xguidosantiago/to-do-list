from datetime import datetime
from clases.nota import nota
from clases.tarea import tarea
from clases.todo import todo
import os, time

# programa
def main ():
    os.system("cls")
    pTodo = todo()
    pTodo.imprimirTareas()

    def listarOpciones():
        print("1. Nueva tarea")
        print("2. Ver tarea")
        print("3. Salir")
        opcion = int(input("ingrese opcion > "))
        return opcion

    def abmTareas(opc):
        if opc == 1:
            pTitulo = input("ingrese el titulo de la tarea \n> ")
            pTodo.crearTarea(pTitulo)
        elif opc == 3:
            print("Saliendo del Programa...")
            time.sleep(2)
            os.system("cls")
            exit()
        elif opc == 2:
            if len(pTodo.getLstTareas()) > 0:
                idTarea = int(input("ingrese ID a visualizar > "))
                while True:
                    os.system("cls")
                    pTarea = pTodo.getTarea(idTarea)
                    if pTarea is None:
                        input("\nLa tarea con el ID ingresado no existe...")
                        return False
                    pNotas = pTarea.getNotas()
                    print(f"\nFecha de creación: {pTarea.getFecha()}\nTitulo: {pTarea.getTitulo()}\nEstado: {pTarea.getEstado()}\nNotas: \n")
                    if len(pNotas) > 0:
                        for pnota in pNotas:
                            print(f"{pnota.getFecha()}: '{pnota.getMensaje()}'")

                    print("-"*30)
                    print("1. Agregar Nota")
                    print("2. Cambiar Estado")
                    print("3. Eliminar")
                    print("4. volver al menu")
                    opcion = int(input("Ingrese opción > "))

                    if opcion == 1:
                        msj = input("ingrese nota: ")
                        pTarea.agregarNota(msj)
                        input("nota añadida exitosamente")
                    elif opcion == 2:
                        pTarea.setEstado()
                        input(f"se modificó estado a {pTarea.getEstado()}")
                    elif opcion == 3:
                        idEliminar = int(input(f"desea eliminar la tarea con ID {idTarea}? 1.si - 2. no > "))
                        if idEliminar == 1:
                            pTodo.eliminarTarea(idTarea)
                            input(f"se eliminó la tarea con ID {idTarea}")
                            return False
                    elif opcion == 4:
                        return False
            else:
                input("\nNo hay tareas cargadas...")

    while True:
        pTodo.imprimirTareas()
        resultado = listarOpciones() 
        abmTareas(resultado)

if __name__ == "__main__":
    main()








    


