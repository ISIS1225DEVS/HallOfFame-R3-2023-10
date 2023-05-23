"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
from collections import Counter
import traceback
import tabulate
import datetime as dt
from datetime import timedelta as td
import matplotlib.pyplot as mpl
import folium

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Ejecutar Requerimiento 9 - Summary")
    print("0- Salir")

def menu_cant_datos(op):
    filename= None
    match op:
        case 1:
            filename="siniestros/datos_siniestralidad-small.csv"
        case 2:
            filename="siniestros/datos_siniestralidad-5pct.csv"
        case 3:
            filename="siniestros/datos_siniestralidad-10pct.csv"
        case 4:
            filename="siniestros/datos_siniestralidad-20pct.csv"
        case 5:
            filename="siniestros/datos_siniestralidad-30pct.csv"
        case 6:
            filename="siniestros/datos_siniestralidad-50pct.csv"
        case 7:
            filename="siniestros/datos_siniestralidad-80pct.csv"
        case 8:
            filename="siniestros/datos_siniestralidad-large.csv"
        case _:
            print("Opción errónea en cantidad de datos, vuelva a elegir.\n")
    return filename  
  
def print_menu_cant_datos()->int:
    print("1- Datos 0.50%")
    print("2- Datos 5%")
    print("3- Datos 10%")
    print("4- Datos 20%")
    print("5- Datos 30%")
    print("6- Datos 50%")
    print("7- Datos 80%")
    print("8- Datos 100%")
    print("0- Salir")
    op = int(input("Seleccione el tamaño de los datos que desea cargar: "))
    return op

def load_data(control, filename):
    """
    Carga los datos
    """
    control= controller.load_data(control, filename)
    datas= mp.get(control["model"], "datas")
    datas= me.getValue(datas)
    size= controller.data_size(datas)
    prim=controller.tres_prim(datas)
    ulti=controller.tres_ult(datas)
    print("Total de accidentes: "+ str(size))
    print("Los primeros registros de accidentes cargados fueron: ")
    lista= crear_lista_carga(prim)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=6))
    print("Los últimos tres registros de accidentes cargados fueron: ")
    lista= crear_lista_carga(ulti)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=6))
    return control

def crear_lista_carga(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "FECHA_OCURRENCIA_ACC": data["FECHA_OCURRENCIA_ACC"],
            "FECHA_HORA_ACC": data["FECHA_HORA_ACC"],
            "Localidad": data["LOCALIDAD"], 
            "Dirección": data["DIRECCION"],
            "Gravedad" : data["GRAVEDAD"],
            "Clase de accidente": data["CLASE_ACC"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista

def convertir_mes_a_num(mes):
    op= mes.lower()
    match op:
        case "enero":       mes=1 
        case "febrero":     mes=2
        case "marzo":       mes=3
        case "abril":       mes=4
        case "mayo":        mes=5
        case "junio":       mes=6
        case "julio":       mes=7
        case "agosto":      mes=8
        case "septiembre":  mes=9
        case "octubre":     mes=10
        case "noviembre":   mes=11
        case _:   mes=12
    return mes
        
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    inicio= input("Ingrese una fecha inicial: ")
    final= input("Ingrese una fecha final: ")
    elementos, altura, nodos, size= controller.req_1(control, inicio, final)
    print("La altura fue de: "+ str(altura))
    print("Los nodos son: "+ str(nodos))
    print("El número de elementos es: "+ str(size))
    print("Hay "+ str(size)+ " elementos entre "+ str(inicio)+ " y "+str(final))
    lista= crear_lista_req_1(elementos)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=6))
    
    
def crear_lista_req_1(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "CODIGO_ACCIDENTE": data["CODIGO_ACCIDENTE"],
            "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],
            "Dirección": data["DIRECCION"],
            "Gravedad" : data["GRAVEDAD"],
            "Clase de accidente": data["CLASE_ACC"],
            "LOCALIDAD":data["LOCALIDAD"],
            "FECHA_HORA_ACC":data["FECHA_HORA_ACC"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    hora_inc= input("Ingrese la hora inicial: ")
    hora_inc= dt.datetime.strptime(hora_inc,'%H:%M')
    hora_inc= hora_inc.strftime('%H:%M:%S')
    hora_fin= input("Ingrese la hora final: ")
    hora_fin= dt.datetime.strptime(hora_fin,'%H:%M')
    hora_fin= hora_fin.strftime('%H:%M:%S')
    anio= input("Ingrese el año: ")
    mes= input("Ingrese el mes: ")
    mes_num= convertir_mes_a_num(mes)
    data_structs=controller.req_2(control, hora_inc, hora_fin, anio, mes_num)
    size= controller.data_size(data_structs)
    print("Hay "+ str(size)+ " accidentes registrados entre "+ hora_inc + " y "+ hora_fin + " de todos los días del mes "+ str(mes) + " de "+ anio)
    lista=crear_lista_req_2(data_structs)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=6))
    
