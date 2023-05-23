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
assert cf
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    mapa= mp.newMap(3,
                maptype='PROBING',
                loadfactor=0.5,
                cmpfunction=compare_map)
    fechas= om.newMap("BST",
                      compare_arbol)
    casos=om.newMap("BST",
                      compare_arbol_caso)
    mp.put(mapa,"fechas", fechas)
    mp.put(mapa, "casos", casos)
    mp.put(mapa, "datas", None)
    return mapa
    


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs, data)

    return data_structs


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def crear_datastructs_fecha(control, datas):
    datas= sort(datas, 3)
    first= lt.firstElement(datas)
    anio= first["ANO_OCURRENCIA_ACC"]
    arbol_fechas= mp.get(control, "fechas")
    arbol_fechas= me.getValue(arbol_fechas)
    for data in lt.iterator(datas):
        if anio == data["ANO_OCURRENCIA_ACC"] and data != first :
            arbol_fechas= crear_arbol_mes(data, arbol_fechas, anio)
        
        else:
            fecha=data["FECHA_OCURRENCIA_ACC"]
            fecha=fecha.strip(" ")
            fecha=fecha.split("/")
            dia=int(fecha[2])
            mes=int(fecha[1])
            anio=data["ANO_OCURRENCIA_ACC"]
            lista=lt.newList(datastructure="ARRAY_LIST",
                                      cmpfunction=compare)
            lt.addLast(lista, data)
            arbol_mes=om.newMap("RBT",
                      compare_arbol)
            arbol_dia=om.newMap("RBT",
                      compare_arbol)
            om.put(arbol_dia, dia, lista)
            om.put(arbol_mes, mes, arbol_dia)
            om.put(arbol_fechas,anio, arbol_mes)
            
    mp.put(control, "fechas", arbol_fechas)
    return control
            
def crear_arbol_mes(data, arbol, anio):
    fecha=data["FECHA_OCURRENCIA_ACC"]
    fecha=fecha.strip(" ")
    fecha=fecha.split("/")
    dia=int(fecha[2])
    mes=int(fecha[1])
    arbol_meses= om.get(arbol, anio)
    arbol_meses=me.getValue(arbol_meses)
    if om.contains(arbol_meses, mes):
        arbol_meses=crear_arbol_dia(arbol_meses, data,mes, dia)
    else:
        lista=lt.newList(datastructure="ARRAY_LIST",
                                      cmpfunction=compare)
        lt.addLast(lista, data)
        arbol_dia=om.newMap("RBT",
                compare_arbol)
        om.put(arbol_dia, dia, lista)
        om.put(arbol_meses, mes, arbol_dia)
    
    om.put(arbol, anio, arbol_meses)
    
    return arbol

def crear_arbol_dia(arbol_meses, data,mes, dia):
    arbol_dias= om.get(arbol_meses, mes)
    arbol_dias= me.getValue(arbol_dias)
    if om.contains(arbol_dias, dia):
        lista=om.get(arbol_dias, dia)
        lista=me.getValue(lista)
        lt.addLast(lista, data)
        om.put(arbol_dias, dia, lista)
        
        
    else:
        lista=lt.newList(datastructure="ARRAY_LIST",
                                      cmpfunction=compare)
        lt.addLast(lista, data) 
        om.put(arbol_dias, dia, lista)
    
    om.put(arbol_meses, mes, arbol_dias)
    
    return arbol_meses
                        
        
            
        
def crear_datastructs_casos(control, datas):
    arbol_casos= mp.get(control, "casos")
    arbol_casos= me.getValue(arbol_casos)
    for data in lt.iterator(datas):
        caso=data["CLASE_ACC"]
        if om.contains(arbol_casos, caso):
            lista_caso=om.get(arbol_casos,caso)
            lista_caso=me.getValue(lista_caso)
            lt.addLast(lista_caso, data)
            om.put(arbol_casos, caso, lista_caso)
        
        else:
            lista=lt.newList(datastructure="ARRAY_LIST",
                                      cmpfunction=compare)
            lt.addLast(lista, data)
            om.put(arbol_casos, caso, lista)
        
    mp.put(control, "casos", arbol_casos)
    
    return control

