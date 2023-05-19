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
import math as mt
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
import branca
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
import webbrowser
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(tipo_mapa, factor_carga, tipo_arbol):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"DATOS_TODOS": None,
                    "Fecha_Occur": None,
                    "Hora_Occur": None,
                    "Anios": None,
                    "Clase_accid": None
                    }
    data_structs["DATOS_TODOS"] = lt.newList("ARRAY_LIST")
    
    data_structs["Fecha_occur"] = om.newMap(omaptype=tipo_arbol,
                                      comparefunction=compareFecha)
    
    data_structs["Hora_occur"] = om.newMap(omaptype=tipo_arbol,
                                      comparefunction=compareHora)
    
    data_structs["Anios"] = mp.newMap(20, 
                                   maptype=tipo_mapa ,
                                   loadfactor=factor_carga,
                                   cmpfunction=compare_by_anio)
    
    data_structs["Clase_accid"] = mp.newMap(20, 
                                   maptype=tipo_mapa ,
                                   loadfactor=factor_carga,
                                   cmpfunction=compare_by_clase)
    return data_structs
    

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["DATOS_TODOS"], data)
    addfecha(data_structs, data)
    adddatas(data_structs, data)
    addclase(data_structs, data)
    return data_structs
    
def addfecha(data_structs, data):
    try:
        fechas = data_structs["Fecha_occur"]
        
        if data["FECHA_OCURRENCIA_ACC"] != "":
            fecha_csv = data["FECHA_OCURRENCIA_ACC"]
        else:
            fecha_csv = ""
        existefecha = om.contains(fechas, fecha_csv)
        if existefecha:
            entry = om.get(fechas, fecha_csv)
            fecha = me.getValue(entry)
        else:
            fecha = new_fecha(fecha_csv)
            om.put(fechas, fecha_csv, fecha)
        lt.addLast(fecha["Datos_fecha"], data)
    except Exception:
        return None

def adddatas(data_structs, data):
    try:
        anios = data_structs['Anios']
        
        if (data['ANO_OCURRENCIA_ACC'] != ""):
            años_csv = int(data['ANO_OCURRENCIA_ACC'])
        else:
            años_csv = 2020
        
        existyear = mp.contains(anios, años_csv)
        if existyear:
            entry = mp.get(anios, años_csv)
            year = me.getValue(entry)
        else:
            year = new_anio(años_csv)
            mp.put(anios, años_csv, year)
        lt.addLast(year['Datos'], data)
        
        mes = year["Mes"]

        if (data['MES_OCURRENCIA_ACC'] != ""):
            mes_csv = (data['MES_OCURRENCIA_ACC'])
        else:
            mes_csv = ""

        existmes = mp.contains(mes, mes_csv)
        if existmes:
            entry = mp.get(mes, mes_csv)
            month = me.getValue(entry)
        else:
            month = new_mes(mes_csv)
            mp.put(mes, mes_csv, month)
        lt.addLast(month["Datos_mes"], data)
        
        om_hora_occur = month["Hora_occur_om"]
        occurredhour = data["HORA_OCURRENCIA_ACC"]
        
        if occurredhour != "":
            crimehour = occurredhour
        else:
            crimehour = ""
            
        existehora = om.contains(om_hora_occur, crimehour)
        if existehora:
            entry = om.get(om_hora_occur, crimehour)
            hora = me.getValue(entry)
        else:
            hora = lt.newList("SINGLE_LINKED")
            om.put(om_hora_occur, crimehour, hora)
        lt.addLast(hora, data)
        
        om_fecha_completa = month["Dia"]
        
        if str(data["FECHA_HORA_ACC"]) != "":
            crimedate = str(data["FECHA_HORA_ACC"])
        else:
            crimedate = ""
        fecha = datetime.datetime.strptime(crimedate.split("+")[0], '%Y/%m/%d %H:%M:%S')
        dia = fecha.day
        existefecha = om.contains(om_fecha_completa, dia)
        if existefecha:
            entry = om.get(om_fecha_completa, dia)
            fechac = me.getValue(entry)
        else:
            fechac = lt.newList("SINGLE_LINKED")
            om.put(om_fecha_completa, dia, fechac)
        lt.addLast(fechac, data)
    except Exception:
        return None

