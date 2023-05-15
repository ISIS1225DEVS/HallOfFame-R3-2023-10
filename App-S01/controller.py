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
import datetime

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control



# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    filename = 'datos_siniestralidad-large.csv'
    accfile = cf.data_dir + filename
    input_file = csv.DictReader(open(accfile, encoding="utf-8"),
                                delimiter=",")
    for data in input_file:
        model.add_data(control, data)
    return control


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def dataSize(control):
    """
    Numero de accidentes leidos
    """
    return model.data_size(control)

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def indexHeight(control):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(control)


def indexSize(control):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(control)

def req_1(control, initialDate, finalDate):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    initialDate = datetime.datetime.strptime(initialDate, '%Y/%m/%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y/%m/%d')
    total, lst = model.req_1(control, initialDate.date(),
                                  finalDate.date())
    return total, lst


def req_2(control, year, month, initialHour, finalHour):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    date = year + "/" + month
    dateMin = date + "/01"
    calMax = date + "/28"
    
    initialHour = datetime.datetime.strptime(initialHour, '%H:%M')
    finalHour = datetime.datetime.strptime(finalHour, '%H:%M')
    dateMin = datetime.datetime.strptime(dateMin, '%Y/%m/%d')
    calMax = datetime.datetime.strptime(calMax, '%Y/%m/%d')
    calMax = calMax.date()
    
    nextMonth = calMax + datetime.timedelta(days = 4)
    dateMax = nextMonth - datetime.timedelta(days = nextMonth.day)
    
    total, lst = model.req_2(control, 
                             initialHour.time(), 
                             finalHour.time(), 
                             dateMin.date(),
                             dateMax)
    return total, lst


def req_3(control, accidente, nombre_via):
    """
    Retorna el resultado del requerimiento 3
    """
    largo, lista = model.req_3(control, accidente, nombre_via)
    return largo, lista


def req_4(control,initialDate, finalDate,gravedad):
    """
    Retorna el resultado del requerimiento 4
    """
    
    initialDate = datetime.datetime.strptime(initialDate, '%Y/%m/%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y/%m/%d')
    size, sublist = model.req_4(control,initialDate.date(), finalDate.date(),gravedad)

    start_time = get_time()
    model.req_4(control,initialDate.date(), finalDate.date(),gravedad)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)

    return size, sublist, delta_t


def req_5(control, year, month, loc):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    date = year + "/" + month
    dateMin = date + "/01"
    calMax = date + "/28"
    
    dateMin = datetime.datetime.strptime(dateMin, '%Y/%m/%d')
    calMax = datetime.datetime.strptime(calMax, '%Y/%m/%d')
    calMax = calMax.date()
    
    nextMonth = calMax + datetime.timedelta(days = 4)
    dateMax = nextMonth - datetime.timedelta(days = nextMonth.day)
    
    total, acc = model.req_5(control, dateMin.date(), dateMax, loc)
    return total, acc

def req_6(control, year, month, coord, rad, num):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    date = year + "/" + month
    dateMin = date + "/01"
    calMax = date + "/28"
    
    dateMin = datetime.datetime.strptime(dateMin, '%Y/%m/%d')
    calMax = datetime.datetime.strptime(calMax, '%Y/%m/%d')
    calMax = calMax.date()
    
    nextMonth = calMax + datetime.timedelta(days = 4)
    dateMax = nextMonth - datetime.timedelta(days = nextMonth.day)
    
    acc = model.req_6(control, dateMin.date(), dateMax, coord, rad, num)
    return acc


def req_7(control,mes, anio):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    primeros_ultimos, lista_total,size = model.req_7(control,mes, anio)

    start_time = get_time()
    model.req_7(control,mes,anio)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return primeros_ultimos, lista_total, size, delta_t


def req_8(control,initialDate, finalDate,clase):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    initialDate = datetime.datetime.strptime(initialDate, '%Y/%m/%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y/%m/%d')
    mapa, size = model.req_8(control,initialDate.date(), finalDate.date(),clase)
    return mapa, size


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
