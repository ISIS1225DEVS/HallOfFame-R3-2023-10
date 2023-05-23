"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import traceback
from tabulate import tabulate
import config as cf
import sys
import controller
import DateTime
import webbrowser
import urllib.parse
import os
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import matplotlib.pyplot as plt

assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit * 10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
    Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print(
            "Tiempo [ms]: ",
            f"{answer[0]:.3f}",
            "||",
            "Memoria [kB]: ",
            f"{answer[1]:.3f}",
        )
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")


def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ("True", "true", "TRUE", "T", "t", "1", 1, True):
        return True
    else:
        return False


def print_menu():
    print("\nBienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, file_size, memflag):
    """
    Carga los datos
    """
    catalog = controller.load_data(
        control, "datos_siniestralidad-" + file_size + ".csv", memflag
    )
    return catalog


def print_data(control, id):
    """
    Función que imprime un dato dado su ID
    """
    # TODO: Realizar la función para imprimir un elemento
    pass


def print_carga_datos():
    global control
    global size
    control = new_controller()
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    print("Cargando información de los archivos ....\n")
    (tamaño, columns), answer, (primeros, ultimos) = load_data(control, size, mem)
    file_primeros = controller.transform_datos_version_carga(primeros)
    file_ultimos = controller.transform_datos_version_carga(ultimos)
    print("-------------------------------------------------------------")
    print("Informacion de los accidentes cargados:")
    print("Total de accidentes: " + str(tamaño))
    print("Total de columnas cargadas: " + str(columns))
    print("-------------------------------------------------------------\n")
    print("Los primeros tres registros de accidentes cargados fueron: \n")
    print(tabulate(file_primeros[0], headers=file_primeros[1], tablefmt="grid"))
    print("\nLos últimos tres registros de accidentes cargados fueron: \n")
    print(tabulate(file_ultimos[0], headers=file_ultimos[1], tablefmt="grid"))
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)


def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("=====IMPORTANTE: Recuerde ingresar la fecha en formato DD/MM/YY=====")
    fecha_inicio = input("Ingrese la fecha inicial del intervalo: ")
    fecha_final = input("Ingrese la fecha final del intervalo: ")
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    data, answer = controller.req_1(control, fecha_inicio, fecha_final, mem)
    cant_acc = lt.size(data)
    data_file = controller.transform_datos_version_req_1y6(data)
    print("---------------------------------------------------------------------")
    print(f"Hay {cant_acc} accidentes registrados entre {fecha_inicio} y {fecha_final}")
    print(
        tabulate(
            data_file[0],
            headers=data_file[1],
            tablefmt="grid",
            maxcolwidths=18,
            maxheadercolwidths=18,
        )
    )
    print(
        "\n=========================================================================================================================="
    )
    print(f"Hay {cant_acc} accidentes registrados entre {fecha_inicio} y {fecha_final}")
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)


def print_req_2(control):
    """
    Función que imprime la solución del Requerimiento 2 en consola
    """
    global meses
    # TODO: Imprimir el resultado del requerimiento 2
    print(
        "=====IMPORTANTE: Recuerde ingresar la hora en formato HH:MM y el mes en número====="
    )
    hora_inicio = input("Ingrese la hora inicial del intervalo: ")
    hora_final = input("Ingrese la hora final del intervalo: ")
    anio = input("Ingrese el año de consulta: ")
    month = int(input("Ingrese el mes de consulta: "))
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    data, answer = controller.req_2(control, hora_inicio, hora_final, anio, month, mem)
    cant_acc = lt.size(data)
    data_file = controller.transform_datos_version_req_2(data)
    print("---------------------------------------------------------------------")
    print(
        f"Hay {cant_acc} accidentes registrados entre {hora_inicio} y {hora_final} de todos los dias del mes de {meses[month]} de {anio}"
    )
    print(
        tabulate(
            data_file[0],
            headers=data_file[1],
            tablefmt="grid",
            maxcolwidths=18,
            maxheadercolwidths=18,
        )
    )
    print(
        "\n=========================================================================================================================="
    )
    print(
        f"Hay {cant_acc} accidentes registrados entre {hora_inicio} y {hora_final} de todos los dias del mes de {meses[month]} de {anio}"
    )
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)


