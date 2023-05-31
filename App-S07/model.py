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
from datetime import datetime
from haversine import haversine, Unit
import folium
import webbrowser
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
    data_structs = {"siniestros": None,
                    "fechas": None,
                    "años": None, 
                    "clases": None}
    
    data_structs["siniestros"] = lt.newList("ARRAY_LIST", compareIds)
    data_structs["fechas"] = om.newMap(omaptype='RBT',
                                      comparefunction=compareFechas)
    data_structs["años"] = mp.newMap(30,
                                maptype='PROBING',
                                loadfactor=0.5,
                                cmpfunction=compareAño)
    data_structs["clases"] = mp.newMap(20,
                                maptype='PROBING',
                                loadfactor=0.5,
                                cmpfunction=compareClase)
    data_structs["años_2"] = mp.newMap(30,
                                maptype='PROBING',
                                loadfactor=0.5,
                                cmpfunction=compareAño)
    
    
    return data_structs


# Funciones para agregar informacion al modelo

def add_siniestro(data_structs, siniestro):
    """
    adicionar un crimen a la lista de crimenes y en el arbol
    """
    
    lt.addLast(data_structs["siniestros"], siniestro)
    updateFechaIndex(data_structs["fechas"], siniestro)
    updateAñoHash(data_structs["años"] ,siniestro)
    updateClaseHash(data_structs["clases"] ,siniestro)
    # TODO lab 9, actualizar el indice por areas reportadas
    #updateAreaIndex(analyzer["areaIndex"], crime)
    return data_structs


