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
import sys
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
csv.field_size_limit(2147483647)

def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    return {'model': model.new_data_structs()}


# Funciones para la carga de datos

def load_data(control, filename, memflag):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    if memflag:
        tracemalloc.start()
        start_memory = get_memory()
    
    start_time = get_time()
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    idx = 0
    
    for accidente in input_file:
        idx += 1
        data = model.new_data(idx, accidente)
        model.add_data(control['model'], data)
    
    end_time = get_time()
    delta_time = float(end_time-start_time)
    acc_todos = control['model']['acc_fecha']
    lista_todos = control['model']['lista_todos']
    
    if memflag:
        end_memory = get_memory()
        tracemalloc.stop()
        delta_mem = delta_memory(end_memory, start_memory)
        return delta_time, model.tree_size(acc_todos), model.first_last_n_elems_list(lista_todos,3), delta_mem
    
    return delta_time, model.tree_size(acc_todos), model.first_last_n_elems_list(lista_todos,3)
    

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


def req_1(control, fecha_inicial, fecha_final, memflag):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    data_structs = control['model']
    if memflag:
        tracemalloc.start()
        start_memory = get_memory()
    
    start_time = get_time()

    result = model.req_1(data_structs, fecha_inicial, fecha_final)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
   
    if memflag:
        end_memory = get_memory()
        tracemalloc.stop()
        delta_memory = float(end_memory-start_memory)
        return result, delta_time, delta_memory
    
    return result, delta_time
    
    


def req_2(control, mes, anio, fecha_hora_inic, fecha_hora_final, memflag):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    data_structs = control['model']
    if memflag:
        tracemalloc.start()
        start_memory = get_memory()
    
    start_time = get_time()

    result = model.req_2(data_structs, mes, anio, fecha_hora_inic, fecha_hora_final)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
   
    if memflag:
        end_memory = get_memory()
        tracemalloc.stop()
        delta_memory = float(end_memory-start_memory)
        return result, delta_time, delta_memory
    
    return result, delta_time


def req_3(control, clase, via):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    data_structs = control['model']
    
    start_time = get_time()

    result = model.req_3(data_structs, clase, via)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
    
    return result, delta_time


def req_4(control,fecha_inicial,fecha_final,gravedad):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    data_structs= control["model"]
    
    start_time= get_time()
    
    result=model.req_4(data_structs, fecha_inicial,fecha_final,gravedad)
    
    end_time=get_time()
    delta_time= delta_time = float(end_time-start_time)
    
    return result,delta_time


def req_5(control, localidad, mes, anio):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    data_structs = control['model']
    
    start_time = get_time()

    result = model.req_5(data_structs, localidad, mes , anio)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
    
    return result, delta_time
    

def req_6(control, mes, anio, radio, latitud, longitud, numero_acc):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    data_structs = control['model']
    
    start_time = get_time()

    result = model.req_6(data_structs, mes, anio, radio, latitud, longitud, numero_acc)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
    
    return result, delta_time


def req_7(control, mes, anio):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    data_structs = control['model']
    
    start_time = get_time()

    result = model.req_7(data_structs, mes, anio)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
    
    return result, delta_time


def req_8(control, fecha_inicial, fecha_final, clase):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    data_structs = control['model']
    
    start_time = get_time()

    result = model.req_8(data_structs, fecha_inicial, fecha_final, clase)
    
    end_time = get_time()
    delta_time = delta_time = float(end_time-start_time)
    
    return result, delta_time


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
