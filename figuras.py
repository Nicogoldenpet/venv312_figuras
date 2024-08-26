#Importando los módulos y librería
import Modules.clases as clases
import Modules.functions as functions
from colorama import Fore,init, just_fix_windows_console

init()
just_fix_windows_console()

def main(): #Definiendo la función principal

    resp = "S"
    while resp == "S": #Si la respuesta del usuario es "Y" se repite el proceso

        functions.ingreso() #Ejecutando la función de ingreso

        #Definiendo las instancias de las clases
        datosrec = clases.Rectangulo("", "")
        datoscir = clases.Circulo("")
        datostri = clases.Triangulo("", "", "")
            
        ancho = None
        while ancho is None: #Si el aprendiz ingresa algo diferente a números, se repetirá hasta que ingrese bien
            try:
                print(Fore.WHITE)
                ancho = float(input("Ingrese el ancho del rectángulo: "))
            except ValueError:
                print(Fore.LIGHTRED_EX, "Solo se permiten números.")

        largo = None
        while largo is None: #Si el aprendiz ingresa algo diferente a números, se repetirá hasta que ingrese bien
            try:
                print(Fore.WHITE)
                largo = float(input("Ingrese el largo del rectángulo: "))
            except ValueError:
                print(Fore.LIGHTRED_EX, "Solo se permiten números.")

        #Integrando los datos a la clase
        datosrec.set_ancho(ancho)
        datosrec.set_largo(largo)

        functions.limpiar_pantalla()
        print("A continuación seguiremos con el círculo")

        radio = None
        while radio is None: #Si el aprendiz ingresa algo diferente a números, se repetirá hasta que ingrese bien
            try:
                print(Fore.WHITE)
                radio = float(input("Ingrese el radio del círculo: "))
            except ValueError:
                print(Fore.LIGHTRED_EX, "Solo se permiten números.")

        datoscir.set_radio(radio) #Integrando los datos a la clase

        functions.limpiar_pantalla()
        print("Por último, seguiremos con el triángulo")

        cateto_a = None
        while cateto_a is None: #Si el aprendiz ingresa algo diferente a números, se repetirá hasta que ingrese bien
            try:
                print(Fore.WHITE)
                cateto_a = float(input("Ingrese el cateto A del triángulo: "))
            except ValueError:
                print(Fore.LIGHTRED_EX, "Solo se permiten números.")

        cateto_b = None
        while cateto_b is None: #Si el aprendiz ingresa algo diferente a números, se repetirá hasta que ingrese bien
            try:
                print(Fore.WHITE)
                cateto_b = float(input("Ingrese el cateto B del triángulo: "))
            except ValueError:
                print(Fore.LIGHTRED_EX, "Solo se permiten números.")

        cateto_c = None
        while cateto_c is None: #Si el aprendiz ingresa algo diferente a números, se repetirá hasta que ingrese bien
            try:
                print(Fore.WHITE)
                cateto_c = float(input("Ingrese el cateto C del triángulo: "))
            except ValueError:
                print(Fore.LIGHTRED_EX, "Solo se permiten números.")

        #Integrando los datos a la clase
        datostri.set_cateto_a(cateto_a)
        datostri.set_cateto_b(cateto_b)
        datostri.set_cateto_c(cateto_c)
                
        functions.resultados(datosrec, datoscir, datostri) #Ejecutando el resultado final con los parámetros de las instancias

        resp=functions.respuesta() #Ejecutando la función para preguntar al usuario si desea repetir
    
if __name__ == "__main__": #Ejecutando la función principal
    main()