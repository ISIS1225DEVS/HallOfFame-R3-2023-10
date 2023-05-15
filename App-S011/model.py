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
import calendar
import folium
import os
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt
from datetime import datetime , timedelta , date
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import rbt as rbt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
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
    
    data_structs = {"data": om.newMap(omaptype='RBT'),"acc": lt.newList('ARRAY_LIST'),'data_acc':mp.newMap(numelements=7,loadfactor=1,maptype='PROBING')}
    
    return data_structs
    
# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    date_acc=data['FECHA_HORA_ACC'][:-3]
    date_time = datetime.strptime(date_acc, '%Y/%m/%d %H:%M:%S')
    isPresent=om.get(data_structs['data'],date_time)
    
    if isPresent==None:
        lista=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista,data)
        om.put(data_structs['data'],date_time,lista)
    else:
        acc_content=isPresent['value']
        lt.addLast(acc_content,data)
        om.put(data_structs['data'],date_time,acc_content)
        
def add_data_acc(data_structs,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    key=data['CLASE_ACC']
    date_time = datetime.strptime(data['FECHA_HORA_ACC'][:-3], '%Y/%m/%d %H:%M:%S')

    if mp.contains(data_structs['data_acc'],key):
        isPresent=om.get(mp.get(data_structs['data_acc'],key)['value'],date_time)

        if isPresent==None:
            lista=lt.newList(datastructure='ARRAY_LIST')
            lt.addLast(lista,data)
            om.put((mp.get(data_structs['data_acc'],key)['value']),date_time,lista)
        else:
            acc_content=isPresent['value']
            lt.addLast(acc_content,data)
            om.put(mp.get(data_structs['data_acc'],key)['value'],date_time,acc_content)

    else:
        mini_map=om.newMap(omaptype='RBT')
        lista=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista,data)
        om.put(mini_map,date_time,lista)
        mp.put(data_structs['data_acc'],key,mini_map)

# Funciones de consulta
def req_1(data_structs,date_init,date_fin):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    data=om.values(data_structs['data'],datetime.strptime(str(date_init+' 00:00:00'), '%Y/%m/%d %H:%M:%S'),datetime.strptime(str(date_fin+' 23:59:59'), '%Y/%m/%d %H:%M:%S'))
    data_set_org=lt.newList(datastructure='ARRAY_LIST')
    for j in lt.iterator(data):
        if j['size']!=1:
            for k in lt.iterator(j):
                lt.addLast(data_set_org,k)
        else:
            lt.addLast(data_set_org,lt.firstElement(j))
    return data_set_org['elements']
            
def req_2(data_structs,init_time,fin_time,year,month):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    
    calendar.monthrange(int(year),int(month))[1]
    data=om.values(data_structs['data'],datetime.strptime(str(year+'/'+month+'/'+'01'+' '+ init_time+':00'),"%Y/%m/%d %H:%M:%S"),datetime.strptime(str(year+'/'+month+'/'+str(calendar.monthrange(int(year),int(month))[1])+' '+ fin_time+':59'),"%Y/%m/%d %H:%M:%S") )
    lista_final=lt.newList(datastructure='ARRAY_LIST')
    init_time,fin_time=datetime.strptime(init_time+':00',"%H:%M:%S"),datetime.strptime(fin_time+':00',"%H:%M:%S")
    for j in lt.iterator(data):
        if j['size']!=1:
            for k in lt.iterator(j):
                acc_time=datetime.strptime(k['HORA_OCURRENCIA_ACC'],"%H:%M:%S")
                if init_time<=acc_time<=fin_time:
                    k['HORA_OCURRENCIA_ACC_CH']=acc_time
                    lt.addLast(lista_final,k)
        else:
            acc_time=datetime.strptime(j['elements'][0]['HORA_OCURRENCIA_ACC'],"%H:%M:%S")
            if init_time<=acc_time<=fin_time:
                j['elements'][0]['HORA_OCURRENCIA_ACC_CH']=acc_time
                lt.addLast(lista_final,j['elements'][0])
    return quk.sort(lista_final,cmp_req2)['elements']

def req_3(data_structs,acc,name_city):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista=None
    lista_final=lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(data_structs['data_acc']['table']):
        if i['key']==acc:
            lista=om.values(i['value'],datetime.strptime(str('2015/01/01 00:00:00'), '%Y/%m/%d %H:%M:%S'),datetime.strptime(str('2023/12/31 23:59:59'), '%Y/%m/%d %H:%M:%S'))
    for j in lt.iterator(lista):
        if j['size']!=1:
            for k in lt.iterator(j):
                if name_city in k['DIRECCION']:
                    lt.addLast(lista_final,k)
        else:
            if name_city in j['elements'][0]['DIRECCION']:
                lt.addLast(lista_final,j['elements'][0])
    return lt.subList(lista_final,lista_final['size']-2,3)['elements']
    
