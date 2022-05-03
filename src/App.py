"""
Módulo APP
Este es el archivo raíz del proyecto, y es el que debe ejecutarse para correr el programa
"""

import Printer
import Utils
import Loader
import MainSolver

menu_option = 0
Printer.print_welcome_msj()
# Mientras no se seleccione la opción 1 ni la opción 2...
while menu_option < 3:
    # Imprime el menú principal en pantalla y espera la elección del usuario
    menu_option = Printer.print_main_menu()
    # Si la opción elegida es la 1 resuelve ejercicio de la guía...
    if menu_option == 1:
        # Borra la pantalla
        Printer.clear_console()
        # Se lee el número de ejercicio que se desea cargar
        print("Resolver un ejercicio de la práctica.\n")
        exercise_num = Utils.check_int_input_range("Ingrese el ejercicio a resolver", 1, 12)
        # Carga valores del ejercicio para calcular
        ex = Loader.load_known_exercise(exercise_num)
        # Se muestra el ejercicio elegido en pantalla
        Printer.print_exercise(ex)
        Printer.press_enter_to("iniciar la resolución")
        # Se controla que el formato del ejercicio sea correcto
        ex_data_ok = Utils.check_data_completeness(ex)
        if ex_data_ok:
            # Resuelve el ejercicio y presenta los resultados
            MainSolver.resolve(ex)
    # Si la opción elegida es la 2 resuelve ejercicio personalizado...
    elif menu_option == 2:
        # Borra la pantalla
        Printer.clear_console()
        # Se inicia la carga manual de datos
        print("Resolver un ejercicio ingresando datos manualmente.\n")
        ex = Loader.load_custom_exercise()
        Printer.clear_console()
        Printer.print_dynamic_table(ex)
        Printer.press_enter_to("iniciar la resolución")
        # Se controla que el formato del ejercicio sea correcto
        ex_data_ok = True
        if ex_data_ok:
            # Resuelve el ejercicio y presenta los resultados
            MainSolver.resolve(ex)
    # Si la opción elegida es la 3 solicita confirmación de salida...
    elif menu_option == 3:
        # Solicita confirmar la acción
        confirm_exit = Utils.confirm_action("salir")
        # Si cancela la opción...
        if not confirm_exit:
            # Vuelve al menú principal
            menu_option = 0
# Si confirma la acción de salir, el programa abandona el "while loop" y finaliza saludando al usuario
Printer.say_goodbye()
