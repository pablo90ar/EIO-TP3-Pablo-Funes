from Exercise import Exercise
from pulp import LpVariable, LpProblem, LpMinimize, makeDict, LpBinary, lpSum, LpMaximize


# Recibe un objeto Exercise, la(s) solución(es) ya conocida(s), crea el problema y lo resuelve
def optimize(ex: Exercise, constrain_list: list):
    # Define si el objetivo del cálculo es minimizar o maximizar
    if ex.minimize:
        sense = LpMinimize
    else:
        sense = LpMaximize
    # Crea un nuevo problema de asignación
    # - Parámetro "name": Es el nombre del problema (y si se exporta el resultado, también es el nombre del archivo)
    # - Parámetro "sense": Define la maximización (LpMaximize) o minimización (LpMinimize) del resultado
    prob = LpProblem("Problema_de_asignación", sense)

    # La tabla de rendimientos, sus agentes y tareas son convertidos en un diccionario
    # - Parámetro "headers": Define los títulos de cada combinación Agente-Tarea
    # - Parámetro "array": Es la lista de filas(sublistas) con los valores de la tabla
    values = makeDict([ex.agent_name, ex.task_name], ex.value, 0)
    # Crea una lista de tuplas conteniendo todas las combinaciones Agente-Tarea
    assign = [(i, j) for i in ex.agent_name for j in ex.task_name]

    # Crea un diccionario 'value_dict' para contener las variables referenciadas
    value_dict = LpVariable.dicts("Asignación", (ex.agent_name, ex.task_name), 0, 1, LpBinary)

    # La función "objetivo" es agregada a la variable que almacena el problema("prob")
    prob += (lpSum([value_dict[i][j] * values[i][j] for (i, j) in assign]), "Suma",)

    # Se agregan restricciones de columna. Cada tarea puede ser asignada a solo un agente.
    for j in ex.task_name:
        prob += lpSum(value_dict[i][j] for i in ex.agent_name) == 1

    # Se agregan restricciones de fila. Cada agente puede ser asignado a solo una tarea.
    for i in ex.agent_name:
        prob += lpSum(value_dict[i][j] for j in ex.task_name) == 1

    # Si existen, se agregan las restricciones que permiten calcular la siguiente solución
    if constrain_list:
        for constrain in constrain_list:
            item_list = []
            for value in constrain:
                item_list.append(value_dict[value["agent"]][value["task"]])
            if ex.minimize:
                prob += lpSum(item for item in item_list) <= ex.get_row_num() - 1
            else:
                prob += lpSum(item for item in item_list) >= ex.get_row_num() + 1



    # El problema se resuelve usando la función correspondiente de PuLP.
    prob.solve()

    return prob, assign
