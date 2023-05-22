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

import calendar as c
import traceback
from tabulate import tabulate
import webbrowser
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import matplotlib.pyplot as plt
import time
  
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

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
    # TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def loadDataSteps():
    print("\n¿Qué archivo de datos desea cargar?")
    print("   datos_somoestralidad-")
    print("   1. small.csv")
    print("   2. 5%.csv")
    print("   3. 10%.csv")
    print("   4. 20%.csv")
    print("   5. 30%.csv")
    print("   6. 50%.csv")
    print("   7. 80%.csv")
    print("   8. large.csv\n")
    op = int(input())
    if op == 1:
        arch = "small.csv"
    elif op == 2:
        arch = "5pct.csv"
    elif op == 3:
        arch = "10pct.csv"
    elif op == 4:
        arch = "20pct.csv"
    elif op == 5:
        arch = "30pct.csv"
    elif op == 6:
        arch = "50pct.csv"
    elif op == 7:
        arch = "80pct.csv"
    else:
        arch = "large.csv"

    print("Usted eligió cargar el archivo datos_siniestralidad-" + arch)

    return ("datos_siniestralidad-" + arch)


def print_menu():
    print("\n{} Bienvenido Al Reto #3 del Grupo 1 {}\n".format("·"*15, "·"*15))
    print("» 1 « Elegir Tamaño de datos")
    print("» 2 « Cargar datos sobre accidentes de trafico")
    print("» 3 « (REQ. 1) Reportar todos los accidentes dado un rango de fechas")
    print("» 4 « (REQ. 2) Reportar todos los accidentes en un intervalo de horas del día para un mes y año")
    print("» 5 « (REQ. 3) Reportar los 3 accidentes más recientes de una clase particular ocurridos a lo largo de una vía")
    print("» 6 « (REQ. 4) Reportar los 5 accidentes más recientes dada una gravedad y un rango de fechas")
    print("» 7 « (REQ. 5) Reportar los 10 accidentes menos recientes ocurridos en un mes y año para una localidad de la ciudad")
    print("» 8 « (REQ. 6) Mostrar los N accidentes ocurridos dentro de una zona específica para un mes y una año")
    print("» 9 « (REQ. 7) Reportar los accidentes más temprano y más tarde para cada día de un mes y año dado, y graficar el histograma de frecuencias de accidentes por hora para ese mismo mes y año")
    print("» 10 « (REQ. 8) Visualizar todos los accidentes de una clase particular para un rango de fechas en el mapa de Bogotá")
    print("» 0 « Salir")


def load_data(control, filename):
    """
    Carga los datos
    """
    # TODO: Realizar la carga de datos
    return controller.load_model(control, filename)

def mes_a_numero(mes):
    mes = mes.lower()
    if mes == "enero":
        return "1"
    elif mes == "febrero":
        return "2"
    elif mes == "marzo":
        return "3"
    elif mes == "abril":
        return "4"
    elif mes == "mayo":
        return "5"
    elif mes == "junio":
        return "6"
    elif mes == "julio":
        return "7"
    elif mes == "agosto":
        return "8"
    elif mes == "septiembre":
        return "9"
    elif mes == "octubre":
        return "10"
    elif mes == "noviembre":
        return "11"
    elif mes == "diciembre":
        return "12"

def print_data(control):
    """
        Función que imprime un dato dado su ID
    """
    # TODO: Realizar la función para imprimir un elemento
    lista_tabulatei, lista_tabulatef, num_elementos = controller.print_data(
        control)
    headers = ["FECHA_OCURRENCIA_ACC",
               "FECHA_HORA_ACC",
               "LOCALIDAD",
               "DIRECCION",
               "GRAVEDAD",
               "CLASE_ACC",
               "LATITUD",
               "LONGITUD"]
    print("{} Informacion de los accidentes cargados {}".format("="*15, "="*15))
    print("Total de accidentes: " + str(num_elementos))
    print("Total de columnas cargadas: 15")
    print("\nLos primeros tres registros de accidentes cargados fueron:")
    print(tabulate(lista_tabulatei, headers, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=12))
    print("Los ultimos tres registros de accidentes cargados fueron:")
    print(tabulate(lista_tabulatef, headers, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=12))


def print_req_1(control, fi, ff):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    x = float(time.perf_counter()*1000)
    lista, size, altura_arbol, tamaño_arbol, min_llave, max_llave = controller.req_1(
        control, fi, ff)
    headers = ["CODIGO_ACCIDENTE",
               "DIA_OCURRENCIA_ACC",
               "DIRECCION",
               "GRAVEDAD",
               "CLASE_ACC",
               "LOCALIDAD",
               "FECHA_OCURRENCIA_ACC",
               "LATITUD",
               "LONGITUD"]
    print("Hay " + str(size) + " accidentes en desde " + fi + " hasta " + ff)
    print(tabulate(lista, headers, tablefmt="grid",
          maxcolwidths=14, maxheadercolwidths=12))
    print("La altura del arbol es: " + str(altura_arbol))
    print("El tamaño del arbol es: " + str(tamaño_arbol))
    print("La llave minima: " + str(min_llave))
    print("La llave maxima: " + str(max_llave))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

