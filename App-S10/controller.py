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
    control={"model":None}
    control["model"]=model.NewAnalyzer()
    return control

# Funciones para la carga de datos

def load_data(control, filename, memflag=True):
    """
    Carga los datos del reto
    """
    start_time=get_time()
    
    if memflag is True:
        tracemalloc.start()
        start_memory= get_memory()
        
    csv.field_size_limit(2147483647)
    file=csv.DictReader(open(filename, encoding="utf-8")) 
    
    for siniestro in file:
        
        model.add_data(control["model"],siniestro)
        
    lista=model.primerosyultimos(control["model"])
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    if memflag is True:
        stop_memory=get_memory()
        tracemalloc.stop()
        memory= delta_memory(stop_memory, start_memory)
        return tiempo, memory,lista      
    
    else:
        return tiempo,lista
        


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


def req_1(control,fechainicial,fechafinal):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time=get_time()
    respuesta=model.req_1(control["model"],fechainicial,fechafinal)
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    return respuesta,tiempo

def req_2(control,año,mes,hora1,hora2):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time=get_time()
    respuesta=model.req_2(control["model"],año,mes,hora1,hora2)
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    return respuesta,tiempo

def req_3(control,clase,via):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time=get_time()
    req3=model.req_3(control["model"],clase,via)
    stop_time=get_time()
    tiempo=delta_time(start_time, stop_time)
    return req3, tiempo


def req_4(control, gravedad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time=get_time()
    req4=model.req_4(control["model"],gravedad,fecha_inicial,fecha_final)
    stop_time=get_time()
    tiempo=delta_time(start_time, stop_time)
    return req4, tiempo


def req_5(control,año,mes,localidad):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time=get_time()
    respuesta=model.req_5(control["model"],año,mes,localidad)
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    return respuesta,tiempo

def req_6(control,año,mes,latitud,longitud,radio,Topn):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time=get_time()
    respuesta=model.req_6(control["model"],año,mes,latitud,longitud,radio,Topn)
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    return respuesta,tiempo


def req_7(control,año,mes):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time=get_time()
    respuesta=model.req_7(control["model"],año,mes)
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    return respuesta,tiempo



def req_8(control,Clase,FechIn,FechaFi):
    """
    Retorna el resultado del requerimiento 8
    """
    start_time=get_time()
    Resp=model.req_8(control["model"],Clase,FechIn,FechaFi)
    stop_time=get_time()
    tiempo= delta_time(start_time, stop_time)  
    return Resp,tiempo


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
