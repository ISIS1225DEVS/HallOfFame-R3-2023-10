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
import math
assert cf

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
    data_structs = {"list_accidents":None,
                    "dates_index": None,
                    "acc_class_av":None,
                    }
    
    data_structs["list_accidents"] = lt.newList("ARRAY_LIST")
    data_structs["dates_index"] = om.newMap(omaptype="RBT",comparefunction=compareDates)
    data_structs["acc_class_av"] = om.newMap(omaptype="RBT",comparefunction=compare)
    
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, accident):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["list_accidents"],accident)
    updateDateIndex(data_structs["dates_index"], accident)
    updateClassAvIndex(data_structs["acc_class_av"], accident)
    return data_structs


# Funciones para creacion de datos

def updateDateIndex(map, accident):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    occurreddate = accident["FECHA_OCURRENCIA_ACC"]
    entry = om.get(map, occurreddate)
    if entry is None:
        dataentry = newDateEntry(accident)
        lst = me.getValue(dataentry)
        om.put(map, occurreddate, lst)
    else:
        dataentry = entry
    addDateIndex(dataentry, accident)
    return map

def newDateEntry(accident):
    entry = {"dateIndex": None, "value": None}
    entry["dateIndex"] = accident["FECHA_OCURRENCIA_ACC"]
    entry["value"] = lt.newList("ARRAY_LIST")
    return entry

def addDateIndex(dataentry, accident):
    lst = me.getValue(dataentry)
    lt.addLast(lst, accident)
    return dataentry



def updateClassAvIndex(map, accident):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    if "AV" in accident["DIRECCION"]:
        acc_class_av = (accident["DIRECCION"].split("-"))[0],accident["CLASE_ACC"]
        entry = om.get(map, acc_class_av)
        if entry is None:
            dataentry = newClassAvEntry(accident)
            lst = me.getValue(dataentry)
            om.put(map, acc_class_av, lst)
        else:
            dataentry = entry
        addClassAvIndex(dataentry, accident)
        return map

def newClassAvEntry(accident):
    entry = {"ClassAvIndex": None, "value": None}
    entry["ClassAvIndex"] = (accident["DIRECCION"].split("-"))[0],accident["CLASE_ACC"]
    entry["value"] = lt.newList("ARRAY_LIST")
    return entry

def addClassAvIndex(dataentry, accident):
    lst = me.getValue(dataentry)
    lt.addLast(lst, accident)
    return dataentry

# Funciones de consulta

def first_and_last3(data_structs):
    accidents = data_structs["list_accidents"]
    size = lt.size(accidents)
    first3 = lt.subList(accidents,1,3)    
    last3 = lt.subList(accidents,size-2,3)
    
    lista_tabulate1 = lt.newList("ARRAY_LIST")
    lista_tabulate2 = lt.newList("ARRAY_LIST")
    
    lista_param = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","LOCALIDAD","DIRECCION",
                   "GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
    lt.addLast(lista_tabulate1,lista_param)
    lt.addLast(lista_tabulate2,lista_param)
    
    for accident in lt.iterator(first3):
        lista_aux = lt.newList("ARRAY_LIST")
        for param in lista_param:
            lt.addLast(lista_aux,accident[param])
        lt.addLast(lista_tabulate1,lista_aux["elements"])
        
    for accident in lt.iterator(last3):
        lista_aux = lt.newList("ARRAY_LIST")
        for param in lista_param:
            lt.addLast(lista_aux,accident[param])
        lt.addLast(lista_tabulate2,lista_aux["elements"])    
            
        
    return lista_tabulate1["elements"], lista_tabulate2["elements"]



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


