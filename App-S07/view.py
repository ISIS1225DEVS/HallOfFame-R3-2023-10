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
from datetime import datetime
import matplotlib.pyplot as plt

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
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
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


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    tamaños = {"small":1, "5pct":2, "10pct":3, "20pct":4, "30pct":5, "50pct":6, "80pct":7, "large":8}
    print(tabulate([tamaños], headers="keys", maxheadercolwidths=6, maxcolwidths=6, tablefmt="double_grid"))
    try:
        t = int(input("Seleccione un tamaño de archivo un tamaño de archivo: "))
        if t not in list(tamaños.values()):
            raise ValueError
        size = list(tamaños.keys())[list(tamaños.values()).index(t)]
    except:
        print("El valor seleccionado no es válido, intente de nuevo.")
        raise 
    
    data_structs, time = controller.load_data(control, "datos_siniestralidad-{}.csv".format(size))
    print("Total de accidentes: ", controller.siniestrosSize(control) )
    
    print(tabulate([["Mostrando los 3 primeros registros de accidentes cargados"]], tablefmt="double_grid"))
    first, last = controller.siniFirstLastThree(control)
    print(filtro_load_data(first))
    print(tabulate([["Mostrando los 3 últimos registros de accidentes cargados"]], tablefmt="double_grid"))
    print(filtro_load_data(last))
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))

    

def print_req_1(control):
    
    initialDate = input("Fecha Inicial (YYYY\MM\DD): ")
    finalDate = input("Fecha Final (YYYY\MM\DD): ")
    num, data, time = controller.req_1(control, initialDate, finalDate)
    print(tabulate([["Hay {} accidentes registrados entre {} y {} ".format(num, initialDate, finalDate)]], tablefmt="double_grid"))
    print(filtro_R1(data))
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    año = input("Año: ")
    mes = (input("Mes: ")).upper()
    hora_i = input("Fecha Inicial (HH:MM:ss): ")
    hora_f = input("Fecha Final (HH:MM:ss): ")
    num, data, time = controller.req_2(control, año, mes, hora_i, hora_f)
    print(tabulate([["Hay {} accidentes registrados para el año {} en el mes de {} entre las {} y las {} ".format(num, año, mes, hora_i, hora_f)]], tablefmt="double_grid"))
    print(filtro_R2(data))
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    clase = (input("Clase: ")).upper()
    via = (input("Vía: ")).upper()
    num, data, time = controller.req_3(control, clase, via)
    print(tabulate([["Hay {} accidentes de la clase {}, ocurridos a lo largo de la vía {} y los 3 más recientes son:".format(num, clase, via)]], tablefmt="double_grid"))
    print(filtro_R3(data))
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el r1
    # resultado del requerimiento 4
    
    fecha_inicial = input("Ingrese la fecha inicial (YYYY/MM/D): ")
    fecha_final = input("Ingrese la fecha final (YYYY/MM/D): ")
    gravedad = input("Ingrese la gravedad que desea consultar: ")
    accidents, time = controller.req_4(control, fecha_inicial, fecha_final, gravedad)
    if accidents:
        print(filtro_r4(accidents))
    else:
        print("No fue posible realizar la búsqueda, por favor intente de nuevo")
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    localidad = input("Localidad en la que ocurrieron los accidentes: ").upper()
    mes = input("Mes en el que ocurrieron los accidentes: ").upper()
    año = input("Año entre 2015 y 2022: ")
    if año not in ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]:
        return
    if mes not in ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO","SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]:
        return
    lista, time = controller.req_5(control, año, mes, localidad)
    filtro_r5(lista)
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    año = (input("Año: "))
    mes = (input("Mes: ")).upper()
    latitud = (input("Latitud: "))
    longitud = (input("Longitud: "))
    radio = (input("Radio: "))
    rank = (input("Número de accidentes: "))
    num, data, time = controller.req_6(control, año, mes, latitud, longitud, radio, rank)
    print(tabulate([["Los {} accidentes más cercanos ocurridos en el año {} y mes {} en la latitud y longitud {}, {}, en un radio de {} KM son:".format(rank, año, mes, longitud, latitud, radio)]], tablefmt="double_grid"))
    print(filtro_R3(data))
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    anio = input("Ingrese el año: ")
    mes = input("Ingrese el mes: ")
    meses = {"ENERO":"01", "FEBRERO":"02", "MARZO":"03", "ABRIL":"04", "MAYO":"05", "JUNIO":"06",
             "JULIO":"07", "AGOSTO":"08", "SEPTIEMBRE":"09", "OCTUBRE":"10", "NOVIEMBRE":"11",
             "DICIEMBRE":"12"}
    try:
        if anio not in ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]:
            raise ValueError
        if mes.upper() not in meses:
            raise ValueError
    except:
        print("Datos no válidos")
        return
    acc_dia, time = controller.req_7(control, anio, meses[mes.upper()])
    print(tabulate([["Primeros y últimos accidentes por dia en el anio {} y mes {}".format(anio, mes)]], tablefmt="double_grid"))
    print(filtro_r7(acc_dia[0]))
    plt.bar(list(acc_dia[1].keys()), list(acc_dia[1].values()))
    plt.title("Número de accidentes por hora en el mes {} y el año {}".format(mes, anio))
    plt.xlabel("Horas del día")
    plt.ylabel("Número de accidentes")
    plt.show()
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    initialDate = input("Fecha Inicial (YYYY\MM\DD): ")
    finalDate = input("Fecha Final (YYYY\MM\DD): ")
    tipo = input("Tipo de accidente: ")
    time = controller.req_8(control, initialDate, finalDate, tipo)
    print(tabulate([["{:.3f}".format(time)]], tablefmt="double_grid"))

