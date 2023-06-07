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
import tabulate as tb
import traceback
import folium
import webbrowser as w
import matplotlib.pyplot as plt



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_controller():
    """
        Se crea una instancia del controlador
    """
    
    control=controller.new_controller()
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
    print("0- Salir")


def load_data(control,file,memoria):
    """
    Carga los datos
    """
    if file==1:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-small.csv", memoria)
    elif file==2:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-5pct.csv",memoria)
    elif file==3:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-10pct.csv", memoria)
    elif file==4:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-20pct.csv", memoria)
    elif file==5:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-30pct.csv", memoria)
    elif file==6:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-50pct.csv", memoria)
    elif file==7:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-80pct.csv", memoria)
    elif file==8:
        data = controller.load_data(control, "Data\siniestros\datos_siniestralidad-large.csv", memoria)
    else:
        print("Archivo no encontrado")

    return data
    


def print_data(data):
    """
        Función que imprime un dato dado su ID
    """
    
    if len(data)==3:
        tiempo, memoria,lista=data
        primeros3,ultimos3,elementos=lista
        
        print("Se cargaron "+ str(elementos) + " accidentes")
        print("\n")
        print("Los primeros tres registros de accidentes cargados")
        print("\n")
        print(tb.tabulate(lt.iterator(primeros3),headers="keys",maxcolwidths=5,maxheadercolwidths=5,tablefmt="double_grid"))
        print("\n")
        print("\n")
        print("Los ultimos tres registros de accidentes cargados")
        print("\n")
        print(tb.tabulate(lt.iterator(ultimos3),headers="keys",maxcolwidths=5,maxheadercolwidths=5,tablefmt="double_grid"))
        print("Tiempo [ms]: ", f"{tiempo:.2f}","||",
              "Memoria [kB]: ", f"{memoria:.2f}") 
        print(memoria)
    else:
        tiempo,lista=data
        primeros3,ultimos3,elementos=lista
        
        print("Se cargaron "+ str(elementos) + " accidentes")
        print("\n")
        print("Los primeros tres registros de accidentes cargados")
        print("\n")
        print(tb.tabulate(lt.iterator(primeros3),headers="keys",maxcolwidths=5,maxheadercolwidths=5,tablefmt="double_grid"))
        print("\n")
        print("Los ultimos tres registros de accidentes cargados")
        print("\n")
        print(tb.tabulate(lt.iterator(ultimos3),headers="keys",maxcolwidths=5,maxheadercolwidths=5,tablefmt="double_grid"))
        print("Tiempo [ms]: ", f"{tiempo:.2f}") 
        
        

