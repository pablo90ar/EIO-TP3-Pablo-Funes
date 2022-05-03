"""
Módulo UTILS:
Este módulo almacena funciones utilizadas para validar información y ejecutar flujos de navegación
La información a validar proviene del ingreso por teclado del usuario.
"""

import Printer
from Exercise import Exercise


# Esta función consulta al usuario si está seguro de la acción que seleccionó y devuelve un booleano
def confirm_action(action: str = None):
    response = ""
    while response == "":
        if action:
            print("¿Confirma que desea " + action + "?")
        else:
            print("¿Confirma la acción?")
        response = input("\n[s]í / [n]o ")
        if (response is "s") or (response is "S"):
            return True
        elif (response is "n") or (response is "N"):
            return False
        else:
            print("Respuesta incorrecta.\nIngrese [s]í o [n]o para aceptar o cancelar la acción " + action + ".")
            response = ""


# Corrobora que un dato de teclado se encuentre dentro de un rango válido parametrizado
def check_int_input_range(var_name: str, min_value: int, max_value: int):
    msj = var_name + " entre " + str(min_value) + " y " + str(max_value) + ". "
    check_ok = False
    int_value = None
    while not check_ok:
        int_value = input(msj)
        if int_value.isdigit() and min_value <= int(int_value) <= max_value:
            check_ok = True
        else:
            print("Ingreso incorrecto.")
    return int(int_value)


# Corrobora que un dato de teclado sea entero y positivo
def check_equal_or_greater(msj: str, v_min: int = 0):
    check_ok = False
    int_value = None
    while not check_ok:
        int_value = input(msj)
        if int_value.isdigit() and int(int_value) >= v_min:
            check_ok = True
        else:
            print("Ingreso incorrecto. Ingrese Un número igual o mayor a " + str(v_min) + ".")
    return int(int_value)


# Comprueba si los datos de un ejercicio obedecen a una matriz rectangular
def check_data_completeness(ex: Exercise):
    rows = ex.get_row_num()
    row_len = []
    for row in range(rows):
        row_len.append(len(ex.value[row]))
    if all(x == row_len[0] for x in row_len):
        return True
    else:
        print("Error: La tabla está incompleta.")
        Printer.press_enter_to("volver al menu")
        return False


# Comprueba si los datos de un ejercicio obedecen a una matriz cuadrada
def check_square_data(ex: Exercise):
    rows = ex.get_row_num()
    cols = ex.get_column_num()
    if rows == cols:
        return True
    else:
        print("Error: La tabla no es cuadrada.")
        Printer.press_enter_to("volver al menu")
        return False
