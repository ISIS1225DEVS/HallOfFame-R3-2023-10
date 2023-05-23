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
from tabulate import tabulate
from DISClib.ADT import list as lt
import datetime

csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = model.new_data_structs()
    return control


# Funciones para la carga de datos


def load_data(control, filename, memflag):
    """
    Carga los datos del reto
    """

    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=",")
    for accident in input_file:
        model.add_data(control, accident)

    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)

    size = model.data_size(control)
    primeros = lt.subList(control["accidents"], 1, 3)
    ultimos = lt.subList(control["accidents"], lt.size(control["accidents"]) - 2, 3)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return size, (delta_time, delta_memory), (primeros, ultimos)

    return size, delta_time, (primeros, ultimos)


# Funciones de ordenamiento


def sort(control):
    """
    Ordena los datos del modelo
    """
    # TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo


def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    # TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, fecha_inicio, fecha_final, memflag):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
    fecha_final = datetime.datetime.strptime(fecha_final, "%d/%m/%Y")
    req_1 = model.req_1(control, fecha_inicio.date(), fecha_final.date())

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_1, (delta_time, delta_memory)

    return req_1, delta_time


def req_2(control, hora_inicio, hora_final, anio, month, memflag):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    initial_hour = datetime.datetime.strptime(hora_inicio, "%H:%M")
    final_hour = datetime.datetime.strptime(hora_final, "%H:%M")
    req_2 = model.req_2(control, initial_hour, final_hour, anio, month)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_2, (delta_time, delta_memory)

    return req_2, delta_time


def req_3(control, acc_class, via, memflag):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    req_3 = model.req_3(control, acc_class, via)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_3, (delta_time, delta_memory)

    return req_3, delta_time


def req_4(control, fecha_inicio, fecha_final, gravedad, memflag):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
    fecha_final = datetime.datetime.strptime(fecha_final, "%d/%m/%Y")
    req_4 = model.req_4(control, fecha_inicio.date(), fecha_final.date(), gravedad)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_4, (delta_time, delta_memory)

    return req_4, delta_time


def req_5(control, anio, month, localidad, memflag):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    req_5 = model.req_5(control, anio, month, localidad)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_5, (delta_time, delta_memory)

    return req_5, delta_time


def req_6(control, anio, month, lat, lon, radio, can_n, memflag):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    req_6 = model.req_6(control, anio, month, lat, lon, radio, can_n)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_6, (delta_time, delta_memory)

    return req_6, delta_time


def req_7(control, anio, month, memflag):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    req_6 = model.req_7(control, anio, month)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_6, (delta_time, delta_memory)

    return req_6, delta_time


def req_8(control, fecha_inicio, fecha_final, clase, memflag):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_time = getTime()

    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()

    fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
    fecha_final = datetime.datetime.strptime(fecha_final, "%d/%m/%Y")
    req_8 = model.req_8(control, fecha_inicio.date(), fecha_final.date(), clase)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)

    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        delta_memory = deltaMemory(stop_memory, start_memory)
        return req_8, (delta_time, delta_memory)

    return req_8, delta_time


# Funciones para medir tiempos de ejecucion


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter() * 1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
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
    delta_memory = delta_memory / 1024.0
    return delta_memory


def transform_datos_version_carga(lista):
    print_result = []
    for i in lt.iterator(lista):
        j = dict(i)
        print_result.append(j)
    retorno = []
    pre_return = []
    for i in range(3):
        pre_return = [
            print_result[i]["CODIGO_ACCIDENTE"],
            print_result[i]["FECHA_HORA_ACC"],
            print_result[i]["LOCALIDAD"],
            print_result[i]["DIRECCION"],
            print_result[i]["GRAVEDAD"],
            print_result[i]["CLASE_ACC"],
            print_result[i]["LATITUD"],
            print_result[i]["LONGITUD"],
        ]
        retorno.append(pre_return)
    headers = [
        "CODIGO_ACCIDENTE",
        "FECHA_HORA_ACC",
        "LOCALIDAD",
        "DIRECCION",
        "GRAVEDAD",
        "CLASE_ACC",
        "LATITUD",
        "LONGITUD",
    ]
    return retorno, headers


