"""
Módulo TABLE MERGER
Este módulo fue sacado de internet, y se utiliza para graficar tablas.
A diferencia de la popular librería "tabulate", este módulo permite fusionar celdas
Esta característica resulta útil para la correcta impresión en consola de la tabla de un ejercicio
"""


# Funciones auxiliares
# Checkea si una celda está dentro de la tabla
def _is_in_rowspan(y, x, rowspan):
    rowspan_value = 0
    row_i = 0
    for i in range(y):
        if (i, x) in rowspan.keys():
            rowspan_value = rowspan[(i, x)]
            row_i = i
    if rowspan_value - (y - row_i) > 0:
        return True
    else:
        return False


# Dibuja una celda "combinada" horizontalmente
def _write_cell(table, y, x, length, rowspan=None):
    if rowspan is None:
        rowspan = {}
    text = table[y][x]
    extra_spaces = ""
    if _is_in_rowspan(y, x, rowspan):
        text = "|"
        for i in range(length):  # according to column width
            text += " "
        print(text, end="")
    else:
        for i in range(length - len(text) - 2):
            extra_spaces += " "  # according to column width
        print(f"| {text} " + extra_spaces, end="")


# Dibuja una celda "combinada" verticalmente
def _write_colspan_cell(length, colspan_value):  # length argument refers to sum of column widths
    text = ""
    for i in range(length + colspan_value - 1):
        text += " "
    print(text, end="")


# Obtiene el ancho máximo de una columna
def _get_max_col_width(table, idx):  # find the longest cell in the column to set the column's width
    maxi = 0
    for row in table:
        if len(row) > idx:  # avoid index out of range error
            cur_len = len(row[idx]) + 2
            if maxi < cur_len:
                maxi = cur_len
    return maxi


# Obtiene el largo de la fila más larga
def _get_max_row_len(table):  # find longest row list (in terms of elements)
    maxi = 0
    for row in table:
        cur_len = len(row)
        if maxi < cur_len:
            maxi = cur_len
    return maxi


# Obtiene el ancho de cada una de las columnas
def _get_all_col_len(table):  # collect in a list the widths of each column
    widths = [_get_max_col_width(table, i) for i in range(_get_max_row_len(table))]
    return widths


# Obtiene el ancho de la fila más larga
def _get_max_row_width(table):  # set the width of the table
    maxi = 0
    for i in range(len(table)):
        cur_len = sum(_get_all_col_len(table)) + len(_get_all_col_len(table)) + 1  # "|" at borders and between cells
        if maxi < cur_len:
            maxi = cur_len
    return maxi


# Imprime un borde horizontal
def _draw_border(table, y, colspan=None, rowspan=None):
    if rowspan is None:
        rowspan = {}
    if colspan is None:
        colspan = {}
    col_widths = _get_all_col_len(table)
    length = _get_max_row_width(table)
    cell_w_count = 0
    cell_counter = 0
    for i in range(length):
        if _is_in_rowspan(y, cell_counter - 1, rowspan) and not (i == cell_w_count or i == length - 1):
            print(" ", end="")
        elif i == cell_w_count or i == length - 1:
            print("+", end="")
            if cell_counter != _get_max_row_len(table):
                cell_w_count += col_widths[cell_counter] + 1
                cell_counter += 1
        else:
            print("-", end="")
    print("")  # next line (end = "\n")


# Convierte todos los elementos de una tabla en texto
def _convert_table(table):  # turns all table elements into strings
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = str(table[i][j])
    return table


# Función principal que combina las funciones auxiliares y dibuja la tabla completa
def tabulate(tab, colspan=None, rowspan=None):
    if rowspan is None:
        rowspan = {}
    if colspan is None:
        colspan = {}
    table = _convert_table(tab)
    table_width = _get_max_row_width(table)
    col_widths = _get_all_col_len(table)
    for y, row in enumerate(table):
        _draw_border(table, y, colspan, rowspan)
        x = 0
        while x < len(row):  # altered for loop
            _write_cell(table, y, x, col_widths[x], rowspan)
            if (y, x) in colspan.keys():
                colspan_value = colspan[(y, x)]
                _write_colspan_cell(sum(col_widths[x + 1:x + colspan_value]), colspan_value)
                x += colspan_value - 1
            x += 1
        print("|")  # end table row
    _draw_border(table, _get_max_row_len(table) - 1)  # close bottom of table
