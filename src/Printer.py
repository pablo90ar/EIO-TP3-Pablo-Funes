"""
Módulo PRINTER:
Este módulo almacena funciones utilizadas para mostrar información en consola
La información puede ser menús, diálogos, la tabla de un problema, etc.
"""

import os
from copy import deepcopy
from Exercise import Exercise
from TableMerger import tabulate
from pprint import PrettyPrinter


# Borra la pantalla de la consola
def clear_console():
    os.system('cls')


# Muestra mensaje de bienvenida
def print_welcome_msj():
    clear_console()
    print("Trabajo Práctico Nº3: Resolución de problemas de asignación\n")
    print("Cátedra: Elementos de la Investigación Operativa")
    print("Alumno: Pablo Funes")
    print("Profesora: Ingeniera Melina Denardi")
    print("Carrera: Tecnicatura universitaria en programación - UTN FRRaf")
    press_enter_to("ir al menú principal")


# Muestra el menú principal y retorna la opción seleccionada
def print_main_menu():
    success = False
    menu_option = 0
    # Mientras no haya una selección exitosa...
    while not success:
        # Limpia consola, muestra el menú, y solicita ingresar opción
        clear_console()
        print("------------- MENU PRINCIPAL -------------\n")
        print("1- Resolver un ejercicio de la guía de práctica")
        print("2- Resolver un ejercicio ingresando los datos manualmente")
        print("3- Salir del programa")
        selection = input('\nSeleccione una opción y presione "Enter" ')
        # Comprueba si el dato ingresado es un número...
        if selection.isnumeric() and selection.isdigit():
            menu_option = int(selection)
            # Si el número ingresado es "1" o "2"...
            if 0 < menu_option < 4:
                # La opción elegida es válida
                success = True
            else:
                # Si el número está fuera del rango permitido, informa al usuario
                input("Opción incorrecta. Ingrese un número del 1 al 3")
        else:
            # Si el dato ingresado no es un número, informa al usuario
            input("Opción incorrecta. Ingrese un número del 1 al 3")
    # Cuando el usuario ingresa una opción válida, retorna la misma
    return menu_option


# Solicita pulsar "Enter" para continuar con el siguiente paso
def press_enter_to(action="continuar"):
    input('\nPresione "Enter" para ' + action + ".")


# Imprime una tabla completa aceptando un objeto Exercise como parámetro
def print_dynamic_table(ex: Exercise):
    # Inserta task_type como título de la fila de tareas
    ex = deepcopy(ex)
    header1 = [" ", ex.task_type]
    for item in range(len(ex.task_name)-1):
        header1.append(" ")
    # Inserta la segunda línea de títulos de la tabla [agent_type | [task_name] ]
    header2 = [ex.agent_type]
    header2.extend(ex.task_name)
    headers = [header1, header2]
    # Inserta las filas con los valores de rendimiento
    rows = ex.value
    # Inserta la columna con los nombres de agentes (si existen)
    for row in range(len(rows)):
        if ex.agent_name[row]:
            rows[row].insert(0, ex.agent_name[row])
        else:
            rows[row].insert(0, "Agente " + str(row + 1))
    # Imprime la tabla
    col_span = {(0, 1): len(ex.task_name)}
    row_span = {}
    tabulate(headers + rows, col_span, row_span)


# Imprime una tabla con los nombres de referencia para la carga manual de datos
def print_generic_table():
    print("""\
+--------------+------------------------------------------------------------+
|              |                          Tareas                            |
+--------------+------------------------------------------------------------+
|   Agentes    |   Tarea-1        Tarea-2        Tarea-3        Tarea-N     |
+--------------+------------------------------------------------------------+
|   Agente-1   |  valor(1,1)     valor(1,2)     valor(1,3)     valor(1,n)   |
|   Agente-2   |  valor(2,1)     valor(2,2)     valor(2,3)     valor(2,n)   |
|   Agente-3   |  valor(3,1)     valor(3,2)     valor(3,3)     valor(3,n)   |
|   Agente-n   |  valor(n,1)     valor(n,2)     valor(n,3)     valor(n,n)   |
+--------------+------------------------------------------------------------+\

""")


# Imprime el ejercicio cargado, incluyendo el texto de la consigna y su tabla de datos
def print_exercise(ex: Exercise):
    pp = PrettyPrinter()
    clear_console()
    print_exercise_title(ex.number)
    pp.pprint(ex.pre_prompt)
    print_dynamic_table(ex)
    pp.pprint(ex.post_prompt)


# Imprime el número del ejercicio
def print_exercise_title(ex_num: int):
    if ex_num != 0:
        print("------------------------------ Ejercicio Nº", ex_num, "------------------------------")
    else:
        print("------------------------------ Ejercicio Personalizado ------------------------------")


# Muestra mensaje de despedida
def say_goodbye():
    input("\n¡Hasta luego!")