def print_req_2(control, fi, ff, hi, hf, mes, año):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    x = float(time.perf_counter()*1000)
    tabla_tabulate, size = controller.req_2(control, fi, ff, hi, hf)
    headers = ["CODIGO_ACCIDENTE",
               "HORA_OCURRENCIA_ACC",
               "FEHCA_OCURRENCIA_ACC",
               "DIA_OCURRENCIA_ACC",
               "LOCALIDAD",
               "DIRECCION",
               "GRAVEDAD",
               "CLASE_ACC",
               "LATITUD",
               "LONGITUD"]
    print("Hay " + str(size) + " accidentes en el intervalo de horas dado " + hi + " y " + hf + " en el año " + año + " y en el mes de "+ mes )
    print(tabulate(tabla_tabulate, headers, tablefmt="grid",
          maxcolwidths=14, maxheadercolwidths=12))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))


def print_req_3(control, clase, calle):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    x = float(time.perf_counter()*1000)
    lista, num_acc = controller.req_3(control, clase, calle)
    if lista != None:
        headers3 = ["CODIGO_ACCIDENTE",
                    "FECHA_HORA_ACC",
                    "DIA_OCURRENCIA_ACC",
                    "LOCALIDAD",
                    "DIRECCION",
                    "GRAVEDAD",
                    "CLASE_ACC",
                    "LATITUD",
                    "LONGITUD"]
        print("Hay " + str(num_acc) + " accidentes de la clase " +
            clase + " registrados en la via " + calle)
        print("Estos son los 3 accidentes mas recientes")
        print(tabulate(lista, headers3, tablefmt="grid",
            maxcolwidths=14, maxheadercolwidths=12))
    else: 
        print("No se encontraron accidentes de la clase " +
            clase + " registrados en la via " + calle)
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

def print_req_4(control, inicio, final, gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    x = float(time.perf_counter()*1000)
    
    lista, inicio, final, gravedad  = controller.req_4(control, inicio, final, gravedad)
    if lista != None:
        headers = ["CODIGO_ACCIDENTE",
                    "FECHA_HORA_ACC",
                    "DIA_OCURRENCIA_ACC",
                    "LOCALIDAD",
                    "DIRECCION",
                    "CLASE_ACC",
                    "LATITUD",
                    "LONGITUD"]
        print("\n{} Req No. 4 Inputs {}".format("="*15, "="*15))
        print("Reporte de los 5 accidentes '" + gravedad + "' más recientes entre '" + inicio + " 00:00:00' y '" + final + " 23:59:59'\n")
        print("{} Req No. 4 Answer {}".format("="*15, "="*15))
        print("Hay " + str(len(lista)) + " accidentes entre las fechas '" + inicio + " 00:00:00' y '" + final + " 23:59:59'\n")
        print(tabulate(lista[0:5], headers, tablefmt="grid",
            maxcolwidths=14, maxheadercolwidths=12))
    else: 
        print("No se encontro ningun accidente el cual cumpla los requisitos que colocaste")
    
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    loc = input('Localidad de Bogotá en la que ocurrieron accidentes: ')
    mes = int(input('Ingrese el mes del año que quiere consultar [1-12]: '))
    anio = int(input('Ingrese el año que quiere consultar [2015-2022]: '))
    x = float(time.perf_counter()*1000)
    l_tab, tot_ac = controller.req_5(control,loc,mes,anio)
    print('Hay {} accidentes ocurridos en la localidad {} en el mes {} del año {}'.format(tot_ac,loc,mes,anio))
    print('Estos son los {} accidentes menos recientes:'.format(len(l_tab)))
    print(tabulate(l_tab, headers="keys", tablefmt="grid", maxcolwidths=18, maxheadercolwidths=18))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

def print_req_6(control, fi, ff, lat, lon, radio, nacc, año, mes):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    x = float(time.perf_counter()*1000)
    lista = controller.req_6(control, fi, ff, lat, lon, radio, nacc)
    headers6 = ["CODIGO_ACCIDENTE",
                "DIA_OCURRENCIA_ACC",
                "DIRECCION",
                "GRAVEDAD",
                "CLASE_ACC",
                "FECHA_HORA_ACC",
                "LATITUD",
                "LONGITUD"]
    print("Los " + str(nacc) + " accidentes más cercanos al punto (" + str(lat) +
          ", " + str(lon) + ") dentro de un radio de " + str(radio) + " km para el mes de " + mes + " de " + año)
    print(tabulate(lista, headers6, tablefmt="grid",maxcolwidths=14, maxheadercolwidths=12))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    mes = int(input('Ingrese el mes del año que quiere consultar [1-12]: '))
    anio = int(input('Ingrese el año que quiere consultar [2015-2022]: '))
    x = float(time.perf_counter()*1000)
    ml_tab, l_graf = controller.req_7(control,mes,anio)
    print('Accidentes más tempranos y tardíos para el mes {} de {}'.format(mes,anio))
    for e in ml_tab:
        print('Accidentes del día {}'.format(e[0]['FECHA_HORA_ACC'][:10]))
        print(tabulate(e, headers="keys", tablefmt="grid", maxcolwidths=18, maxheadercolwidths=18))
    print('Construyendo e imprimiendo histograma de frecuencias de accidentes por hora para ese mismo mes y año...')
    plt.rcParams["figure.figsize"] = (9.5,6.5)
    plt.bar(l_graf[0],l_graf[1])
    plt.title('Frecuencia de {} accidentes por hora del día para el mes {} de {}'.format(sum(l_graf[1]),mes,anio))
    plt.xlabel('Hora del día')
    plt.ylabel('Número de accidentes')
    plt.xticks(rotation=90)
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))
    plt.show()
    

