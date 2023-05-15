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
import datetime as dt
import math as ma
assert cf
import folium

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
    dataStructs = {"datos":None, 
                   "fecha": None}
    
    dataStructs ["datos"] = lt.newList(datastructure="ARRAY_LIST")
    dataStructs ["fecha"] = om.newMap(omaptype="RBT", comparefunction= Fecha)
    
    return (dataStructs)

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    nuevoDict = {"CODIGO_ACCIDENTE": int(data["CODIGO_ACCIDENTE"]),
        "FECHA_HORA_ACC": data["FECHA_HORA_ACC"], 
        "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],        
        "LOCALIDAD": data["LOCALIDAD"],
        "DIRECCION": data["DIRECCION"],
        "GRAVEDAD": data["GRAVEDAD"],
        "CLASE_ACC": data["CLASE_ACC"],
        "LATITUD": data["LATITUD"],
        "LONGITUD": data["LONGITUD"],
        "HORA_OCURRENCIA_ACC":data["HORA_OCURRENCIA_ACC"]}
    
    datos = dict(nuevoDict)
    datos.pop("DIA_OCURRENCIA_ACC")
    datos.pop("HORA_OCURRENCIA_ACC")
    lt.addLast(data_structs ["datos"], datos )
    
    om.put(data_structs ["fecha"], data["FECHA_HORA_ACC"], nuevoDict)
    
    return data_structs
    
# Funciones para creacion de datos
def Fecha(elm1, elm2):
    if elm1 > elm2:
        return -1
    elif elm1 < elm2:
        return 1
    else:
        return 0


def req_1(data_structs, fechaInicia, fechaFinal ):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    fechaInicia = fechaInicia +str(" 00:00:00+00")
    fechaFinal = fechaFinal + str(" 23:59:59+00")
    llavesImportantes = om.keys(data_structs ["fecha"], fechaFinal, fechaInicia) 
    lista = lt.newList(datastructure="ARRAY_LIST")
    for elemnt in lt.iterator(llavesImportantes):
        datos = dict(me.getValue(om.get(data_structs ["fecha"], elemnt)))
        datos.pop("HORA_OCURRENCIA_ACC")
        lt.addLast(lista, datos)
    return lista["elements"]



def req_2(data_structs, mes, año, horaInicio, HoraFinal):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    rango1 = año + "/" + str(mes) + "/01" + " " + horaInicio + ":00+00"
    rango2 = año + "/" + str(mes) + "/31" + " " + HoraFinal + ":00+00"
    llavesImportantes = om.values(data_structs ["fecha"], rango2,  rango1) 
    lista = lt.newList(datastructure="ARRAY_LIST")
    for elemnt in lt.iterator(llavesImportantes):
        elmetoHora =elemnt["HORA_OCURRENCIA_ACC"]
        if len(elemnt["HORA_OCURRENCIA_ACC"]) < 8:
            elmetoHora= "0"+elemnt["HORA_OCURRENCIA_ACC"]
        if (horaInicio) <= elmetoHora <= (HoraFinal): 
            datos = dict(elemnt)
            datos.pop("HORA_OCURRENCIA_ACC")
            lt.addLast(lista, datos)
    return lista["elements"]


def req_3(data_structs, direccion, accidente):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    llaves = om.valueSet(data_structs['fecha'])
    lst = lt.newList(datastructure='ARRAY_LIST')
    for elmt in lt.iterator(llaves):
        if accidente.lower() == elmt['CLASE_ACC'].lower() and direccion.lower() in elmt['DIRECCION'].lower():
            data = dict(elmt)
            data.pop('CLASE_ACC')
            data.pop('HORA_OCURRENCIA_ACC')
            lt.addLast(lst, data)
    merg.sort(lst, cmpFecha)
    return lst


