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


import datetime
import math
import config as cf
import folium
from folium.plugins import FastMarkerCluster, MarkerCluster
from branca.element import Template, MacroElement
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
Se define la estructura de un catálogo de accidentes. El catálogo tendrá
n listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = {
        "accidents": None,  # accidents = La lista normalita de accidentes
        "dateIndex": None,  # dateIndex = Indice por fecha compuesto, arbol dentro de arbol.
        "cmpdataIndex": None,  # cmpdataIndex = Indice por fecha completa, osea, indice por "AA/MM/DD"
    }

    catalog["accidents"] = lt.newList("ARRAY_LIST", compareIds)
    catalog["dateIndex"] = om.newMap(omaptype="RBT", comparefunction=compareDates)
    catalog["cmpdataIndex"] = om.newMap(omaptype="RBT", comparefunction=compareDates)
    return catalog


# Funciones para agregar informacion al modelo


def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["accidents"], data)
    updateDateIndex(data_structs["dateIndex"], data)
    updatecmpDateIndex(data_structs["cmpdataIndex"], data)
    return data_structs


def updateDateIndex(map, data):
    """
    Se toma la fecha del accidente y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de accidentes
    y se actualiza el indice de tipos de accidentes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de accidentes
    """
    occurred_year = data["ANO_OCURRENCIA_ACC"]
    entry = om.get(map, occurred_year)
    if entry is None:
        datentry = newDataEntry(data)
        om.put(map, occurred_year, datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, data)
    return map


def addDateIndex(datentry, data):
    """
    Actualiza un indice de tipo de accidentes.  Este indice tiene una lista
    de accidentes y una tabla de hash cuya llave es el tipo de accidente y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry["lstaccidents"]
    lt.addLast(lst, data)
    monthIndex = datentry["monthIndex"]
    fecha = datetime.datetime.strptime(data["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d")
    hora = datetime.datetime.strptime(data["HORA_OCURRENCIA_ACC"], "%H:%M:%S")
    mes = fecha.month
    dia = fecha.day
    localidad = data["LOCALIDAD"]
    monthentry = om.get(monthIndex, mes)
    if monthentry is None:
        entry = newMonthEntry(data, dia, hora, localidad)
        lt.addLast(entry["lstaccidents"], data)
        om.put(monthIndex, mes, entry)
    else:
        entry = me.getValue(monthentry)
        day_entry = om.get(entry["dayIndex"], dia)
        if day_entry is None:
            list_days = newDayEntry(data, hora)
            lt.addLast(list_days["lstaccidents"], data)
            om.put(entry["dayIndex"], dia, list_days)
        else:
            list_days = me.getValue(day_entry)
            subhour_entry = om.get(list_days["subhourIndex"], hora)
            if subhour_entry is None:
                list_subhours = lt.newList("ARRAY_LIST", compareIds)
                lt.addLast(list_subhours, data)
                om.put(list_days["subhourIndex"], hora, list_subhours)
            else:
                list_subhours = me.getValue(subhour_entry)
                lt.addLast(list_subhours, data)
            lt.addLast(list_days["lstaccidents"], data)
        hour_entry = om.get(entry["hourIndex"], hora)
        if hour_entry is None:
            list_hours = lt.newList("ARRAY_LIST", compareIds)
            lt.addLast(list_hours, data)
            om.put(entry["hourIndex"], hora, list_hours)
        else:
            hour_list = me.getValue(hour_entry)
            lt.addLast(hour_list, data)
        localidad_entry = mp.get(entry["localidadIndex"], localidad)
        if localidad_entry is None:
            list_localidad = lt.newList("ARRAY_LIST", compareIds)
            lt.addLast(list_localidad, data)
            mp.put(entry["localidadIndex"], localidad, list_localidad)
        else:
            list_localidad = me.getValue(localidad_entry)
            lt.addLast(list_localidad, data)
        lt.addLast(entry["lstaccidents"], data)
    return datentry


def updatecmpDateIndex(map, data):
    """
    Se toma la fecha del accidente y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de accidentes
    y se actualiza el indice de tipos de accidentes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de accidentes
    """
    occurred_date = data["FECHA_OCURRENCIA_ACC"]
    accident_date = datetime.datetime.strptime(occurred_date, "%Y/%m/%d")
    entry = om.get(map, accident_date.date())
    if entry is None:
        # data_entry = lt.newList("ARRAY_LIST", compareIds)
        data_entry = newcmpDataEntry(data)
        # lt.addLast(data_entry, data)
        om.put(map, accident_date.date(), data_entry)
    else:
        data_entry = me.getValue(entry)
    addcmpDateIndex(data_entry, data)
    return map


def addcmpDateIndex(datentry, data):
    """
    Actualiza un indice de tipo de accidentes. Este indice tiene una lista
    de accidentes y una tabla de hash cuya llave es el tipo de accidente y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry["lstaccidents"]
    lt.addLast(lst, data)
    class_Index = datentry["classIndex"]
    class_entry = mp.get(class_Index, data["CLASE_ACC"])
    gravedad_Index = datentry["gravedadIndex"]
    gravedad_entry = mp.get(gravedad_Index, data["GRAVEDAD"])
    if class_entry is None:
        entry = newClassEntry(data["CLASE_ACC"], data)
        # lt.addLast(entry["lstaccidents"], data)
        mp.put(class_Index, data["CLASE_ACC"], entry)
    else:
        entry = me.getValue(class_entry)
        lt.addLast(entry["lstaccidents"], data)
    if gravedad_entry is None:
        gr_entry = newGravedadEntry(data["GRAVEDAD"], data)
        lt.addLast(entry["lstaccidents"], data)
        mp.put(gravedad_Index, data["GRAVEDAD"], gr_entry)
    else:
        gr_entry = me.getValue(gravedad_entry)
        lt.addLast(gr_entry["lstaccidents"], data)
    return datentry


