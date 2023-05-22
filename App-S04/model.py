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
import calendar as c
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
import datetime
import math as m
import folium
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_catalog():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {
        "data": None,
        "accidentes": None
    }
    catalog["data"] = om.newMap(omaptype= "RBT")
    catalog["accidentes"] = lt.newList("ARRAY_LIST")
    
    return catalog


# Funciones para agregar informacion al modelo

def strafecha(fecha):
    lstfecha = fecha.split("/")
    dia = int(lstfecha[2])
    mes = int(lstfecha[1])
    año = int(lstfecha[0])
    return año,mes,dia

def add_data(catalog, dato):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    map = catalog["data"]
    lista_acc = catalog["accidentes"]
    año,mes,dia = strafecha(dato["FECHA_OCURRENCIA_ACC"])
    fecha = datetime.date(año,mes,dia)
    conjunto = om.get(map, fecha)
    
    if conjunto != None:
        lista = me.getValue(conjunto)
    else:
        lista = lt.newList("ARRAY_LIST")
      
    lt.addLast(lista, dato)  
    om.put(map, fecha, lista)
    lt.addLast(lista_acc, dato)
    
    return catalog
   
def resumen_acc(data):
    final = lt.newList("ARRAY_LIST")
    lt.addLast(final, data["FECHA_OCURRENCIA_ACC"])
    lt.addLast(final, data["FECHA_HORA_ACC"])
    lt.addLast(final, data["LOCALIDAD"])
    lt.addLast(final, data["DIRECCION"])
    lt.addLast(final, data["GRAVEDAD"])
    lt.addLast(final, data["CLASE_ACC"])
    lt.addLast(final, data["LATITUD"])
    lt.addLast(final, data["LONGITUD"])
    return final["elements"]

def resumen_acc_2(data):
    final = lt.newList("ARRAY_LIST")
    lt.addLast(final, data["CODIGO_ACCIDENTE"])
    lt.addLast(final, data["DIA_OCURRENCIA_ACC"])
    lt.addLast(final, data["DIRECCION"])
    lt.addLast(final, data["GRAVEDAD"])
    lt.addLast(final, data["CLASE_ACC"])
    lt.addLast(final, data["LOCALIDAD"])
    lt.addLast(final, data["FECHA_HORA_ACC"])
    lt.addLast(final, data["LATITUD"])
    lt.addLast(final, data["LONGITUD"])
    return final["elements"]

def resumen_acc_22(data):
    final = lt.newList("ARRAY_LIST")
    lt.addLast(final, data["CODIGO_ACCIDENTE"])
    lt.addLast(final, data["HORA_OCURRENCIA_ACC"])
    lt.addLast(final, data["FECHA_OCURRENCIA_ACC"])
    lt.addLast(final, data["DIA_OCURRENCIA_ACC"])
    lt.addLast(final, data["LOCALIDAD"])
    lt.addLast(final, data["DIRECCION"])
    lt.addLast(final, data["GRAVEDAD"])
    lt.addLast(final, data["CLASE_ACC"])
    lt.addLast(final, data["LATITUD"])
    lt.addLast(final, data["LONGITUD"])
    return final["elements"]

def resumen_acc_3(data):
    final = lt.newList("ARRAY_LIST")
    lt.addLast(final, data["CODIGO_ACCIDENTE"])
    lt.addLast(final, data["FECHA_HORA_ACC"])
    lt.addLast(final, data["DIA_OCURRENCIA_ACC"])
    lt.addLast(final, data["LOCALIDAD"])
    lt.addLast(final, data["DIRECCION"])
    lt.addLast(final, data["GRAVEDAD"])
    lt.addLast(final, data["CLASE_ACC"])
    lt.addLast(final, data["LATITUD"])
    lt.addLast(final, data["LONGITUD"])
    return final["elements"]

def resumen_acc_4(data):
    final = lt.newList("ARRAY_LIST")
    lt.addLast(final, data["CODIGO_ACCIDENTE"])
    lt.addLast(final, data["FECHA_HORA_ACC"])
    lt.addLast(final, data["DIA_OCURRENCIA_ACC"])
    lt.addLast(final, data["LOCALIDAD"])
    lt.addLast(final, data["DIRECCION"])
    lt.addLast(final, data["CLASE_ACC"])
    lt.addLast(final, data["LATITUD"])
    lt.addLast(final, data["LONGITUD"])
    return final["elements"]

def resumen_acc_6(data):
    final = lt.newList("ARRAY_LIST")
    lt.addLast(final, data["CODIGO_ACCIDENTE"])
    lt.addLast(final, data["DIA_OCURRENCIA_ACC"])
    lt.addLast(final, data["DIRECCION"])
    lt.addLast(final, data["GRAVEDAD"])
    lt.addLast(final, data["CLASE_ACC"])
    lt.addLast(final, data["FECHA_HORA_ACC"])
    lt.addLast(final, data["LATITUD"])
    lt.addLast(final, data["LONGITUD"])
    return final["elements"]
       
      