def print_req_3(control):
    """
    Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    acc_class = input("Ingrese la clase del accidente: ")
    via = input("Ingrese la via: ")
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    (data, cant_acc), answer = controller.req_3(control, acc_class, via, mem)
    data_file = controller.transform_datos_version_req_1y6(data)
    print("---------------------------------------------------------------------")
    print(f"Hay {cant_acc} accidentes de clase {acc_class} registrados en la via {via}")
    print("Estos son los 3 accidentes mas recientes")
    print(
        tabulate(
            data_file[0],
            headers=data_file[1],
            tablefmt="grid",
            maxcolwidths=18,
            maxheadercolwidths=18,
        )
    )
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)


def print_req_4(control):
    """
    Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    fecha_inicio = input("Ingrese la fecha inicial del intervalo: ")
    fecha_final = input("Ingrese la fecha final del intervalo: ")
    gravedad = input("Ingrese la gravedad la cual quiere verificar: ")
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    (retorno, cant_acc), answer = controller.req_4(
        control, fecha_inicio, fecha_final, gravedad, mem
    )
    tabulatex = controller.transform_datos_req4(retorno)
    print("---------------------------------------------------------------------")
    print(
        f"Hay {cant_acc} accidentes de gravedad {gravedad} registrados entre {fecha_inicio} y {fecha_final}"
    )
    print("Estos son los 5 accidentes mas recientes")
    print(
        tabulate(
            tabulatex[0],
            headers=tabulatex[1],
            tablefmt="grid",
            maxcolwidths=18,
            maxheadercolwidths=18,
        )
    )
    printLoadDataAnswer(answer)


def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    """
    global meses
    # TODO: Imprimir el resultado del requerimiento 5
    print("=====IMPORTANTE: Recuerde ingresar el mes en número=====")
    anio = input("Ingrese el año de consulta: ")
    month = int(input("Ingrese el mes de consulta: "))
    localidad = input("Ingrese la localidad de consulta: ")
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    data, answer = controller.req_5(control, anio, month, localidad, mem)
    cant_acc = lt.size(data)
    data_file = controller.transform_datos_version_req_5(data)
    print("---------------------------------------------------------------------")
    print(
        f"Hay {cant_acc} accidentes ocurridos en la localidad de {localidad.upper()} en el mes {meses[month]} del año {anio}"
    )
    print("Estos son los 10 accidentes menos recientes: ")
    print(
        tabulate(
            data_file[0],
            headers=data_file[1],
            tablefmt="grid",
            maxcolwidths=18,
            maxheadercolwidths=18,
        )
    )
    print(
        "\n=========================================================================================================================="
    )
    print(
        f"Hay {cant_acc} accidentes ocurridos en la localidad de {localidad.upper()} en el mes {meses[month]} del año {anio}"
    )
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)


def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """
    global meses
    # TODO: Imprimir el resultado del requerimiento 6
    print("=====IMPORTANTE: Recuerde ingresar el mes en número=====")
    anio = input("Ingrese el año de consulta: ")
    month = int(input("Ingrese el mes de consulta: "))
    print("Ingrese las coordenadas del centro del area")
    lat = input("Latitud: ")
    lon = input("Longitud: ")
    radio = float(input("Ingrese el radio del area en Km: "))
    can_n = int(input("Ingrese el numero de accidentes que desea: "))
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    (data, flag), answer = controller.req_6(
        control, anio, month, lat, lon, radio, can_n, mem
    )
    cant_acc = lt.size(data)
    data_file = controller.transform_datos_version_req_1y6(data)
    print("---------------------------------------------------------------------")
    if flag:
        print(f"No existen {can_n} accidentes dentro del radio dado")
    if cant_acc == 1:
        print(
            f"El {cant_acc} accidente más cercanos al punto ({lat}, {lon}) dentro de un radio de {radio}km para el mes de {meses[month]} de {anio}"
        )
    else:
        print(
            f"Los {cant_acc} accidentes más cercanos al punto ({lat}, {lon}) dentro de un radio de {radio}km para el mes de {meses[month]} de {anio}"
        )
    print(
        tabulate(
            data_file[0],
            headers=data_file[1],
            tablefmt="grid",
            maxcolwidths=18,
            maxheadercolwidths=18,
        )
    )
    print(
        "\n=========================================================================================================================="
    )
    if flag:
        print(f"No existen {can_n} accidentes dentro del radio dado")
    if cant_acc == 1:
        print(
            f"El {cant_acc} accidente más cercanos al punto ({lat}, {lon}) dentro de un radio de {radio}km para el mes de {meses[month]} de {anio}"
        )
    else:
        print(
            f"Los {cant_acc} accidentes más cercanos al punto ({lat}, {lon}) dentro de un radio de {radio}km para el mes de {meses[month]} de {anio}"
        )
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)