#Filtros con tabulate
def filtro_load_data(data):

    accidentes=[]
    for sinis in lt.iterator(data):
        
        accidente = {"Código del accidente":sinis["CODIGO_ACCIDENTE"], 
                "Fecha y hora del accidente": datetime.strptime(sinis["FECHA_HORA_ACC"], '%Y/%m/%d %H:%M:%S+%f'),
                "Localidad":sinis["LOCALIDAD"], 
                "Dirección":sinis["DIRECCION"], 
                "Gravedad":(sinis["GRAVEDAD"]), 
                "Clase de accidente":(sinis["CLASE_ACC"]), 
                "Latitud":(sinis["LATITUD"]), 
                "Longitud":(sinis["LONGITUD"])}
        accidentes.append(accidente)
    
    return tabulate(accidentes, headers="keys", maxheadercolwidths=15, maxcolwidths=15, tablefmt="grid")

def filtro_R1(data):
    accidentes=[]
    for siniestros in lt.iterator(data):
        for sinis in lt.iterator(siniestros["lstaccidentes"]):
            accidente = {"Código del accidente":sinis["CODIGO_ACCIDENTE"], 
                "Fecha y hora del accidente": datetime.strptime(sinis["FECHA_HORA_ACC"], '%Y/%m/%d %H:%M:%S+%f'),
                "Día del accidente":sinis["DIA_OCURRENCIA_ACC"],
                "Localidad":sinis["LOCALIDAD"], 
                "Dirección":sinis["DIRECCION"], 
                "Gravedad":(sinis["GRAVEDAD"]), 
                "Clase de accidente":(sinis["CLASE_ACC"]), 
                "Latitud":(sinis["LATITUD"]), 
                "Longitud":(sinis["LONGITUD"])}
            accidentes.append(accidente)
            
    accidentes.reverse()
            
    return tabulate(accidentes, headers="keys", maxheadercolwidths=15, maxcolwidths=15, tablefmt="grid")

def filtro_R2(data):
    accidentes=[]
    for siniestros in lt.iterator(data):
        for sinis in lt.iterator(siniestros["lstaccidentes"]):
            accidente = {"Código del accidente":sinis["CODIGO_ACCIDENTE"], 
                "Hora del accidente": datetime.strptime(sinis["HORA_OCURRENCIA_ACC"], '%H:%M:%S'),
                "Fecha del accidente": datetime.strptime(sinis["FECHA_OCURRENCIA_ACC"], '%Y/%m/%d'),
                "Día del accidente":sinis["DIA_OCURRENCIA_ACC"],
                "Localidad":sinis["LOCALIDAD"], 
                "Dirección":sinis["DIRECCION"], 
                "Gravedad":(sinis["GRAVEDAD"]), 
                "Clase de accidente":(sinis["CLASE_ACC"]), 
                "Latitud":(sinis["LATITUD"]), 
                "Longitud":(sinis["LONGITUD"])}
            accidentes.append(accidente)
            
    
            
    return tabulate(accidentes, headers="keys", maxheadercolwidths=15, maxcolwidths=15, tablefmt="grid")