def addclase(data_structs, data):
    try:
        clase = data_structs['Clase_accid']
        
        if (data['CLASE_ACC'] != ""):
            clase_csv = str(data['CLASE_ACC'])
        else:
            clase_csv = ""
        
        existyear = mp.contains(clase, clase_csv)
        if existyear:
            entry = mp.get(clase, clase_csv)
            clase_dato = me.getValue(entry)
        else:
            clase_dato = new_clase(clase_csv)
            mp.put(clase, clase_csv, clase_dato)
        lt.addLast(clase_dato['Datos_clase'], data)
    except Exception:
        return None

# Funciones para creacion de datos

def new_anio(year):
    """
    Crea una nueva estructura para modelar los datos
    """
    entrada = {"Año" : "" , "Datos": None, "Mes": None}
    entrada['Año'] = year
    entrada['Datos'] = lt.newList("SINGLE_LINKED")
    entrada["Mes"] = mp.newMap(100 ,
                                   maptype="CHAINING" ,
                                   loadfactor=4, 
                                   cmpfunction=compare_by_mes)
    return entrada

def new_mes(mes):
    """
    Crea una nueva estructura para modelar los datos
    """
    entrada = {"Mes_mp" : "" , "Datos_mes": None, "Hora_occur_om": None, "Dia":None}
    entrada['Mes_mp'] = mes
    entrada['Datos_mes'] = lt.newList("SINGLE_LINKED")
    entrada["Hora_occur_om"] = om.newMap("RBT",
                                         comparefunction=compareHora)
    entrada["Dia"] = om.newMap("RBT",
                                comparefunction=compareFecha)
    return entrada

def new_clase(clase):
    """
    Crea una nueva estructura para modelar los datos
    """
    entrada = {"Clase": "", "Datos_clase": None}
    entrada["Clase"] = clase
    entrada["Datos_clase"] = lt.newList("SINGLE_LINKED")
    return entrada

def new_fecha(fecha):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    entrada = {"Fecha": "", "Datos_fecha": None}
    entrada["Fecha"] = fecha
    entrada["Datos_fecha"] = lt.newList("SINGLE_LINKED")
    return entrada

def cmp_crimenes_by_reciente_antiguo(crimen1, crimen2):
    if (crimen1["FECHA_HORA_ACC"]) > (crimen2["FECHA_HORA_ACC"]):
        return True
    else:
        return False

def req_1(data_structs, fecha1, fecha2):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    resultado = lt.newList("ARRAY_LIST")
    
    om_fechas = data_structs["Fecha_occur"]
    for fechas in lt.iterator(om.values(om_fechas, fecha1, fecha2)):
        for eleme in lt.iterator(fechas["Datos_fecha"]):
            lt.addLast(resultado, eleme)
    merg.sort(resultado, cmp_crimenes_by_reciente_antiguo)
    return resultado


def req_2(data_structs, year, mes, tiempo1, tiempo2):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    resultado = lt.newList("ARRAY_LIST")
    
    dic_anio = mp.get(data_structs["Anios"], year)
    if not dic_anio:
        return False
    dic_anio=me.getValue(dic_anio)
    mes = mp.get(dic_anio["Mes"], mes)
    if not mes:
        return False
    lt_mes = me.getValue(mes)
    om_hora = lt_mes["Hora_occur_om"]
    for eleme in lt.iterator(om.values(om_hora, tiempo1, tiempo2)):
        for dato in lt.iterator(eleme):
            lt.addLast(resultado, dato)
    merg.sort(resultado, cmp_crimenes_by_reciente_antiguo)
    return resultado
    
def req_3(data_structs, clase, nombre_via):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    resultado = lt.newList("ARRAY_LIST")
    
    mapa_clase = mp.get(data_structs["Clase_accid"], clase)
    if not mapa_clase:
        return False
    clase = (me.getValue(mapa_clase))
    lt_clase = clase["Datos_clase"]
    for eleme in lt.iterator(lt_clase):
        if nombre_via in str(eleme["DIRECCION"]):
            lt.addLast(resultado, eleme)
    merg.sort(resultado, cmp_crimenes_by_reciente_antiguo)
    return resultado