def crear_lista_req_2(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "CODIGO_ACCIDENTE": data["CODIGO_ACCIDENTE"],
            "HORA_OCURRENCIA_ACC": data["HORA_OCURRENCIA_ACC"],
            "FECHA_OCURRENCIA_ACC": data["FECHA_OCURRENCIA_ACC"],
            "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],
            "LOCALIDAD":data["LOCALIDAD"],
            "Dirección": data["DIRECCION"],
            "Gravedad" : data["GRAVEDAD"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    clase_acc= input("Ingrese la clase del accidente: ")
    via_name= input("Ingrese el nombre de la via de la ciudad: ")
    respuesta= controller.req_3(control, clase_acc, via_name)
    respuesta= controller.tres_prim(respuesta)
    
    size= controller.data_size(respuesta)
    print("Hay "+ str(size)+ " accidentes ocurridos en la localidad de ")
    lista=crear_lista_req_3(respuesta)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 11,maxheadercolwidths=12))
    
def crear_lista_req_3(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "CODIGO_ACCIDENTE": data["CODIGO_ACCIDENTE"],
            "FECHA_HORA_ACC": data["FECHA_HORA_ACC"],
            "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],
            "lOCALIDAD": data["LOCALIDAD"],
            "Dirección": data["DIRECCION"],
            "Gravedad" : data["GRAVEDAD"],
            "Clase de accidente": data["CLASE_ACC"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    fecha_ini= input("Ingrese la fecha inicial: ")
    fecha_fin= input("Ingrese la fecha final: ")
    clase_acc= input("Ingrese la gravedad del accidente: ")
    respuesta, size= controller.req_4(control, fecha_ini, fecha_fin, clase_acc)
    
    print("Hay "+ str(size)+ " accidentes entre las fechas de " + fecha_ini + " y " + fecha_fin)
    lista=crear_lista_req_4(respuesta)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 11,maxheadercolwidths=12))
    
def crear_lista_req_4(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "CODIGO_ACCIDENTE": data["CODIGO_ACCIDENTE"],
            "FECHA_HORA_ACC": data["FECHA_HORA_ACC"],
            "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],
            "lOCALIDAD": data["LOCALIDAD"],
            "Dirección": data["DIRECCION"],
            "Clase de accidente": data["CLASE_ACC"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    localidad= input("Ingrese la localidad: ")
    anio= input("Ingrese el año: ")
    mes= input("Ingrese el mes: ")
    mes_num=convertir_mes_a_num(mes)
    respuesta= controller.req_5(control, localidad, anio, mes_num)
    
    size= controller.data_size(respuesta)
    print("Hay "+ str(size)+ " accidentes ocurridos en la localidad de " + str(localidad)+ " en el mes de "+ str(mes) + " del "+ anio)
    respuesta= controller.diez_prim(respuesta)
    lista=crear_lista_req_5(respuesta)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=8))

def crear_lista_req_5(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "CODIGO_ACCIDENTE": data["CODIGO_ACCIDENTE"],
            "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],
            "Dirección": data["DIRECCION"],
            "Gravedad" : data["GRAVEDAD"],
            "Clase de accidente": data["CLASE_ACC"],
            "FECHA_HORA_ACC": data["FECHA_HORA_ACC"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    anio= input("Ingrese el año: ")
    mes= input("Ingrese el mes: ")
    lat=input("Ingrese la latidud del area central: ")
    lon=input("Ingrese la longitud del area central: ")
    rad=input("Ingrese el radio del área en km: ")
    top=input("Ingrese el numero de accidentes: ")
    
    mes_num=convertir_mes_a_num(mes)
    respuesta=controller.req_6(control, top, lat, lon, rad, anio, mes_num)
    
    size= controller.data_size(respuesta)
    print("los "+ str(top)+ " accidentes más cercanos al punto: " + str(lat)+ ", " + str(lon)+ " dentro de un radio de "+ str(rad) + " Km para el mes de "+ str(mes)+ " de "+ str(anio))
    lista=crear_lista_req_5(respuesta)
    header = lista[0].keys()
    rows =  [x.values() for x in lista]
    print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=6))
    
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    anio= input("Ingrese el año: ")
    mes= input("Ingrese el mes: ")
    mes_num=convertir_mes_a_num(mes)
    
    queue, horas= controller.req_7(control, anio, mes_num)
    
    print("Accidentes más tempranos y tardios para el mes de "+ str(mes)+ " de "+ str(anio))
    
    for i in range(qu.size(queue)):
        dato = qu.dequeue(queue)
        first = lt.firstElement(dato)
        fecha = first["FECHA_OCURRENCIA_ACC"]
        print("Los accidentes del día " + str(fecha))
        
        lista=crear_lista_req_7(dato)
        header = lista[0].keys()
        rows =  [x.values() for x in lista]
        print(tabulate.tabulate(rows,header,tablefmt="grid",maxcolwidths= 10,maxheadercolwidths=6))
        
    size=lt.size(horas)
    dicc= crear_dicc_req_7(horas)
    names = list(dicc.keys())
    values = list(dicc.values())
    mpl.figure(figsize=(10,10))
    mpl.bar(range(len(dicc)), values, tick_label=names)       

    
    mpl.title('Frecuencia de '+ str(size)+ " accidentes por hora del día "+ " para el mes de "+ str(mes)+ " de "+ str(anio))
    mpl.xlabel('Hora del día')
    mpl.xticks(fontsize=7, rotation=90)
    mpl.ylabel('Número de accidentes')
    mpl.show()
    
    