def req_1(data_structs, fecha_i, fecha_f):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    values = om.values(data_structs['dates_index'], fecha_i, fecha_f)
    list_sis = lt.newList("ARRAY_LIST")
    for value in lt.iterator(values):
        for val in lt.iterator(value):
            lt.addFirst(list_sis, val)
    
    param = lt.newList("ARRAY_LIST")
    lt.addLast(param, 'CODIGO_ACCIDENTE')
    lt.addLast(param, 'DIA_OCURRENCIA_ACC')
    lt.addLast(param, 'DIRECCION')
    lt.addLast(param, 'GRAVEDAD')
    lt.addLast(param, 'CLASE_ACC')
    lt.addLast(param, 'LOCALIDAD')
    lt.addLast(param, 'FECHA_HORA_ACC')
    lt.addLast(param, 'LATITUD')
    lt.addLast(param, 'LONGITUD')
    
    final_list = lt.newList("ARRAY_LIST")
    
    for siniestro in lt.iterator(list_sis):
        aux_list = []
        for par in lt.iterator(param):
            aux_list.append(siniestro[par])
        lt.addLast(final_list, aux_list)
    
    f_list = merg.sort(final_list, compareDatesandhour)
    
    return param, f_list


def req_2(data_structs,horamin_initial,horamin_final,anio,mes):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    mes = MonthNameToNumber(mes)
            
    horamin_initial = horamin_initial + ":00"
    horamin_final = horamin_final + ":00"
    
    horamin_initial = horamin_initial.split(":")
    horamin_final = horamin_final.split(":")
    for i in range(0,3):
        horamin_initial[i] = int(horamin_initial[i])
        horamin_final[i] = int(horamin_final[i])


    rbt = data_structs["dates_index"]
    fecha_initial = "{0}/{1}/01".format(anio,mes)
    fecha_final = "{0}/{1}/31".format(anio,mes)

    values = om.values(rbt,fecha_initial,fecha_final)
    array = lt.newList("ARRAY_LIST")
    for element in lt.iterator(values):
        for accident in lt.iterator(element):
            lt.addLast(array,accident)

    ranged_array = lt.newList("ARRAY_LIST")
    for accident in lt.iterator(array):
        horamin = accident["HORA_OCURRENCIA_ACC"]
        
        horamin = horamin.split(":")
        for i in range(0,3):
            horamin[i] = int(horamin[i])
            
        if (horamin >= horamin_initial) and (horamin <= horamin_final):
            lt.addLast(ranged_array,accident)
    
    ranged_sorted_array = merg.sort(ranged_array,compareHours)
    
    param = ["CODIGO_ACCIDENTE","HORA_OCURRENCIA_ACC","FECHA_OCURRENCIA_ACC",
             "DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC",
             "LATITUD","LONGITUD"]
    
    lista_tabulate = lt.newList("ARRAY_LIST")
    lt.addLast(lista_tabulate,param)
    
    for accident in lt.iterator(ranged_sorted_array):
        lista_aux = lt.newList("ARRAY_LIST")
        for x in param:
            lt.addLast(lista_aux,accident[x])
        lt.addLast(lista_tabulate,lista_aux["elements"])
   
    return lista_tabulate["elements"]

def MonthNameToNumber(mes):
    if not mes.isdecimal():
        mes = mes.upper()
        if mes == "ENERO":
            mes = "01"
        elif mes == "FEBRERO":
            mes = "02"
        elif mes == "MARZO":
            mes = "03"
        elif mes == "ABRIL":
            mes = "04"
        elif mes == "MAYO":
            mes = "05"           
        elif mes == "JUNIO":
            mes = "06"           
        elif mes == "JULIO":
            mes = "07"           
        elif mes == "AGOSTO":
            mes = "08"           
        elif mes == "SEPTIEMBRE":
            mes = "09"           
        elif mes == "OCTUBRE":
            mes = "10"           
        elif mes == "NOVIEMBRE":
            mes = "11"
        elif mes == "DICIEMBRE":
            mes = "12"
    if len(mes) == 1:
        mes = "0"+mes
                      
    return mes