def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola
    """
    global meses
    # TODO: Imprimir el resultado del requerimiento 7
    print("=====IMPORTANTE: Recuerde ingresar el mes en número=====")
    anio = input("Ingrese el año de consulta: ")
    month = int(input("Ingrese el mes de consulta: "))
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    (data, lt_matplot), answer = controller.req_7(control, anio, month, mem)
    print("---------------------------------------------------------------------")
    print(f"Accidente más temprano y tardío para el mes de {meses[month]} de {anio}")
    for i in lt.iterator(data):
        fecha = lt.firstElement(i)["FECHA_OCURRENCIA_ACC"]
        print(f"Accidentes del día {fecha}")
        data_file = controller.transform_datos_version_req_1y6(i)
        print(
            tabulate(
                data_file[0],
                headers=data_file[1],
                tablefmt="grid",
                maxcolwidths=18,
                maxheadercolwidths=18,
            )
        )
    print(
        "\n=========================================================================================================================="
    )
    print(f"Accidente más temprano y tardío para el mes de {meses[month]} de {anio}")
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)
    # Definir los datos de la gráfica
    nombres = [
        "0:00:00",
        "1:00:00",
        "2:00:00",
        "3:00:00",
        "4:00:00",
        "5:00:00",
        "6:00:00",
        "7:00:00",
        "8:00:00",
        "9:00:00",
        "10:00:00",
        "11:00:00",
        "12:00:00",
        "13:00:00",
        "14:00:00",
        "15:00:00",
        "16:00:00",
        "17:00:00",
        "18:00:00",
        "19:00:00",
        "20:00:00",
        "21:00:00",
        "22:00:00",
        "23:00:00",
    ]
    valores = lt_matplot

    # Crear la gráfica de barras
    plt.bar(nombres, valores)

    # Configurar las etiquetas del eje x y y
    plt.xlabel("Hora del día")
    plt.ylabel("Número de accidentes")
    plt.title(
        f"Frecuencia de accidentes por hora del día\nPara el mes de {meses[month]} de {anio}"
    )

    # Rotar las etiquetas del eje x en 90 grados
    plt.xticks(rotation=90)

    # Mostrar la gráfica
    plt.show()


def print_req_8(control):
    """
    Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print("=====IMPORTANTE: Recuerde ingresar la fecha en formato DD/MM/YY=====")
    fecha_inicio = input("Ingrese la fecha inicial del intervalo: ")
    fecha_final = input("Ingrese la fecha final del intervalo: ")
    clase = input("Ingrese la clase a analizar: ")
    print("Desea observar el uso de memoria? (True/False)")
    mem = input("Respuesta: ")
    mem = castBoolean(mem)
    (data, mapa), answer = controller.req_8(
        control, fecha_inicio, fecha_final, clase, mem
    )
    print(
        "\n=========================================================================================================================="
    )
    print(f"Hay {data} accidentes registrados entre {fecha_inicio} y {fecha_final}")
    print(
        "==========================================================================================================================\n"
    )
    printLoadDataAnswer(answer)
    mapa.save("mapa.html")

    filepath = os.path.abspath("mapa.html")
    webbrowser.open(filepath)


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    size = "20pct"
    meses = {
        1: "ENERO",
        2: "FEBRERO",
        3: "MARZO",
        4: "ABRIL",
        5: "MAYO",
        6: "JUNIO",
        7: "JULIO",
        8: "AGOSTO",
        9: "SEPTIEMBRE",
        10: "OCTUBRE",
        11: "NOVIEMBRE",
        12: "DICIEMBRE",
    }
    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        try:
            if int(inputs) == 1:
                print_carga_datos()

            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")

            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