def crear_dicc_req_7(data_structs):
    dicc={}
    lista=[]
    for i in range(24):
        time= td(hours=i)
        dicc[str(time)]=0
    
    for hora in lt.iterator(data_structs):
        lista.append(hora)
        
    num_datos= dict(Counter(lista))
    
    for i in num_datos:
        time= td(hours=i)
        dicc[str(time)]= num_datos[i]
    
        
    return dicc
def crear_lista_req_7(data_structs):
    lista=[]
    for data in lt.iterator(data_structs):
        dicc={
            "CODIGO_ACCIDENTE": data["CODIGO_ACCIDENTE"],
            "DIA_OCURRENCIA_ACC": data["DIA_OCURRENCIA_ACC"],
            "Dirección": data["DIRECCION"],
            "Gravedad" : data["GRAVEDAD"],
            "Clase de accidente": data["CLASE_ACC"],
            "LOCALIDAD": data["LOCALIDAD"],
            "FECHA_HORA_ACC": data["FECHA_HORA_ACC"],
            "Latitud": data["LATITUD"],
            "Longitud": data["LONGITUD"]
            
        }
        lista.append(dicc)
    
    return lista


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    #TODO
    inicio= input("Ingrese una fecha inicial: ")
    final= input("Ingrese una fecha final: ")
    clase = input("Ingrese la clase del accidente: ")
    lista, color = controller.req_8(control, inicio, final, clase)
    m = folium.Map(location=[4.3556, -74.0451], zoom_start=15)
    a = 0
    for i in lt.iterator(lista):
        folium.Marker([i["LATITUD"], i["LONGITUD"]], icon=folium.Icon(color=lt.getElement(color, a))).add_to(m)
        a += 1
    output_file = "map_bogota.html"
    m.save(output_file)
    
def print_req_9(control):
    resultados= ["tiempo , memoria"]
    op= int(input("elige el requerimento: "))
    match op:
            case 1: 
                inicio= input("Ingrese una fecha inicial: ")
                final= input("Ingrese una fecha final: ")
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_1_redux(control,inicio,final))
                    
            case 2: 
                hora_inc= input("Ingrese la hora inicial: ")
                hora_inc= dt.datetime.strptime(hora_inc,'%H:%M')
                hora_inc= hora_inc.strftime('%H:%M:%S')
                hora_fin= input("Ingrese la hora final: ")
                hora_fin= dt.datetime.strptime(hora_fin,'%H:%M')
                hora_fin= hora_fin.strftime('%H:%M:%S')
                anio= input("Ingrese el año: ")
                mes= input("Ingrese el mes: ")
                mes_num= convertir_mes_a_num(mes)
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_2_redux(control, hora_inc, hora_fin, anio, mes_num))
                    
            case 3: 
                clase_acc= input("Ingrese la clase del accidente: ")
                via_name= input("Ingrese el nombre de la via de la ciudad: ")
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_3_redux(control, clase_acc, via_name))
                    
            case 4: 
                fecha_ini= input("Ingrese la fecha inicial: ")
                fecha_fin= input("Ingrese la fecha final: ")
                clase_acc= input("Ingrese la gravedad del accidente: ")
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_4_redux(control, fecha_ini, fecha_fin, clase_acc))
                    
            case 5: 
                localidad= input("Ingrese la localidad: ")
                anio= input("Ingrese el año: ")
                mes= input("Ingrese el mes: ")
                mes_num=convertir_mes_a_num(mes)
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_5_redux(control, localidad, anio, mes_num))
                    
            case 6: 
                anio= input("Ingrese el año: ")
                mes= input("Ingrese el mes: ")
                lat=input("Ingrese la latidud del area central: ")
                lon=input("Ingrese la longitud del area central: ")
                rad=input("Ingrese el radio del área en km: ")
                top=input("Ingrese el numero de accidentes: ")
                mes_num=convertir_mes_a_num(mes)
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_6_redux(control, int(top), float(lat), float(lon), rad, anio, mes_num))
                    
            case 7: 
                anio= input("Ingrese el año: ")
                mes= input("Ingrese el mes: ")
                mes_num=convertir_mes_a_num(mes)
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_7_redux(control, anio, mes_num))
                    
            case 8: 
                inicio= input("Ingrese una fecha inicial: ")
                final= input("Ingrese una fecha final: ")
                clase = input("Ingrese la clase del accidente: ")
                
                for i in range(1,9):
                    control = new_controller()
                    filename = menu_cant_datos(i)
                    data = load_data(control, filename)
                    resultados.append(controller.req_8_redux(control, inicio, final, clase))  
    for i in resultados:
        print(str(i))  

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                op = print_menu_cant_datos()
                filename = menu_cant_datos(op)
                data = load_data(control, filename)
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)
            
            elif int(inputs) == 10:
                print_req_9(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
