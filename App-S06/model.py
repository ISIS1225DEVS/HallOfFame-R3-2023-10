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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
#a

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import datetime
import math as m


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    accidentes = {'acc_fecha': om.newMap(omaptype='RBT', comparefunction=compare_date_time_tuples),
                  'acc_clase': mp.newMap(numelements=8, maptype='PROBING', loadfactor=0.5),
                  'acc_gravedad': mp.newMap(numelements=8, maptype='PROBING', loadfactor=0.5),
                  'acc_localidad': mp.newMap(numelements=60, maptype='PROBING', loadfactor=0.5),
                  'acc_anio_mes': mp.newMap(numelements=100, maptype='PROBING', loadfactor=0.5),
                  'lista_todos': lt.newList('ARRAY_LIST')}
    return accidentes


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    data_date_time = data['FECHA_HORA_ACC']
    data_gravedad = data['GRAVEDAD']
    data_clase = data['CLASE_ACC']
    data_localidad = data['LOCALIDAD']
    data_anio = data['ANO_OCURRENCIA_ACC']
    data_mes = data['MES_OCURRENCIA_ACC']
    
    datastructs_anio_mes = data_structs['acc_anio_mes']
    datastructs_gravedad = data_structs['acc_gravedad']
    datastructs_clase = data_structs['acc_clase']
    datastructs_localidad = data_structs['acc_localidad']
    datastructs_lista = data_structs['lista_todos']
    
    tupla_anio_mes = (data_anio, data_mes)
    
    lt.addLast(datastructs_lista, data)
    
    datastructs_fecha = data_structs['acc_fecha']
    data_structs['acc_fecha'] = insert_to_tree(datastructs_fecha, data_date_time, data)
    
    
    agregar_a_filtro(datastructs_gravedad, data_gravedad, data)
    agregar_a_filtro(datastructs_clase, data_clase, data)
    agregar_a_filtro(datastructs_localidad, data_localidad, data)
    agregar_a_filtro(datastructs_anio_mes, tupla_anio_mes, data)
    
    

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    data = {'idx': id}
    for column in info.keys():
        if info[column].isnumeric():
            data[column] = int(info[column])
        else:
            data[column] = str(info[column])
    fecha = info['FECHA_OCURRENCIA_ACC'].split('/')
    hora = info['HORA_OCURRENCIA_ACC'].split(':')
    data['FECHA_HORA_ACC'] = datetime.datetime(year=int(fecha[0]), month=int(fecha[1]), day=int(fecha[2]), hour= int(hora[0]), minute=int(hora[1]), second = int(hora[2]))
    lista_calles = data['DIRECCION'].split('-')
    if len(lista_calles) >= 2:
        data['CALLE_ACC'] = lista_calles[0].strip()
        data['CARRERA_ACC'] = lista_calles[1].strip()
    else:
        data['CALLE_ACC'] = lista_calles[0].strip()
        data['CARRERA_ACC'] = '00'
    data['LATITUD'] = float(data['LATITUD'])
    data['LONGITUD'] = float(data['LONGITUD'])
    return data
            
        

        
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, fecha_final, fecha_inicial):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    data_structs_fecha = data_structs['acc_fecha']
    accidentes_rango = om.values(data_structs_fecha, fecha_inicial, fecha_final)
    lista_result = elems_rango_a_lista(accidentes_rango)
    size_accidentes = lt.size(lista_result)
    return size_accidentes, lista_result