def req_3(data_structs,clase_accidente,nombre_via):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    acc_class_av = data_structs["acc_class_av"]
    
    nombre_via = nombre_via.upper()
    clase_accidente = clase_accidente.upper()
    
    if "AV " in nombre_via:
        llave = om.get(acc_class_av,(nombre_via,clase_accidente))
    else:
        nombre_via = "AV " + str(nombre_via)
        llave = om.get(acc_class_av,(nombre_via,clase_accidente))
    
    lista_acc = llave["value"]
    merg.sort(lista_acc,compareDatesreq3)
    sublista = lt.subList(lista_acc,1,3)
    param = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC",
             "LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC",
             "LATITUD","LONGITUD"]
    
    lista_tabulate = lt.newList("ARRAY_LIST")
    lt.addLast(lista_tabulate,param)
    
    for accident in lt.iterator(sublista):
        lista_aux = lt.newList("ARRAY_LIST")
        for x in param:
            lt.addLast(lista_aux,accident[x])
        lt.addLast(lista_tabulate,lista_aux["elements"])
   
    return lt.size(lista_acc),lista_tabulate["elements"]


def req_4(data_structs, fecha_i, fecha_f, g_accidente):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    list_rank = om.values(data_structs['dates_index'], fecha_i, fecha_f)
    list_acc = lt.newList("ARRAY_LIST")
    for value in lt.iterator(list_rank):
        for x in lt.iterator(value):
            if x["GRAVEDAD"] == g_accidente:
                lt.addLast(list_acc, x)
                
    param = lt.newList("ARRAY_LIST")
    lt.addLast(param, "CODIGO_ACCIDENTE")
    lt.addLast(param, "FECHA_HORA_ACC")
    lt.addLast(param, "DIA_OCURRENCIA_ACC")
    lt.addLast(param, "LOCALIDAD")
    lt.addLast(param, "DIRECCION")
    lt.addLast(param, "GRAVEDAD")
    lt.addLast(param, "CLASE_ACC")
    lt.addLast(param, "LATITUD")
    lt.addLast(param, "LONGITUD")
    
    grav_list = lt.newList("ARRAY_LIST")
    
    merg.sort(list_acc, comparereq4)
    
    sorted_list = lt.subList(list_acc,1,5)
        
    for accident in lt.iterator(sorted_list):
        aux = lt.newList("ARRAY_LIST")
        for pr in lt.iterator(param):
            lt.addLast(aux,accident[pr])
        lt.addLast(grav_list,aux["elements"])
    
    
    lt.addFirst(grav_list, param["elements"])
    
    return list_acc, grav_list["elements"]

def req_5(data_structs, localidad, mes, año):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    
    # Se crea una lista con Los meses
    month_list = lt.newList("ARRAY_LIST")
    lt.addLast(month_list, "ENERO")
    lt.addLast(month_list, "FEBRERO")
    lt.addLast(month_list, "MARZO")
    lt.addLast(month_list, "ABRIL")
    lt.addLast(month_list, "MAYO")
    lt.addLast(month_list, "JUNIO")
    lt.addLast(month_list, "JULIO")
    lt.addLast(month_list, "AGOSTO")
    lt.addLast(month_list, "SEPTIEMBRE")
    lt.addLast(month_list, "OCTUBRE")
    lt.addLast(month_list, "NOVIEMBRE")
    lt.addLast(month_list, "DICIEMBRE")
    
    # Buscamos a que número corresponde el mes dado
    mes = lt.isPresent(month_list, mes)
    
    # Creamos un formato año/mes/día para el año y mes dado donde los días comienzan en 01 y terminan en 31
    if mes != None:
        fecha_i = "{0}/{1:02d}/01".format(año, mes)
        fecha_f = "{0}/{1:02d}/31".format(año, mes)
    
    # Se obtienen los valores que están entre el rango tomando en cuenta los extremos
    values = om.values(data_structs['dates_index'], fecha_i, fecha_f)
    
    # Lista para guardar los accidentes ocurridos en el rango de tiempo que correspondan a la localidad dada
    local_list = lt.newList("ARRAY_LIST")
    
    # Se buscan en los accidentes ocurridos en el rango de tiempo que correspondan a la localidad dada
    for dias in lt.iterator(values):
        for siniestro in lt.iterator(dias):
            if siniestro["LOCALIDAD"] == localidad:
                lt.addLast(local_list, siniestro)
    
    # Ordeno la lista de fecha mas reciente a menos reciente
    aux_list = merg.sort(local_list, compareDatesandhourreq5)
    
    # Hacer sublista de 10 si es mayor a 10 si no dejar igual
    if lt.size(aux_list) > 10:
        f_list = lt.subList(aux_list, 1, 10)
    else:
        f_list = aux_list
    
    # Parametros a utilizar
    param = lt.newList("ARRAY_LIST")
    lt.addLast(param, 'CODIGO_ACCIDENTE')
    lt.addLast(param, 'DIA_OCURRENCIA_ACC')
    lt.addLast(param, 'DIRECCION')
    lt.addLast(param, 'GRAVEDAD')
    lt.addLast(param, 'CLASE_ACC')
    lt.addLast(param, 'FECHA_HORA_ACC')
    lt.addLast(param, 'LATITUD')
    lt.addLast(param, 'LONGITUD')
    
    final_list = lt.newList("ARRAY_LIST")
    
    for siniestro in lt.iterator(f_list):
        aux_list = []
        for par in lt.iterator(param):
            aux_list.append(siniestro[par])
        lt.addLast(final_list, aux_list)
    
    return param, final_list


