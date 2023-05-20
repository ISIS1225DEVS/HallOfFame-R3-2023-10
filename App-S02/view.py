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
import traceback
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster

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
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
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
    print("0- Salir")


def load_data(control,filename):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    info,fal3 = controller.load_data(control,filename)
    return info,fal3


def print_fal3(fal3):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    
    print("Los primeros 3 registros de accidentes cargados fueron:\n")
    print(tabulate(fal3[0],tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12)) 
    print("Los ultimos 3 registros de accidentes cargados fueron:\n")
    print(tabulate(fal3[1],tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12))
    


def print_req_1(control,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    param, tabla = controller.req_1(control,fecha_i,fecha_f)
    final_table = [param['elements']] + tabla['elements']
    print("Hay " + str(lt.size(tabla)) + " accidentes registrados entre " + fecha_i + " y " + fecha_f + ".\n")
    print(tabulate(final_table, tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12))
    
def print_req_2(control,horamin_initial,horamin_final,anio,mes):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    req2 = controller.req_2(control,horamin_initial,horamin_final,anio,mes)
    print(("Hay {0} en el intervalo de horas dado {1}:00 y " 
          "{2}:00 en el año {3} y en el mes {4}").format(len(req2)-1,horamin_initial,horamin_final,anio,mes))
    print(tabulate(req2, tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12))


def print_req_3(control,clase_accidente,nombre_via):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    size,req3 = controller.req_3(control,clase_accidente,nombre_via)
    print(("Hay {0} accidentes de la clase {1} ocurrido a lo largo de la via {2}" 
          " y los tres más recientes son:\n".format(size,clase_accidente,nombre_via)))
    print(tabulate(req3, tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12))
    
def print_req_4(control,fecha_i,fecha_f,gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    size, req4 = controller.req_4(control,fecha_i,fecha_f,gravedad)
    
    print("Hay " + str(lt.size(size)) + " accidentes registrados entre " + fecha_i + " y " + fecha_f + ".\n")
    print(tabulate(req4, tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12))
    
def print_req_5(control, localidad, mes, año, Memory):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    mes = mes.upper()
    localidad = localidad.upper()
    delta, final_list = controller.req_5(control, localidad, mes, año, Memory)
    final_table = [final_list[0]['elements']] + final_list[1]['elements']
    print("Hay {0} accidentes ocurridos en la localidad de {1} en el mes de {2} del año {3}.\n".format(len(final_list[1]['elements']), localidad, mes, año))
    if len(final_list[1]['elements']) != 0:
        print("Estos son los 10 accidentes menos recientes:\n")
        print(tabulate(final_table, tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=12))
    if len(delta) == 2:
        print("Tiempo: {0} ms \n Memoria: {1} kb".format(delta[0], delta[1]))
    else:
        print("Tiempo: {0} ms".format(delta[0]))
        


def print_req_6(control,topN,coordenadas,radio,mes,anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    req6 = controller.req_6(control,topN,coordenadas,radio,mes,anio)
    print(("Los {0} accidentes más cercanos al punto ({1},{2}) dentro de un radio de {3} km "
           "para el mes {4} de {5}").format(topN,coordenadas[0],coordenadas[1],radio,mes,anio))
    print(tabulate(req6, tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=13))
    
    
def print_req_7(control, mes, año):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    hours_list, tables = controller.req_7(control, mes, año)
    print("Accidentes más tempranos y tardios para el mes de {0} del año {1}.\n".format(mes, año))
    for i in lt.iterator(tables):
        fecha = lt.getElement(i, 1)["FECHA_HORA_ACC"].split(" ")[0]
        print("Accidentes del día {0}".format(fecha))
        print(tabulate(i['elements'], tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                       maxcolwidths=12,maxheadercolwidths=13))
        
    # Crear labels para la gráfica de barras
    string_bins_list = [str(i) + ":00:00" for i in range(0,24)]
    
    hours_list = hours_list['elements']
    
    # Contar el número de accidentes por cada una de las horas
    int_bins_list = [hours_list.count(i) for i in range(0,24)]
    
    # Graficar el diagrama de barras
    plt.figure()
    plt.bar(string_bins_list, int_bins_list)
    plt.xticks(rotation='vertical')
    plt.title("Frecuencia de {0} accidentes por hora del día\n Para el mes de {1} de {2}".format(len(hours_list), mes, año))
    plt.xlabel("Hora del día")
    plt.ylabel("Número de accidentes")
    plt.subplots_adjust(left=0.125,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
    plt.show()

def print_req_8(control, fecha_inicial, fecha_final, clase, Memory):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    clase = clase.upper()
    delta, req8 = controller.req_8(control, fecha_inicial, fecha_final, clase, Memory)
    print("Hay {0} accidentes entre las fechas {1} y {2}.".format(len(req8['elements']), fecha_inicial, fecha_final))
    my_map = folium.Map(location = [4.64873653, -74.07124224], zoom_start=16)
    c = {"SOLO DANOS" : "green", "CON HERIDOS" : "blue", "CON MUERTOS" : "red"}
    mc = MarkerCluster().add_to(my_map)
    for loc in lt.iterator(req8):
        folium.Marker(
        location = loc["LOCATION"],
        popup = "Fecha: {0}\n Hora:{1}".format(loc["FECHA_OCURRENCIA_ACC"], loc["HORA_OCURRENCIA_ACC"]),
        icon = folium.Icon(color= c[loc["GRAVEDAD"]]),).add_to(mc)
    my_map.save('index.html')
    if len(delta) == 2:
        print("Tiempo: {0} ms \n Memoria: {1} kb".format(delta[0], delta[1]))
    else:
        print("Tiempo: {0} ms".format(delta[0]))

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False

def print_menu_load_data():
    print("="*60)
    print("1- small")
    print("2- 5pct")
    print("3- 10pct")
    print("4- 20pct")
    print("5- 30pct")
    print("6- 50pct")
    print("7- 80pct")
    print("8- large")
     
    inputs_size = input('Seleccione una opción para continuar\n')
    working = True
    while working:
        if int(inputs_size) == 1:
            size = "small"
            working = False
        elif int(inputs_size) == 2:
            size = "5pct"
            working = False
        elif int(inputs_size) == 3:
            size = "10pct"
            working = False
        elif int(inputs_size) == 4:
            size = "20pct"
            working = False
        elif int(inputs_size) == 5:
            size = "30pct"
            working = False
        elif int(inputs_size) == 6:
            size = "50pct"
            working = False
        elif int(inputs_size) == 7:
            size = "80pct"
            working = False    
        elif int(inputs_size) == 8:
            size = "large"
            working = False                    
        else:
            print("Opción errónea, vuelva a elegir.\n")
    return size

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
                control = new_controller()
                size = print_menu_load_data()
                print("Cargando información de los archivos ....\n")
                filename = "siniestros/datos_siniestralidad-{0}.csv".format(size)
                data,fal3 = load_data(control,filename)
                tables = print_fal3(fal3)
                
            elif int(inputs) == 2:
                fecha_inicial = input("ingrese la fecha inicial del intervalo: ")
                fecha_final = input("ingrese la fecha final del intervalo: ")
                fecha_inicial = "/".join(fecha_inicial.split("/")[::-1])
                fecha_final = "/".join(fecha_final.split("/")[::-1])
                print('\n')
                print_req_1(control,fecha_inicial,fecha_final)

            elif int(inputs) == 3:
                horamin_initial = input("Ingrese hora y minutos (hh:mm) iniciales del intervalo de tiempo:\n")
                horamin_final = input("Ingrese hora y minutos (hh:mm) finales del intervalo de tiempo:\n")
                anio = input("Ingrese año de consulta:\n")
                mes = input("Ingrese mes de consulta:\n")
                print_req_2(control,horamin_initial,horamin_final,anio,mes)

            elif int(inputs) == 4:
                clase_accidente = input("Indique clase de accidente que desea consultar:\n")
                nombre_via = input("Indique el nombre de la vía:\n")
                print_req_3(control,clase_accidente,nombre_via)

            elif int(inputs) == 5:
                fecha_i = input("ingrese la fecha inicial del intervalo: ")
                fecha_f = input("ingrese la fecha final del intervalo: ")
                gravedad = input("ingrese la gravedad del accidente: ").upper()
                fecha_i = "/".join(fecha_i.split("/")[::-1])
                fecha_f = "/".join(fecha_f.split("/")[::-1])
                print('\n')
                print_req_4(control,fecha_i,fecha_f,gravedad)

            elif int(inputs) == 6:
                localidad = input("Ingrese la localidad de Bogotá de interés:\n")
                mes = input("Ingrese un mes de interés:\n")
                año = input("Ingrese un año de interés:\n")
                print("Desea observar el uso de memoria? (True/False)")
                Flag = input("Respuesta: ")
                print_req_5(control, localidad, mes, año, castBoolean(Flag))

            elif int(inputs) == 7:
                topN = int(input("Ingrese el número N de accidentes más cercanos que desea consultar:\n"))
                print("Especifique coordenadas por favor...")
                latitud = float(input("Ingrese latitud:\n"))
                longitud = float(input("ingrese longitud:\n"))
                coordenadas = latitud,longitud
                radio = float(input("Ingrese el radio del area en km:\n"))
                mes = input("Ingrese mes a consultar:\n").upper()
                anio = input("Ingrese año a consultar:\n")
                print_req_6(control,topN,coordenadas,radio,mes,anio)

            elif int(inputs) == 8:
                mes = input("Ingrese un mes de interés:\n")
                año = input("Ingrese un año de interés:\n")
                print_req_7(control, mes, año)

            elif int(inputs) == 9:
                fecha_inicial = input("ingrese la fecha inicial del intervalo: ")
                fecha_final = input("ingrese la fecha final del intervalo: ")
                clase = input("Ingrese la clase deseada: ")
                print('\n')
                print("Desea observar el uso de memoria? (True/False)")
                Flag = input("Respuesta: ")
                print_req_8(control, fecha_inicial, fecha_final, clase, castBoolean(Flag))

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