def req_4(data_structs, fechaInicia, fechaFinal, gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    fechaInicia = fechaInicia +str(" 00:00:00+00")
    fechaFinal = fechaFinal + str(" 23:59:59+00")
    llavesImportantes = om.values(data_structs ["fecha"],   fechaFinal, fechaInicia)
    ListaGraveda = lt.newList(datastructure="ARRAY_LIST")
        
    for item in lt.iterator(llavesImportantes ):
        if item["GRAVEDAD"].lower() == gravedad.lower():
            datos = dict(item)
            datos.pop("GRAVEDAD")
            datos.pop('HORA_OCURRENCIA_ACC')
            lt.addLast(ListaGraveda, datos)
    
    return ListaGraveda["elements"]


def req_5(data_structs, mes, año, localidad):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    Fecha_inicio =  año + "/" + str(mes) + "/01" + str(" 00:00:00+00")
    Fecha_fin = año + "/" + str(mes) + "/31" + str(" 23:59:59+00")
    acc_count = 0
    acc_map = om.values(data_structs ["fecha"], Fecha_fin, Fecha_inicio)
    acc_lista = lt.newList(datastructure="ARRAY_LIST")

    for acc in lt.iterator(acc_map):
        if acc is not None and acc["LOCALIDAD"].lower() == localidad.lower():
            accidentes= dict(acc)
            accidentes.pop("LOCALIDAD")
            lt.addLast(acc_lista, accidentes)
            acc_count += 1
            if acc_count == 10:
                break

    return acc_lista["elements"]

def req_6(data_structs, año, mes, coordenadas, Radio, top):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    latitud1, longitud1=  coordenadas
    rango1 = año + "/" + str(mes) + "/01" + " 00:00:00+00" 
    rango2 = año + "/" + str(mes) + "/31" + " 23:59:59+00"
    llavesImportantes = om.values(data_structs ["fecha"], rango2,  rango1)
    latitud1 = ma.radians(float(latitud1))
    longitud1 = ma.radians(float(longitud1))
    mapa = om.newMap(omaptype='RBT', comparefunction= ordenar)
    for elemnt in lt.iterator(llavesImportantes):
        latitud2 = ma.radians(float(elemnt["LATITUD"]))
        longitud2 = ma.radians(float(elemnt["LONGITUD"]))
        D = 2*(ma.asin(ma.sqrt((ma.sin((latitud2-latitud1)/2)**2)+ma.cos(latitud1)*ma.cos(latitud2)*(ma.sin((longitud2-longitud1)/2)**2))))*6371
        if D <= float(Radio):
            datos = dict(elemnt)
            datos.pop("HORA_OCURRENCIA_ACC")
            om.put(mapa, D,datos)
    
    llaves = om.valueSet(mapa)
    if int(top)  >= lt.size(llaves):
        lista = llaves
    else:
        lista = lt.subList(llaves, 1, int(top))
    listaImprimir= []
    for elemnto in lt.iterator(lista):
        listaImprimir.append(elemnto)
    return (listaImprimir)

def ordenar(elm1, elm2):
    if elm1 > elm2:
        return 1
    elif elm1 < elm2:
        return -1
    else:
        return 0

def req_7(data_structs, año, mes ):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    rango1 = año + "/" + str(mes) + "/01" + " 00:00:00+00" 
    rango2 = año + "/" + str(mes) + "/31" + " 23:59:59+00"
    llavesImportantes = om.values(data_structs ["fecha"], rango2,  rango1)
    #dia del mes
    tbaladiames = om.newMap(omaptype = "RBT", comparefunction=ordenar)
    for item in lt.iterator(llavesImportantes):
        datos = dict(item)
        datos.pop("HORA_OCURRENCIA_ACC")
        dia = datos["FECHA_HORA_ACC"][8:10]
        llave = om.contains(tbaladiames, dia)
        if llave:
            elementodiames = me.getValue(om.get(tbaladiames, dia) )
            lt.addLast(elementodiames, item) 
        else:
            om.put(tbaladiames,dia, lt.newList(datastructure="ARRAY_LIST"))
            elementodiames = me.getValue(om.get(tbaladiames, dia))
            lt.addLast(elementodiames, item)
    
    tabalahora = om.newMap(omaptype = "RBT", comparefunction=ordenar)
    
    for item in lt.iterator(llavesImportantes):
        hora = int(str(item["HORA_OCURRENCIA_ACC"][0:2]).replace(":", ""))
        llave = om.contains(tabalahora, hora)
        if llave:
            elementohora = me.getValue(om.get(tabalahora, hora))+1
            om.put(tabalahora,hora, elementohora ) 
        else:
            om.put(tabalahora,hora, 1)
    
    return  tbaladiames, tabalahora

def req_8(data_structs, fechaInicia, fechaFinal, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    fechaInicia = fechaInicia +str(" 00:00:00+00")
    fechaFinal = fechaFinal + str(" 23:59:59+00")
    llavesImportantes = om.keys(data_structs["fecha"], fechaFinal, fechaInicia)
    lista = lt.newList(datastructure='ARRAY_LIST')
    mapa = folium.Map(location=[4.658275, -74.051290])
    x = 0

    for elemnt in lt.iterator(llavesImportantes):
        datos = dict(me.getValue(om.get(data_structs ["fecha"], elemnt)))
        datos.pop("HORA_OCURRENCIA_ACC")
        lt.addLast(lista, datos)
    for accidente in lista['elements']:
        if accidente['CLASE_ACC'] == clase:
            x += 1
            latitud = accidente['LATITUD']
            longitud = accidente['LONGITUD']
            color = ''
            tooltip = ''
            if accidente['GRAVEDAD'] == 'SOLO DANOS':
                color = 'orange'
                tooltip = 'Solo Daños'
            elif accidente['GRAVEDAD'] == 'CON HERIDOS':
                color = 'blue'
                tooltip = 'Con heridos'
            elif accidente['GRAVEDAD'] == 'CON MUERTOS':
                color = 'red'
                tooltip = 'Con Muerto'
            folium.Marker([float(latitud), float(longitud)], icon=folium.Icon(color=color),tooltip=tooltip).add_to(mapa)
    folium.Map.show_in_browser(mapa)
    return(x, mapa)
    


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpFecha(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    return (data_1["FECHA_HORA_ACC"] > data_2["FECHA_HORA_ACC"])