# Funciones para creacion de datos


def newClassEntry(classgrp, data):
    """
    Crea una entrada en el indice por clase de accidente, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    clentry = {"class_acc": None, "lstaccidents": None}
    clentry["class_acc"] = classgrp
    clentry["lstaccidents"] = lt.newList("SINGLE_LINKED", compareClasses)
    lt.addLast(clentry["lstaccidents"], data)
    return clentry


def newGravedadEntry(gradevadgrp, data):
    """
    Crea una entrada en el indice por gravedad de accidente, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    grentry = {"gravedad_acc": None, "lstaccidents": None}
    grentry["gravedad_acc"] = gradevadgrp
    grentry["lstaccidents"] = lt.newList("SINGLE_LINKED", compareClasses)
    lt.addLast(grentry["lstaccidents"], data)
    return grentry


def newcmpDataEntry(data):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {"classIndex": None, "gravedadIndex": None, "lstaccidents": None}
    entry["classIndex"] = mp.newMap(
        numelements=7, maptype="PROBING", loadfactor=0.5, cmpfunction=compareMap
    )
    entry["gravedadIndex"] = mp.newMap(
        numelements=3, maptype="PROBING", loadfactor=0.5, cmpfunction=compareMap
    )
    entry["lstaccidents"] = lt.newList("ARRAY_LIST", compareIds)
    lt.addLast(entry["lstaccidents"], data)
    return entry


