"""
Módulo RESOLVER
Este módulo contiene funciones utilizadas para la resolución de ejercicios
"""

import Printer
import pprint
from Exercise import Exercise
from pulp import LpProblem, LpMinimize, LpStatus, LpVariable, lpSum, value
pp = pprint.PrettyPrinter()


# Esta función toma como parámetro el objeto tipo "Exercise" y realiza el cálculo de asignación con la librería PuLP
def resolve(ex: Exercise):
    # Borra la consola
    Printer.clear_console()
    Printer.print_exercise_title(ex.number)
    # Muestra los valores del ejercicio en formato pedido por PuLP
    print("\nAgentes: " + str(ex.agent_name))
    print("\nTareas: " + str(ex.task_name))
    print("\nRendimientos: " + str(ex.value))

    Printer.press_enter_to("volver al menú")
'''
    cell_value = {}
    for i in range(ex.get_row_num()):
        cell_value.update({ex.agent_name[i]: {}})
        for j in range(ex.get_column_num()):
            cell_value[ex.agent_name[i]].update({ex.task_name[j]: ex.value[i][j]})
    print("\nRendimientos: ")
    pp.pprint(cell_value)


    # Inicia el cálculo del ejercicio
    problem = LpProblem("Transporte", LpMinimize)
    routes = [(i, j) for i in ex.agent_name for j in ex.task_name]
    amount = LpVariable.dicts("Cantidades", (ex.agent_name, ex.task_name), 0)
    problem += lpSum(amount[i][j] * cell_value[i][j] for (i, j) in routes)
    # Restricciones
    for j in ex.task_name:
        problem += lpSum(amount[i][j] for i in ex.agent_name) == demand[j]
    # Restricciones
    for i in ex.agent_name:
        problem += lpSum(amount[i][j] for j in ex.task_name) <= offer[i]
    Printer.press_enter_to("calcular y mostrar los resultados")
    # Resolución final del ejercicio
    problem.solve()
    Printer.clear_console()
    Printer.print_exercise_title(ex.number)
    print("Solución:")
    print("Status:", LpStatus[problem.status])
    # Impresión de la solución
    for v in problem.variables():
        if v.varValue > 0:
            print(v.name, "=", v.varValue)
    print("El costo mínimo es:", value(problem.objective))
    # Vuelve al menú principal
'''
