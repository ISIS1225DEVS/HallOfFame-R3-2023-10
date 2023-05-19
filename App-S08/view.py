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
import matplotlib.pyplot as plt
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo_mapa, factor_carga, tipo_arbol):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo_mapa, factor_carga, tipo_arbol)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Accidentes en un rango de fechas establecido")
    print("3- Accidentes en un intervalo de horas del día para un mes y año establecido")
    print("4- Los 3 accidentes más recientes de una clase particular ocurridos a lo largo de una vía")
    print("5- Los 5 accidentes más recientes en una gravedad y un rango de fechas establecido")
    print("6- Los 10 accidentes menos recientes ocurridos en un mes y año para una localidad de la ciudad")
    print("7- Mostrar los accidentes ocurridos dentro de una zona específica para un mes y un año")
    print("8- Los accidentes más temprano y más tarde para cada día de un mes y año dado, y grafica de accidentes por hora para ese mismo mes y año")
    print("9- Visualizar todos los accidentes de una clase particular para un rango de fechas en el mapa de Bogotá")
    print("0- Salir")


def load_data(control, filename, mem):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data = controller.load_data(control, filename, mem)
    return data


def print_req_1(control, fecha1, fecha2, mem):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    return controller.req_1(control, fecha1, fecha2, mem)


def print_req_2(control, year, mes, tiempo1, tiempo2, mem):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    return controller.req_2(control, year, mes, tiempo1, tiempo2, mem)


def print_req_3(control, clase, nombre_via, mem):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    return controller.req_3(control, clase, nombre_via, mem)


def print_req_4(control, fecha_inicial, fecha_final, gravedad, mem):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    return controller.req_4(control, fecha_inicial, fecha_final, gravedad, mem)


def print_req_5(control, year, mes, localidad, mem):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    return controller.req_5(control, year, mes, localidad, mem)


def print_req_6(control, year, mes, longitud, latitud, radio, top, mem):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    return controller.req_6(control, year, mes, longitud, latitud, radio, top, mem)


def print_req_7(control, year, mes, escala, mem):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    return controller.req_7(control, year, mes, escala, mem)


def print_req_8(control, fecha1, fecha2, clase, mem):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    return controller.req_8(control, fecha1, fecha2, clase, mem)

def tabular(data, header):
    arr=[]
    for dato in lt.iterator(data):
        forr = dict((k,dato[k]) for k in (header)if k in dato)
        arr.append(forr)
    rows = [x.values() for x in arr]
    print(tabulate(rows, header, tablefmt="grid", maxcolwidths=16)) 