def req_2(data_structs, mes, anio, hora_minutos_iniciales, hora_minutos_finales):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    tupla_anio_mes = (anio,mes)
    datastructs_anio_mes = data_structs['acc_anio_mes']
    data_anio_mes_k_v = mp.get(datastructs_anio_mes, tupla_anio_mes)
    data_anio_mes = me.getValue(data_anio_mes_k_v)
    
    tree_anio_mes = om.newMap(omaptype='RBT')
    
    for elem in lt.iterator(data_anio_mes):
        tree_anio_mes_aux = tree_anio_mes
        data_hora_str = elem['HORA_OCURRENCIA_ACC']
        data_hora_list = data_hora_str.split(':')
        data_hora = datetime.time(int(data_hora_list[0]), int(data_hora_list[1]), int(data_hora_list[2]))
        tree_anio_mes = insert_to_tree(tree_anio_mes_aux, data_hora, elem)
    
    data_entre_horas_aux = om.values(tree_anio_mes, hora_minutos_iniciales, hora_minutos_finales)
    data_entre_horas = elems_rango_a_lista(data_entre_horas_aux)
    
    
    size_accidentes = lt.size(data_entre_horas)
    
    return size_accidentes, data_entre_horas


def req_3(data_structs, clase, via):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    datastructs_clase = data_structs['acc_clase']
    data_clase_k_v = mp.get(datastructs_clase, clase)
    data_clase = me.getValue(data_clase_k_v)
    
    rbt_via = om.newMap('RBT')

    
    for elem in lt.iterator(data_clase):
        calle = elem['CALLE_ACC']
        carrera =  elem['CARRERA_ACC']
        if via in [calle,carrera]:
            rbt_via_aux = rbt_via
            rbt_via = om.put(rbt_via_aux, elem['FECHA_HORA_ACC'], elem)
    
    
    result = lt.newList('ARRAY_LIST')
    
    if om.isEmpty(rbt_via):
        return result
    
    for i in range(3):
        rbt_max_key = om.maxKey(rbt_via)
        rbt_max = me.getValue(om.get(rbt_via, rbt_max_key))
        rbt_via_aux = rbt_via
        rbt_via = om.deleteMax(rbt_via_aux)
        lt.addLast(result, rbt_max)
    return lt.size(data_clase), result

