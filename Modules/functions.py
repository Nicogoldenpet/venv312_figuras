#Importando los módulos
import msvcrt
import platform
import os
from colorama import Fore,init, just_fix_windows_console
import Modules.clases as clases

init()
just_fix_windows_console()


def ingreso(): #Definiendo la función de ingreso
    print("---------------------------------------------------------------")
    print("|                                                             |")
    print("|                                                             |")
    print("|                 BIENVENIDO AL CALCULADOR DE                 |")
    print("|                ÁREAS Y PERIMETROS DE FIGURAS                |")
    print("|                                                             |")
    print("|            PARA INGRESAR PRESIONE CUALQUIER TECLA           |")
    print("|                                                             |")
    print("|                                                             |")
    print("---------------------------------------------------------------")
    msvcrt.getch()
    limpiar_pantalla()
    

def limpiar_pantalla(): #Definiendo la función para limpiar pantalla
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def resultados(datosrec, datoscir, datostri): #Definiendo la función para mostrar los resultados con los parámetros de las instancias
    limpiar_pantalla()
    print("---------------------------------------------------------------")
    print("|             LOS RESULTADOS SON LOS SIGUIENTES               |")
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    print("  RECTÁNGULO -- ÁREA:", datosrec.informe_arearectangulo(), "------- PERÍMETRO:", datosrec.informe_perirectangulo())
    print("  CÍRCULO -- ÁREA:", datoscir.informe_areacirculo(), "------- PERÍMETRO:", datoscir.informe_pericirculo())
    print("  TRIÁNGULO -- ÁREA:", datostri.informe_areatriangulo(), "------- PERÍMETRO:", datostri.informe_peritriangulo())
    print("---------------------------------------------------------------")


def respuesta(): #Definiendo la función para que el usuario ingrese una respuesta
    resp = None
    while resp != "S" and resp != "N":
        print("¿Desea ingresar nuevos datos? (El programa se reiniciará) (S/N): ")
        resp = msvcrt.getwch()
    return resp