"""
Módulo RESOLVER
Este módulo contiene funciones utilizadas para la resolución de ejercicios
"""

import Printer
import pprint

from Exercise import Exercise
from pulp import value, LpStatus, LpProblem
from LpSolver import optimize

pp = pprint.PrettyPrinter()


# imprime la lista de soluciones agrandándola a medida que el usuario solicita más resultados
def print_solution(solutions: list):
    Printer.clear_console()
    for s in solutions:
        print("\nSolución N°:", s["sol_num"])
        print("Tipo de solución:", s["sol_type"])
        for a in s["assignments"]:
            print(a)
        print("Valor de la solución objetivo:", s["sol_obj"])


# devuelve una solución con el formato de restricción para ser agregada al próximo cálculo
def new_solution(c_list: list, prob: LpProblem, assign: list, solution: dict, sol_count: int, exercise: Exercise):
    # Agrega las asignaciones de agentes a tareas a la solución
    c_list.append([])
    i = 0
    a_num = 1
    solution.update({"assignments": []})
    for v in prob.variables():
        if v.varValue == 1.0:
            solution_row = "Se asigna el agente \"" + assign[i][0] + "\""
            solution_row += " a la tarea \"" + assign[i][1]
            solution_row += "\" siendo su " + exercise.coef_name + " de " + str(v.dj) + "\"."

            # Agrega un renglón de asignación al diccionario solución
            solution["assignments"].append(solution_row)

            # Actualiza la lista de restricciones con un nuevo resultado
            c_list[sol_count].append({"agent": assign[i][0], "task": assign[i][1]})
            a_num += 1
        i += 1

    # Agrega el valor encontrado al dict "solution"
    solution.update({"sol_obj": value(prob.objective)})

    return solution


# Esta función toma como parámetro el objeto tipo "Exercise" y realiza el cálculo de asignación con la librería PuLP
def resolve(exercise: Exercise):
    # Borra la consola
    Printer.clear_console()
    Printer.print_exercise_title(exercise.number)
    # Muestra los valores del ejercicio en formato pedido por PuLP
    print("\nAgentes: " + str(exercise.agent_name))
    print("\nTareas: " + str(exercise.task_name))
    print("\nRendimientos: " + str(exercise.value))

    Printer.press_enter_to("calcular")

    constrain_list = []  # Lista de restricciones a agregar
    solutions = []  # Lista de soluciones para imprimir todas juntas en pantalla
    limit = 0  #
    calc_count = 0
    best_result = 0
    print("soluciones:", len(solutions))
    solved = False
    while not solved:
        sol_count = len(solutions)
        prob, assign = optimize(exercise, constrain_list)
        sol_type = LpStatus[prob.status]
        solution = {"sol_num": sol_count + 1}

        # Si se encuentra un resultado...
        if sol_type == "Optimal":
            if calc_count == 0:
                solution.update({"sol_type": "Factible Óptima Única"})
                best_result = value(prob.objective)

            # si no es el primer cálculo, y se trata de una solución factible óptima...
            if calc_count > 0 and best_result == value(prob.objective):
                limit += 1
                solutions[0]["sol_type"] = "Factible Óptima Alternativa"
                solution.update({"sol_type": "Factible Óptima Alternativa"})

            # si no es el primer cálculo, y se trata de una solución factible no óptima...
            if calc_count > 0 and best_result != value(prob.objective):
                print_solution(solutions)
                limit = calc_count
                confirm = input('\nPresione "Enter" para calcular la siguiente solución alternativa (si la hay). Para salir ingrese "s". ')
                if confirm is "s":
                    solved = True
                else:
                    solution.update({"sol_type": "Factible Alternativa (no óptima)"})

            if not solved:
                # Agrega el diccionario solución a la lista de soluciones
                solutions.append(new_solution(constrain_list, prob, assign, solution, sol_count, exercise))
                print_solution(solutions)
                calc_count += 1

        # Si no encuentra más resultados...
        if sol_type is "Infeasible":
            solved = True
            print_solution(solutions)
            print("\nNo existen más soluciones.")
            Printer.press_enter_to("volver al menú")
