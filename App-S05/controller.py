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

csv.field_size_limit(2147483647)

def new_controller():
    """
    Crea una instancia del modelo
    """
    # TODO: Llamar la función del modelo que crea las estructuras de datos
    return model.new_data_structs()


# Funciones para la carga de datos


def load_data(control, filename, memflag):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    DANEFile = cf.data_dir + archivo(filename)
    inputFile = csv.DictReader(open(DANEFile, encoding="utf-8"))
    for item in inputFile:
        model.add_data(control, item)
   
    datos = control
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime


# Funciones de ordenamiento
def archivo(percentage):
    if int(percentage) == 1:
        archivo ="siniestros\datos_siniestralidad-5pct.csv"
    elif int(percentage) == 2:
        archivo = "siniestros\datos_siniestralidad-10pct.csv"
    elif int(percentage) == 3:
        archivo = "siniestros\datos_siniestralidad-20pct.csv"
    elif int(percentage) == 4:
        archivo = "siniestros\datos_siniestralidad-30pct.csv"
    elif int(percentage) == 5:
        archivo = "siniestros\datos_siniestralidad-50pct.csv"
    elif int(percentage) == 6:
        archivo = "siniestros\datos_siniestralidad-80pct.csv"
    elif int(percentage) == 7:
        archivo = "siniestros\datos_siniestralidad-large.csv"
    elif int(percentage) == 8:
        archivo = "siniestros\datos_siniestralidad-small.csv"
    return archivo


def req_1(control, fechaInicia, fechaFinal, memflag):
    """
    Retorna el resultado del requerimiento 1
    """
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    datos = model.req_1(control, fechaInicia, fechaFinal)
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime

def req_2(data_structs, mes, año, horaInicio, HoraFinal, memflag):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    meses = {"enero": "01","febrero": "02","marzo": "03","abril": "04","mayo": 
            "05","junio": "06","julio": "07","agosto": "08","septiembre": "09",
            "octubre": "10","noviembre": "11","diciembre": "12"}
    mes = meses[mes.lower()]
    datos = model.req_2(data_structs, mes, año, horaInicio, HoraFinal)
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime
    


def req_3(data_structs, direccion, accidente, memflag):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    datos = model.req_3(data_structs, direccion, accidente)
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime


def req_4(data_structs, fechaInicia, fechaFinal, gravedad, memflag):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    datos = model.req_4(data_structs, fechaInicia, fechaFinal, gravedad)
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime


def req_5(data_structs, mes, año, localidad, memflag):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
    meses = {"enero": "01","febrero": "02","marzo": "03","abril": "04","mayo": 
            "05","junio": "06","julio": "07","agosto": "08","septiembre": "09",
            "octubre": "10","noviembre": "11","diciembre": "12"}
    mes = meses[mes.lower()]
    
    datos= model.req_5(data_structs, mes, año, localidad)
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime

def req_6(data_structs, año, mes, cordenadas, Radio, top, memflag):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
    
    meses = {"enero": "01","febrero": "02","marzo": "03","abril": "04","mayo": 
            "05","junio": "06","julio": "07","agosto": "08","septiembre": "09",
            "octubre": "10","noviembre": "11","diciembre": "12"}
    mes = meses[mes.lower()]
    
    datos= model.req_6(data_structs, año, mes, cordenadas, Radio, top)
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime

def req_7(controler, año, mes, memflag):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    meses = {"enero": "01","febrero": "02","marzo": "03","abril": "04","mayo": 
            "05","junio": "06","julio": "07","agosto": "08","septiembre": "09",
            "octubre": "10","noviembre": "11","diciembre": "12"}
    mes = meses[mes.lower()]
    datos = model.req_7(controler, año, mes)
    stopTime = get_time()
    
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory
    return datos, deltaTime


def req_8(control, fechaInicia, fechaFinal, clase, memflag):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    startTime = get_time()
    
    if memflag is True:
        tracemalloc.start()
        startMemory = get_memory()
        
    datos = model.req_8(control, fechaInicia, fechaFinal, clase)
        
    stopTime = get_time()
    deltaTime = delta_time(stopTime, startTime)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, startMemory)
        return datos, deltaTime, deltaMemory

    # respuesta sin medir memoria
    return datos, deltaTime

# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(end, start):
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