def agregar_datas(control, datas):
    mp.put(control, "datas", datas)
    return control

def new_list():
    data_structs=lt.newList(datastructure="ARRAY_LIST",
                                      cmpfunction=compare)
    return data_structs

def RBT_rango_fechas_1(mapa, inicio, final):
    arbol=om.newMap("RBT", 
                    compare_arbol_caso)
    dia_in, mes_in, anio_in= divir_fecha(inicio)
    dia_fin, mes_fin, anio_fin= divir_fecha(final)
    if anio_in==anio_fin:
        arb_meses=om.get(mapa, anio_in)
        arb_meses=me.getValue(arb_meses)
        if mes_in==mes_fin:
            mes= om.get(arb_meses, mes_in)
            mes= me.getValue(mes)
            agregar=om.values(mes, dia_in, dia_fin)
            arbol= agregar_arbol(agregar, arbol)
            
        else:            
            meses= om.values(arb_meses, mes_in, mes_fin)
            first_mes=lt.firstElement(meses)
            last_mes=lt.lastElement(meses)
            meses2=meses
            for mes in lt.iterator(meses2):
                if mes == first_mes:
                    max = om.maxKey(mes)
                    agregar= om.values(mes, dia_in, max)
                    arbol= agregar_arbol(agregar, arbol)
                elif mes == last_mes:
                    min = om.minKey(mes)
                    agregar= om.values(mes, min, dia_fin)
                    arbol= agregar_arbol(agregar, arbol)
                else:
                    agregar= om.valueSet(mes)
                    arbol= agregar_arbol(agregar, arbol)                  
                            
    else:
        anios=om.values(mapa, anio_in, anio_fin)
        first_anio=lt.firstElement(anios)
        last_anio=lt.lastElement(anios)
        for anio in lt.iterator(anios):
            if anio == first_anio:
                max = om.maxKey(anio)
                meses_min= om.values(anio, mes_in, max)
                first_mes=lt.firstElement(meses_min)
                last_mes=lt.lastElement(meses_min)
                meses2=meses_min
                for mes in lt.iterator(meses2):
                    if mes == first_mes:
                        max = om.maxKey(mes)
                        agregar= om.values(mes, dia_in, max)
                        arbol= agregar_arbol(agregar, arbol)
                    elif mes == last_mes:
                        min = om.minKey(mes)
                        agregar= om.values(mes, min, dia_fin)
                        arbol= agregar_arbol(agregar, arbol)
                    else:
                        agregar= om.valueSet(mes)
                        arbol= agregar_arbol(agregar, arbol)
            elif last_anio== anio:
                min = om.minKey(anio)
                meses_max= om.values(anio, min, mes_fin)
                first_mes=lt.firstElement(meses_max)
                last_mes=lt.lastElement(meses_max)
                meses2=meses_max
                for mes in lt.iterator(meses2):
                    if mes == first_mes:
                        max = om.maxKey(mes)
                        agregar= om.values(mes, dia_in, max)
                        arbol= agregar_arbol(agregar, arbol)
                    elif mes == last_mes:
                        min = om.minKey(mes)
                        agregar= om.values(mes, min, dia_fin)
                        arbol= agregar_arbol(agregar, arbol)
                    else:
                        agregar= om.valueSet(mes)
                        arbol= agregar_arbol(agregar, arbol)
            
            else:
                meses=om.valueSet(anio)
                for mes in lt.iterator(meses):
                    dias= om.valueSet(mes)
                    arbol= agregar_arbol(agregar, arbol)
    return arbol