def req_4(data_structs, fecha_inicial, fecha_final, gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    resultado = lt.newList("ARRAY_LIST")
    
    om_fechas = data_structs["Fecha_occur"]
    for lts in lt.iterator(om.values(om_fechas, fecha_inicial, fecha_final)):
        datos_fecha = lts["Datos_fecha"]
        for dato in lt.iterator(datos_fecha):
            if dato["GRAVEDAD"] == gravedad:
                lt.addLast(resultado, dato)
    merg.sort(resultado, cmp_crimenes_by_reciente_antiguo)
    return resultado
    
def req_5(data_structs, year, mes, localidad):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    resultado = lt.newList("ARRAY_LIST")
    
    dic_anio = mp.get(data_structs["Anios"], year)
    if not dic_anio:
        return False
    dic_anio=me.getValue(dic_anio)
    mes = mp.get(dic_anio["Mes"], mes)
    if not mes:
        return False
    lt_mes = me.getValue(mes)
    lt_mes = (lt_mes["Datos_mes"])
    for eleme in lt.iterator(lt_mes):
        if str(eleme["LOCALIDAD"]) == localidad:
            lt.addLast(resultado, eleme)
    merg.sort(resultado, cmp_crimenes_by_reciente_antiguo)
    return resultado

#REQ 6
def radio_math (longitud_1, longitud_2, latitud_1, latitud_2):
    longitud_1, longitud_2, latitud_1, latitud_2 = map(mt.radians, [longitud_1, longitud_2, latitud_1, latitud_2])
    
    resta_longitud=(longitud_2-longitud_1)/2
    resta_latitudes=(latitud_2-latitud_1)/2
    cos_lat_1= mt.cos(latitud_1)
    cos_lat_2= mt.cos(latitud_2)
    raiz=mt.sqrt((mt.sin(resta_latitudes)**2)+(cos_lat_1*cos_lat_2*(mt.sin(resta_longitud)**2)))
    total=2*(mt.asin(raiz))*6371.009
    return total

def cmp_by_req6(crimen1, crimen2):
    if (crimen1["RADIO"]) < (crimen2["RADIO"]):
        return True
    else:
        return False

def req_6(data_structs, year, mes, longitud, latitud, radio, top):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    resultado = lt.newList("ARRAY_LIST")
    
    dic_anio = mp.get(data_structs["Anios"], year)
    if not dic_anio:
        return False
    dic_anio=me.getValue(dic_anio)
    mes = mp.get(dic_anio["Mes"], mes)
    if not mes:
        return False
    lt_mes = me.getValue(mes)
    lt_mes = (lt_mes["Datos_mes"])
    for eleme in lt.iterator(lt_mes):
        latitud2 = float(eleme["LATITUD"])
        longitud2 = float(eleme["LONGITUD"])
        radio_intervalo = radio_math(longitud, longitud2, latitud, latitud2)
        eleme["RADIO"] = radio_intervalo
        if radio_intervalo <= radio:
            lt.addLast(resultado, eleme)
    merg.sort(resultado, cmp_by_req6)
    if top < lt.size(resultado):
        lt_top = lt.subList(resultado,1,top)
    else:
        lt_top = resultado
    return lt_top


def req_7(data_structs, year, mes, escala):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    resultado = lt.newList("ARRAY_LIST")
    
    dic_anio = mp.get(data_structs["Anios"], year)
    if not dic_anio:
        return False
    dic_anio=me.getValue(dic_anio)
    mes_mp = mp.get(dic_anio["Mes"], mes)
    if not mes_mp:
        return False
    lt_mes = me.getValue(mes_mp)
    om_fecha_dia = lt_mes["Dia"]
    unicos_dias = lt.newList("ARRAY_LIST")
    unico = 0
    for dias_dt in lt.iterator(om.keySet(om_fecha_dia)):
        if dias_dt != unico:
            unico = dias_dt
            lt.addLast(unicos_dias, unico)
    for dias_en_lista in lt.iterator(unicos_dias):
        dias = om.get(om_fecha_dia, dias_en_lista)
        dic_dias = me.getValue(dias)
        merg.sort(dic_dias, cmp_crimenes_by_reciente_antiguo)
        maximo = lt.firstElement(dic_dias)
        minimo = lt.lastElement(dic_dias)
        lt.addLast(resultado, minimo)
        lt.addLast(resultado, maximo)
    graf=[]
    for hora in range(0,24):
        cuantos=0
        for dato in lt.iterator(lt_mes["Datos_mes"]):
            dat= dato["HORA_OCURRENCIA_ACC"]
            dat= dat[0:2]
            dat= int(dat.replace(":",""))
            if dat == hora:
                cuantos+=1
        graf.append(cuantos)
    return resultado , graf, str(lt.size(lt_mes["Datos_mes"]))


def req_8(data_structs, fecha1, fecha2, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    resultado = lt.newList("ARRAY_LIST")
    
    om_fechas = data_structs["Fecha_occur"]
    lista_coo = []
    for fechas in lt.iterator(om.values(om_fechas, fecha1, fecha2)):
        for eleme in lt.iterator(fechas["Datos_fecha"]):
            if eleme["CLASE_ACC"] == clase:
                lt.addLast(resultado, eleme)
                lista_coo.append(eleme["LATITUD"])
                lista_coo.append(eleme["LONGITUD"])
    if lt.size(resultado) <= 0 :
        return False
    m = folium.Map(location=lista_coo[0:2], zoom_start=16)
    marker_cluster = MarkerCluster(disableClusteringAtZoom=24).add_to(m)
    i = 2
    for eleme in lt.iterator(resultado):
        html="<p> Codigo de accidente: "+eleme["CODIGO_ACCIDENTE"]+"</p><p> Fecha de accidente: "+ eleme["FECHA_OCURRENCIA_ACC"]+"</p><p> Hora en la que ocurrio el accidente: "+ eleme["HORA_OCURRENCIA_ACC"]+"</p><p> Dia en el que ocurrio el accidente: "+ eleme["DIA_OCURRENCIA_ACC"]+"</p><p> Dirección de accidente: "+ eleme["DIRECCION"]+"</p><p> Gravedad de accidente: "+ eleme["GRAVEDAD"] +"</p><p> Clase de accidente: "+ eleme["CLASE_ACC"]+ "</p><p> Latitud: "+ eleme["LATITUD"]+ "</p><p> Longitud: "+eleme["LONGITUD"]
        iframe=branca.element.IFrame(html=html, width=500, height=300)
        if eleme["GRAVEDAD"] == "SOLO DANOS":
            folium.Marker(location=lista_coo[i-2:i],icon=folium.Icon(color="green"),popup=folium.Popup(iframe, max_width=500)).add_to(m)
            folium.Marker(location=lista_coo[i-2:i],icon=folium.Icon(color="green"),popup=folium.Popup(iframe, max_width=500)).add_to(marker_cluster)
        elif eleme["GRAVEDAD"] == "CON HERIDOS":
            folium.Marker(location=lista_coo[i-2:i],icon=folium.Icon(color="blue"),popup=folium.Popup(iframe, max_width=500)).add_to(m)
            folium.Marker(location=lista_coo[i-2:i],icon=folium.Icon(color="blue"),popup=folium.Popup(iframe, max_width=500)).add_to(marker_cluster)
        else:
            folium.Marker(location=lista_coo[i-2:i],icon=folium.Icon(color="red"),popup=folium.Popup(iframe, max_width=500)).add_to(m)
            folium.Marker(location=lista_coo[i-2:i],icon=folium.Icon(color="red"),popup=folium.Popup(iframe, max_width=500)).add_to(marker_cluster)
        i += 2
        if i > lt.size(resultado):
            break
    m.save('mapa.html') # para abrir y visualizar el mapa, debes abrir el archivo mapa.html que se encuentra en la carpeta del reto
    #webbrowser.open_new_tab('mapa.html')
    return lt.size(resultado)


# Funciones utilizadas para comparar elementos dentro de una lista

def compareFecha(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareHora(hora1, hora2):
    """
    Compara dos areas
    """
    if (hora1 == hora2):
        return 0
    elif (hora1 > hora2):
        return 1
    else:
        return -1
    
def compare_by_anio(year, data):
    anioentry = me.getKey(data)
    if (year == anioentry):
        return 0
    elif (year > anioentry):
        return 1
    else:
        return -1
    
def compare_by_clase(clase, data):
    claseentry = me.getKey(data)
    if clase == claseentry:
        return 0
    elif clase > claseentry:
        return 1
    else:
        return -1
    
def compare_by_mes(mes, data):
    mesentry = me.getKey(data)
    if (mes == mesentry):
        return 0
    elif (mes > mesentry):
        return 1
    else:
        return -1
# Funciones de ordenamiento

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
