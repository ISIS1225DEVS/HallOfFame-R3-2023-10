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

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {'model': None}
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    filename = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                delimiter=",")
    
    for accident in input_file:
        model.add_data(control["model"],accident)
    
    fal3 = model.first_and_last3(control["model"])   
    
    return control,fal3


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    
    req1=  model.req_1(control["model"], fecha_i, fecha_f)
    
    return req1

def req_2(control,horamin_initial,horamin_final,anio,mes):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req2 = model.req_2(control["model"],horamin_initial,horamin_final,anio,mes)
    return req2


def req_3(control,clase_accidente,nombre_via):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    size,req3 = model.req_3(control["model"],clase_accidente,nombre_via)
    return size,req3


def req_4(control,fecha_i,fecha_f,gravedad):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    
    size, req_4 = model.req_4(control["model"],fecha_i,fecha_f,gravedad)
    
    return size, req_4
def req_5(control, localidad, mes, año, Memory):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar ecl requerimiento 5
    start_t = get_time()

    # inicializa el proceso para medir memoria
    if Memory:
        tracemalloc.start()
        start_m = get_memory()
    
    req5 = model.req_5(control["model"], localidad, mes, año)
    # toma el tiempo al final del proceso
    stop_t = get_time()
    # calculando la diferencia en tiempo
    delta_t = delta_time(start_t, stop_t)
    
    # finaliza el proceso para medir memoria
    if Memory:
        stop_m = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_m = delta_memory(stop_m, start_m)
        # respuesta con los datos de tiempo y memoria
        return (delta_t, delta_m) , req5
    else:
        return (delta_t, ), req5

def req_6(control,topN,coordenadas,radio,mes,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    req6 = model.req_6(control["model"],topN,coordenadas,radio,mes,anio)
    return req6


def req_7(control, mes, año):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    
    hours, req7 = model.req_7(control["model"],mes, año)
    
    return hours, req7

def req_8(control, fecha_inicial, fecha_final, clase, Memory):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_t = get_time()

    # inicializa el proceso para medir memoria
    if Memory:
        tracemalloc.start()
        start_m = get_memory()
    
    req8 = model.req_8(control["model"], fecha_inicial, fecha_final, clase)
    # toma el tiempo al final del proceso
    stop_t = get_time()
    # calculando la diferencia en tiempo
    delta_t = delta_time(start_t, stop_t)
    
    # finaliza el proceso para medir memoria
    if Memory:
        stop_m = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_m = delta_memory(stop_m, start_m)
        # respuesta con los datos de tiempo y memoria
        return (delta_t, delta_m) , req8
    else:
        return (delta_t, ), req8



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