def transform_datos_version_req_5(lista):
    print_result = []
    for i in lt.iterator(lista):
        j = dict(i)
        print_result.append(j)
    retorno = []
    pre_return = []
    for i in range(lt.size(lista)):
        pre_return = [
            print_result[i]["CODIGO_ACCIDENTE"],
            print_result[i]["FECHA_HORA_ACC"],
            print_result[i]["DIA_OCURRENCIA_ACC"],
            print_result[i]["DIRECCION"],
            print_result[i]["GRAVEDAD"],
            print_result[i]["CLASE_ACC"],
            print_result[i]["LATITUD"],
            print_result[i]["LONGITUD"],
        ]
        retorno.append(pre_return)
    headers = [
        "CODIGO_ACCIDENTE",
        "FECHA_HORA_ACC",
        "DIA_OCURRENCIA_ACC",
        "DIRECCION",
        "GRAVEDAD",
        "CLASE_ACC",
        "LATITUD",
        "LONGITUD",
    ]
    return retorno, headers


def transform_datos_version_req_1y6(lista):
    print_result = []
    for i in lt.iterator(lista):
        j = dict(i)
        print_result.append(j)
    retorno = []
    pre_return = []
    for i in range(lt.size(lista)):
        pre_return = [
            print_result[i]["CODIGO_ACCIDENTE"],
            print_result[i]["FECHA_HORA_ACC"],
            print_result[i]["DIA_OCURRENCIA_ACC"],
            print_result[i]["LOCALIDAD"],
            print_result[i]["DIRECCION"],
            print_result[i]["GRAVEDAD"],
            print_result[i]["CLASE_ACC"],
            print_result[i]["LATITUD"],
            print_result[i]["LONGITUD"],
        ]
        retorno.append(pre_return)
    headers = [
        "CODIGO_ACCIDENTE",
        "FECHA_HORA_ACC",
        "DIA_OCURRENCIA_ACC",
        "LOCALIDAD",
        "DIRECCION",
        "GRAVEDAD",
        "CLASE_ACC",
        "LATITUD",
        "LONGITUD",
    ]
    return retorno, headers


def transform_datos_version_req_2(lista):
    print_result = []
    for i in lt.iterator(lista):
        j = dict(i)
        print_result.append(j)
    retorno = []
    pre_return = []
    for i in range(lt.size(lista)):
        pre_return = [
            print_result[i]["CODIGO_ACCIDENTE"],
            print_result[i]["HORA_OCURRENCIA_ACC"],
            print_result[i]["FECHA_OCURRENCIA_ACC"],
            print_result[i]["DIA_OCURRENCIA_ACC"],
            print_result[i]["LOCALIDAD"],
            print_result[i]["DIRECCION"],
            print_result[i]["GRAVEDAD"],
            print_result[i]["CLASE_ACC"],
            print_result[i]["LATITUD"],
            print_result[i]["LONGITUD"],
        ]
        retorno.append(pre_return)
    headers = [
        "CODIGO_ACCIDENTE",
        "HORA_OCURRENCIA_ACC",
        "FECHA_OCURRENCIA_ACC",
        "DIA_OCURRENCIA_ACC",
        "LOCALIDAD",
        "DIRECCION",
        "GRAVEDAD",
        "CLASE_ACC",
        "LATITUD",
        "LONGITUD",
    ]
    return retorno, headers


def transform_datos_req4(lista):
    print_result = []
    for i in lt.iterator(lista):
        j = dict(i)
        print_result.append(j)
    retorno = []
    pre_return = []
    for i in range(lt.size(lista)):
        pre_return = [
            print_result[i]["CODIGO_ACCIDENTE"],
            print_result[i]["FECHA_HORA_ACC"],
            print_result[i]["DIA_OCURRENCIA_ACC"],
            print_result[i]["LOCALIDAD"],
            print_result[i]["DIRECCION"],
            print_result[i]["CLASE_ACC"],
            print_result[i]["LATITUD"],
            print_result[i]["LONGITUD"],
        ]
        retorno.append(pre_return)
    headers = [
        "CODIGO_ACCIDENTE",
        "FECHA_HORA_ACC",
        "DIA_OCURRENCIA_ACC",
        "LOCALIDAD",
        "DIRECCION",
        "CLASE_ACC",
        "LATITUD",
        "LONGITUD",
    ]
    return retorno, headers