def RBT_rango_fechas(mapa, inicio, final):
    arbol=om.newMap("RBT", 
                    compare_arbol_caso)
    dia_in, mes_in, anio_in= divir_fecha(inicio)
    dia_fin, mes_fin, anio_fin= divir_fecha(final)
    if anio_in==anio_fin:
        arb_meses=om.get(mapa, anio_in)
        arb_meses=me.getValue(arb_meses)
        if mes_in==mes_fin:
            mes= om.get(arb_meses, mes_in)
            mes= me.getValue(mes)
            agregar=om.values(mes, dia_in, dia_fin)
            arbol= agregar_arbol_fecha(agregar, arbol)
            
        else:            
            meses= om.values(arb_meses, mes_in, mes_fin)
            first_mes=lt.firstElement(meses)
            last_mes=lt.lastElement(meses)
            meses2=meses
            for mes in lt.iterator(meses2):
                if mes == first_mes:
                    max = om.maxKey(mes)
                    agregar= om.values(mes, dia_in, max)
                    arbol= agregar_arbol_fecha(agregar, arbol)
                elif mes == last_mes:
                    min = om.minKey(mes)
                    agregar= om.values(mes, min, dia_fin)
                    arbol= agregar_arbol_fecha(agregar, arbol)
                else:
                    agregar= om.valueSet(mes)
                    arbol= agregar_arbol_fecha(agregar, arbol)                  
                            
    else:
        anios=om.values(mapa, anio_in, anio_fin)
        first_anio=lt.firstElement(anios)
        last_anio=lt.lastElement(anios)
        for anio in lt.iterator(anios):
            if anio == first_anio:
                max = om.maxKey(anio)
                meses_min= om.values(anio, mes_in, max)
                first_mes=lt.firstElement(meses_min)
                last_mes=lt.lastElement(meses_min)
                meses2=meses_min
                for mes in lt.iterator(meses2):
                    if mes == first_mes:
                        max = om.maxKey(mes)
                        agregar= om.values(mes, dia_in, max)
                        arbol= agregar_arbol_fecha(agregar, arbol)
                    elif mes == last_mes:
                        min = om.minKey(mes)
                        agregar= om.values(mes, min, dia_fin)
                        arbol= agregar_arbol_fecha(agregar, arbol)
                    else:
                        agregar= om.valueSet(mes)
                        arbol= agregar_arbol_fecha(agregar, arbol)
            elif last_anio== anio:
                min = om.minKey(anio)
                meses_max= om.values(anio, min, mes_fin)
                first_mes=lt.firstElement(meses_max)
                last_mes=lt.lastElement(meses_max)
                meses2=meses_max
                for mes in lt.iterator(meses2):
                    if mes == first_mes:
                        max = om.maxKey(mes)
                        agregar= om.values(mes, dia_in, max)
                        arbol= agregar_arbol_fecha(agregar, arbol)
                    elif mes == last_mes:
                        min = om.minKey(mes)
                        agregar= om.values(mes, min, dia_fin)
                        arbol= agregar_arbol_fecha(agregar, arbol)
                    else:
                        agregar= om.valueSet(mes)
                        arbol= agregar_arbol_fecha(agregar, arbol)
            
            else:
                meses=om.valueSet(anio)
                for mes in lt.iterator(meses):
                    dias= om.valueSet(mes)
                    arbol= agregar_arbol_fecha(agregar, arbol)
    return arbol
            
def agregar_arbol_fecha(data_struts, arbol):
    for dia in lt.iterator(data_struts):
        for data in lt.iterator(dia):
            if om.contains(arbol, data["FECHA_OCURRENCIA_ACC"]):
                entry= om.get(arbol, data["FECHA_OCURRENCIA_ACC"])
                lista= me.getValue(entry)
                lt.addLast(lista, data)
                om.put(arbol, data["FECHA_OCURRENCIA_ACC"], lista)
            
            else:
                lista=lt.newList(datastructure="ARRAY_LIST",
                                      cmpfunction=compare) 
                lt.addLast(lista, data)
                om.put(arbol, data["FECHA_OCURRENCIA_ACC"], lista)
            
    return arbol         

def obtener_primero(list):
    anio= lt.firstElement(list)
    meses= om.valueSet(anio)
    dias= lt.firstElement(meses)
    dias= om.valueSet(dias)
    dia= lt.firstElement(dias)
    dia= lt.firstElement(dia)
    
    return dia 