def carga_tabulate(catalog):
    lista_acc = catalog["accidentes"] 
    num_accidentes = lt.size(lista_acc)
    lista_tabulatei = []
    lista_tabulatef = []
    lista_tabulatei.append(resumen_acc(lt.getElement(lista_acc, 1)))
    lista_tabulatei.append(resumen_acc(lt.getElement(lista_acc, 2)))
    lista_tabulatei.append(resumen_acc(lt.getElement(lista_acc, 3)))
    lista_tabulatef.append(resumen_acc(lt.getElement(lista_acc, num_accidentes-2)))
    lista_tabulatef.append(resumen_acc(lt.getElement(lista_acc, num_accidentes-1)))
    lista_tabulatef.append(resumen_acc(lt.getElement(lista_acc, num_accidentes)))
    
    return lista_tabulatei, lista_tabulatef , num_accidentes

# Funciones de consulta


def req_1(catalog, fi, ff):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    mapa = catalog["data"]
    ai,mi,di = strafecha(fi)
    af,mf,df = strafecha(ff)
    valores = om.values(mapa, datetime.date(ai,mi,di), datetime.date(af,mf,df))
    tabla_tabulate = []
    size = 0
    for ldia in lt.iterator(valores):
        size += lt.size(ldia)
        quk.sort(ldia, hora_sortcriteria)
        for acc in lt.iterator(ldia):
            dato = resumen_acc_2(acc)
            tabla_tabulate.append(dato)
    
    altura_arbol = om.height(mapa)
    tamaño_arbol = om.size(mapa)
    me_llave = om.minKey(mapa)
    ma_llave = om.maxKey(mapa)
    tabla_tabulate.reverse()  
       
    return tabla_tabulate, size, altura_arbol, tamaño_arbol, me_llave, ma_llave


def req_2(catalog, fi, ff, hi, hf):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    mapa = catalog["data"]
    ai,mi,di = strafecha(fi)
    af,mf,df = strafecha(ff)
    valores = om.values(mapa, datetime.date(ai,mi,di), datetime.date(af,mf,df))
    tabla = lt.newList("ARRAY_LIST")
    tabla_tabulate = []
    size = 0
    for ldia in lt.iterator(valores):
        for acc in lt.iterator(ldia):
            hora_acc = acc["HORA_OCURRENCIA_ACC"]
            if hi <= hora_acc <= hf:
                dato = resumen_acc_22(acc)
                size += 1
                lt.addLast(tabla, dato)
    
    quk.sort(tabla, req2_sortcriteria)
    for acc in lt.iterator(tabla):
        tabla_tabulate.append(acc)
    return tabla_tabulate, size
           
                
def req_3(catalog, clase, calle):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    mapa = catalog["data"]
    final = lt.newList("ARRAY_LIST")
    valores = om.valueSet(mapa)
    for valor in lt.iterator(valores):
        for acc in lt.iterator(valor):
            if clase.lower() in acc["CLASE_ACC"].lower() and calle.lower() in acc["DIRECCION"].lower():
                lt.addLast(final, acc)
        
    if lt.size(final) != 0:
                  
        quk.sort(final, req3_sortcriteria)

        lista_tabulate = []
        lista_tabulate.append(resumen_acc_3(lt.getElement(final, 1)))
        lista_tabulate.append(resumen_acc_3(lt.getElement(final, 2)))
        lista_tabulate.append(resumen_acc_3(lt.getElement(final, 3)))
        size = lt.size(final)
        
    else:
        return None, None
    
    return lista_tabulate, size
    
    