def filtro_R3(data):
    accidentes=[]
    
    for sinis in lt.iterator(data):
        accidente = {"Código del accidente":sinis["CODIGO_ACCIDENTE"], 
                    "Fecha y hora del accidente": datetime.strptime(sinis["FECHA_HORA_ACC"], '%Y/%m/%d %H:%M:%S+%f'),
                    "Día del accidente":sinis["DIA_OCURRENCIA_ACC"],
                    "Localidad":sinis["LOCALIDAD"], 
                    "Dirección":sinis["DIRECCION"], 
                    "Gravedad":(sinis["GRAVEDAD"]), 
                    "Clase de accidente":(sinis["CLASE_ACC"]), 
                    "Latitud":(sinis["LATITUD"]), 
                    "Longitud":(sinis["LONGITUD"])}
        accidentes.append(accidente)
            
    accidentes.reverse()
            
    return tabulate(accidentes, headers="keys", maxheadercolwidths=15, maxcolwidths=15, tablefmt="grid")

def filtro_R6(data):
    accidentes=[]
    
    for sinis in lt.iterator(data):
        accidente = {"Código del accidente":sinis["CODIGO_ACCIDENTE"], 
                    "Fecha y hora del accidente": datetime.strptime(sinis["FECHA_HORA_ACC"], '%Y/%m/%d %H:%M:%S+%f'),
                    "Día del accidente":sinis["DIA_OCURRENCIA_ACC"],
                    "Localidad":sinis["LOCALIDAD"], 
                    "Dirección":sinis["DIRECCION"], 
                    "Gravedad":(sinis["GRAVEDAD"]), 
                    "Clase de accidente":(sinis["CLASE_ACC"]), 
                    "Latitud":(sinis["LATITUD"]), 
                    "Longitud":(sinis["LONGITUD"])}
        accidentes.append(accidente)
            
    accidentes.reverse()
            
    return tabulate(accidentes, headers="keys", maxheadercolwidths=15, maxcolwidths=15, tablefmt="grid")
    
def filtro_r4(accidents):
    table = []
    for i in lt.iterator(accidents):
        agregar = {"Código acc.":i["CODIGO_ACCIDENTE"], "Fecha-Hora acc.":i["FECHA_HORA_ACC"],
                   "Dia ocurrencia acc.":i["DIA_OCURRENCIA_ACC"], "Localidad":i["LOCALIDAD"],
                   "Dirección":i["DIRECCION"], "Clase acc.":i["CLASE_ACC"], "Latitud":i["LATITUD"],
                   "Longitud":i["LONGITUD"]}
        table.append(agregar)
        
    return tabulate(table, headers="keys", maxheadercolwidths=15, maxcolwidths=15, tablefmt="grid")
    
def filtro_r7(accidents):
    for dia in accidents:
        print(tabulate([["Accidentes más temprano y tarde para el día {}".format(dia)]], tablefmt="double_grid"))
        filtro = []
        for j in accidents[dia]:
            agregar = {"Código accidente":j["CODIGO_ACCIDENTE"], "Fecha y hora acc.":j["FECHA_HORA_ACC"],
                       "Dia accidente":j["DIA_OCURRENCIA_ACC"], "Localidad":j["LOCALIDAD"],
                       "Dirección":j["DIRECCION"], "Gravedad":j["GRAVEDAD"], "Clase acc.":j["CLASE_ACC"],
                       "Latitud":j["LATITUD"], "Longitud":j["LONGITUD"]}
            filtro.append(agregar)
        print(tabulate(filtro, headers="keys", maxheadercolwidths=6, maxcolwidths=6, tablefmt="grid"))
        
def filtro_r5(accidents):
    lista = []
    for i in lt.iterator(accidents):
        agregar = {"Código accidente":i["CODIGO_ACCIDENTE"], "Fecha y hora acc.":i["FECHA_HORA_ACC"],
                   "Día del accidente":i["DIA_OCURRENCIA_ACC"], "Dirección":i["DIRECCION"],
                   "Gravedad":i["GRAVEDAD"], "Clase accidente":i["CLASE_ACC"], "Latitud":i["LATITUD"],
                   "Longitud":i["LONGITUD"]}
        lista.append(agregar)
    print(tabulate(lista, headers="keys", maxheadercolwidths=6, maxcolwidths=6, tablefmt="grid"))
# Se crea el controlador asociado a la vista
control = None
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
                control = new_controller()
                print("Cargando información de los archivos ....\n")
                load_data(control)
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