# Se crea el controlador asociado a la vista
filename = "-small"
factor_carga = 0.5
tipo_mapa = "PROBING"
tipo_arbol = "RBT"
control = new_controller(tipo_mapa, factor_carga, tipo_arbol)
mem = False

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False

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
                #mem = input("Desea observar el uso de memoria? (True/False)\n")
                #mem = castBoolean(mem)
                filename = str(input("Elija el tamaño de la muestra que desea: (-5pct, -10pct, -20pct, -30pct, -50pct, -80pct, -large o -small)\n"))
                data = load_data(control, filename, mem)
                print("Total de datos cargados: "+str(lt.size(data[0]["DATOS_TODOS"]))+"\n")
                print("Los primeros tres registros de accidentes cargados fueron:\n")
                primeros = lt.subList(data[0]["DATOS_TODOS"], 1, 3)
                ultimos = lt.subList(data[0]["DATOS_TODOS"], lt.size(data[0]["DATOS_TODOS"])-2, 3)
                header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                tabular(primeros, header)           
                print("\n")
                print("Los últimos tres registros de accidentes cargados fueron:\n")
                tabular(ultimos, header)
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                
            elif int(inputs) == 2:
                fecha1 = str(input("Ingrese fecha inicial (Y/M/D): "))
                fecha2 = str(input("Ingrese fecha final (Y/M/D): "))
                data = print_req_1(control, fecha1, fecha2, mem)
                if lt.size(data[0]) > 0:
                    header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                    print("Hay "+str(lt.size(data[0]))+" accidentes entre "+fecha1+" y "+fecha2)
                    tabular(data[0], header)
                else:
                    print("\n")
                    print("No existen accidentes entre "+fecha1+" y "+fecha2)
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                
            elif int(inputs) == 3:
                year = int(input("Ingrese año: "))
                mes = str(input("Ingrese mes: "))
                mes = mes.upper()
                tiempo1 = str(input("Ingrese el tiempo inicial (H:M:S): "))
                tiempo2 = str(input("Ingrese el tiempo final (H:M:S): "))
                data = print_req_2(control, year, mes, tiempo1, tiempo2, mem)
                if data[0] != False:
                    if lt.size(data[0]) > 0:
                        header = ["CODIGO_ACCIDENTE","HORA_OCURRENCIA_ACC","FECHA_OCURRENCIA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                        print("Hay "+str(lt.size(data[0]))+" accidentes en "+mes+" del "+str(year)+" entre las "+tiempo1+" y las "+tiempo2)
                        tabular(data[0], header)
                    else:
                        print("\n")
                        print("No existen accidentes en "+mes+" del "+str(year)+" entre las "+tiempo1+" y las "+tiempo2)
                else:
                    print("\n")
                    print("¡Ingresó algún parámetro mal!")
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                
            elif int(inputs) == 4:
                clase = str(input("Ingrese clase de accidente: "))
                clase = clase.upper()
                nombre_via = str(input("Ingrese nombre de la via: "))
                nombre_via = nombre_via.upper()
                data = print_req_3(control, clase, nombre_via, mem)
                if data[0] != False:
                    if lt.size(data[0]) > 0:
                        header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                        print("Hay "+str(lt.size(data[0]))+" registros de clase "+clase+" en la via "+nombre_via)
                        if lt.size(data[0]) < 3:
                            print("Estos son los "+str(lt.size(data[0]))+" accidentes más recientes")
                            tabular(data[0], header)
                        else:
                            print("Estos son los 3 accidentes más recientes")
                            data_sub = lt.subList(data[0], 1, 3)
                            tabular(data_sub, header)
                    else:
                        print("\n")
                        print("No existen accidentes de clase "+clase+" en la via "+nombre_via)
                else:
                    print("\n")
                    print("¡Ingresó algún parámetro mal!")
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                    
            elif int(inputs) == 5:
                fecha_inicial = str(input("Ingrese la fecha incial (Y/M/D): "))
                fecha_final = str(input("Ingrese la fecha final (Y/M/D): "))
                gravedad = str(input("Ingrese la gravedad del accidente (SOLO DANOS, CON MUERTOS, CON HERIDOS): "))
                gravedad = gravedad.upper()
                data = print_req_4(control, fecha_inicial, fecha_final, gravedad, mem)
                if lt.size(data[0]) > 0:
                    header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","CLASE_ACC","LATITUD","LONGITUD"]
                    print("Hay "+str(lt.size(data[0]))+" accidentes de gravedad "+gravedad+" registrados entre "+fecha_inicial+" y "+fecha_final)
                    if lt.size(data[0]) < 5:
                        print("Estos son los "+str(lt.size(data[0]))+" más recientes")
                        tabular(data[0], header)
                    else:
                        print("Estos son los 5 más recientes")
                        data_sub = lt.subList(data[0], 1, 5)
                        tabular(data_sub, header)
                else:
                    print("\n")
                    print("No existen accidentes de gravedad "+gravedad+" registrados entre "+fecha_inicial+" y "+fecha_final)
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                    
            elif int(inputs) == 6:
                year = int(input("Ingrese año: "))
                mes = str(input("Ingrese mes: "))
                mes = mes.upper()
                localidad = str(input("Ingrese localidad: "))
                localidad = localidad.upper()
                data = print_req_5(control, year, mes, localidad, mem)
                if data[0] != False:
                    if lt.size(data[0]) > 0:
                        header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                        print("Hay "+str(lt.size(data[0]))+" registros en la localidad "+localidad+" en el mes "+mes+" del año "+str(year))
                        if lt.size(data[0]) < 10:
                            print("Estos son los "+str(lt.size(data[0]))+" más recientes")
                            tabular(data[0], header)
                        else:
                            print("Estos son los 10 más recientes")
                            data_sub = lt.subList(data[0], 1, 10)
                            tabular(data_sub, header)
                    else:
                        print("\n")
                        print("No existen accidentes en la localidad "+localidad+" en el mes "+mes+" del año "+str(year))
                else:
                    print("\n")
                    print("¡Ingresó algún parámetro mal!")
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                    
            elif int(inputs) == 7:
                year = int(input("Ingrese año: "))
                mes = str(input("Ingrese mes: "))
                mes = mes.upper()
                latitud = float(input("Ingrese latitud: "))
                longitud = float(input("Ingrese longitud: "))
                radio = float(input("Ingrese radio (km): "))
                top = int(input("Ingrese número de accidentes a visualizar: "))
                data = print_req_6(control, year, mes, longitud, latitud, radio, top, mem)
                if data[0] != False:
                    if lt.size(data[0]) > 0:
                        header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                        if lt.size(data[0]) >= top:
                            print("Los "+str(top)+" accidentes más cercanos al punto ("+str(latitud)+", "+str(longitud)+") dentro de un radio de "+str(radio)+" km para el mes de "+mes+" del "+str(year))
                            data_sub = lt.subList(data[0],1,top)
                            tabular(data_sub, header)
                        else:
                            print("Hay solo "+str(lt.size(data[0]))+" accidentes cercanos al punto ("+str(latitud)+", "+str(longitud)+") dentro de un radio de "+str(radio)+" km para el mes de "+mes+" del "+str(year))
                            tabular(data[0], header)
                    else:
                        print("\n")
                        print("No existen accidentes cercanos al punto ("+str(latitud)+", "+str(longitud)+") dentro de un radio de "+str(radio)+" km para el mes de "+mes+" del "+str(year))
                else:
                    print("\n")
                    print("¡Ingresó algún parámetro mal!")
                if len(data) == 2:
                    time = data[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 3:
                    time = data[1]
                    memory = data[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                    
            elif int(inputs) == 8:
                year = int(input("Ingrese año: ")) #2019
                mes = str(input("Ingrese mes: ")) #"DICIEMBRE"
                mes = mes.upper()
                escala = int(input("Ingrese la escala del eje Y de la grafica de barras: ")) #4
                data = (print_req_7(control, year, mes, escala, mem))
                print("\n")
                if data[0] != False:   
                    if lt.size(data[0]) > 0:
                        header = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
                        i=1
                        while i < lt.size(data[0]):
                            sub = lt.subList(data[0], i, 2)
                            for elemen in lt.iterator(sub):
                                print("Accidentes del dia "+str(elemen["FECHA_OCURRENCIA_ACC"]))
                                break
                            tabular(sub, header)
                            i+=2
                        horizontal=["0:00:00","1:00:00", "2:00:00","3:00:00","4:00:00","5:00:00","6:00:00",
                                    "7:00:00","8:00:00","9:00:00","10:00:00","11:00:00","12:00:00","13:00:00",
                                    "14:00:00","15:00:00","16:00:00","17:00:00","18:00:00","19:00:00","20:00:00",
                                    "21:00:00","22:00:00","23:00:00"]
                        frecuencia=data[2]
                        vertical=data[1]
                        eje_y = [v/max(vertical)*escala for v in vertical]
                        plt.bar(horizontal, eje_y)
                        plt.xticks(rotation=90)
                        plt.subplots_adjust(bottom=0.20)
                        #plt.ylim(0, escala*1.05)
                        plt.xlabel('Horas del día')
                        plt.ylabel('Número de accidentes')
                        plt.title('Frecuencia de '+frecuencia+' accidentes por hora del día\nPara el mes de '+mes+' de '+str(year))
                        plt.show()
                    else:
                        print("\n")
                        print("No existen accidentes para el mes de "+mes+" del "+str(year))
                else:
                    print("\n")
                    print("¡Ingresó algún parámetro mal!")
                if len(data) == 4:
                    time = data[3]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(data) == 5:
                    time = data[3]
                    memory = data[4]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")
                    

            elif int(inputs) == 9:
                fecha1 = str(input("Ingrese la fecha incial (Y/M/D): "))
                fecha2 = str(input("Ingrese la fecha final (Y/M/D): "))
                clase = str(input("Ingrese clase de accidente: "))
                clase = clase.upper()
                cantidad = print_req_8(control, fecha1, fecha2, clase, mem)
                if cantidad[0] != False:
                    print("Hay "+str(cantidad[0])+" accidentes entre las fechas "+fecha1+" y "+fecha2)
                else:
                    print("\n")
                    print("¡Ingresó algún parámetro mal!")
                if len(cantidad) == 2:
                    time = cantidad[1]
                    print("Tiempo [ms]: ", f"{time:.3f}")
                elif len(cantidad) == 3:
                    time = cantidad[1]
                    memory = cantidad[2]
                    print('Tiempo [ms]: ', f"{time:.3f}", '||',
                        'Memoria [kB]: ', f"{memory:.3f}")

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