def print_req_8(control, fi, ff, clase):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    x = float(time.perf_counter()*1000)
    my_map, numacc = controller.req_8(control, fi, ff, clase)
    print("Hay " + str(numacc) + " registrados")
    my_map.save("map.html")
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))
    webbrowser.open("map.html")


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    # ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                arch = loadDataSteps()

            elif int(inputs) == 2:
                x = float(time.perf_counter()*1000)
                print("\nCargando información de los archivos ....\n")
                model = load_data(control, arch)
                print_data(model)
                y = float(time.perf_counter()*1000)
                print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

            elif int(inputs) == 3:
                print("¿Desde que fecha quiere consultar?")
                print("Porfavor pongala en el formato aaaa/mm/dd")
                fi = input("")
                print("Hasta que fecha quiere consultar?")
                print("Porfavor pongala en el formato aaaa/mm/dd")
                ff = input("")
                print_req_1(control, fi, ff)

            elif int(inputs) == 4:
                print("¿Que año quiere consultar?")
                año = input("")
                print("¿Que mes quiere consultar?")
                mes = input("")
                mesn = mes_a_numero(mes)
                di, df = c.monthrange(int(año), int(mesn))
                fi = año + "/" + mesn + "/" + "1" 
                ff = año + "/" + mesn + "/" + str(df)
                print("¿Desde que hora quiere consultar?")
                print("Porfavor pongala en formato HH:MM")
                hi = input("")
                print("¿Hasta que hora quiere consultar?")
                print("Porfavor pongala en formato HH:MM")
                hh = input("")
                print_req_2(control, fi, ff, hi, hh, mes, año)

            elif int(inputs) == 5:
                print("Porfavor ingrese la clase de accidente: ")
                clase = input("")
                print("Porfavor ingrese la calle que quiere buscar")
                calle = input("")
                print_req_3(control, clase, calle)

            elif int(inputs) == 6:
                print("\n¿Desde que fecha quiere consultar?")
                print("Porfavor pongala en el formato aaaa/mm/dd")
                inicio = input("")
                print("\n¿Hasta que fecha quiere consultar?")
                print("Porfavor pongala en el formato aaaa/mm/dd")
                final = input("")
                print("\nPorfavor ingrese la gravedad de los accidentes que desea buscar:")
                gravedad = input("").upper()
                print_req_4(control, inicio, final, gravedad)

            elif int(inputs) == 7:
                print_req_5(control)

            elif int(inputs) == 8:
                print("¿Que año quiere consultar?")
                año = input("")
                print("¿Que mes quiere consultar?")
                mes = input("")
                mesn = mes_a_numero(mes)
                di, df = c.monthrange(int(año), int(mesn))
                fi = año + "/" + mesn + "/" + "1"
                ff = año + "/" + mesn + "/" + str(df)

                print("¿Que latitud quiere consultar?")
                lat = float(input(""))
                print("¿Que longitud quiere consultar?")
                lon = float(input(""))

                print("¿Cual es el radio del area a consultar?")
                radio = float(input(""))
                print("¿Cuantos accidentes quiere consultar?")
                nacc = int(input(""))

                print_req_6(control, fi, ff, lat, lon, radio, nacc, año, mes)

            elif int(inputs) == 9:
                print_req_7(control)

            elif int(inputs) == 10:
                print("¿Desde que fecha quiere consultar?")
                print("Porfavor pongala en el formato aaaa/mm/dd")
                fi = input("")
                print("Hasta que fecha quiere consultar?")
                print("Porfavor pongala en el formato aaaa/mm/dd")
                ff = input("")
                print("Que tipo de accidente quiere consultar")
                clase = input("")
                print_req_8(control, fi, ff, clase)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa\n")

            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
