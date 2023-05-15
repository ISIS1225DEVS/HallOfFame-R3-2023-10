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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import matplotlib.pyplot as plt
import folium
import numpy as np

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
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Accidentes ocurridos dentro de un rango de fechas dado")
    print("3- Accidentes ocurridos dentro de horas del día para un mes y año dado")
    print("4- Los 3 accidentes más recientes de una clase particular ocurridos a lo largo de una via")
    print("5- Los 5 accidentes más recientes dada una gravedad y un rango de fechas")
    print("6- Los 5 accidentes más recientes dada una gravedad y un rango de fechas")
    print("7- Numero de accidentes ocurridos dentro de una zona específica para un mes y un año")
    print("8- Los accidentes más tempranos y más tarde para cada dia de un mes y año dado")
    print("9- Todos los accidentes de una clase particular para un rango de fechas en el mapa de Bogota")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data = controller.load_data(control)
    return data


def print_carga(control):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    lista = control['accidents']
    
    primeros = lt.subList(lista,1,3)
    ultimos = lt.subList(lista,lt.size(lista)-3,3)

    headers = ["Código del accidente", "Fecha y hora del accidente", "Localidad", 
               "Dirección", "Gravedad", "Clase de accidente", "Latitud",
               "Longitud"]
    
    table = []
    table_grande = []
    table_grande2 = []
    
    for elements in lt.iterator(primeros):
        table = [elements["CODIGO_ACCIDENTE"], 
                 elements["FECHA_HORA_ACC"], 
                 elements["LOCALIDAD"],
                 elements["DIRECCION"],
                 elements["GRAVEDAD"], 
                 elements["CLASE_ACC"], 
                 elements["LATITUD"], 
                 elements["LONGITUD"]]
        table_grande.append(table)

    for elements in lt.iterator(ultimos):
        table2 = [elements["CODIGO_ACCIDENTE"], 
                 elements["FECHA_HORA_ACC"], 
                 elements["LOCALIDAD"],
                 elements["DIRECCION"],
                 elements["GRAVEDAD"], 
                 elements["CLASE_ACC"], 
                 elements["LATITUD"], 
                 elements["LONGITUD"]]
        table_grande2.append(table2)


    print("Los primeros tres registros de accidentes cargados fueron: ")
    print("\n",tabulate(table_grande,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("Los ultimos tres registros de accidentes cargados fueron: ")
    print("\n",tabulate(table_grande2,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    

def print_req_1(control, initialDate, finalDate):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    total, lst = controller.req_1(control, initialDate, finalDate)
    headers = ["Código del accidente",
               "Fecha y hora del accidente",
               "Día del accidente",
               "Localidad",
               "Dirección",
               "Gravedad",
               "Clase de accidente",
               "Latitud",
               "Longitud"]
    acc = []
    
    for lstdate in lt.iterator(lst):
        table = [
            lstdate["CODIGO_ACCIDENTE"],
            lstdate["FECHA_HORA_ACC"],
            lstdate["DIA_OCURRENCIA_ACC"],
            lstdate["LOCALIDAD"],
            lstdate["DIRECCION"],
            lstdate["GRAVEDAD"],
            lstdate["CLASE_ACC"],
            lstdate["LATITUD"],
            lstdate["LONGITUD"]
            ]
        acc.append(table)
    
    print("\nHay", total, "accidentes registrados entre", initialDate, "y", finalDate)
    print(tabulate(acc,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")



def print_req_2(control, year, month, initialHour, finalHour):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    total, lst = controller.req_2(control, year, month, initialHour, finalHour)
    headers = ["Código del accidente",
               "Día del accidente",
               "Dirección",
               "Gravedad",
               "Clase de accidente",
               "Localidad",
               "Fecha y hora del accidente",
               "Latitud",
               "Longitud"]
    
    if month == "1":
        month = "ENERO"
    elif month == "2":
        month = "FEBRERO"
    elif month == "3":
        month = "MARZO"
    elif month == "4":
        month = "ABRIL"
    elif month == "5":
        month = "MAYO"
    elif month == "6":
        month = "JUNIO"
    elif month == "7":
        month = "JULIO"
    elif month == "8":
        month = "AGOSTO"
    elif month == "9":
        month = "SEPTIEMBRE"
    elif month == "10":
        month = "OCTUBRE"
    elif month == "11":
        month = "NOVIEMBRE"
    elif month == "12":
        month = "DICIEMBRE"

    acc = []

    for lstdate in lt.iterator(lst):
        table = [
            lstdate["CODIGO_ACCIDENTE"],
            lstdate["DIA_OCURRENCIA_ACC"],
            lstdate["DIRECCION"],
            lstdate["GRAVEDAD"],
            lstdate["CLASE_ACC"],
            lstdate["LOCALIDAD"],
            lstdate["FECHA_HORA_ACC"],
            lstdate["LATITUD"],
            lstdate["LONGITUD"]
            ]
        acc.append(table)
    
    
    print("\nHay", total, "accidentes registrados entre", initialHour, "y", finalHour, "de todos los dias del mes de " + month + " de " + year)
    print(tabulate(acc,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")


def print_req_3(control, accidente, nombre_via):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    largo, lista = controller.req_3(control, accidente, nombre_via)
    
    headers = ["Codigo del accidente",
            "Fecha_Hora_ACC", 
            "Dia de ocurrencia", 
            "Localidad",
            "Direccion", 
            "Gravedad", 
            "Clase", 
            "Latitud", 
            "Longitud"]

    tab = []
    tabla = []

    for elementos in lt.iterator(lista):
        tab = [elementos["CODIGO_ACCIDENTE"], 
            elementos["FECHA_HORA_ACC"],
            elementos["DIA_OCURRENCIA_ACC"], 
            elementos["LOCALIDAD"],
            elementos["DIRECCION"],  
            elementos["GRAVEDAD"], 
            elementos["CLASE_ACC"], 
            elementos["LATITUD"], 
            elementos["LONGITUD"]]
    
        if tab not in tabla:
            tabla.append(tab)

    print("\nHay " + str(largo) + " accidentes de la clase " + accidente + " en la via " + nombre_via)
    print("Estos son los 3 accidentes más recientes")
    print() 
    print(tabulate(tabla,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")


def print_req_4(control,initialDate, finalDate,gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    size, lista, time= controller.req_4(control,initialDate, finalDate,gravedad)

    table = []
    table_grande = []
    headers = ["Codigo del accidente", "Dia de ocurrencia", "Direccion", "Clase del accidente", 
               "Localidad","Fecha y hora del accidente", "Latitud", "Longitud"]
    if size != 0:
        for elements in lt.iterator(lista):
            table = [elements["CODIGO_ACCIDENTE"], elements["DIA_OCURRENCIA_ACC"], 
                 elements["DIRECCION"],elements["CLASE_ACC"],  elements["LOCALIDAD"],
                 elements["FECHA_HORA_ACC"], elements["LATITUD"], 
                 elements["LONGITUD"]]
        
            if table not in table_grande:
                table_grande.append(table)
    
        print("\nHay", size, " accidentes de gravedad " + gravedad + " entre ", initialDate, " y ", finalDate)
        print("\n",tabulate(table_grande,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    else:
        print("Ingrese datos validos.")

    print("Tiempo de ejecucion: " , time)
    


def print_req_5(control, year, month, loc):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    total, acc = controller.req_5(control, year, month, loc)
    headers = ["Código del accidente",
               "Fecha y hora del accidente",
               "Día del accidente",
               "Dirección",
               "Gravedad",
               "Clase de accidente",
               "Latitud",
               "Longitud"]
    
    if month == "1":
        month = "ENERO"
    elif month == "2":
        month = "FEBRERO"
    elif month == "3":
        month = "MARZO"
    elif month == "4":
        month = "ABRIL"
    elif month == "5":
        month = "MAYO"
    elif month == "6":
        month = "JUNIO"
    elif month == "7":
        month = "JULIO"
    elif month == "8":
        month = "AGOSTO"
    elif month == "9":
        month = "SEPTIEMBRE"
    elif month == "10":
        month = "OCTUBRE"
    elif month == "11":
        month = "NOVIEMBRE"
    elif month == "12":
        month = "DICIEMBRE"
    
    
    print("\nHay", total, "accidentes occurridos en la localidad", loc, "en el mes de " + month + " del año " + year)
    print("Estos son los accidentes menos recientes:")
    print(tabulate(acc,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")



def print_req_6(control, year, month, coord, rad, num):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    acc = controller.req_6(control, year, month, coord, rad, num)
    headers = ["Código del accidente",
               "Fecha y hora del accidente",
               "Día del accidente",
               "Localidad",
               "Dirección",
               "Gravedad",
               "Clase de accidente",
               "Latitud",
               "Longitud"]
    
    if month == "1":
        month = "ENERO"
    elif month == "2":
        month = "FEBRERO"
    elif month == "3":
        month = "MARZO"
    elif month == "4":
        month = "ABRIL"
    elif month == "5":
        month = "MAYO"
    elif month == "6":
        month = "JUNIO"
    elif month == "7":
        month = "JULIO"
    elif month == "8":
        month = "AGOSTO"
    elif month == "9":
        month = "SEPTIEMBRE"
    elif month == "10":
        month = "OCTUBRE"
    elif month == "11":
        month = "NOVIEMBRE"
    elif month == "12":
        month = "DICIEMBRE"
        
    print("\nLos", num, "accidentes mas cercanas al punto", coord, "dentro del radio de", rad, "km para el mes de " + month + " de " + year)
    print(tabulate(acc,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")


def print_req_7(control,mes, anio):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    lista_dias, lista_total, size, time= controller.req_7(control,mes, anio)

    headers = ["Codigo del accidente", "Dia de ocurrencia", "Direccion", "Clase del accidente", 
               "Localidad","Fecha y hora del accidente", "Latitud", "Longitud"]
    
    table_grande = []

    for elements in lt.iterator(lista_dias):
        table = []
        dia = elements['FECHA_OCURRENCIA_ACC']
        table = [elements["CODIGO_ACCIDENTE"], elements["DIA_OCURRENCIA_ACC"], 
                 elements["DIRECCION"],elements["CLASE_ACC"],  elements["LOCALIDAD"],
                 elements["FECHA_HORA_ACC"], elements["LATITUD"], 
                 elements["LONGITUD"]]
        if len(table_grande) <2:
            table_grande.append(table)

        if len(table_grande) == 2:
            print("Accidentes del dia " + dia)
            print(tabulate(table_grande,headers,tablefmt="fancy_grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
            table_grande = []
            

    
    

    times = []
    dic_times = {"0:00:00" : 0, "1:00:00" : 0, "2:00:00" :0, "3:00:00" :0, "4:00:00" :0, "5:00:00" :0,
                "6:00:00" :0, "7:00:00":0, "8:00:00":0, "9:00:00":0, "10:00:00":0, "11:00:00":0,
                "12:00:00":0,"13:00:00":0,"14:00:00":0,"15:00:00":0,"16:00:00":0,"17:00:00":0,
                "18:00:00":0,"19:00:00":0,"20:00:00":0,"21:00:00":0,"22:00:00":0,"23:00:00":0}

    
    for element in lt.iterator(lista_total):
        hora_element = element['HORA_OCURRENCIA_ACC'][0:2]
        if ":" in hora_element:
            hora_element = element['HORA_OCURRENCIA_ACC'][0]
        hora_element = hora_element + ":" + "00" + ":" + "00"
        
        times.append(hora_element)

        if hora_element not in dic_times:
            dic_times[hora_element] = 1
        else:
            dic_times[hora_element] +=1

    month = mes

    if month == "1":
        month = "ENERO"
    elif month == "2":
        month = "FEBRERO"
    elif month == "3":
        month = "MARZO"
    elif month == "4":
        month = "ABRIL"
    elif month == "5":
        month = "MAYO"
    elif month == "6":
        month = "JUNIO"
    elif month == "7":
        month = "JULIO"
    elif month == "8":
        month = "AGOSTO"
    elif month == "9":
        month = "SEPTIEMBRE"
    elif month == "10":
        month = "OCTUBRE"
    elif month == "11":
        month = "NOVIEMBRE"
    elif month == "12":
        month = "DICIEMBRE"

      
    plt.bar(dic_times.keys(),dic_times.values(),width=0.4)
    plt.xlabel("Hora del día")
    plt.ylabel("Número de accidentes")
    plt.title("Frecuencia de " + str(size) + " accidentes por hora del día\n Para el mes de " + month + " de " + anio)
    plt.xticks(rotation = 90)
    plt.xticks(size = 7)
    plt.show()

    print("Tiempo de ejecucion: " , time)


    

def print_req_8(control,initialDate, finalDate, clase):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    mapa, size = controller.req_8(control,initialDate, finalDate, clase)
    print("Hay " + str(size) + " accidentes reportados entre " + initialDate + " y " + finalDate)
    mapa.show_in_browser()

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_data(control)
                size = controller.dataSize(control)
                columnas = controller.indexHeight(control)
                print("----------------------------------------------")
                print("Informacion de los accidentes cargados: ")
                print("Total de accidentes: ", size)
                print("Total de columnas cargadas: ", columnas)
                print("----------------------------------------------\n")
                print_carga(control)
                
            elif int(inputs) == 2:
                elementos = controller.indexSize(control)
                altura = controller.indexHeight(control)
                initialDate = input("Fecha Inicial (YYYY/MM/DD): ")
                finalDate = input("Fecha Final (YYYY/MM/DD): ")
                print("\n---------------------Req No. 1 Answer-------------------------\n")
                print_req_1(control, initialDate, finalDate)

            elif int(inputs) == 3:
                year = input("Año de consulta (YYYY): ")
                month = input("Mes de consulta (MM): ")
                initialHour = input("Hora Inicial (HH:MM): ")
                finalHour = input("Hora Final (HH:MM): ")
                print("\n---------------------Req No. 2 Answer-------------------------\n")
                print_req_2(control, year, month, initialHour, finalHour)

            elif int(inputs) == 4:
                accidente = input("Clase de accidente: ")
                nombre_via = input("Nombre de la via: ")
                print("\n---------------------Req. 3-------------------------\n")
                print_req_3(control, accidente, nombre_via)

            elif int(inputs) == 5:
                initialDate = input("Fecha Inicial (YYYY/MM/DD): ")
                finalDate = input("Fecha Final (YYYY/MM/DD): ")
                gravedad = input("Gravedad del accidente: ")
                print("\n---------------------Req No. 4 Inputs-------------------------")
                print("Reporte de los 5 accidentes " + gravedad + " más recientes entre " + initialDate + " y " + finalDate + "\n")
                print("\n---------------------Req No. 4 Answer-------------------------")
                print_req_4(control,initialDate, finalDate,gravedad)

            elif int(inputs) == 6:
                year = input("Año de consulta (YYYY): ")
                month = input("Mes de consulta (MM): ")
                loc = input("Localidad: ")
                print("\n---------------------Req. 5-------------------------\n")
                print_req_5(control, year, month, loc)

            elif int(inputs) == 7:
                year = input("Año de consulta (YYYY): ")
                month = input("Mes de consulta (MM): ")
                latitude = input("Latitud: ")
                longitude = input("Longitud: ")
                rad = float(input("Radio del area (km): "))
                num = int(input("Numero de accidentes: "))
                coord = (float(latitude), float(longitude))
                print("\n---------------------Req No. 6 Answer-------------------------\n")
                print_req_6(control, year, month, coord, rad, num)

            elif int(inputs) == 8:
                anio = input("Año entre 2015 y 2022 (YYYY): ")
                mes = input("Mes (MM): ")
                month = mes
                if month == "1":
                    month = "ENERO"
                elif month == "2":
                    month = "FEBRERO"
                elif month == "3":
                    month = "MARZO"
                elif month == "4":
                    month = "ABRIL"
                elif month == "5":
                    month = "MAYO"
                elif month == "6":
                    month = "JUNIO"
                elif month == "7":
                    month = "JULIO"
                elif month == "8":
                    month = "AGOSTO"
                elif month == "9":
                    month = "SEPTIEMBRE"
                elif month == "10":
                    month = "OCTUBRE"
                elif month == "11":
                    month = "NOVIEMBRE"
                elif month == "12":
                    month = "DICIEMBRE"
        
                print("\n---------------------Req No. 7 Answer-------------------------\n")
                print("Accidentes más temprano y tardíos para el mes de " + month + " de " + anio)
                print_req_7(control,mes, anio)

            elif int(inputs) == 9:
                initialDate = input("Fecha Inicial (YYYY/MM/DD): ")
                finalDate = input("Fecha Final (YYYY/MM/DD): ")
                clase = input("Clase de accidente: ")
                print("\n---------------------Req No. 8 Answer-------------------------\n")
                print_req_8(control,initialDate, finalDate,clase)
                
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
