"""
Módulo LOADER
Este módulo contiene funciones orientadas a leer archivos para colocar información en variables
Esto le permite al programa manipular dicha información y realizar cálculos
"""

import json
import Printer
import Utils
from Exercise import Exercise


# Carga ejercicio de la práctica para ser resuelto y lo devuelve al finalizar
def load_known_exercise(ex_num):
    # Se abre el archivo "Problems.json" que contiene los ejercicios de la práctica
    with open('./src/Problems.json', encoding="utf-8") as file:
        exercise = json.load(file)["data"][ex_num - 1]
    # Se crea un objeto tipo "Exercise" vacío y se lo llena con los valores del ejercicio elegido
    ex = Exercise()
    ex.number = exercise["number"]
    ex.pre_prompt = exercise["pre_prompt"]
    ex.post_prompt = exercise["post_prompt"]
    ex.agent_type = exercise["agent_type"]
    ex.agent_name = exercise["agent_name"]
    ex.task_type = exercise["task_type"]
    ex.task_name = exercise["task_name"]
    ex.value = exercise["value"]
    return ex


# Carga un ejercicio personalizado con todos los valores a pedido usuario y lo devuelve al finalizar
def load_custom_exercise():
    Printer.print_generic_table()
    # Se crea un objeto tipo "Exercise" vacío y se lo llena con los valores del ejercicio elegido
    ex = Exercise()
    ex.agent_type = input("Paso 1/11 - Ingrese el tipo de agente. Valor por defecto: [Agentes] ") or "Agentes"
    ex.task_type = input("Paso 2/11 - Ingrese el tipo de tarea. Valor por defecto: [Tareas] ") or "Tareas"
    input_msj = "Paso 3/11 - Ingrese la cantidad de agentes (filas) de la tabla. (mínimo 2) "
    agent_number = Utils.check_equal_or_greater(input_msj, 2)
    input_msj = "Paso 4/11 - Ingrese la cantidad de tareas (columnas) de la tabla. (mínimo 2) "
    task_number = Utils.check_equal_or_greater(input_msj, 2)
    for i in range(agent_number):
        num = str(i + 1)
        ex.agent_name.append(input("Paso 5/11 - Dato " + str(num) + "/" + str(agent_number)
                                   + " - Ingrese el nombre del agente N°" + num
                                   + ". Valor por defecto: [Agente-" + num + "] ") or "Agente-" + num)
    for j in range(task_number):
        num = str(j + 1)
        ex.task_name.append(input("Paso 6/11 - Dato " + str(num) + "/" + str(task_number)
                                  + " - Ingrese el nombre de la tarea N°" + num
                                  + ". Valor por defecto: [Tarea-" + num + "] ") or "Tarea-" + num)
    for i in range(agent_number):
        ex.value.append([])
        for j in range(task_number):
            input_msj = "Paso 7/11 - Dato " + str(i * task_number + j + 1) + "/" \
                        + str(agent_number * task_number) + " Ingrese el rendimiento de " \
                        + ex.agent_name[i] + " para la tarea " + ex.task_name[j] + "."
            ex.value[i].append(Utils.check_equal_or_greater(input_msj))
    return ex