def req_4(data_structs,fecha_inicial,fecha_final,gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    data_structs_gravedad=data_structs["acc_gravedad"]
    data_gravedad_k_v=mp.get(data_structs_gravedad,gravedad)
    data_gravedad=me.getValue(data_gravedad_k_v)
    map_gravedad=om.newMap("RBT")
    
    for elem in lt.iterator(data_gravedad):
        data_fecha_str=elem["FECHA_OCURRENCIA_ACC"]
        data_fecha_list=data_fecha_str.split("/")
        fecha_elem= datetime.date(day=int(data_fecha_list[2]), month=int(data_fecha_list[1]),year=int(data_fecha_list[0]))
        if fecha_elem>=fecha_inicial and fecha_elem<=fecha_final:
            if not (om.contains(map_gravedad,data_fecha_str)):
                om.put(map_gravedad,data_fecha_str,lt.newList("ARRAY_LIST"))
                gravedad_fecha_list=om.get(map_gravedad,data_fecha_str)["value"]
                lt.addLast(gravedad_fecha_list,elem)
            else:
                gravedad_fecha_list=om.get(map_gravedad,data_fecha_str)["value"]
                lt.addLast(gravedad_fecha_list,elem)
                
    result_list=merg.sort(gravedad_fecha_list,sort_criteria_fecha)
    return result_list


def req_5(data_structs, localidad_s, mes, anio):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    tupla_anio_mes = (int(anio),mes)
    datastructs_anio_mes = data_structs['acc_anio_mes']
    data_anio_mes_k_v = mp.get(datastructs_anio_mes, tupla_anio_mes)
    data_anio_mes = me.getValue(data_anio_mes_k_v)
    
    map_localidad=om.newMap ("RBT")
    
    for elem in lt.iterator(data_anio_mes):
        localidad = elem['LOCALIDAD']
        if not (om.contains(map_localidad,localidad)):
            om.put(map_localidad,localidad,lt.newList("ARRAY_LIST"))
            localidad_list=om.get(map_localidad,localidad)["value"]
            lt.addLast(localidad_list,elem)
        else:
            localidad_list=om.get(map_localidad,localidad)["value"]
            lt.addLast(localidad_list,elem)
    
    result_list=om.get(map_localidad,localidad_s)['value'] 
    result_list=merg.sort(result_list,sort_criteria_fecha_inversa)
    return result_list
   
    

def req_6(data_structs, mes, anio, radio, latitud, longitud, numero_acc):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    tupla_anio_mes = (anio,mes)
    datastructs_anio_mes = data_structs['acc_anio_mes']
    data_anio_mes_k_v = mp.get(datastructs_anio_mes, tupla_anio_mes)
    data_anio_mes = me.getValue(data_anio_mes_k_v)
    
    latitud_rad = float(latitud) * (m.pi/180)
    longitud_rad = float(longitud) * (m.pi/180)
    
    RBT_distancia = om.newMap('RBT')
    
    for elem in lt.iterator(data_anio_mes):
        elem_latitud_deg = float(elem['LATITUD'])
        elem_longitud_deg = float(elem['LONGITUD'])
        elem_latitud_rad = elem_latitud_deg * (m.pi/180)
        elem_longitud_rad = elem_longitud_deg * (m.pi/180)
        distancia = calcular_distacia_rad(elem_latitud_rad, elem_longitud_rad, latitud_rad, longitud_rad)
        RBT_distancia_aux = RBT_distancia
        if distancia <= radio:
            RBT_distancia = om.put(RBT_distancia_aux, distancia, elem)
    
    list_result = lt.newList('ARRAY_LIST', cmpfunction= compare_id)
    
    if om.isEmpty(RBT_distancia):
        return list_result
    
    for i in range(numero_acc):
        tupla_elem_min_key = om.minKey(RBT_distancia)
        elem_min = me.getValue(om.get(RBT_distancia, tupla_elem_min_key))
        if not lt.isPresent(list_result, elem_min):
            distancia = tupla_elem_min_key
            elem_min['DISTANCIA'] = distancia
        lt.addLast(list_result, elem_min)
        RBT_distancia_aux = RBT_distancia
        if om.size(RBT_distancia) > 1:
            RBT_distancia = om.deleteMin(RBT_distancia_aux)

    return list_result
    
               
    
    

def req_7(data_structs, mes, anio):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    mapa_horas = om.newMap('BST')
        
    tupla_anio_mes = (anio,mes)
    datastructs_anio_mes = data_structs['acc_anio_mes']
    data_anio_mes_k_v = mp.get(datastructs_anio_mes, tupla_anio_mes)
    data_anio_mes = me.getValue(data_anio_mes_k_v)
    
    rbt_fechas = om.newMap(omaptype='RBT')
    
    for elem in lt.iterator(data_anio_mes):
        
        elem_hora_str = elem['HORA_OCURRENCIA_ACC']
        elem_hora_list = elem_hora_str.split(':')
        elem_hora = datetime.time(hour = int(elem_hora_list[0]), minute=int(elem_hora_list[1]), second = int(elem_hora_list[2]))
        
        elem_hora_interval = datetime.time(hour=int(elem_hora_list[0]), minute=0, second=0)
        
        if not om.contains(mapa_horas, str(elem_hora_interval)):
            mapa_horas_aux = mapa_horas
            mapa_horas = om.put(mapa_horas_aux, str(elem_hora_interval), 1)
        else:
            num_elems = me.getValue(om.get(mapa_horas, str(elem_hora_interval)))
            num_elems += 1
            mapa_horas_aux = mapa_horas
            mapa_horas = om.put(mapa_horas_aux, str(elem_hora_interval), num_elems)
        
        elem['HORA_ACC'] = elem_hora
        
        elem_fecha_str = elem['FECHA_OCURRENCIA_ACC']
        elem_fecha_list = elem_fecha_str.split('/')
        elem_fecha = datetime.date(year = int(elem_fecha_list[0]), month = int(elem_fecha_list[1]), day = int(elem_fecha_list[2]))
        elem['FECHA_ACC'] = elem_fecha
        
        if not om.contains(rbt_fechas, elem_fecha):
            min_heap_fecha_ = mpq.newMinPQ(compare_time_minpq)
            max_heap_fecha_ = mpq.newMinPQ(compare_time_maxpq)
            
            min_heap_fecha = mpq.insert(min_heap_fecha_,elem)
            max_heap_fecha = mpq.insert(max_heap_fecha_,elem)
            
            tupla_min_max_heap = (min_heap_fecha, max_heap_fecha)
            rbt_fechas_aux = rbt_fechas
            rbt_fechas = om.put(rbt_fechas_aux, elem_fecha, tupla_min_max_heap)
        else:
            key_value_fecha = om.get(rbt_fechas, elem_fecha)
            tupla_min_max_aux = me.getValue(key_value_fecha)
            min_heap = tupla_min_max_aux[0]
            max_heap = tupla_min_max_aux[1]
            
            min_heap_aux = min_heap
            max_heap_aux = max_heap
            
            min_heap = mpq.insert(min_heap_aux, elem)
            max_heap = mpq.insert(max_heap_aux,elem)
            
            tupla_min_max = (min_heap, max_heap)
            rbt_fechas_aux = rbt_fechas
            rbt_fechas = om.put(rbt_fechas_aux, elem_fecha, tupla_min_max)
        
    for h in range(0,24):
        time_interval = str(datetime.time(h, 0, 0))
        if not om.contains(mapa_horas, time_interval):
            mapa_horas_aux = mapa_horas
            mapa_horas = om.put(mapa_horas_aux, time_interval, 0)

    lista_result = lt.newList('ARRAY_LIST')
   
    for key in lt.iterator(om.keySet(rbt_fechas)):
        lista_fecha = lt.newList('ARRAY_LIST')
        min_max_heap_max_elem = me.getValue(mp.get(rbt_fechas, key))
        
        min_heap_max_elem = min_max_heap_max_elem[0]
        max_heap_max_elem = min_max_heap_max_elem[1]
        
        min_elem_heap = mpq.delMin(min_heap_max_elem)
        max_elem_heap = mpq.delMin(max_heap_max_elem)
        
        lt.addLast(lista_fecha, max_elem_heap)
        lt.addLast(lista_fecha, min_elem_heap)
        
        lt.addLast(lista_result, lista_fecha)
    return mapa_horas, lista_result
        
        
    
    
    
    


def req_8(data_structs, fecha_inical, fecha_final, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8

    hash_elems= mp.newMap(numelements=8, maptype='PROBING', loadfactor=0.5)
    
    contador = 0

    datastructs_clase = data_structs['acc_clase']
    data_clase_k_v = mp.get(datastructs_clase, clase)
    data_clase = me.getValue(data_clase_k_v)
    
    for elem in lt.iterator(data_clase):
        data_fecha_str = elem['FECHA_OCURRENCIA_ACC']
        data_fecha_list = data_fecha_str.split('/')
        fecha_elem = datetime.date(day = int(data_fecha_list[2]), month = int(data_fecha_list[1]), year = int(data_fecha_list[0]))
        accidente_gravedad = elem['GRAVEDAD']
        if fecha_elem>=fecha_inical and fecha_elem <= fecha_final:
            agregar_a_filtro(hash_elems, accidente_gravedad, elem)
            contador += 1
    for key in ['SOLO DANOS', 'CON HERIDOS', 'CON MUERTOS']:
        if not mp.contains(hash_elems, key):
            empty_list = lt.newList('ARRAY_LIST')
            mp.put(hash_elems, key, empty_list)
    return contador, hash_elems
    
    


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def compare_date_time_tuples(date_time_1, date_time_2):
   if date_time_1 < date_time_2:
       return 1
   elif date_time_1==date_time_2:
       return 0
   else:
       return -1
   
def compare_date_time_tuples_minpq(elem1, elem2):
   if elem1['FECHA_HORA_ACC'] < elem2['FECHA_HORA_ACC']:
       return 1
   elif elem1['FECHA_HORA_ACC'] == elem2['FECHA_HORA_ACC']:
       return 0
   else:
       return -1

def compare_time_maxpq(elem1, elem2):
   if elem1['HORA_ACC'] > elem2['HORA_ACC']:
       return 1
   elif elem1['HORA_ACC'] == elem2['HORA_ACC']:
       if elem1['CODIGO_ACCIDENTE'] < elem2['CODIGO_ACCIDENTE']:
           return 1
       else:
           return 0
   else:
       return -1

def compare_time_minpq(elem1, elem2):
   if elem1['HORA_ACC'] < elem2['HORA_ACC']:
       return 1
   elif elem1['HORA_ACC'] == elem2['HORA_ACC']:
       if elem1['CODIGO_ACCIDENTE'] < elem2['CODIGO_ACCIDENTE']:
           return 1
       else:
           return 0
   else:
       return -1

def compare_distancias_tupla_distanica_elem(elem1, elem2):
    if elem1[0] > elem2[0]:
        return 1
    elif elem1[0] == elem2[0]:
        return 0
    else:
        return -1

def compare_id(elem1, elem2):
    if elem1['idx'] > elem2['idx']:
        return 1
    elif elem1['idx'] == elem2['idx']:
        return 0
    else:
        return -1
    
   
def tree_size(tree):
    return om.size(tree)

def tree_elems(tree):
    return om.valueSet(tree)

def first_last_n_elems_list(list, n):
    if lt.size(list) <= 2*n:
        return list
    else:
        first_n_elems = lt.subList(list, 1, n)
        last_n_elems = lt.subList(list, 1-n, n)
        return first_n_elems, last_n_elems
    
def elems_rango_a_lista(rango):
    list_result = lt.newList('ARRAY_LIST')
    for elem in lt.iterator(rango):
        for acc in lt.iterator(elem):
            lt.addLast(list_result, acc)
    return list_result

def sort_criteria_fecha(entry_1,entry_2):
    if entry_1["FECHA_OCURRENCIA_ACC"]< entry_2["FECHA_OCURRENCIA_ACC"]:
        return True
    else:
        return False

def sort_criteria_fecha_inversa(entry_1, entry_2):
    if entry_1['FECHA_HORA_ACC'] > entry_2['FECHA_HORA_ACC']:
        return True
    else:
        return False

def sort_criteria_fecha_anio(entry_1, entry_2):
    if entry_1['HORA_OCURRENCIA_ACC'] < entry_2['HORA_OCURRENCIA_ACC']:
        return True
    elif entry_1['HORA_OCURRENCIA_ACC'] == entry_2['HORA_OCURRENCIA_ACC']:
        if entry_1['FECHA_OCURRENCIA_ACC'] > entry_2['FECHA_OCURRENCIA_ACC']:
            return True
        else:
            return False
    else:
        return False

def agregar_a_filtro(hash_filtro, key, data):
    if not mp.contains(hash_filtro, key):
        list_clase = lt.newList('ARRAY_LIST')
        lt.addLast(list_clase, data)
        mp.put(hash_filtro, key, list_clase)
    else:
        key_value_clase = mp.get(hash_filtro, key)
        list_clase_ = me.getValue(key_value_clase)
        lt.addLast(list_clase_, data)
        
def insert_to_tree(map, key, data):
    if not om.contains(map, key):
        list_key = lt.newList('ARRAY_LIST')
        lt.addLast(list_key, data)
        om.put(map, key, list_key)
    else:
        key_value = me.getValue(om.get(map, key))
        lt.addLast(key_value, data)
    return map

def calcular_distacia_rad(latitud_1, longitud_1, latitud_2, longitud_2):
    A = m.sin((latitud_2-latitud_1)/2)**2
    B = m.cos(latitud_1)*m.cos(latitud_2)*(m.sin((longitud_2-longitud_1)/2)**2)
    result = 2*6371*m.asin(m.sqrt(A+B))
    return result