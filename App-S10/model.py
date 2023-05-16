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
assert cf
from datetime import timedelta
from math import radians, cos, sin, asin, sqrt



"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def NewAnalyzer():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
      
    Analyzer={"todo":None,
              "fechas":None,
              "AMH":None,
              "clases":None,
              "gravedad":None,
              "localidades":None,
              }
    
    Analyzer["todo"]=lt.newList(datastructure="ARRAY_LIST")
    Analyzer["fechas"]=om.newMap(omaptype="RBT",comparefunction=comparefechas)
    Analyzer["AMH"]=mp.newMap(maptype="PROBING",
                              loadfactor=0.5,
                              numelements=193)
    
    Analyzer["clases"]=mp.newMap(maptype="PROBING",
                                   loadfactor=0.5,
                                   numelements=17)
    Analyzer["gravedad"]=mp.newMap(maptype="PROBING",
                                   loadfactor=0.5,
                                   numelements=6)
    Analyzer["localidades"]=mp.newMap(maptype="PROBING",
                                   loadfactor=0.5,
                                   numelements=41)
    return Analyzer
# Funciones para agregar informacion al modelo

def add_data(Analyzer, siniestro):
    
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(Analyzer["todo"],siniestro)
    
    actualizacion_fechas(Analyzer["fechas"],siniestro)
    actualizacion_AMH(Analyzer["AMH"],siniestro)
    actualizacion_clases(Analyzer["clases"],siniestro)
    actualizacion_gravedad(Analyzer["gravedad"],siniestro)
    actualizacion_localidades(Analyzer["localidades"],siniestro)
    
    
# Funciones para creacion de datos
def actualizacion_fechas(arbol,siniestro):
    fechaausar=siniestro["FECHA_HORA_ACC"].split(sep="+")
    fecha_ocurrencia=datetime.strptime(fechaausar[0], "%Y/%m/%d %H:%M:%S")  
    entrada=om.get(arbol,fecha_ocurrencia)  
    if entrada is None:
        entradafecha=nuevafecha()
        om.put(arbol,fecha_ocurrencia,entradafecha)
    else:
        entradafecha=me.getValue(entrada)
    lt.addLast(entradafecha["lst"],siniestro)  
    actualizacioncodigo(entradafecha["codigo"],siniestro)
        
def nuevafecha():
    valores={"codigo":None,
             "lst":None}
    valores["codigo"]=om.newMap(omaptype="RBT",comparefunction=cmpcodigo)
    valores["lst"]=lt.newList(datastructure="ARRAY_LIST")
    return valores

def actualizacioncodigo(arbol,siniestro):
    codigo=siniestro["CODIGO_ACCIDENTE"]
    om.put(arbol,codigo,siniestro)
    