def obtener_ultimo(list):
    anio= lt.lastElement(list)
    meses= om.valueSet(anio)
    dias= lt.lastElement(meses)
    dias= om.valueSet(dias)
    dia= lt.lastElement(dias)
    dia= lt.lastElement(dia)
    
    return dia 
    
    
    anio_in= om.valueSet()

def agregar_arbol(data_struts, arbol):
    for dia in lt.iterator(data_struts):
        for data in lt.iterator(dia):
            om.put(arbol, data["FORMULARIO"], data)
            
    return arbol

# Funciones de consulta

def calcular_haversine(lat1, lon1, lat2, lon2):
    radio = 6371

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = radio * c

    return distancia



def divir_fecha(fecha):
    fecha= fecha.split("/")
    return int(fecha[0]), int(fecha[1]), int(fecha[2])

def sacar_hora(data_structs):
    hora=data_structs["FECHA_HORA_ACC"].split(" ")
    hora=hora[1]
    hora=hora.split(":")
    return int(hora[0])

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def tres_prim(data_structs):    
    if lt.size(data_structs)<=3:
        return data_structs
    else:
        data_structs2=lt.newList(datastructure="ARRAY_LIST")
        primer = lt.firstElement(data_structs)
        segundo= lt.getElement(data_structs, 2)
        tercero= lt.getElement(data_structs, 3)
        
        lt.addLast(data_structs2, primer)
        lt.addLast(data_structs2, segundo)
        lt.addLast(data_structs2, tercero)
        
        
        return data_structs2
    
def tres_ult(data_structs):
    if lt.size(data_structs)<=3:
        return data_structs
    else:
        data_structs2=lt.newList(datastructure="ARRAY_LIST")
        ultimo= lt.lastElement(data_structs)
        penultimo=lt.getElement(data_structs, -2)
        antepenultimo=lt.getElement(data_structs, -3)
        lt.addLast(data_structs2, antepenultimo)
        lt.addLast(data_structs2, penultimo)
        lt.addLast(data_structs2, ultimo)
        return data_structs2
    
def diez_prim(data_structs):
    if lt.size(data_structs)<=10:
        return data_structs
    else:
        data_structs2=lt.newList(datastructure="ARRAY_LIST")
        primer = lt.firstElement(data_structs)
        segundo= lt.getElement(data_structs, -9)
        tercero= lt.getElement(data_structs, -8)
        cuarto= lt.getElement(data_structs, -7)
        quinto=lt.getElement(data_structs, -6)
        sexto=lt.getElement(data_structs, -5)
        septimo=lt.getElement(data_structs, -4)
        ocho= lt.getElement(data_structs, -3)
        nueve= lt.getElement(data_structs, -2)
        diez=lt.getElement(data_structs, -1)
        
        lt.addLast(data_structs2, primer)
        lt.addLast(data_structs2, segundo)
        lt.addLast(data_structs2, tercero)
        lt.addLast(data_structs2, cuarto)
        lt.addLast(data_structs2, quinto)
        lt.addLast(data_structs2, sexto)
        lt.addLast(data_structs2, septimo)
        lt.addLast(data_structs2, ocho)
        lt.addLast(data_structs2, nueve)
        lt.addLast(data_structs2, diez)
        
        return data_structs2
    
def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return int(lt.size(data_structs))


def req_1(data_structs, inicio, final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    RBT= RBT_rango_fechas_1(arbol, inicio, final)
    altura= om.height(RBT)
    nodos= om.keySet(RBT)
    nodos= lt.size(nodos)
    elementos= om.valueSet(RBT)
    elementos_size= lt.size(elementos) 
    elementos= sort(elementos, 5)
    return elementos, altura, nodos, elementos_size


def req_2(data_structs, hora_inc, hora_fin, anio, mes):
    """
    Función que soluciona el requerimiento 2
    """
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, int(anio))
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, mes)
    arbol=me.getValue(arbol)
    hora_inc= hora_inc.replace(":", "")
    hora_fin= hora_fin.replace(":", "")
    dias= om.valueSet(arbol)
    respuesta= lt.newList(datastructure="ARRAY_LIST")
    for dia in lt.iterator(dias):
        for data in lt.iterator(dia):
            hora=data["HORA_OCURRENCIA_ACC"].replace(":", "")
            if int(hora)>= int(hora_inc) and int(hora)<=int(hora_fin):
                lt.addFirst(respuesta, data)
            
    return respuesta
                


