"""
Módulo EXERCISE
Este módulo contiene la entidad utilizada para almacenar todos los datos relevantes de un ejercicio de transporte
"""


# Clase Exercise: utilizada para cargar y manipular los datos de un ejercicio que provienen del archivo "Problems.json"
# Esta clase define el esquema, estructura o molde de la tabla de asignación de un ejercicio práctico
class Exercise:
    number: int  # El número de ejercicio en la guía
    pre_prompt: str  # Consigna del problema antes de la tabla
    post_prompt: str  # Consigna del problema después de la tabla
    agent_type: str  # Nombre de la columna agente
    agent_name: list  # Lista con los nombres de los agentes
    task_type: str  # Nombre de la fila de tareas
    task_name: list  # Lista con los nombres de las tareas
    value: list  # value[i][j] Es el rendimiento del agente(i) en la tarea(j)

    def __init__(self):
        self.number = 0
        self.pre_prompt = ""
        self.post_prompt = ""
        self.agent_type = ""
        self.agent_name = []
        self.task_type = ""
        self.task_name = []
        self.value = []

    # Función que devuelve el número de columnas de la tabla de valores de un ejercicio
    def get_column_num(self):
        return len(self.value[0])

    # Función que devuelve el número de filas de la tabla de valores de un ejercicio
    def get_row_num(self):
        return len(self.value)

    # Referencia de las variables usadas:
    """
    +---------------+----------------------------------------------------------------+
    |               |                           task_type                            |
    +---------------+----------------------------------------------------------------+
    |  agent_type   |  task_name[0]    task_name[1]    task_name[2]    task_name[n]  |
    +---------------+----------------------------------------------------------------+
    | agent_name[0] |  value[0][0]     value[0][1]     value[0][2]     value[0][n]   |
    | agent_name[1] |  value[1][0]     value[1][1]     value[1][2]     value[1][n]   |
    | agent_name[2] |  value[2][0]     value[2][1]     value[2][2]     value[2][n]   |
    | agent_name[n] |  value[n][0]     value[n][1]     value[n][2]     value[n][n]   |
    +---------------+----------------------------------------------------------------+
    """