def req_6(data_structs,topN,coordenadas,radio,mes,anio):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    mes = MonthNameToNumber(mes)
    lat1,lon1 = coordenadas
    lat1 = float(lat1)
    lon1 = float(lon1)
    
    rbt = data_structs["dates_index"]
    fecha_initial = "{0}/{1}/01".format(anio,mes)
    fecha_final = "{0}/{1}/31".format(anio,mes)

    values = om.values(rbt,fecha_initial,fecha_final)
    array = lt.newList("ARRAY_LIST")
    for element in lt.iterator(values):
        for accident in lt.iterator(element):
            lt.addLast(array,accident)
    
    near_accidents = mpq.newMinPQ(comparereq6)
    for accident in lt.iterator(array):
        lat2 = float(accident["LATITUD"])
        lon2 = float(accident["LONGITUD"])
        distancia = haversine(lat1,lon1,lat2,lon2)
        if distancia <= float(radio):
            lista_aux = lt.newList("ARRAY_LIST")
            lt.addLast(lista_aux,distancia)
            lt.addLast(lista_aux,accident)
            mpq.insert(near_accidents,lista_aux["elements"])
    
    lista_min = lt.newList("ARRAY_LIST")
    for i in range(0,topN):
        minimum = mpq.delMin(near_accidents)
        lt.addLast(lista_min,minimum)
    
    param = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC",
             "LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD","DISTANCIA(km)"]
    
    lista_tabulate = lt.newList("ARRAY_LIST")
    lt.addLast(lista_tabulate,param)
    for accident in lt.iterator(lista_min):
        lista_aux = lt.newList("ARRAY_LIST")
        for x in param:
            if x == "DISTANCIA(km)":
                lt.addLast(lista_aux,str(round(accident[0],3)))
            else:
                lt.addLast(lista_aux,accident[1][x])
        lt.addLast(lista_tabulate,lista_aux["elements"])
    
    return lista_tabulate["elements"]


