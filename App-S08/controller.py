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


def new_controller(tipo_mapa, factor_carga, tipo_arbol):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs(tipo_mapa, factor_carga, tipo_arbol)
    return control


# Funciones para la carga de datos

def load_data(control, filename, mem):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    Data_File = cf.data_dir + "siniestros/datos_siniestralidad"+str(filename)+".csv"
    input_file = csv.DictReader(open(Data_File, encoding="utf-8"), delimiter=",")
    for Data in input_file:
        model.add_data(data_structs, Data)
    model.sort(data_structs)
        
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return data_structs, delta_Time, delta_Memory

    else:
        return data_structs, delta_Time

def req_1(control, fecha1, fecha2, mem):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    req1 = model.req_1(data_structs, fecha1, fecha2)
        
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return req1, delta_Time, delta_Memory

    else:
        return req1, delta_Time


def req_2(control, year, mes, tiempo1, tiempo2, mem):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    req2 = model.req_2(data_structs, year, mes, tiempo1, tiempo2)
        
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return req2, delta_Time, delta_Memory

    else:
        return req2, delta_Time

def req_3(control, clase, nombre_via, mem):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    resultado = model.req_3(data_structs, clase, nombre_via)
    
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return resultado, delta_Time, delta_Memory

    else:
        return resultado, delta_Time

def req_4(control, fecha_inicial, fecha_final, gravedad, mem):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    resultado = model.req_4(data_structs, fecha_inicial, fecha_final, gravedad)
            
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return resultado, delta_Time, delta_Memory

    else:
        return resultado, delta_Time

def req_5(control, year, mes, localidad, mem):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    resultado = model.req_5(data_structs, year, mes, localidad)
        
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return resultado, delta_Time, delta_Memory

    else:
        return resultado, delta_Time

def req_6(control, year, mes, longitud, latitud, radio, top, mem):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    resultado = model.req_6(data_structs, year, mes, longitud, latitud, radio, top)
        
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return resultado, delta_Time, delta_Memory

    else:
        return resultado, delta_Time

def req_7(control, year, mes, escala, mem):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    if model.req_7(data_structs, year, mes, escala) != False:
        resultado = model.req_7(data_structs, year, mes, escala)[0]
        graf = model.req_7(data_structs, year, mes, escala)[1]
        str_size = model.req_7(data_structs, year, mes, escala)[2]
    else:
        resultado = False
        graf = []
        str_size = ""
    
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return resultado, graf, str_size, delta_Time, delta_Memory

    else:
        return resultado, graf, str_size, delta_Time

def req_8(control, fecha1, fecha2, clase, mem):
    """
    Retorna el resultado del requerimiento 8
    """
    start_time = get_time()
    
    if mem is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    data_structs = control
    req8 = model.req_8(data_structs, fecha1, fecha2, clase)
        
    stop_time = get_time()
    delta_Time = delta_time(start_time, stop_time)

    if mem is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        delta_Memory = delta_memory(stop_memory, start_memory)
        return req8, delta_Time, delta_Memory

    else:
        return req8, delta_Time

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
