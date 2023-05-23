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
    control = {
        "model": None
    }
    control["model"]=model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO OK: Realizar la carga de 
    start = get_time()
    data=crear_lista_datos(filename)
    control["model"]= model.crear_datastructs_fecha(control["model"], data)
    control["model"] = model.crear_datastructs_casos(control["model"], data)
    control["model"] = model.agregar_datas(control["model"], data)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return control

def crear_lista_datos(filename):
    lista=model.new_list()
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for data in input_file:
        model.add_data(lista, data)
    
    return lista
# Funciones de ordenamiento

def sort(control, num):
    """
    Ordena los datos del modelo
    """
    control=model.sort(control, num)
    return control


# Funciones de consulta sobre el catálogo
def tres_prim(data_structs):
    data_structs=model.tres_prim(data_structs)
    return data_structs

def tres_ult(data_structs):
    data_structs=model.tres_ult(data_structs)
    return data_structs

def diez_prim(data_structs):
    data_structs=model.diez_prim(data_structs)
    return data_structs

def data_size(data_structs):
    size=model.data_size(data_structs)
    
    return size
    
def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, inicio, final):
    """
    Retorna el resultado del requerimiento 1
    """
    start = get_time()
    respuesta= model.req_1(control["model"], inicio, final)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return respuesta


def req_2(control, hora_inc, hora_fin, anio, mes):
    """
    Retorna el resultado del requerimiento 2
    """
    start = get_time()
    data_structs=model.req_2(control["model"], hora_inc, hora_fin, anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return data_structs


def req_3(control,clase_acc, via_name):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start = get_time()
    respuesta= model.req_3(control["model"],clase_acc, via_name)
    deltatime= delta_time(start,get_time())
    print(deltatime)
    return respuesta


def req_4(control, fecha_ini, fecha_fin, clase_acc):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start = get_time()
    respuesta, size= model.req_4(control["model"], fecha_ini, fecha_fin, clase_acc)
    deltatime= delta_time(start, get_time())
    print(deltatime)
    return respuesta, size


def req_5(control, localidad, anio, mes):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start = get_time()
    respuesta= model.req_5(control["model"], localidad, anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return respuesta

def req_6(control, top, lat, lon, rad, anio, mes):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start = get_time()
    respuesta= model.req_6(control["model"], top, float(lat), float(lon), rad, anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return respuesta


def req_7(control, anio, mes):
    """
    Retorna el resultado del requerimiento 7
    """
    start = get_time()
    queue, horas= model.req_7(control["model"], anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return queue, horas


def req_8(control, inicio, final, clase):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start = get_time()
    respuesta, color= model.req_8(control["model"], inicio, final, clase)
    end= get_time()
    deltatime = delta_time(start, end)
    print(deltatime)
    return respuesta, color

def req_1_redux(control, inicio, final):
    start = get_time()
    output= model.req_1(control["model"], inicio, final)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_1(control["model"], inicio, final)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory

def req_2_redux(control, hora_inc, hora_fin, anio, mes):
    start = get_time()
    output= model.req_2(control["model"], hora_inc, hora_fin, anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_2(control["model"], hora_inc, hora_fin, anio, mes)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory

def req_3_redux(control,clase_acc, via_name):
    start = get_time()
    output= model.req_3(control["model"],clase_acc, via_name)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_3(control["model"],clase_acc, via_name)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory

def req_4_redux(control, fecha_ini, fecha_fin, clase_acc):
    start = get_time()
    output= model.req_4(control["model"], fecha_ini, fecha_fin, clase_acc)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_4(control["model"], fecha_ini, fecha_fin, clase_acc)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory
    
def req_5_redux(control, localidad, anio, mes):
    start = get_time()
    output= model.req_5(control["model"], localidad, anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_5(control["model"], localidad, anio, mes)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory
    
def req_6_redux(control, top, lat, lon, rad, anio, mes):
    start = get_time()
    output= model.req_6(control["model"], top, lat, lon, rad, anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_6(control["model"], top, lat, lon, rad, anio, mes)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory
    
def req_7_redux(control, anio, mes):
    start = get_time()
    output= model.req_7(control["model"], anio, mes)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_7(control["model"], anio, mes)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory
    
def req_8_redux(control, inicio, final, clase):
    start = get_time()
    output= model.req_8(control["model"], inicio, final, clase)
    end= get_time()
    deltatime = delta_time(start, end)
    
    tracemalloc.start()
    start_memory = get_memory()
    output= model.req_8(control["model"], inicio, final, clase)
    stop_memory = get_memory()
    tracemalloc.stop()
    deltamemory = delta_memory(stop_memory, start_memory)
    
    return deltatime , deltamemory

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
