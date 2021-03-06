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
    coef_name: str  # El tipo de unidad de los valores. Por ejemplo rendimiento, costo, tiempo, etc.
    minimize: bool  # El modo de optimización. Puede ser "minimizar" o "maximizar" resultado

    def __init__(self):
        self.number = 0
        self.pre_prompt = ""
        self.post_prompt = ""
        self.agent_type = ""
        self.agent_name = []
        self.task_type = ""
        self.task_name = []
        self.value = []
        self.coef_name = ""
        self.minimize = True


    # Función que devuelve el número de columnas de la tabla de valores de un ejercicio
    def get_column_num(self):
        return len(self.value[0])

    # Función que devuelve el número de filas de la tabla de valores de un ejercicio
    def get_row_num(self):
        return len(self.value)

    def generate_dummy_cells(self):
        extra_rows = self.get_row_num() - self.get_column_num()
        # Si hay más filas que columnas... (rectángulo vertical)
        if extra_rows > 0:
            # Para la fila de tareas
            for x in range(extra_rows):
                # Se le agrega un título de columna extra
                self.task_name.append("Dummy Task"+str(x+1))
            # Para cada fila de la tabla...
            for r in range(self.get_row_num()):
                # Por cada fila extra que esta tenga...
                for x in range(extra_rows):
                    # Se le agrega un cero al final
                    self.value[r].append(0)
        # Si hay más columnas que filas... (rectángulo horizontal)
        if extra_rows < 0:
            extra_cols = -1*extra_rows
            # Para la columna de agentes
            for x in range(extra_cols):
                # Se le agrega un título de fila extra
                self.agent_name.append("Dummy Agent "+str(x+1))
                # Se le agrega una fila vacía extra
                self.value.append([])
                # Y se llena esa fila extra con un 0 por columna
                for r in range(self.get_column_num()):
                    self.value[-1].append(0)







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