def req_4(data_structs, inicio, final, gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    mapa = data_structs["data"]
    ai,mi,di = strafecha(inicio)
    af,mf,df = strafecha(final)
    valores = om.values(mapa, datetime.date(ai,mi,di), datetime.date(af,mf,df))
    accidentes = []
    for ldia in lt.iterator(valores):
        quk.sort(ldia, hora_sortcriteria)
        for acc in lt.iterator(ldia):
            if gravedad in acc["GRAVEDAD"]:
                dato = resumen_acc_4(acc)
                accidentes.append(dato)
    accidentes.reverse()
    return accidentes, inicio, final, gravedad


def req_5(data_structs,l,m,a):
    """
    Función que soluciona el requerimiento 5
    """
    # Se obtiene el ultimo dia del mes para dicho mes en dicho año
    d = c.monthrange(int(a), int(m))
    df = d[1]
    mapa = data_structs['data']
    # Obtenemos los valores para este mes en dicho año
    valores = om.values(mapa, datetime.date(a,m,1), datetime.date(a,m,df))
    l_tab = []
    tot_ac = 0
    for lista in lt.iterator(valores):
        merg.sort(lista, hora_sortcriteria)
        for ac in lt.iterator(lista):
            if l == ac["LOCALIDAD"]:
                ac_l = {
                    'CODIGO_ACCIDENTE':ac['CODIGO_ACCIDENTE'],
                    'DIA_OCURRENCIA_ACC':ac['DIA_OCURRENCIA_ACC'],
                    'DIRECCION':ac['DIRECCION'],
                    'GRAVEDAD':ac['GRAVEDAD'],
                    'CLASE_ACC':ac['CLASE_ACC'],
                    'FECHA_HORA_ACC':ac['FECHA_HORA_ACC'],
                    'LATITUD':ac['LATITUD'],
                    'LONGITUD':ac['LONGITUD']
                }
                l_tab += [ac_l]
                tot_ac += 1
    if len(l_tab) > 10:
        return l_tab[::-1][:11], tot_ac
    else:
        return l_tab[::-1], tot_ac

def rad(distancia_en_grados):
    return m.radians(distancia_en_grados)

def distancia(lat1, lon1, lat2, lon2):

    distancia_final = 2*(m.asin(m.sqrt(pow(m.sin((lat2-lat1)/2), 2)+(m.cos(lat1)*m.cos(lat2)*pow(m.sin((lon2-lon1)/2), 2)))))*6371
    return distancia_final

def req_6(catalog, fi, ff, latg, long, radio, nacc):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    mapa = catalog["data"]
    latc = rad(latg)
    lonc = rad(long)
    ai,mi,di = strafecha(fi)
    af,mf,df = strafecha(ff)
    valores = om.values(mapa, datetime.date(ai,mi,di), datetime.date(af,mf,df))
    lista_final = lt.newList("ARRAY_LIST")
    
    
    for ldia in lt.iterator(valores):
        for acc in lt.iterator(ldia):
            latacc = m.radians(float(acc["LATITUD"]))
            lonacc = m.radians(float(acc["LONGITUD"]))
            dist = distancia(latacc, lonacc, latc, lonc)
            if dist <= radio:
                acc["DIST_CENTRO"] = dist
                lt.addLast(lista_final, acc)
    
    quk.sort(lista_final, req6_sortcriteria)
    
    lista_tabulate = []
    num_accidentes = lt.size(lista_final)
    if num_accidentes <= nacc:
        for i in range(1, num_accidentes + 1):
            lista_tabulate.append(resumen_acc_6(lt.getElement(lista_final, i)))
    else:
        for i in range(1, nacc + 1):
            lista_tabulate.append(resumen_acc_6(lt.getElement(lista_final, i)))
               
    return lista_tabulate
        
def req_7(data_structs,m,a):
    """
    Función que soluciona el requerimiento 7
    """
    # Se obtiene el ultimo dia del mes para dicho mes en dicho año
    d = c.monthrange(int(a), int(m))
    df = d[1]
    mapa = data_structs['data']
    # Obtenemos los valores para este mes en dicho año
    valores = om.values(mapa, datetime.date(a,m,1), datetime.date(a,m,df))
    ml_tab = []
    l_graf = [
        ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00",
            "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    for lista in lt.iterator(valores):
        merg.sort(lista, hora_sortcriteria)
        if not(lt.isEmpty(lista)):
            air = lt.firstElement(lista)
            afr = lt.lastElement(lista)
            ai = {
                'CODIGO_ACCIDENTE':air['CODIGO_ACCIDENTE'],
                'DIA_OCURRENCIA_ACC':air['DIA_OCURRENCIA_ACC'],
                'DIRECCION':air['DIRECCION'],
                'GRAVEDAD':air['GRAVEDAD'],
                'CLASE_ACC':air['CLASE_ACC'],
                'LOCALIDAD':air['LOCALIDAD'],
                'FECHA_HORA_ACC':air['FECHA_HORA_ACC'],
                'LATITUD':air['LATITUD'],
                'LONGITUD':air['LONGITUD']
            }
            af = {
                'CODIGO_ACCIDENTE':afr['CODIGO_ACCIDENTE'],
                'DIA_OCURRENCIA_ACC':afr['DIA_OCURRENCIA_ACC'],
                'DIRECCION':afr['DIRECCION'],
                'GRAVEDAD':afr['GRAVEDAD'],
                'CLASE_ACC':afr['CLASE_ACC'],
                'LOCALIDAD':afr['LOCALIDAD'],
                'FECHA_HORA_ACC':afr['FECHA_HORA_ACC'],
                'LATITUD':afr['LATITUD'],
                'LONGITUD':afr['LONGITUD']
            }
            ml_tab += [[ai,af]]
        for ac in lt.iterator(lista):
            l_graf[1][int(ac['HORA_OCURRENCIA_ACC'].split(":")[0])] += 1
    return ml_tab, l_graf


def req_8(catalog, fi, ff, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    mapaom = catalog["data"]
    numacc = 0
    ai,mi,di = strafecha(fi)
    af,mf,df = strafecha(ff)
    valores = om.values(mapaom, datetime.date(ai,mi,di), datetime.date(af,mf,df))
    
    mapafo = folium.Map(location=[4.651807, -74.076831], zoom_start=15)

    for ldia in lt.iterator(valores):
        for acc in lt.iterator(ldia):
            if acc["CLASE_ACC"] == clase:
                gravedad = acc["GRAVEDAD"]
                lat = acc["LATITUD"]
                lon = acc["LONGITUD"]
                codigo_acc = acc["CODIGO_ACCIDENTE"]
                
                popup = ("Gravedad: " + gravedad + "\n" +
                         "Latitud: " + lat + "\n" +
                         "Longitud: " + lon)
                
                if gravedad == "SOLO DANOS":
                    folium.Marker([lat, lon], 
                                  popup="<i>"+popup+"</i>", 
                                  tooltip=codigo_acc, 
                                  icon=folium.Icon(color="green", 
                                                   icon="info-sign"),).add_to(mapafo)
                elif gravedad == "CON HERIDOS":
                    folium.Marker([lat, lon], 
                                  popup="<i>"+popup+"</i>", 
                                  tooltip=codigo_acc, 
                                  icon=folium.Icon(color="blue", 
                                                   icon="info-sign"),).add_to(mapafo) 
                else:
                    folium.Marker([lat, lon], 
                                  popup="<i>"+popup+"</i>", 
                                  tooltip=codigo_acc, 
                                  icon=folium.Icon(color="red", 
                                                   icon="info-sign"),).add_to(mapafo)
                numacc += 1
    return mapafo, numacc
            
    
    


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpdates(dato1, dato2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    año1,mes1,dia1 = strafecha(dato1["FECHA_OCURRENCIA_ACC"])
    date1 = datetime.time(año1,mes1,dia1)
    año2,mes2,dia2 = strafecha(dato2["FECHA_OCURRENCIA_ACC"])
    date2 = datetime.time(año2,mes2,dia2)
    
    if date1 < date2:
        return True
    else:
        return False
    

# Funciones de ordenamiento

def req2_sortcriteria(data1, data2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    if data1[1] > data2[1]:
        return False
    elif data1[1] < data2[1]:
        return True 
    

def hora_sortcriteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    fecha1 = data_1["FECHA_HORA_ACC"]
    fecha2 = data_2["FECHA_HORA_ACC"]
    hora_com1= (fecha1.split(" "))[1].split(":")
    hora1 = int(hora_com1[0]) 
    minuto1 = int(hora_com1[1])
    
    hora_com2 = (fecha2.split(" "))[1].split(":")
    hora2 = int(hora_com2[0]) 
    minuto2 = int(hora_com2[1])
    
    if hora1 > hora2:
        return False
    elif hora1 < hora2:
        return True
    else:
        if minuto1 > minuto2:
            return False
        elif minuto1 < minuto2:
            return True
        else:
            if int(data_1['CODIGO_ACCIDENTE']) > int(data_2['CODIGO_ACCIDENTE']):
                return False
            else:
                return True
        
def req3_sortcriteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    f1 = data_1["FECHA_HORA_ACC"].split(" ")
    f2 = data_2["FECHA_HORA_ACC"].split(" ")
    
    año1,mes1,dia1 = strafecha(data_1["FECHA_OCURRENCIA_ACC"])
    date1 = datetime.date(año1,mes1,dia1)
    año2,mes2,dia2 = strafecha(data_2["FECHA_OCURRENCIA_ACC"])
    date2 = datetime.date(año2,mes2,dia2)
    
    hora_com1= (f1[1].split(":"))
    hora1 = int(hora_com1[0]) 
    minuto1 = int(hora_com1[1])
    
    hora_com2 = (f2[1].split(":"))
    hora2 = int(hora_com2[0]) 
    minuto2 = int(hora_com2[1])
    
    if date1 > date2:
        return True
    elif date1 < date2:
        return False
    else:    
        if hora1 > hora2:
            return False
        elif hora1 < hora2:
            return True
        else:
            if minuto1 > minuto2:
                return False
            else:
                return True
    
def req6_sortcriteria(data1, data2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    if data1["DIST_CENTRO"] > data2["DIST_CENTRO"]:
        return False
    elif data1["DIST_CENTRO"] < data2["DIST_CENTRO"]:
        return True 


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