def newMonthEntry(data, dia, hora, localidad):
    """
    Crea una entrada en el indice por tipo de accidente, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    entry = {
        "dayIndex": None,
        "hourIndex": None,
        "localidadIndex": None,
        "lstaccidents": None,
    }
    entry["dayIndex"] = om.newMap(omaptype="RBT", comparefunction=compareDates)
    entry["hourIndex"] = om.newMap(omaptype="RBT", comparefunction=compareHours)
    entry["localidadIndex"] = mp.newMap(
        numelements=20, maptype="PROBING", cmpfunction=compareMap
    )
    entry["lstaccidents"] = lt.newList("ARRAY_LIST", compareIds)
    dayEntry = newDayEntry(data, hora)
    list_hours = lt.newList("ARRAY_LIST", compareIds)
    lt.addLast(list_hours, data)
    list_localidad = lt.newList("ARRAY_LIST", compareIds)
    lt.addLast(list_localidad, data)
    om.put(entry["dayIndex"], dia, dayEntry)
    om.put(entry["hourIndex"], hora, list_hours)
    mp.put(entry["localidadIndex"], localidad, list_localidad)
    lt.addLast(entry["lstaccidents"], data)
    return entry


def newDayEntry(data, hora):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {"subhourIndex": None, "lstaccidents": None}
    entry["subhourIndex"] = om.newMap(omaptype="RBT", comparefunction=compareDates)
    entry["lstaccidents"] = lt.newList("ARRAY_LIST", compareIds)
    list_hours = lt.newList("ARRAY_LIST", compareIds)
    lt.addLast(list_hours, data)
    om.put(entry["subhourIndex"], hora, list_hours)
    lt.addLast(entry["lstaccidents"], data)
    return entry


def newDataEntry(data):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {"monthIndex": None, "lstaccidents": None}
    entry["monthIndex"] = om.newMap(omaptype="RBT", comparefunction=compareDates)
    entry["lstaccidents"] = lt.newList("ARRAY_LIST", compareIds)
    lt.addLast(entry["lstaccidents"], data)
    return entry


def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    # TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta


def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    # TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    # TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["accidents"]), len(
        lt.firstElement(data_structs["accidents"])
    )


lat_0 = 0
lon_0 = 0


def req_1(data_structs, fecha_inicio, fecha_final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    lst = om.values(data_structs["cmpdataIndex"], fecha_inicio, fecha_final)
    lst_rt = lt.newList("ARRAY_LIST", compareIds)
    for lista in lt.iterator(lst):
        for elemento in lt.iterator(lista["lstaccidents"]):
            if lt.isPresent(lst_rt, elemento) == 0:
                lt.addLast(lst_rt, elemento)
    merg.sort(lst_rt, cmp_accidentes_by_full_date)
    return lst_rt


def req_2(data_structs, initial_hour, final_hour, anio, month):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    anio_tree = om.get(data_structs["dateIndex"], anio)
    month_big_tree = me.getValue(anio_tree)["monthIndex"]
    month_special_tree = om.get(month_big_tree, month)
    hour_tree = me.getValue(month_special_tree)["hourIndex"]
    wanted_hours = om.values(hour_tree, initial_hour, final_hour)
    lst_rt = lt.newList("ARRAY_LIST", compareIds)
    for lista in lt.iterator(wanted_hours):
        for elemento in lt.iterator(lista):
            if lt.isPresent(lst_rt, elemento) == 0:
                lt.addLast(lst_rt, elemento)
    merg.sort(lst_rt, cmp_accidentes_date)
    return lst_rt


def req_3(data_structs, acc_class, via):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3

    wanted_accidents = lt.newList("ARRAY_LIST")
    for elemento in lt.iterator(data_structs["accidents"]):
        if elemento["CLASE_ACC"] == acc_class:
            accidente_vias = elemento["DIRECCION"].split("-")
            if via in accidente_vias[0]:
                lt.addLast(wanted_accidents, elemento)
    merg.sort(wanted_accidents, cmp_accidentes_by_full_date)
    top3 = lt.subList(wanted_accidents, 1, 3)
    return top3, lt.size(wanted_accidents)


def req_4(data_structs, fecha_inicio, fecha_final, gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lst = om.values(data_structs["cmpdataIndex"], fecha_inicio, fecha_final)
    lst_rt = lt.newList("ARRAY_LIST", compareIds)
    for lista in lt.iterator(lst):
        a = mp.get(lista["gravedadIndex"], gravedad)
        if a != None:
            valor = me.getValue(a)
            for accidente in lt.iterator(valor["lstaccidents"]):
                lt.addLast(lst_rt, accidente)
    merg.sort(lst_rt, cmp_accidentes_by_full_date)
    tamaño = lt.size(lst_rt)
    if int(tamaño) > 5:
        lista2 = lt.subList(lst_rt, 1, 5)
        return lista2, tamaño

    else:
        return lst_rt, tamaño


def req_5(data_structs, anio, month, localidad):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    anio_tree = om.get(data_structs["dateIndex"], anio)
    month_big_tree = me.getValue(anio_tree)["monthIndex"]
    month_special_tree = om.get(month_big_tree, month)
    local_table = me.getValue(month_special_tree)["localidadIndex"]
    wanted_loc = mp.get(local_table, localidad)
    wanted_loc = me.getValue(wanted_loc)
    merg.sort(wanted_loc, cmp_accidentes_by_full_date)
    if lt.size(wanted_loc) < 10:
        return wanted_loc
    else:
        return lt.subList(wanted_loc, 1, 10)


def req_6(data_structs, anio, month, lat, lon, radio, can_n):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    global lat_0
    global lon_0
    lat_0 = lat
    lon_0 = lon
    anio_tree = om.get(data_structs["dateIndex"], anio)
    month_big_tree = me.getValue(anio_tree)["monthIndex"]
    month_special_tree = om.get(month_big_tree, month)
    specific_list = me.getValue(month_special_tree)["lstaccidents"]
    merg.sort(specific_list, cmp_accidentes_by_distance)
    prelista = lt.subList(specific_list, 1, can_n)
    lista_rt = lt.newList("ARRAY_LIST", compareIds)
    for item in lt.iterator(prelista):
        if (
            abs(distancia_haversine(lat, lon, item["LATITUD"], item["LONGITUD"]))
            < radio
        ):
            lt.addLast(lista_rt, item)
        else:
            break
    if lt.size(lista_rt) < can_n:
        return lista_rt, True
    else:
        return lista_rt, False


def req_7(data_structs, anio, month):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    anio_tree = om.get(data_structs["dateIndex"], anio)
    month_big_tree = me.getValue(anio_tree)["monthIndex"]
    month_special_tree = om.get(month_big_tree, month)
    days_trees = me.getValue(month_special_tree)["dayIndex"]
    list_keys = om.keySet(days_trees)
    lt_retornable = lt.newList("ARRAY_LIST", compareIds)
    for llave in lt.iterator(list_keys):
        lt_dia = lt.newList("ARRAY_LIST", compareIds)
        day_entry = om.get(days_trees, llave)
        day_subhour_index = me.getValue(day_entry)["subhourIndex"]
        primera_llave = om.minKey(day_subhour_index)
        primeros_acc = om.get(day_subhour_index, primera_llave)
        primeros_acc = me.getValue(primeros_acc)
        ultima_llave = om.maxKey(day_subhour_index)
        ultimos_acc = om.get(day_subhour_index, ultima_llave)
        ultimos_acc = me.getValue(ultimos_acc)
        merg.sort(primeros_acc, cmp_accidentes_by_codigo)
        merg.sort(ultimos_acc, cmp_accidentes_by_codigo)
        primero = lt.firstElement(primeros_acc)
        ultimo = lt.firstElement(ultimos_acc)
        lt.addLast(lt_dia, primero)
        lt.addLast(lt_dia, ultimo)
        lt.addLast(lt_retornable, lt_dia)
    # =============== Parte 2 ===============
    franjas_horarias = [
        ("0:00", "0:59"),
        ("1:00", "1:59"),
        ("2:00", "2:59"),
        ("3:00", "3:59"),
        ("4:00", "4:59"),
        ("5:00", "5:59"),
        ("6:00", "6:59"),
        ("7:00", "7:59"),
        ("8:00", "8:59"),
        ("9:00", "9:59"),
        ("10:00", "10:59"),
        ("11:00", "11:59"),
        ("12:00", "12:59"),
        ("13:00", "13:59"),
        ("14:00", "14:59"),
        ("15:00", "15:59"),
        ("16:00", "16:59"),
        ("17:00", "17:59"),
        ("18:00", "18:59"),
        ("19:00", "19:59"),
        ("20:00", "20:59"),
        ("21:00", "21:59"),
        ("22:00", "22:59"),
        ("23:00", "23:59"),
    ]
    hour_tree = me.getValue(month_special_tree)["hourIndex"]
    lista_cantidad_acc = []
    for franja in franjas_horarias:
        initial_hour = datetime.datetime.strptime(franja[0], "%H:%M")
        final_hour = datetime.datetime.strptime(franja[1], "%H:%M")
        wanted_hours = om.values(hour_tree, initial_hour, final_hour)
        contador = 0
        for hora in lt.iterator(wanted_hours):
            contador += lt.size(hora)
        lista_cantidad_acc.append(contador)
    return lt_retornable, lista_cantidad_acc


def req_8(data_structs, fecha_inicio, fecha_final, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    lst = om.values(data_structs["cmpdataIndex"], fecha_inicio, fecha_final)
    lst_rt = lt.newList("ARRAY_LIST", compareIds)
    accidentes = 0
    for lista in lt.iterator(lst):
        lt_counter = lt.newList("ARRAY_LIST", compareIds)
        for item_c in lt.iterator(lista["lstaccidents"]):
            if lt.isPresent(lt_counter, item_c) == 0:
                lt.addLast(lt_counter, item_c)
        accidentes += lt.size(lt_counter)
        tabla = lista["classIndex"]
        lista_clase = mp.get(tabla, clase)
        if lista_clase is not None:
            lista_clase = me.getValue(lista_clase)
            for item in lt.iterator(lista_clase["lstaccidents"]):
                if lt.isPresent(lst_rt, item) == 0:
                    lt.addLast(lst_rt, item)
    # ==================== Parte 2 ====================
    map = folium.Map(location=[4.6097, -74.0817], zoom_start=12, control_scale=True)
    mc = MarkerCluster()
    for evento in lt.iterator(lst_rt):
        mc.add_child(
            folium.Marker(
                location=[float(evento["LATITUD"]), float(evento["LONGITUD"])],
                icon=create_icon(evento["GRAVEDAD"]),
            )
        )
    map.add_child(mc)
    leyenda_html = """
    <div style="position: fixed; 
        top: 10px; right: 10px; width: 160px; height: 130px; 
        border:2px solid grey; z-index:9999; font-size:14px;
        background-color: white;
        ">
        <p><strong>Leyenda</strong></p>
        <p style="margin-left: 10px;"><i class="fa fa-circle" style="color:green;"></i> SOLO DANOS</p>
        <p style="margin-left: 10px;"><i class="fa fa-circle" style="color:orange;"></i> CON HERIDOS</p>
        <p style="margin-left: 10px;"><i class="fa fa-circle" style="color:red;"></i> CON MUERTOS</p>
    </div>
    """
    folium.Marker(
        [4.7128, -74.0060],
        icon=folium.DivIcon(icon_size=(150, 90), icon_anchor=(0, 0), html=leyenda_html),
    ).add_to(map)
    return accidentes, map


# Funciones utilizadas para comparar elementos dentro de una lista


def create_icon(gravedad):
    color_gravedad = {
        "SOLO DANOS": "green",
        "CON HERIDOS": "orange",
        "CON MUERTOS": "red",
    }
    color = color_gravedad[gravedad]
    return folium.Icon(color=color, icon="map-marker")


def haversine(lat1, lon1, lat2, lon2):
    # Convertir las coordenadas de latitud y longitud de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calcular la diferencia de latitud y longitud
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Aplicar la fórmula de Haversine
    a = math.sqrt(
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    )
    d = 2 * math.asin(a) * 6371

    return d


def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    # TODO: Crear función comparadora de la lista
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
    # TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    # TODO: Crear función de ordenamiento
    pass


# Funciones de Comparacion


def compareIds(id1, id2):
    """
    Compara dos accidentees
    """
    if id1["CODIGO_ACCIDENTE"] == id2["CODIGO_ACCIDENTE"]:
        return 0
    elif id1["CODIGO_ACCIDENTE"] > id2["CODIGO_ACCIDENTE"]:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if date1 == date2:
        return 0
    elif date1 > date2:
        return 1
    else:
        return -1


def compareHours(date1, date2):
    """
    Compara dos fechas
    """
    if date1 == date2:
        return 0
    elif date1 > date2:
        return 1
    else:
        return -1


def compareMap(year, data):
    bookentry = me.getKey(data)
    if year == bookentry:
        return 0
    elif year > bookentry:
        return 1
    else:
        return -1


def compareClasses(class1, class2):
    """
    Compara dos clases de accidentes
    """
    class_acc = me.getKey(class2)
    if class1 == class_acc:
        return 0
    elif class1 > class_acc:
        return 1
    else:
        return -1


def cmp_accidentes_by_full_date(accidente1, accidente2):
    """
    Devuelve verdadero (True) si la fecha de accidente1 es mayor que la fecha de accidente2, de lo contrario devuelva falso (False).
    Args:
    accidente1: información del primer registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    accidente2: información del segundo registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    “Descuentos tributarios”
    """
    fecha_1 = datetime.datetime.fromisoformat(
        accidente1["FECHA_HORA_ACC"][:-3].replace("/", "-")
    )
    fecha_2 = datetime.datetime.fromisoformat(
        accidente2["FECHA_HORA_ACC"][:-3].replace("/", "-")
    )
    if fecha_1 > fecha_2:
        return True
    else:
        return False


def cmp_accidentes_date(accidente1, accidente2):
    """
    Devuelve verdadero (True) si la fecha de accidente1 es mayor que la fecha de accidente2, de lo contrario devuelva falso (False).
    Args:
    accidente1: información del primer registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    accidente2: información del segundo registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    “Descuentos tributarios”
    """
    fecha_1 = datetime.datetime.fromisoformat(
        accidente1["FECHA_HORA_ACC"][:-3].replace("/", "-")
    )
    fecha_2 = datetime.datetime.fromisoformat(
        accidente2["FECHA_HORA_ACC"][:-3].replace("/", "-")
    )
    hora_1 = datetime.datetime.strptime(accidente1["HORA_OCURRENCIA_ACC"][:-3], "%H:%M")
    hora_2 = datetime.datetime.strptime(accidente2["HORA_OCURRENCIA_ACC"][:-3], "%H:%M")
    if fecha_1 > fecha_2:
        if hora_1 == hora_2:
            return False
        else:
            return True
    else:
        return False


def cmp_accidentes_by_distance(accidente1, accidente2):
    """
    Devuelve verdadero (True) si la distancia de accidente1 es mayor que la distancia de accidente2, de lo contrario devuelva falso (False).
    Args:ss
    accidente1: información del primer registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    accidente2: información del segundo registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    “Descuentos tributarios”
    """
    global lat_0
    global lon_0
    distance_1 = distancia_haversine(
        lat_0, lon_0, accidente1["LATITUD"], accidente1["LONGITUD"]
    )
    distance_2 = distancia_haversine(
        lat_0, lon_0, accidente2["LATITUD"], accidente2["LONGITUD"]
    )
    if abs(distance_1) < abs(distance_2):
        return True
    else:
        return False


def cmp_accidentes_by_codigo(accidente1, accidente2):
    """
    Devuelve verdadero (True) si la distancia de accidente1 es mayor que la distancia de accidente2, de lo contrario devuelva falso (False).
    Args:ss
    accidente1: información del primer registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    accidente2: información del segundo registro de accidentes que incluye la fecha completa en formato %Y/%m/%d %H:%M:%S
    “Descuentos tributarios”
    """
    if accidente1["CODIGO_ACCIDENTE"] > accidente2["CODIGO_ACCIDENTE"]:
        return True
    else:
        return False


def distancia_haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en kilometros entre dos puntos
    definidos por su latitud y longitud utilizando la
    formula de Haversine.

    lat1, lon1: latitud y longitud del primer punto en grados decimales.
    lat2, lon2: latitud y longitud del segundo punto en grados decimales.
    """
    radio_tierra = 6371  # Radio de la Tierra en kilometros

    # Convertir latitud y longitud a radianes
    lat1_rad, lon1_rad = math.radians(float(lat1)), math.radians(float(lon1))
    lat2_rad, lon2_rad = math.radians(float(lat2)), math.radians(float(lon2))

    # Diferencias de latitud y longitud
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Calculo de la distancia
    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    )
    distancia = 2 * math.asin(math.sqrt(a)) * radio_tierra

    return distancia