def actualizacion_AMH(mapa,siniestro):
    fecha_ocurrencia=datetime.strptime(siniestro["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d") 
    
    año= fecha_ocurrencia.year
    mes=fecha_ocurrencia.month
    codigo=str(año)+str(mes)
    llaveAM=int(codigo)
    entrada=mp.get(mapa,llaveAM)
    if entrada is None:
        entradaAM=nuevaAM()
        mp.put(mapa,llaveAM,entradaAM)
    else:
        entradaAM=me.getValue(entrada)
    actualizacionhoras(entradaAM["arbolhoras"],siniestro)
    lt.addLast(entradaAM["lstsiniestros"],siniestro)
        
def nuevaAM():
    valores={"lstsiniestros":None,
             "arbolhoras":None}
    
    valores["lstsiniestros"]=lt.newList(datastructure="ARRAY_LIST")
    valores["arbolhoras"]=om.newMap(omaptype="RBT",comparefunction=CompareHoras)
    return valores

def actualizacionhoras(arbol,siniestro):
    hora_ocurrencia=datetime.strptime(siniestro["HORA_OCURRENCIA_ACC"],"%H:%M:%S")
    entrada=om.get(arbol,hora_ocurrencia)
    if entrada is None:
        entradaH=nuevahora()
        om.put(arbol,hora_ocurrencia,entradaH)
    else:
        entradaH=me.getValue(entrada)
    lt.addLast(entradaH,siniestro)
    
        
def nuevahora():
    lista=lt.newList(datastructure="ARRAY_LIST")
    return lista

def actualizacion_clases(mapa,siniestro):
    clase=siniestro["CLASE_ACC"]
    entrada=mp.get(mapa,clase)
    if entrada is None:
        entradaC=nuevaclase()
        mp.put(mapa,clase,entradaC)
        
    else:
        entradaC=me.getValue(entrada)
        
    actualizacion_fechasC(entradaC,siniestro) 
    
def nuevaclase():
    arbol=om.newMap(omaptype="RBT",comparefunction=comparefechas)
    return arbol   

def actualizacion_fechasC(arbol,siniestro):
    fecha1=siniestro["FECHA_HORA_ACC"].split(sep="+")
    fecha_ocurrencia=datetime.strptime(fecha1[0], "%Y/%m/%d %H:%M:%S")
    if om.get(arbol,fecha_ocurrencia) is None:
        nuevaentrada=lt.newList(datastructure="ARRAY_LIST")
        om.put(arbol,fecha_ocurrencia,nuevaentrada)
    else:
        nuevaentrada=me.getValue(om.get(arbol,fecha_ocurrencia))
    lt.addLast(nuevaentrada,siniestro)
    
    
            
def actualizacion_gravedad(mapa,siniestro):
    
    gravedad=siniestro["GRAVEDAD"]
    
    entrada=mp.get(mapa,gravedad)
    if entrada is None:
        entradaG=nuevagravedad()
        mp.put(mapa,gravedad,entradaG)
    else:
        entradaG=me.getValue(entrada)
    actualizacion_fechasG(entradaG,siniestro) 
       
def nuevagravedad():
    arbol=om.newMap(omaptype="RBT",comparefunction=comparefechas)
    return arbol

def actualizacion_fechasG(arbol,siniestro):
    fecha_ocurrencia=datetime.strptime(siniestro["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d")
    if om.get(arbol,fecha_ocurrencia) is None:
        nuevaentrada=lt.newList(datastructure="ARRAY_LIST")
        om.put(arbol,fecha_ocurrencia,nuevaentrada)
    else:
        nuevaentrada=me.getValue(om.get(arbol,fecha_ocurrencia))
    lt.addLast(nuevaentrada,siniestro)

def actualizacion_localidades(mapa,siniestro):
    localidad=siniestro["LOCALIDAD"]   
    entrada=mp.get(mapa,localidad)
    if entrada is None:
        nuevaentradaL=nuevalocalidad()
        mp.put(mapa,localidad,nuevaentradaL)
    else:
        nuevaentradaL=me.getValue(entrada)
    actualizacion_fechasLoc(nuevaentradaL,siniestro)
    
def nuevalocalidad():
    arbol=om.newMap(omaptype="RBT",comparefunction=comparefechas)
    return arbol

def actualizacion_fechasLoc(arbol,siniestro):
    fecha1=siniestro["FECHA_HORA_ACC"].split(sep="+")
    fecha_ocurrencia=datetime.strptime(fecha1[0], "%Y/%m/%d %H:%M:%S")
    if om.get(arbol,fecha_ocurrencia) is None:
        nuevaentrada=lt.newList(datastructure="ARRAY_LIST")
        om.put(arbol,fecha_ocurrencia,nuevaentrada)
    else:
        nuevaentrada=me.getValue(om.get(arbol,fecha_ocurrencia))
    lt.addLast(nuevaentrada,siniestro)
    
def primerosyultimos(Analyzer):
      primeros3=lt.subList(Analyzer["todo"],1,3)
      primeros3_1=lt.newList(datastructure="ARRAY_LIST")
      for siniestro in lt.iterator(primeros3):
          formato={"Código del accidente":siniestro["CODIGO_ACCIDENTE"],
                     "Hora del accidente":siniestro["HORA_OCURRENCIA_ACC"],
                     "Fecha y hora del accidente":siniestro["FECHA_HORA_ACC"],
                     "Dia del accidente":siniestro["DIA_OCURRENCIA_ACC"],
                     "Localidad":siniestro["LOCALIDAD"],
                     "Dirección":siniestro["DIRECCION"],
                     "Gravedad":siniestro["GRAVEDAD"],
                     "Clase de accidente":siniestro["CLASE_ACC"],
                     "Latitud":siniestro["LATITUD"],
                     "Longitud":siniestro["LONGITUD"]
                     }
          lt.addLast(primeros3_1,formato)
      ultimos3=lt.subList(Analyzer["todo"],lt.size(Analyzer["todo"])-2,3) 
      ultimos3_1=lt.newList(datastructure="ARRAY_LIST")
      
      for siniestro in lt.iterator(ultimos3):
          formato={"Código del accidente":siniestro["CODIGO_ACCIDENTE"],
                     "Hora del accidente":siniestro["HORA_OCURRENCIA_ACC"],
                     "Fecha y hora del accidente":siniestro["FECHA_HORA_ACC"],
                     "Dia del accidente":siniestro["DIA_OCURRENCIA_ACC"],
                     "Localidad":siniestro["LOCALIDAD"],
                     "Dirección":siniestro["DIRECCION"],
                     "Gravedad":siniestro["GRAVEDAD"],
                     "Clase de accidente":siniestro["CLASE_ACC"],
                     "Latitud":siniestro["LATITUD"],
                     "Longitud":siniestro["LONGITUD"]
                     }
          lt.addLast(ultimos3_1,formato)
      elementos=lt.size(Analyzer["todo"]) 
      return primeros3_1,ultimos3_1,elementos

# Funciones de consulta


def req_1(Analyzer,fechainicial,fechafinal):
    """
    Función que soluciona el requerimiento 1
    """
    fechainicial1=fechainicial + " 00:00:00"
    fechainicial1_1=datetime.strptime(fechainicial1, "%Y/%m/%d %H:%M:%S")
    fechafinal1=fechafinal + " 23:59:59"
    fechafinal1_1=datetime.strptime(fechafinal1, "%Y/%m/%d %H:%M:%S")
    fechafinal2=fechafinal1_1+timedelta(seconds=1)
    lista=om.values(Analyzer["fechas"],fechainicial1_1,fechafinal2)
    elementos=0
    for sublistas in lt.iterator(lista):
       tamaño=lt.size(sublistas["lst"])
       elementos+=tamaño
       
    return lista,elementos

def req_2(Analyzer,año,mes,hora1,hora2):
    """
    Función que soluciona el requerimiento 2
    """
    horainicial=datetime.strptime(hora1,"%H:%M:%S")
    horafinal=datetime.strptime(hora2,"%H:%M:%S")
    
    horafinal1=horafinal+timedelta(seconds=1)
    
    mes1=datetime.strptime(mes,"%B").month
    
    año1=año
    codigoAMH= int(str(año1) + str(mes1))
    
    estructura=Analyzer["AMH"]
    arbol=me.getValue(mp.get(estructura,codigoAMH))
    siniestros=om.values(arbol["arbolhoras"],horainicial,horafinal1)
    
    total=0
    siniestros2=lt.newList(datastructure="ARRAY_LIST")  
    for sublistas in lt.iterator(siniestros):
        total+=lt.size(sublistas)
        for siniestro in lt.iterator(sublistas):
            formato={"Código del accidente":siniestro["CODIGO_ACCIDENTE"],
                     "Hora del accidente":siniestro["HORA_OCURRENCIA_ACC"],
                     "Fecha y hora del accidente":siniestro["FECHA_HORA_ACC"],
                     "Dia del accidente":siniestro["DIA_OCURRENCIA_ACC"],
                     "Localidad":siniestro["LOCALIDAD"],
                     "Dirección":siniestro["DIRECCION"],
                     "Gravedad":siniestro["GRAVEDAD"],
                     "Clase de accidente":siniestro["CLASE_ACC"],
                     "Latitud":siniestro["LATITUD"],
                     "Longitud":siniestro["LONGITUD"]
                     }
            lt.addLast(siniestros2,formato)  
    merg.sort(siniestros2,comparefechas0)
      
    return siniestros2,total


def req_3(analyzer,clase,via):
    MapClase=analyzer["clases"]
    FechasClase=me.getValue(mp.get(MapClase,clase))
    Min=datetime.strptime("2015/01/01 00:00:01", "%Y/%m/%d %H:%M:%S")
    Max=datetime.strptime("2022/12/31 23:59:59", "%Y/%m/%d %H:%M:%S")
    FechasRecientes=om.values(FechasClase,Min,Max)
    Fech= lt.subList(FechasRecientes, 0,lt.size(FechasRecientes)) 
    Resp=lt.newList(datastructure="ARRAY_LIST")
    for Requerimiento in lt.iterator(Fech):
        for Formato in lt.iterator(Requerimiento):
            Form={
                "CODIGO_ACCIDENTE":Formato["CODIGO_ACCIDENTE"],
               "FECHA_HORA_ACC": Formato["FECHA_HORA_ACC"],
               "DIA_OCURRENCIA_ACC":Formato["DIA_OCURRENCIA_ACC"],
               "LOCALIDAD":Formato["LOCALIDAD"],
               "DIRECCION": Formato["DIRECCION"],
               "GRAVEDAD":Formato["GRAVEDAD"],
               "CLASE_ACC": Formato["CLASE_ACC"],
               "LATITUD":Formato["LATITUD"],
               "LONGITUD":Formato["LONGITUD"]
               }
            if via in Form["DIRECCION"]:
                lt.addFirst(Resp,Form)
    Final=lt.newList(datastructure="ARRAY_LIST")
    for elements in range(1,4):
        lt.addLast(Final,lt.getElement(Resp,elements))
    return Final


def req_4(analyzer, gravedad, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    fecha_final=datetime.strptime(fecha_final, "%Y/%m/%d %H:%M:%S")
    fecha_inicial=datetime.strptime(fecha_inicial, "%Y/%m/%d %H:%M:%S")
    mapa_gravedades=analyzer["gravedad"]
    arbol_fechas=me.getValue(mp.get(mapa_gravedades,gravedad))
    valores=om.values(arbol_fechas,fecha_inicial,fecha_final)
    final= lt.subList(valores, lt.size(valores)-4,5)
    total= lt.subList(valores, lt.size(valores)-4,5)
    final=lt.newList("ARRAY_LIST")
    for resultado in lt.iterator(total):
        for r in lt.iterator(resultado):
            r={"CODIGO_ACCIDENTE":r["CODIGO_ACCIDENTE"],
               "FECHA_HORA_ACC": r["FECHA_HORA_ACC"],
               "DIA_OCURRENCIA_ACC":r["DIA_OCURRENCIA_ACC"],
               "LOCALIDAD":r["LOCALIDAD"],
               "DIRECCION": r["DIRECCION"],
               "CLASE_ACC": r["CLASE_ACC"],
               "LATITUD":r["LATITUD"],
               "LONGITUD":r["LONGITUD"]}
            lt.addFirst(final,r)
    return final


def req_5(control,año,mes,localidad):
    """
    Función que soluciona el requerimiento 5
    """
    estrucutra=control["localidades"]
    mes1=datetime.strptime(mes,"%B").month
    primerafecha=año+"/"+str(mes1)+"/"+"01" + " " + "00:00:00"
    fechainicial1=datetime.strptime(primerafecha, "%Y/%m/%d %H:%M:%S")
    ultimafecha=año+"/"+str(mes1+1)+"/"+"01" + " " + "00:00:00"
    if mes1 ==12:
        ultimafecha=str(int(año)+1)+"/"+"01"+"/"+"01" + " " + "00:00:00"
    
    
    fechafinal1=datetime.strptime(ultimafecha, "%Y/%m/%d %H:%M:%S")
    
    arbolfechas=me.getValue(mp.get(estrucutra,localidad))
    
    lista=om.values(arbolfechas,fechainicial1,fechafinal1)
    
    tamaño=0
    
    listafinal=lt.newList(datastructure="ARRAY_LIST")
    
    for sublista in lt.iterator(lista):
        tamaño+=lt.size(sublista)
        for siniestro in lt.iterator(sublista):
                formato={"Código del accidente":siniestro["CODIGO_ACCIDENTE"],
                     "Hora del accidente":siniestro["HORA_OCURRENCIA_ACC"],
                     "Fecha y hora del accidente":siniestro["FECHA_HORA_ACC"],
                     "Dia del accidente":siniestro["DIA_OCURRENCIA_ACC"],
                     "Localidad":siniestro["LOCALIDAD"],
                     "Dirección":siniestro["DIRECCION"],
                     "Gravedad":siniestro["GRAVEDAD"],
                     "Clase de accidente":siniestro["CLASE_ACC"],
                     "Latitud":siniestro["LATITUD"],
                     "Longitud":siniestro["LONGITUD"]
                     }
                lt.addFirst(listafinal,formato)
    
    if lt.size(listafinal)<10:
        return listafinal,tamaño
    else:
        listaaentregar=lt.subList(listafinal,lt.size(listafinal)-9,10)
        return listaaentregar,tamaño

    
        

def req_6(Analyzer,año,mes,latitud1,longitud1,radio,Topn):
    """
    Función que soluciona el requerimiento 6
    """
    arboldistancias=om.newMap(omaptype="RBT",comparefunction=distanciaalcentro)
    estructura=Analyzer["AMH"]
    mes1=datetime.strptime(mes,"%B").month
    codigoAMH= int(año + str(mes1))
    mapa=me.getValue(mp.get(estructura,codigoAMH))
    latitud1_1=float(latitud1)
    longitud1_1=float(longitud1)
    for siniestro in lt.iterator (mapa["lstsiniestros"]):
        distancia=0
        latitud2=float(siniestro["LATITUD"])
        longitud2=float(siniestro["LONGITUD"])

        diferencialatitudes=radians(latitud2-latitud1_1)
      
        diferencialongitudes=radians(longitud2-longitud1_1)
        raiz=sin((diferencialatitudes)/2)**2 + cos(radians(latitud1_1))*cos(radians(latitud2))*sin((diferencialongitudes)/2)**2
        
        distancia=2*asin(sqrt(raiz))
        radio=6370
        distanciafinal=distancia*radio
        formato = {"Código del accidente":siniestro["CODIGO_ACCIDENTE"],
                     "Fecha y hora del accidente":siniestro["FECHA_HORA_ACC"],
                     "Dia del accidente":siniestro["DIA_OCURRENCIA_ACC"],
                     "Localidad":siniestro["LOCALIDAD"],
                     "Dirección":siniestro["DIRECCION"],
                     "Gravedad":siniestro["GRAVEDAD"],
                     "Clase de accidente":siniestro["CLASE_ACC"],
                     "Latitud":siniestro["LATITUD"],
                     "Longitud":siniestro["LONGITUD"]
                     
                     }
       
        if distancia<=float(radio):
            om.put(arboldistancias,distanciafinal,formato)
    valores=mp.valueSet(arboldistancias)
    tamaño=lt.size(valores)
    sublista=lt.subList(valores,1,int(Topn))
    return tamaño,sublista
            
            
def req_7(Analyzer,año,mes):
    """
    Función que soluciona el requerimiento 7
    """
    estructura=Analyzer["fechas"]
    mes1=datetime.strptime(mes,"%B").month
    primerafecha=año+"/"+str(mes1)+"/"+"01" + " " + "00:00:00"
    fecha1formato=datetime.strptime(primerafecha, "%Y/%m/%d %H:%M:%S")
    
    
    listafinal=lt.newList(datastructure="ARRAY_LIST")
    centinela=True
    ultimafecha=año+"/"+str(mes1+1)+"/"+"01" + " " + "00:00:00"
    
    if mes1+1==13:
        ultimafecha=str(int(año)+1)+"/"+"1"+"/"+"01" + " " + "00:00:00"
    fecha2formato=datetime.strptime(ultimafecha, "%Y/%m/%d %H:%M:%S")
    
    while centinela:
        diareferenia=fecha1formato.day
        nodo1=om.ceiling(estructura,fecha1formato)
        
        nodo1_1=me.getValue(om.get(estructura,nodo1))
        arbolnodo=nodo1_1["codigo"]
        mincodigo=om.minKey(arbolnodo)
        dato=me.getValue(om.get(arbolnodo,mincodigo))
        diacodigo=datetime.strptime(dato["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d").day
        formato={"Código del accidente":dato["CODIGO_ACCIDENTE"],
                     "Fecha y hora del accidente":dato["FECHA_HORA_ACC"],
                     "Dia del accidente":dato["DIA_OCURRENCIA_ACC"],
                     "Localidad":dato["LOCALIDAD"],
                     "Dirección":dato["DIRECCION"],
                     "Gravedad":dato["GRAVEDAD"],
                     "Clase de accidente":dato["CLASE_ACC"],
                     "Latitud":dato["LATITUD"],
                     "Longitud":dato["LONGITUD"]
                     
                     }
        
       
        
        mayor=fecha1formato + timedelta(hours=23,minutes=59,seconds=59)
        nodo2=om.floor(estructura,mayor)
        nodo2_1=me.getValue(om.get(estructura,nodo2))
        arbolnodo2=nodo2_1["codigo"]
        mincodigo2=om.minKey(arbolnodo2)
        
        dato2=me.getValue(om.get(arbolnodo2,mincodigo2))
        diacodigo2=datetime.strptime(dato2["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d").day
        
        formato2={"Código del accidente":dato2["CODIGO_ACCIDENTE"],
                     "Fecha y hora del accidente":dato2["FECHA_HORA_ACC"],
                     "Dia del accidente":dato2["DIA_OCURRENCIA_ACC"],
                     "Localidad":dato2["LOCALIDAD"],
                     "Dirección":dato2["DIRECCION"],
                     "Gravedad":dato2["GRAVEDAD"],
                     "Clase de accidente":dato2["CLASE_ACC"],
                     "Latitud":dato2["LATITUD"],
                     "Longitud":dato2["LONGITUD"]
                     
                     }
        
        if diacodigo == diareferenia and diacodigo2==diareferenia:
            
            lt.addLast(listafinal,formato)
            lt.addLast(listafinal,formato2)
            
        elif diacodigo == diareferenia:
            lt.addLast(listafinal,formato)
            lt.addLast(listafinal,formato)
        
        elif diacodigo2==diareferenia:
            lt.addLast(listafinal,formato2)
            lt.addLast(listafinal,formato2)
        
        
            
        
        fecha1formato=fecha1formato+timedelta(days=1)
        
        if fecha1formato>=fecha2formato:
            centinela=False
    
    
    
    estructura2=Analyzer["AMH"]
    codigoAMH= int(año + str(mes1))
    arbol=me.getValue(mp.get(estructura2,codigoAMH))
    
    listapython=[] 
    listafrecuencias=[]
    
    i=0
    p=0
    while str(p)+str(i)!="24":      
        hora1=str(p)+str(i)+":00:00"
        hora2=str(p)+str(i)+":59:00"
        listapython.append(hora1)
        lista=om.values(arbol["arbolhoras"],datetime.strptime(hora1, "%H:%M:%S"),datetime.strptime(hora2, "%H:%M:%S"))
        frecuencia=0
        for sublistas in lt.iterator(lista):
            frecuencia+=lt.size(sublistas)    
            
        listafrecuencias.append(frecuencia)
        
        i+=1
        if i==10:
            p+=1
            i=0
            
    
    return listafinal,listafrecuencias,listapython  
    
    


def req_8(Analyzer,Clase,FechIn,FechaFi):
    """
    Función que soluciona el requerimiento 8
    """
    FechaInicial=datetime.strptime(FechIn, "%Y/%m/%d")
    FechaFinal=datetime.strptime(FechaFi, "%Y/%m/%d")
    MapaClase=Analyzer["clases"]
    Fechas=me.getValue(mp.get(MapaClase,Clase))
    FechasRango=om.values(Fechas,FechaInicial,FechaFinal)
    ListaFechas= lt.subList(FechasRango, 0,lt.size(FechasRango)-1)
    final=lt.newList(datastructure="ARRAY_LIST")
    for Requerimiento in lt.iterator(ListaFechas):
        for Formato in lt.iterator(Requerimiento):
            Form={
                "CODIGO_ACCIDENTE":Formato["CODIGO_ACCIDENTE"],
               "FECHA_HORA_ACC": Formato["FECHA_HORA_ACC"],
               "DIA_OCURRENCIA_ACC":Formato["DIA_OCURRENCIA_ACC"],
               "LOCALIDAD":Formato["LOCALIDAD"],
               "DIRECCION": Formato["DIRECCION"],
               "GRAVEDAD":Formato["GRAVEDAD"],
               "CLASE_ACC": Formato["CLASE_ACC"],
               "LATITUD":Formato["LATITUD"],
               "LONGITUD":Formato["LONGITUD"]
               }
            lt.addFirst(final, Formato)
    return ListaFechas


# Funciones utilizadas para comparar elementos dentro de una lista



# Funciones de ordenamiento

def cmpcodigo(codigo1,codigo2):
    if (codigo1 == codigo2):
        return 0
    elif (codigo1 > codigo2):
        return 1
    else:
        return -1
    
def distanciaalcentro(dato1,dato2):
    dato1=dato1
    dato2=dato2
    if (dato1 == dato2):
        return 0
    elif (dato1 > dato2):
        return 1
    else:
        return -1
    

def comparefechas0(fecha1, fecha2):
    """
    Función encargada de comparar dos datos
    """
    hora1=fecha1["Hora del accidente"]
    hora2=fecha2["Hora del accidente"]
    centinela=False
    if hora1==hora2:
        dia1=fecha1["Fecha y hora del accidente"].split(sep=" ")
        dia1final=datetime.strptime(dia1[0], "%Y/%m/%d")
        
        dia2=fecha2["Fecha y hora del accidente"].split(sep=" ")
        dia2final=datetime.strptime(dia2[0], "%Y/%m/%d")
        

        if dia1final != dia2final:
            centinela=dia1final < dia2final
    return centinela
 
def comparefechas1(siniestro1,siniestro2):
      fecha1=siniestro1["Fecha y hora del accidente"].split(sep="+")
      fecha1final=datetime.strptime(fecha1[0], "%Y/%m/%d %H:%M:%S")
      fecha2=siniestro2["Fecha y hora del accidente"].split(sep="+")
      fecha2final=datetime.strptime(fecha2[0], "%Y/%m/%d %H:%M:%S")
      if fecha1final==fecha2final:
                return 0
      elif (fecha1final < fecha2final):
               return 1
      else:
               return -1 
      
    
def comparefechas(fecha1, fecha2):
    """
    Función encargada de comparar dos datos
    """

    if type(fecha1)==str:
        fecha1=datetime.strptime(fecha1, "%Y/%m/%d %H:%M:%S") 
        fecha2=datetime.strptime(fecha2, "%Y/%m/%d %H:%M:%S") 
        
    if (fecha1 == fecha2):
        return 0
    elif (fecha1 > fecha2):
        return 1
    else:
        return -1


def CompareAM(AM1, AM2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if (AM1 == AM2):
        return 0
    elif (AM1 > AM2):
        return 1
    else:
        return -1

def CompareHoras(hora1,hora2):
    if (hora1 == hora2):
        return 0
    elif (hora1 > hora2):
        return 1
    else:
        return -1
 
def comparefechasdic(fecha1,fecha2):
     fecha1=fecha1["FECHA_OCURRENCIA_ACC"] 
     fecha2=fecha2["FECHA_OCURRENCIA_ACC"] 
     
     if type(fecha1)==str:
        fecha1=datetime.strptime(fecha1, "%Y/%m/%d") 
        fecha2=datetime.strptime(fecha2, "%Y/%m/%d") 
    
     if (fecha1 == fecha2):
        return 0
     elif (fecha1 > fecha2):
        return 1
     else:
        return -1


 
def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