def req_4(data_structs,date_init,date_fin,grav_acc):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    data=om.values(data_structs['data'],datetime.strptime(str(date_init+' 00:00:00'), '%Y/%m/%d %H:%M:%S'),datetime.strptime(str(date_fin+' 23:59:59'), '%Y/%m/%d %H:%M:%S'))
    lista_final=lt.newList(datastructure='ARRAY_LIST')

    for j in lt.iterator(data):
        if j['size']!=1:
            for k in lt.iterator(j):
                if grav_acc==k['GRAVEDAD']:
                    lt.addLast(lista_final,k)
        else:
            if grav_acc==j['elements'][0]['GRAVEDAD']:
                lt.addLast(lista_final,j['elements'][0])
    return lt.subList(lista_final,lista_final['size']-4,5)['elements']

def req_5(data_structs,zone,month,year):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    data=om.values(data_structs['data'],datetime.strptime(str(year+'/'+month+'/'+'01'+' '+'00:00:00'),"%Y/%m/%d %H:%M:%S"),datetime.strptime(str(year+'/'+month+'/'+str(calendar.monthrange(int(year),int(month))[1])+' '+' '+'23:59:59'),"%Y/%m/%d %H:%M:%S") )
    lista_final=lt.newList(datastructure='ARRAY_LIST')

    for j in lt.iterator(data):
        if j['size']!=1:
            for k in lt.iterator(j):
                 if zone==k['LOCALIDAD']:
                     lt.addLast(lista_final,k)
        else:
            if zone==j['elements'][0]['LOCALIDAD']:
                lt.addLast(lista_final,j['elements'][0])
    return lt.subList(lista_final,lista_final['size']-9,10)['elements']



def req_6(data_structs,month,year,latitude,lenght,ratio,num_accidents):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    data=om.values(data_structs['data'],datetime.strptime(str(year+'/'+month+'/'+'01'+' '+'00:00:00'),"%Y/%m/%d %H:%M:%S"),datetime.strptime(str(year+'/'+month+'/'+str(calendar.monthrange(int(year),int(month))[1])+' '+' '+'23:59:59'),"%Y/%m/%d %H:%M:%S") )

    lista_final=lt.newList(datastructure='ARRAY_LIST')
    for j in lt.iterator(data):
        if j['size']!=1:
            for k in lt.iterator(j):
                k['DISTANCIA_PARAMETRO_PUNTO']=haversine_equation(lenght,latitude,k['LONGITUD'],k['LATITUD'])

                if float(k['DISTANCIA_PARAMETRO_PUNTO'])<=float(ratio):
                    lt.addLast(lista_final,k)
        else:
            j['elements'][0]['DISTANCIA_PARAMETRO_PUNTO']=haversine_equation(lenght,latitude,j['elements'][0]['LONGITUD'],j['elements'][0]['LATITUD'])
            
            if float(j['elements'][0]['DISTANCIA_PARAMETRO_PUNTO'])<=float(ratio):
                lt.addLast(lista_final,j['elements'][0])
                
    return quk.sort(lista_final,cmp_req6)['elements'][:int(num_accidents)]
   
    