def req_3(data_structs,clase_acc,Direccion):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    arbol_key_val= mp.get(data_structs, "casos")
    arbol_array= me.getValue(arbol_key_val)
    arbol_hash= om.get(arbol_array, clase_acc)
    registro= me.getValue(arbol_hash)
    respuesta= lt.newList(datastructure="ARRAY_LIST")
    
    for data in lt.iterator(registro):
        Direccion_data= data["DIRECCION"]
        if  Direccion.lower() in Direccion_data.lower():
            lt.addLast(respuesta, data)
                
    return merg.sort(respuesta,sort_req_1)
            


def req_4(data_structs, fecha_ini, fecha_fin, clase_acc):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    respuesta = lt.newList()
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    rbt = RBT_rango_fechas(arbol, fecha_ini, fecha_fin)
    rbt_size = om.size(RBT_rango_fechas_1(arbol, fecha_ini, fecha_fin))
    i = 0
    dia = me.getValue(mp.get(rbt, om.maxKey(rbt)))

    while i < 5:
        
        if lt.size(dia) == 0:
            om.deleteMax(rbt)
            if om.isEmpty(rbt):
                return respuesta, rbt_size
            dia = me.getValue(mp.get(rbt, om.maxKey(rbt)))
        min = lt.lastElement(dia)
        if min['GRAVEDAD'] == clase_acc:
            lt.addLast(respuesta, min)
            i+=1
        lt.removeLast(dia)
        
        
    
    return respuesta, rbt_size

def req_5(data_structs, localidad, anio, mes):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, int(anio))
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, mes)
    arbol=me.getValue(arbol)
    respuesta= lt.newList(datastructure="ARRAY_LIST")
    dias= om.valueSet(arbol)
    for dia in lt.iterator(dias):
        for data in lt.iterator(dia):
            localidad_data=data["LOCALIDAD"]
            if localidad.lower()==localidad_data.lower():
                lt.addFirst(respuesta, data)
                
    return respuesta


def req_6(data_structs, top, lat, lon, rad, anio, mes):
    """
    Función que soluciona el requerimiento 6
    """
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, int(anio))
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, mes)
    arbol=me.getValue(arbol)
    respuesta= om.newMap("RBT", 
                    compare_arbol_caso)
    dias= om.valueSet(arbol)
    for dia in lt.iterator(dias):
        for data in lt.iterator(dia):
            lat2=float(data["LATITUD"])
            lon2=float(data["LONGITUD"])
            distancia=calcular_haversine(lat,lon,lat2,lon2)
            if distancia<= float(rad):
                if int(om.size(respuesta))<int(top):
                    om.put(respuesta, distancia, data)
                else:
                    max= om.maxKey(respuesta)
                    if distancia<max:
                        om.deleteMax(respuesta)
                        om.put(respuesta,distancia, data)
                        
    return om.valueSet(respuesta)


def req_7(data_structs, anio, mes):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, int(anio))
    arbol= me.getValue(arbol)
    arbol= om.get(arbol, mes)
    arbol=me.getValue(arbol)
    lista=lt.newList(datastructure="ARRAY_LIST")
    queue= qu.newQueue()
    lista_hora=lt.newList(datastructure="ARRAY_LIST")
    
    dias= om.valueSet(arbol)
    for dia in lt.iterator(dias):
        dia= sort(dia, 3)
        first=lt.firstElement(dia)
        dia_invertido=sort(dia, 4)
        last= lt.firstElement(dia_invertido)
        lt.addLast(lista, first)
        lt.addLast(lista, last)
        lista= sort(lista, 2)
        qu.enqueue(queue, lista)
        lista=lt.newList(datastructure="ARRAY_LIST")
        for data in lt.iterator(dia):
            hora=sacar_hora(data)
            lt.addLast(lista_hora, hora)
            
    lista_hora= sort(lista_hora, 6)
            
    return queue, lista_hora     
            