def print_req_1(control,fechaincio,fechafinal):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    respuesta=controller.req_1(control,fechaincio,fechafinal)
    req,tiempo=respuesta
    lista,elementos=req
    lista_imprimir=lt.newList(datastructure="ARRAY_LIST")
    
    print("hay "+ str(elementos) + " accidentes registrados entre " + fechaincio +" y " + fechafinal)
   
    for sublistas in lt.iterator(lista):
        for siniestro in lt.iterator(sublistas["lst"]):
            formato={"Código del accidente":siniestro["CODIGO_ACCIDENTE"],
                     "Fecha y hora del accidente":siniestro["FECHA_HORA_ACC"],
                     "Dia del accidente":siniestro["DIA_OCURRENCIA_ACC"],
                     "Localidad":siniestro["LOCALIDAD"],
                     "Dirección":siniestro["DIRECCION"],
                     "Gravedad":siniestro["GRAVEDAD"],
                     "Clase de accidente":siniestro["CLASE_ACC"],
                     "Latitud":siniestro["LATITUD"],
                     "Longitud":siniestro["LONGITUD"]
                     }
            lt.addFirst(lista_imprimir,formato)
          
            
    print(tb.tabulate(lt.iterator(lista_imprimir),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
    
    print("Tiempo [ms]: ", f"{tiempo:.2f}")
    
    

def print_req_2(control,mes,año,hora1,hora2):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    respuesta=controller.req_2(control,mes,año,hora1,hora2)
    req,tiempo=respuesta
    lista,elementos=req
    print("hay "+ str(elementos) + " accidentes registrados entre " + hora1 +" y " + hora2)
    
    print(tb.tabulate(lt.iterator(lista),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
    
    print("Tiempo [ms]: ", f"{tiempo:.2f}")         
    
    

def print_req_3(control,clase,via):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print("Los 3 accidentes más recientes de clase ", clase, " ocurridos en la via  ", via, " son: ")
    req3,tiempo=controller.req_3(control, clase, via)
    print(tb.tabulate(lt.iterator(req3),headers="keys",maxcolwidths=13,maxheadercolwidths=13,tablefmt="double_grid"))
    print("Tiempo [ms]: ", f"{tiempo:.2f}")


def print_req_4(control, gravedad, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print("Estos son los 5 accidentes de gravedad ", gravedad, " más recientes entre ", fecha_inicial, " y ", fecha_final)
    req4,tiempo=controller.req_4(control, gravedad, fecha_inicial, fecha_final)
    total=lt.newList("ARRAY_LIST")
    for resultado in lt.iterator(req4):
        for r in lt.iterator(resultado):
            r={"CODIGO_ACCIDENTE":r["CODIGO_ACCIDENTE"],
               "FECHA_HORA_ACC": r["FECHA_HORA_ACC"],
               "DIA_OCURRENCIA_ACC":r["DIA_OCURRENCIA_ACC"],
               "LOCALIDAD":r["LOCALIDAD"],
               "DIRECCION": r["DIRECCION"],
               "CLASE_ACC": r["CLASE_ACC"],
               "LATITUD":r["LATITUD"],
               "LONGITUD":r["LONGITUD"]}
            lt.addFirst(total,r)
            
    print(tb.tabulate(lt.iterator(total),headers="keys",maxcolwidths=13,maxheadercolwidths=13,tablefmt="double_grid"))
    print("Tiempo [ms]: ", f"{tiempo:.2f}")


def print_req_5(control,año,mes,localidad):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    respuesta=controller.req_5(control,año,mes,localidad)
    req,tiempo=respuesta
    lista,elementos=req
    print("hay "+ str(elementos) + " accidentes registrados en" + localidad +" para el mes " + mes +" en el año "+ año)

    print(tb.tabulate(lt.iterator(lista),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
    
    print("Tiempo [ms]: ", f"{tiempo:.2f}")   
   
    

def print_req_6(control,año,mes,latitud,longitud,radio,Topn):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    respuesta=controller.req_6(control,año,mes,latitud,longitud,radio,Topn)
    req,tiempo=respuesta
    valores,sublista=req
    print("el top"+ Topn +"de accidentes mas cercanos al punto"+ "(" + latitud +", "+longitud + ")" "dentro de un radio de " + radio +
          "Km para el mes" + mes + "de" + año)
    
    print(tb.tabulate(lt.iterator(sublista),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))

    print("Número de accidentes totales: " + str(valores))
    
    print("Tiempo [ms]: ", f"{tiempo:.2f}")   
    
def print_req_7(control,año,mes):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    respuesta=controller.req_7(control,año,mes)
    req,tiempo=respuesta
    listafinal,listafrecuencia,listahoras=req
    print(tb.tabulate(lt.iterator(listafinal),headers="keys",maxcolwidths=8,maxheadercolwidths=8,tablefmt="double_grid"))
    positions=range(len(listafrecuencia))
    titulo="Frecuencia de accidentes en "+ mes+ " de "+ año
    plt.bar(positions,listafrecuencia)
    plt.xlabel("Horas")
    plt.ylabel("Frecuencia")
    plt.xticks(positions,listahoras,rotation=75)
    plt.title(titulo)
    plt.show()
    
    print("Tiempo [ms]: ", f"{tiempo:.2f}")  
def print_req_8(control,clase,Fecha_Inicial,Fecha_Final):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    respuesta,tiempo=controller.req_8(control,clase,Fecha_Inicial,Fecha_Final)
    m = folium.Map(location=[4.624088, -74.079902], zoom_start=12, tiles="Stamen terrain")
    for Casos in lt.iterator(respuesta):
        for Puntos in lt.iterator(Casos):
            latitud=Puntos["LATITUD"]
            longitud=Puntos["LONGITUD"]
            Dirección=Puntos["DIRECCION"]
        folium.Marker(location=[latitud, longitud],popup=Dirección,icon=folium.Icon(color="red",icon="cloud"),).add_to(m)
    m.save("Bogotá.html")
    w.open("Bogotá.html")
    print("Tiempo [ms]: ", f"{tiempo:.2f}")
    

def castBoolean(value):
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False


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
                control=new_controller()
                print("Ingrese el archivo que quiere cargar")
                print("1- Small")
                print("2- 5%")
                print("3- 10%")
                print("4- 20%")
                print("5- 30%")
                print("6- 50%")
                print("7- 80%")
                print("8- 100%")
                file=int(input("archivo: "))
                memoria=castBoolean(input("¿Desea medir memoria?: "))
                
                print("Cargando información de los archivos ....\n")
                
                data = load_data(control,file,memoria)
                print_data(data)
            elif int(inputs) == 2:
                fecha1=input("indique fecha inicial del intervalo ")
                fecha2=input("indique fecha final del intervalo ")
                print_req_1(control,fecha1,fecha2)

            elif int(inputs) == 3:
                año=input("Indique año consulta: ")
                mes=input("Indique mes consulta: ")
                hora1=input("indique hora inicial del intervalo ")
                hora2=input("indique hora final del intervalo ")
                print_req_2(control,año,mes,hora1,hora2)

            elif int(inputs) == 4:
                cla=input("Indique la clase de accidente: \n")
                clase=cla.upper()
                vi=input("Indique la via donde ocurrio el accidente: \n")
                via=vi.upper()
                print_req_3(control,clase,via)

            elif int(inputs) == 5:
                gravedad=input("Indique la gravedad del accidente: ")
                fecha_inicio=input("Indique la fecha inicial")
                fecha_final=input("Indique la fecha final")
                print_req_4(control, gravedad, fecha_inicio, fecha_final)

            elif int(inputs) == 6:
                año=input("Indique año consulta: ")
                mes=input("Indique mes consulta: ")
                localidad=input("Indique la localidad deseada")
                print_req_5(control,año,mes,localidad)
                

            elif int(inputs) == 7:
                año=input("Indique año consulta: ")
                mes=input("Indique mes consulta: ")
                latitud=input("indique latitud: ")
                longitud=input("indique longitud: ")
                radio=input("indique el radio: ")
                Topn=input("indique el número de accidentes: ")
                print_req_6(control,año,mes,latitud,longitud,radio,Topn)
                

            elif int(inputs) == 8:
                año=input("Indique año consulta: ")
                mes=input("Indique mes consulta: ")
                
                print_req_7(control,año,mes)

            elif int(inputs) == 9:
                cla=input("Indique la clase de accidente :\n")
                clase=cla.upper()
                Fecha_Inicial=input("Indique la fecha inicial :\n")
                Fecha_Final=input("Indique la Fecha final (año/mes /dia) :\n")
                print_req_8(control,clase,Fecha_Inicial,Fecha_Final)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