def req_7(data_structs,year,month):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    init_time="00:00"
    fin_time="23:59"
    lista=req_2(data_structs,init_time,fin_time,year,month)
    list_month=lt.newList(datastructure="ARRAY_LIST")
    for i in range(1,calendar.monthrange(int(year),int(month))[1]+1):
        date_cmp=datetime(int(year),int(month),i,0,0)
        list_per_day=lt.newList(datastructure="ARRAY_LIST")
        max_min=lt.newList(datastructure="ARRAY_LIST")
        max_min['key']=i
        for j in lista:
            date_var=datetime.strptime(j['FECHA_OCURRENCIA_ACC'],'%Y/%m/%d')
            if date_cmp == date_var:
                lt.addLast(list_per_day,j)
        if list_per_day["size"]>1:
            lt.addLast(max_min,lt.firstElement(list_per_day))
            lt.addLast(max_min,lt.lastElement(list_per_day))
        elif list_per_day["size"]==1:
            lt.addLast(max_min,lt.firstElement(list_per_day))
        if max_min["size"]!=0:
            lt.addLast(list_month,max_min)
    mapa=mp.newMap(numelements=23,loadfactor=1,maptype='PROBING')
    lista_horas=lt.newList(datastructure='ARRAY_LIST')
    l=[lt.addLast(lista_horas,f'0{i}:00:00') for i in range(0,10)]
    k=[lt.addLast(lista_horas,f'{i}:00:00') for i in range(10,24)]
    for k in lista:
        l=datetime.strptime(k['HORA_OCURRENCIA_ACC'],"%H:%M:%S").time()
        for t in range(0,24):
            
            if t<=9:
                l
                if not mp.contains(mapa,f'0{t}:00:00') :
                    value=lt.newList(datastructure='ARRAY_LIST')
                    mp.put(mapa,f'0{t}:00:00',value)
                if datetime.strptime(f'0{t}:00:00',"%H:%M:%S").time()<=l<=datetime.strptime(f'0{t}:59:59',"%H:%M:%S").time():    
                    lt.addLast(mp.get(mapa,f'0{t}:00:00')['value'],k)         
            else:
                l
                if not mp.contains(mapa,f'{t}:00:00'):
                    value=lt.newList(datastructure='ARRAY_LIST')
                    mp.put(mapa,f'{t}:00:00',value)
                if datetime.strptime(f'{t}:00:00',"%H:%M:%S").time()<=l<=datetime.strptime(f'{t}:59:59',"%H:%M:%S").time():  
                    lt.addLast(mp.get(mapa,f'{t}:00:00')['value'],k)
    datos_tuplas=lt.newList(datastructure='ARRAY_LIST')    
    size=0                              
    for j in lt.iterator(mapa['table']):
        if j['key']!=None:
            size+=j['value']['size']
            lt.addLast(datos_tuplas,(j['key'],j['value']['size']))
    
    df=pd.DataFrame(datos_tuplas['elements'],columns=['key', 'value'])
    
    df = df.set_index("key").loc[lista_horas['elements']].reset_index()
    plt.bar(df["key"], df["value"])
    plt.xticks(rotation=90)
    plt.xlabel("Hora del día")
    plt.ylabel("Número de accidentes")
    plt.title(f"Frecuencia de {size} accidentes por hora del día, para el mes: {month} año: {year}")
    plt.show()
    return list_month


def req_8(data_structs,date_init,date_fin,type_acc):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8

    m = folium.Map(location=[4.6097, -74.0817], zoom_start=12)    
    lista=None
    lista_final=lt.newList(datastructure='ARRAY_LIST')

    for i in lt.iterator(data_structs['data_acc']['table']):
        if i['key']==type_acc:
            lista=om.values(i['value'],datetime.strptime(str(date_init+' 00:00:00'), '%Y/%m/%d %H:%M:%S'),datetime.strptime(str(date_fin+' 23:59:59'), '%Y/%m/%d %H:%M:%S'))
    for j in lt.iterator(lista):
        if j['size']!=1:
            for k in lt.iterator(j):
                if k['GRAVEDAD']=='CON HERIDOS':
                    folium.Marker(location=[float(k['LATITUD']),float(k['LONGITUD'])],popup='CON HERIDOS '+type_acc,icon=folium.Icon(color='green')).add_to(m)
                elif k['GRAVEDAD']=='CON MUERTOS':
                    folium.Marker(location=[float(k['LATITUD']),float(k['LONGITUD'])],popup='CON MUERTOS '+type_acc,icon=folium.Icon(color='red')).add_to(m)
                else:
                    folium.Marker(location=[float(k['LATITUD']),float(k['LONGITUD'])],popup='SOLO DANOS '+type_acc,icon=folium.Icon(color='black')).add_to(m)
        else:
                if j['elements'][0]['GRAVEDAD']=='CON HERIDOS':
                    folium.Marker(location=[float(j['elements'][0]['LATITUD']),float(j['elements'][0]['LONGITUD'])],popup='CON HERIDOS '+type_acc,icon=folium.Icon(color='green')).add_to(m)
                elif j['elements'][0]['GRAVEDAD']=='CON MUERTOS':
                    folium.Marker(location=[float(j['elements'][0]['LATITUD']),float(j['elements'][0]['LONGITUD'])],popup='CON MUERTOS '+type_acc,icon=folium.Icon(color='red')).add_to(m)
                else:
                    folium.Marker(location=[float(j['elements'][0]['LATITUD']),float(j['elements'][0]['LONGITUD'])],popup='SOLO DANOS '+type_acc,icon=folium.Icon(color='black')).add_to(m)           
    m.save('mapa.html')
    webbrowser.get('safari').open('file://' + os.path.abspath('mapa.html'))
    
# Funciones de ordenamiento

def cmp_req2(data_1,data_2):
    return data_1["HORA_OCURRENCIA_ACC_CH"]<=data_2["HORA_OCURRENCIA_ACC_CH"]
def cmp_req6(data_1,data_2):
    return  float(data_1['DISTANCIA_PARAMETRO_PUNTO'])<=float(data_2['DISTANCIA_PARAMETRO_PUNTO'])
def haversine_equation(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = radians(float(lon1)),radians(float(lat1)),radians(float(lon2)),radians(float(lat2))
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r