def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos geográficos utilizando la ecuación de Haversine.
    Los puntos geográficos se especifican mediante su latitud y longitud en grados decimales.
    """
    R = 6371  # radio de la tierra en km

    # convertir latitud y longitud a radianes
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # calcular la diferencia de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # aplicar la ecuación de Haversine
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    distancia = R * c

    return distancia

def req_7(data_structs, mes, año):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    # Se crea una lista con Los meses
    month_list = lt.newList("ARRAY_LIST")
    lt.addLast(month_list, "ENERO")
    lt.addLast(month_list, "FEBRERO")
    lt.addLast(month_list, "MARZO")
    lt.addLast(month_list, "ABRIL")
    lt.addLast(month_list, "MAYO")
    lt.addLast(month_list, "JUNIO")
    lt.addLast(month_list, "JULIO")
    lt.addLast(month_list, "AGOSTO")
    lt.addLast(month_list, "SEPTIEMBRE")
    lt.addLast(month_list, "OCTUBRE")
    lt.addLast(month_list, "NOVIEMBRE")
    lt.addLast(month_list, "DICIEMBRE")
    
    # Buscamos a que número corresponde el mes dado
    mes = lt.isPresent(month_list, mes)
    
    # Creamos un formato año/mes/día para el año y mes dado donde los días comienzan en 01 y terminan en 31
    if mes != None:
        fecha_i = "{0}/{1:02d}/01".format(año, mes)
        fecha_f = "{0}/{1:02d}/31".format(año, mes)
    
    # Se obtienen los valores y llaves que están entre el rango tomando en cuenta los extremos
    values = om.values(data_structs['dates_index'], fecha_i, fecha_f)
    
    # Lista de horas para todos los días del mes en el años dado
    hours_list = lt.newList("ARRAY_LIST")
    
    # Obtener todas las horas de accidentes
    for value in lt.iterator(values):
        for v in lt.iterator(value):
            # Se obtiene la hora solamente en int
            hour = int(v['HORA_OCURRENCIA_ACC'].split(':')[0])
            lt.addLast(hours_list, hour)
    
    # Ordenar la lista
    hours_list = merg.sort(hours_list, comparehourslist)
    
    # Parametros a utilizar
    param = lt.newList("ARRAY_LIST")
    lt.addLast(param, 'CODIGO_ACCIDENTE')
    lt.addLast(param, 'DIA_OCURRENCIA_ACC')
    lt.addLast(param, 'DIRECCION')
    lt.addLast(param, 'GRAVEDAD')
    lt.addLast(param, 'CLASE_ACC')
    lt.addLast(param, 'LOCALIDAD')
    lt.addLast(param, 'FECHA_HORA_ACC')
    lt.addLast(param, 'LATITUD')
    lt.addLast(param, 'LONGITUD')
    
    # Ordenar los accidentes de cada uno de los días por horas
    for value in lt.iterator(values):
        value = merg.sort(value, compareHourreq7)
    
    # Nueva lista para valores
    values_list = lt.newList("ARRAY_LIST")
    
    # Obtengo una lista con todas las horas y parámetros
    for value in lt.iterator(values):
        first = lt.getElement(value, 1)
        last = lt.getElement(value, lt.size(value))
        
        # Obtener el penultimo ya que en el caso del primero se tiene en cuenta que si
        # el primero y el segundo tienen la misma hora se toma el que tenga menor código
        lastbutone = lt.getElement(value, lt.size(value))
        
        # Si el penultimo y el último tienen la misma hora el que tenga menor código se escogerá el de menor código
        if lastbutone['FECHA_HORA_ACC'] == last['FECHA_HORA_ACC'] and lastbutone['CODIGO_ACCIDENTE'] < last['CODIGO_ACCIDENTE']:
            last = lastbutone
                
        aux_list = lt.newList("ARRAY_LIST")
        
        dictionary = {}
        for p in lt.iterator(param):
            dictionary[p] = first[p]
        lt.addLast(aux_list, dictionary)
        
        dictionary = {}
        for p in lt.iterator(param):
            dictionary[p] = last[p]
        lt.addLast(aux_list, dictionary)
        
        lt.addLast(values_list, aux_list)
    
    return hours_list, values_list


def req_8(data_structs, fecha_inicial, fecha_final, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
    # Modificar formato de fecha
    fecha_inicial = "/".join(fecha_inicial.split("/")[::-1])
    fecha_final = "/".join(fecha_final.split("/")[::-1])
    
    # Obtener los valores correspondientes al rango de fechas
    values = om.values(data_structs['dates_index'], fecha_inicial, fecha_final)
    
    # Lista para guardar los siniestros
    values_list = lt.newList("ARRAY_LIST")
    
    #Lista de parametros
    param = lt.newList("ARRAY_LIST")
    lt.addLast(param, "FECHA_OCURRENCIA_ACC")
    lt.addLast(param, "HORA_OCURRENCIA_ACC")
    
    # Para guardar los siniestros que esten en la clase dada y solo los parámetros deseados
    for value in lt.iterator(values):
        for v in lt.iterator(value):
            if v["CLASE_ACC"] == clase:
                dictionary = {"GRAVEDAD": v["GRAVEDAD"], "LOCATION": [float(v["LATITUD"]), float(v["LONGITUD"])]}
                for p in lt.iterator(param):
                    dictionary[p] = v[p]
                lt.addLast(values_list, dictionary)
    
    return values_list



# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if (data_1 == data_2):
        return 0
    elif data_1 > data_2:
        return 1
    else:
        return -1

def comparereq6(data1,data2):
    
    if data1[0] == data2[0]:
        return data1[1]["FECHA_OCURRENCIA_ACC"] < data2[1]["FECHA_OCURRENCIA_ACC"]
    else:
        return data1[0] > data2[0]

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareDatesreq3(acc1,acc2):
    date1 = acc1["FECHA_OCURRENCIA_ACC"]
    date2 = acc2["FECHA_OCURRENCIA_ACC"]
    
    if date1 == date2:
        hour1 = acc1["HORA_OCURRENCIA_ACC"].split(":")
        hour2 = acc2["HORA_OCURRENCIA_ACC"].split(":")
        for i in range(0,3):
            hour1[i] = int(hour1[i])
            hour2[i] = int(hour2[i])
        return hour1 > hour2
    else:
        return date1 > date2

def compareDatesandhour(date1, date2):
    """
    Compara dos fechas
    """
    if (date1[6] == date2[6]):
            return True
    elif (date1[6] > date2[6]):
        return True
    else:
        return False

def compareDatesandhourreq5(date1, date2):
    """
    Compara dos fechas
    """
    if (date1["FECHA_HORA_ACC"] == date2["FECHA_HORA_ACC"]):
            return True
    elif (date1["FECHA_HORA_ACC"] > date2["FECHA_HORA_ACC"]):
        return True
    else:
        return False

def compareHourreq7(date1, date2):
    """
    Compara dos fechas
    """
    if (date1["FECHA_HORA_ACC"] == date2["FECHA_HORA_ACC"]):
        if (date1["CODIGO_ACCIDENTE"] < date2["CODIGO_ACCIDENTE"]):
            return True
        else:
            return False
    elif (date1["FECHA_HORA_ACC"] < date2["FECHA_HORA_ACC"]):
        return True
    else:
        return False
    
def comparehourslist(hour1, hour2):
    if (hour1 == hour2):
        return True
    elif(hour1 < hour2):
        return True
    else:
        return False
    
def compareHours(acc1,acc2):
    hour1 = acc1["HORA_OCURRENCIA_ACC"].split(":")
    hour2 = acc2["HORA_OCURRENCIA_ACC"].split(":")
    
    for i in range(0,3):
        hour1[i] = int(hour1[i])
        hour2[i] = int(hour2[i])

    if (hour1 == hour2):
        return acc1["FECHA_OCURRENCIA_ACC"] < acc2["FECHA_OCURRENCIA_ACC"]
    else:
        return hour1 < hour2
def comparereq4 (date1, date2):
    
    dat1 = date1["FECHA_OCURRENCIA_ACC"]
    dat2 = date2["FECHA_OCURRENCIA_ACC"]

    if dat1 == dat2:
        hour1 = date1["HORA_OCURRENCIA_ACC"].split(":")
        hour2 = date2["HORA_OCURRENCIA_ACC"].split(":")
        for i in range(0,3):
            hour1[i] = int(hour1[i])
            hour2[i] = int(hour2[i])
        return hour1 > hour2
    else:
        return dat1 > dat2
        
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