def req_8(data_structs, inicio, final, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    color = lt.newList(datastructure="ARRAY_LIST")
    lista = lt.newList(datastructure="ARRAY_LIST")
    arbol= mp.get(data_structs, "fechas")
    arbol= me.getValue(arbol)
    rbt= RBT_rango_fechas_1(arbol, inicio, final)
    for i in lt.iterator(om.valueSet(rbt)):
        if i["CLASE_ACC"]==clase:
            lt.addLast(lista, i)
            if i["GRAVEDAD"] == "CON MUERTOS":
                lt.addLast(color, "red")
            elif i["GRAVEDAD"] == "CON HERIDOS":
                lt.addLast(color, "orange")
            else:
                lt.addLast(color, "green")
    return lista, color


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if int(data_1["CODIGO_ACCIDENTE"]) > int(data_2["CODIGO_ACCIDENTE"]):
        return 1
    elif int(data_1["CODIGO_ACCIDENTE"]) < int(data_2["CODIGO_ACCIDENTE"]):
        return -1
    else:
        return 0
    
def compare_map(data_1, data_2):
    data_2=me.getKey(data_2)
    if data_1 > data_2:
        return 1
    elif data_1 < data_2:
        return -1
    else:
        return 0
    
def compare_arbol(data_1, data_2):
    if int(data_1) > int(data_2):
        return 1
    elif int(data_1) < int(data_2):
        return -1
    else:
        return 0
def compare_arbol_caso(data_1, data_2):
    if data_1 > data_2:
        return 1
    elif data_1 < data_2:
        return -1
    else:
        return 0


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
    if int(data_1["ANO_OCURRENCIA_ACC"]) < int(data_2["ANO_OCURRENCIA_ACC"]):
            return True
    elif int(data_1["ANO_OCURRENCIA_ACC"]) == int(data_2["ANO_OCURRENCIA_ACC"]):
        return int(data_1["CODIGO_ACCIDENTE"])< int(data_2["CODIGO_ACCIDENTE"])
    else:
        return False


def sort(data_structs, num):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    if num == 1:
        lista=merg.sort(data_structs, sort_criteria)
    elif num ==2:
        lista=merg.sort(data_structs, sort_data)
    elif num == 3:
        lista=merg.sort(data_structs, sort_req_7)
    elif num ==4:
        lista=merg.sort(data_structs, sort_req_7_invertido)
    elif num==5:
        lista=merg.sort(data_structs, sort_req_1)
    elif num==6:
        lista=merg.sort(data_structs, sort_hora_req_7)
    return lista

        
def sort_data(data_1, data_2):
    return data_1["FECHA_HORA_ACC"]<data_2["FECHA_HORA_ACC"]

def sort_req_7(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    if data_1["FECHA_HORA_ACC"]<data_2["FECHA_HORA_ACC"]:
        return True
    elif data_1["FECHA_HORA_ACC"] ==data_2["FECHA_HORA_ACC"]:
        return data_1["CODIGO_ACCIDENTE"]>data_2["CODIGO_ACCIDENTE"]
    else: return False
    
def sort_req_7_invertido(data_1, data_2):
    if data_1["FECHA_HORA_ACC"]>data_2["FECHA_HORA_ACC"]:
        return True
    elif data_1["FECHA_HORA_ACC"] ==data_2["FECHA_HORA_ACC"]:
        return data_1["CODIGO_ACCIDENTE"]>data_2["CODIGO_ACCIDENTE"]
    else: return False

def sort_hora_req_7(data_1, data_2):
    return int(data_1)< int(data_2)
    
    
def sort_req_1(data_1, data_2):
    return data_1["FECHA_HORA_ACC"]>data_2["FECHA_HORA_ACC"]
