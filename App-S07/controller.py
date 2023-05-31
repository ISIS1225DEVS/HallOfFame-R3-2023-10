"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc
from datetime import datetime
from tabulate import tabulate

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def new_controller():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    
    
    data_structs = model.new_data_structs()
    
    return data_structs


# Funciones para la carga de datos

def load_data(data_structs, siniestrosfile):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    siniestrosfile = cf.data_dir + siniestrosfile
    input_file = csv.DictReader(open(siniestrosfile, encoding="utf-8"),
                                delimiter=",")
    for siniestro in input_file:
        model.add_siniestro(data_structs, siniestro)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return data_structs, deltaTime

def siniestrosSize(data_structs):
    """
    Numero de crimenes leidos
    """
    return model.siniestrosSize(data_structs)

def siniFirstLastThree(data_structs):
    return model.siniFirstLastThree(data_structs)
    

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo
def req_1(data_structs, initialDate, finalDate):
    start_time = get_time()
    finalDate = finalDate + " 23:59:59"

    initialDate = datetime.strptime(initialDate, "%Y/%m/%d")
    finalDate = datetime.strptime(finalDate, "%Y/%m/%d %H:%M:%S")
    print("Fecha inicial", initialDate)
    print("Fecha final", finalDate)
    number, lst = model.req_1(data_structs, initialDate, finalDate)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return number, lst, deltaTime


def req_2(data_structs, año, mes, initialDate, finalDate):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = get_time()
    año = int(año)
    initialDate = datetime.strptime(initialDate, "%H:%M:%S")
    finalDate = datetime.strptime(finalDate, "%H:%M:%S")
    num, lst = model.req_2(data_structs, año, mes, initialDate, finalDate)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return(num, lst, deltaTime)


def req_3(data_structs, clase, via):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    num, lst = model.req_3(data_structs, clase, via)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return num, lst, deltaTime


def req_4(control, fi, ff, grav):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    ff = ff + " 23:59:59"
    try:
        fi = datetime.strptime(fi, "%Y/%m/%d")
        ff = datetime.strptime(ff, "%Y/%m/%d %H:%M:%S")
        grav = grav.upper()
        print(grav)
    except:
        return None
    database = control["fechas"]
    accidents = model.req_4(database, fi, ff, grav)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return accidents, deltaTime


def req_5(control, año, mes, localidad):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    accidentes = model.req_5(control, año, mes, localidad)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return accidentes, deltaTime

def req_6(data_structs, año, mes, latitud, longitud, radio, rank):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    num, lst = model.req_6(data_structs, int(año), mes, float(latitud), float(longitud), float(radio), int(rank))
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return num, lst, deltaTime


def req_7(control, anio, mes):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    inicio = anio+"/"+mes+"/"+"01"
    if int(mes) < 10:
        fin = anio+"/"+"0"+str(int(mes)+1)+"/"+"01"
    elif int(mes) >=10 and int(mes)<12:
        fin = anio+"/"+str(int(mes)+1)+"/"+"01"
    else:
        fin = str(int(anio)+1)+"/"+"01"+"/"+"01"
    fi = datetime.strptime(inicio, "%Y/%m/%d")
    ff = datetime.strptime(fin, "%Y/%m/%d")
    acc_dia = model.req_7(control["fechas"], fi, ff)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return acc_dia, deltaTime


def req_8(control, initialdate, finaldate, tipo):
    """
    Retorna el resultado del requerimiento 8
    """
    start_time = get_time()
    finalDate = finaldate + " 23:59:59"
    initialDate = datetime.strptime(initialdate, "%Y/%m/%d")
    finalDate = datetime.strptime(finalDate, "%Y/%m/%d %H:%M:%S")
    model.req_8(control, initialDate, finalDate, tipo)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return deltaTime


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