def updateFechaIndex(map, siniestro):
    """
    Se toma la fecha del siniestro y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = siniestro["FECHA_HORA_ACC"]
    sinidate = datetime.strptime(occurreddate, '%Y/%m/%d %H:%M:%S+%f')
    entry = om.get(map, sinidate)
    if entry is None:
        datentry = newFechaEntry(siniestro)
        om.put(map, sinidate, datentry)
    else:
        datentry = me.getValue(entry)
        addFechaIndex(datentry, siniestro)
    return map

def addFechaIndex(datentry, siniestro):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry["lstaccidentes"]
    lt.addLast(lst, siniestro)
    return datentry

def newFechaEntry(siniestro):
    """
    Crea una entrada en el indice por fechas, es decir el arbol binario
    """
    entry = {"lstaccidentes": None}
    entry["lstaccidentes"] = lt.newList("ARRAY_LIST", compareFechas)
    lt.addLast(entry["lstaccidentes"], siniestro)
    return entry

def updateAñoHash(map, siniestro):
    """
   
    """
    year = int(siniestro["ANO_OCURRENCIA_ACC"])
    entry = mp.get(map, year)
    if entry is None:
        datentry = newAñoEntry()
        datentry = addAñoIndex(datentry, siniestro)
        mp.put(map, year, datentry)
    else:
        datentry = me.getValue(entry)
        addAñoIndex(datentry, siniestro)
    return map

def newAñoEntry():
    """
    Crea una entrada en el indice por fechas, es decir el arbol binario
    """
    entry = {"meses": None}
    entry["meses"] = mp.newMap(24,
                                maptype='PROBING',
                                loadfactor=0.5,
                                cmpfunction=compareMes)
    return entry

def addAñoIndex(datentry, siniestro):
    """
  
    """
    mapa_mes = datentry["meses"]
    mes = siniestro["MES_OCURRENCIA_ACC"]
    mesentry = mp.get(mapa_mes, mes)
    if mesentry is None:
        entry = newMesEntry()
        entry = addMesIndex(entry, siniestro)
        addFechaIndex(entry, siniestro)
        mp.put(mapa_mes, mes, entry)
    else:
        entry = me.getValue(mesentry)
        addMesIndex(entry, siniestro)
        addFechaIndex(entry, siniestro)

    return datentry

def addMesIndex(datentry, siniestro):
    """

    """   
    tree_hora = datentry["horas"]
    hora = siniestro["HORA_OCURRENCIA_ACC"]
    hora = datetime.strptime(hora, '%H:%M:%S')
    
    horaentry = om.get(tree_hora, hora)
    
    if(horaentry is None):
        entry = newHoraEntry()
        entry = addHoraIndex(entry, siniestro)
        om.put(tree_hora, hora, entry)
    else:
        entry = me.getValue(horaentry)
        addHoraIndex(entry, siniestro)
        
    return datentry


def newMesEntry():
    """
    Crea una entrada en el indice por fechas, es decir el arbol binario
    """
    entry = {"horas": None,
             "lstaccidentes": None}
    entry["horas"] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    entry["lstaccidentes"] = lt.newList("ARRAY_LIST", compareFechas)
    
    return entry

def addHoraIndex(datentry, siniestro):
    """
    """
    lst = datentry["lstaccidentes"]
    lt.addLast(lst, siniestro)
    return datentry

def newHoraEntry():
    """
    Crea una entrada en el indice por fechas, es decir el arbol binario
    """
    entry = {"lstaccidentes": None}
    entry["lstaccidentes"] = lt.newList("ARRAY_LIST", compareFechas)

    return entry



def updateClaseHash(map, siniestro):
    """
   
    """
    clase = (siniestro["CLASE_ACC"])
    entry = mp.get(map, clase)
    if entry is None:
        datentry = newClaseEntry()
        datentry = addClaseIndex(datentry, siniestro)
        mp.put(map, clase, datentry)
    else:
        datentry = me.getValue(entry)
        addClaseIndex(datentry, siniestro)
    return map



def addClaseIndex(datentry, siniestro):
    """

    """
    
    tree_fechas = datentry["dates"]
    fecha = siniestro["FECHA_HORA_ACC"]
    fecha = datetime.strptime(fecha, '%Y/%m/%d %H:%M:%S+%f')
    
    fechaentry = om.get(tree_fechas, fecha)
    if(fechaentry is None):
        entry = newDateEntry()
        entry = addDateIndex(entry, siniestro)
        om.put(tree_fechas, fecha, entry)
    else:
        entry = me.getValue(fechaentry)
        addDateIndex(entry, siniestro)
    return datentry

def newClaseEntry():
    """
    Crea una entrada en el indice por fechas, es decir el arbol binario
    """
    entry = {"dates": None}
    entry["dates"] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    return entry

def addDateIndex(datentry, siniestro):
    """
    """
    lst = datentry["lstaccidentes"]
    lt.addLast(lst, siniestro)
    return datentry

def newDateEntry():
    """
    Crea una entrada en el indice por fechas, es decir el arbol binario
    """
    entry = {"lstaccidentes": None}
    entry["lstaccidentes"] = lt.newList("ARRAY_LIST", compareFechas)

    return entry
# Funciones para creacion de datos


# Funciones de consulta

def siniestrosSize(data_structs):
    """
    Número de crimenes
    """
    return lt.size(data_structs["siniestros"])

def siniFirstLastThree(data_structs):
    """
    Número de crimenes
    """
    first = lt.subList(data_structs["siniestros"], 1, 3)
    last = lt.subList(data_structs["siniestros"], siniestrosSize(data_structs)-2, 3)
   
    return first, last

def req_1(data_structs, initialDate, finalDate):
    """
    gets accidents by range
    """
    
    lst = om.values(data_structs["fechas"], initialDate, finalDate)
    num_siniestros = 0
  
    for lstdate in lt.iterator(lst):
        num_siniestros += lt.size(lstdate["lstaccidentes"])
        
    return num_siniestros, lst


def req_2(data_structs, año, mes, hora_i, hora_f):
    """
    Función que soluciona el requerimiento 2
    """
    num_siniestros = 0
    
    mes_kv = mp.get(data_structs["años"], año)
    mes_hash = me.getValue(mes_kv)
    hora_kv = mp.get(mes_hash["meses"], mes)
    hora_tree = me.getValue(hora_kv)
    lst = om.values(hora_tree["horas"], hora_i, hora_f)
    for lstdate in lt.iterator(lst):
        num_siniestros += lt.size(lstdate["lstaccidentes"])
    
    return num_siniestros, lst


def req_3(data_structs, clase, via):
    """
    Reportar los 3 accidentes más recientes de una clase 
    particular ocurridos a lo largo de una vía
    
    tiene una esctructura de datos como entrada, una clase y una vía
    
    retorna el numero de accidentes y una lista con el ranking
    """
  
    # TODO: Realizar el requerimiento 3
    num_siniestros = 0
    data = lt.newList("ARRAY_LIST")

    mes_kv = mp.get(data_structs["clases"], clase)
    tree = me.getValue(mes_kv)
    lst = om.valueSet(tree["dates"])
    for lstdate in lt.iterator(lst):
        for accidente in lt.iterator(lstdate["lstaccidentes"]):
            
            if via in accidente["DIRECCION"]:
                num_siniestros += lt.size(lstdate["lstaccidentes"])
    
                lt.addLast(data, accidente)
                
    rank = lt.subList(data, -2, 3)
    
    return num_siniestros, rank


def req_4(data_base, fi, ff, grav):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    acc_range = om.values(data_base, fi, ff)
    grav_acc = lt.newList()
    for accident in lt.iterator(acc_range):
        for i in lt.iterator(accident["lstaccidentes"]):
            if i["GRAVEDAD"] == grav:
                lt.addFirst(grav_acc, i)
    if lt.size(grav_acc) <= 5:
        return grav_acc
    else:
        return lt.subList(grav_acc, 1, 5)



def req_5(data_structs, año, mes, localidad):
    
    mes_kv = mp.get(data_structs["años"], int(año))
    mes_hash = me.getValue(mes_kv)
    accidentes_kv = mp.get(mes_hash["meses"], mes)
    acc = me.getValue(accidentes_kv)
   
    accidentes_lst = (acc["lstaccidentes"])
    
    listaAux=lt.newList("ARRAY_LIST",compare)
    for a in lt.iterator(accidentes_lst):
        if a["LOCALIDAD"]==localidad:
            lt.addFirst(listaAux, a)
    
    merg.sort(listaAux, sort_criteria_req5)
    t=lt.size(listaAux)
    if t > 10:
        sin = lt.subList(listaAux, t-10, 10)
    else:
        sin = listaAux
    
    #ordenar 
    #sacar los ultimos 10 
    return sin


def req_6(data_structs, año, mes, latitud, longitud, radio, N):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    centro = (latitud, longitud)
    num_siniestros = 0
    radrank = 0
    data = lt.newList()
    
    
    
    
    mes_kv = mp.get(data_structs["años"], año)

    mes_hash = me.getValue(mes_kv)
    accidentes_kv = mp.get(mes_hash["meses"], mes)
    
    acc = me.getValue(accidentes_kv)
    accidentes_lst = (acc["lstaccidentes"])
   
    for accidente in lt.iterator(accidentes_lst):
        
        latitud_sinis = float(accidente["LATITUD"])
        longitud_sinis = float(accidente["LONGITUD"])
        coordenada = latitud_sinis, longitud_sinis
        rad = haversine(centro, coordenada)
        rad = float(rad)
        
        if (rad <= radio and radrank <= rad):
            lt.addLast(data, accidente)
             
        
    num_siniestros = lt.size(data)      
    rank = lt.subList(data, 1, N)
    
    return num_siniestros, rank


def req_7(database, fi, ff):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    acc_range = om.values(database, fi, ff)
    horas = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0,
             "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0,
             "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0,
             "21":0, "22":0, "23":0}
    first_last = {}
    dia = "0"
    for accident in lt.iterator(acc_range):
        for i in lt.iterator(accident["lstaccidentes"]):
            horas[(i["HORA_OCURRENCIA_ACC"].split(":")[0])] +=1
            dia_i = (i["FECHA_OCURRENCIA_ACC"].split("/"))[2]
            if dia_i != dia and dia == "0":
                first_last[dia_i] = []
                first_last[dia_i].append(i)
            elif dia_i != dia and dia != "0":
                fecha_split = i["FECHA_OCURRENCIA_ACC"].split("/")
                if dia_i > "10":
                    anterior = me.getValue(om.get(database, om.floor(database, (datetime.strptime(fecha_split[0]+"/"+fecha_split[1]+"/"+str(int(fecha_split[2])-1)+" 23:59:59", "%Y/%m/%d %H:%M:%S")))))
                elif dia_i <= "10":
                    anterior = me.getValue(om.get(database, om.floor(database, (datetime.strptime(fecha_split[0]+"/"+fecha_split[1]+"/"+"0"+str(int(fecha_split[2])-1)+" 23:59:59", "%Y/%m/%d %H:%M:%S")))))
                first_last[(lt.firstElement(anterior["lstaccidentes"])["FECHA_OCURRENCIA_ACC"].split("/"))[2]].append(lt.firstElement(anterior["lstaccidentes"]))
                first_last[dia_i] = []
                first_last[dia_i].append(i)
            dia = dia_i
    first_last[max(first_last.keys())].append(lt.lastElement(lt.lastElement(acc_range)["lstaccidentes"]))
    return first_last, horas


def req_8(data_structs, fecha_inicial, fecha_final, tipo):
    """
    Función que soluciona el requerimiento 8
    """
    #sacar los accidentes por fechas
    #sacar los tipos de accidente
    #esto en una lista
    keylo=fecha_inicial
    keyhi= fecha_final
    lt1=lt.newList("ARRAY_LIST", compare)
    lista=om.values(data_structs["fechas"], keylo, keyhi)
    for j in lt.iterator(lista):
        for i in lt.iterator(j["lstaccidentes"]):
            if str(i["CLASE_ACC"])==str(tipo).upper():
                lt.addLast(lt1, i)
    m=folium.Map(location=[4.6097, -74.0817], zoom_start=13)   
    colors = {"SOLO DANOS":"orange", "CON HERIDOS":"red", "CON MUERTOS":"black"}
    pops = {"SOLO DANOS":"Sólo daños", "CON HERIDOS":"Con heridos", "CON MUERTOS":"Con muertos"}
    #iterar por elemento en la lista
    for i in lt.iterator(lt1):
        folium.Marker(location=[i["LATITUD"], i["LONGITUD"]],
                      popup=pops[i["GRAVEDAD"]],
                      icon=folium.Icon(color=colors[i["GRAVEDAD"]], icon="info-sign")).add_to(m)
    m.save("map.html")
    webbrowser.open_new_tab("map.html")

# Funciones utilizadas para comparar elementos dentro de una lista


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

# Funciones de ordenamiento

def compareFechas(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compare(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareMes(date1, date2):
    """
    Compara dos fechas
    """
    date2 = me.getKey(date2)
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareZonas(date1, date2):
    """
    Compara dos fechas
    """
    date2 = me.getKey(date2)
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareAño(date1, date2):
    """
    Compara dos fechas
    """

    date2 = me.getKey(date2)
    
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def compareClase(date1, date2):
    """
    Compara dos fechas
    """
    date2 = me.getKey(date2)
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    


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

def sort_criteria_req1(data_1, data_2):
    return int(data_1["total_saldo_a_pagar"]) > int(data_2["total_saldo_a_pagar"])


def sort_criteria_req5(data_1, data_2):
    return (data_1["FECHA_HORA_ACC"]) > (data_2["FECHA_HORA_ACC"])