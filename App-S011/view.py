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
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

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
    return controller.new_controller()


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


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LOCALIDAD", "FECHA_HORA_ACC","LATITUD", "LONGITUD"]
    data=controller.load_data(control)
    first_3=lt.subList(control["acc"], 1, 3)['elements']
    last_3 = lt.subList(control["acc"], lt.size(control["acc"])-2, 3)['elements']
    print(f'Se cargaron: {data} accidentes.')
    print("Los primeros 3 accidentes son: \n")
    tabulate_data(first_3, headers)
    print("\nLos primeros 3 accidentes son: \n")
    tabulate_data(last_3, headers)

def tabulate_data(data_set,header):
    data_set_org=[]
    for i in data_set:
        i=dict([(key,val) for key,val in i.items() if key in header])
        data_set_org.append(i)
    rows=[x.values() for x in data_set_org]
    print(tabulate(rows,list(data_set_org[0].keys()),tablefmt='grid',stralign='center',maxheadercolwidths=13,maxcolwidths=13))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    headers = ["CODIGO_ACCIDENTE", "FECHA_HORA_ACC", "DIA_OCURRENCIA_ACC", "LOCALIDAD", "DIRECCION", "GRAVEDAD", "CLASE_ACC","LATITUD","LONGITUD"]
    initial_date = input("Ingrese la fecha inicial (AAAA/MM/DD): ")
    final_date = input("Ingrese la fecha final (AAAA/MM/DD): ")
    data=controller.req_1(control, initial_date, final_date)
    tabulate_data(data[::-1],headers)
    
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    headers=["CODIGO_ACCIDENTE", "HORA_OCURRENCIA_ACC", "FECHA_OCURRENCIA_ACC", "DIA_OCURRENCIA_ACC", "LOCALIDAD", "DIRECCION", "GRAVEDAD","CLASE_ACC", "LATITUD"]
    year = input("Ingrese el año de consulta (AAAA): ")
    month = input("Ingrese el mes de consulta (MM): ")
    init_time= input("Ingrese la hora y minutos iniciales en horario militar (23:59): ")
    fin_time= input("Ingrese la hora y minutos finales en horario militar (23:59): ")
    tabulate_data(controller.req_2(control,init_time,fin_time,year,month),headers)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    headers=["CODIGO_ACCIDENTE", "FECHA_HORA_ACC", "DIA_OCURRENCIA_ACC", "LOCALIDAD", "DIRECCION", "GRAVEDAD", "CLASE_ACC","LATITUD", "LONGITUD"]
    acc=input("Ingrese la clase de accidente: ")
    name_city= input("Ingrese la via: ")
    tabulate_data(controller.req_3(control,acc,name_city)[::-1],headers)


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    headers=["CODIGO_ACCIDENTE", "FECHA_HORA_ACC", "DIA_OCURRENCIA_ACC", "LOCALIDAD", "DIRECCION", "CLASE_ACC", "LATITUD","LONGITUD"]
    date_init=input("Ingrese la fecha inicial (AAAA/MM/DD): ")
    date_fin= input("Ingrese la fecha final (AAAA/MM/DD): ")
    gravedad = input("Ingrese la gravedad del accidente: ")
    tabulate_data(controller.req_4(control,date_init,date_fin,gravedad)[::-1],headers)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    headers=["CODIGO_ACCIDENTE", "FECHA_HORA_ACC", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LATITUD","LONGITUD"]
    zone= input("Ingrese la localidad: ")
    year = input("Ingrese el año AAAA: ")
    month = input("Ingrese el mes MM: ")
    tabulate_data(controller.req_5(control,zone,month,year)[::-1],headers)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    headers=['CODIGO_ACCIDENTE','FECHA_HORA_ACC','DIA_OCURRENCIA_ACC','LOCALIDAD','DIRECCION','GRAVEDAD','CLASE_ACC','LATITUD','LONGITUD']
    month=input('Month MM: ')
    num_accidents=input('Number of accidents: ')
    year=input('Year AAAA: ')
    latitude=input('Latitude: ')
    lenght=input('Length: ')
    ratio=input('Radio: ')
    tabulate_data(controller.req_6(control,month,year,latitude,lenght,ratio,num_accidents),headers)

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    year = input("Ingrese el año de consulta (AAAA): ")
    month = input("Ingrese el mes de consulta (MM): ")
    headers=['CODIGO_ACCIDENTE','FECHA_HORA_ACC','DIA_OCURRENCIA_ACC','LOCALIDAD','DIRECCION','GRAVEDAD','CLASE_ACC','LATITUD','LONGITUD']
    res= controller.req_7(control,year,month)
    for i in lt.iterator(res):
        if i["size"]>1:
            print(f"Accidentes del día {year+'/'+month+'/'+str(i['key'])}")
            tabulate_data(i["elements"],headers)
        else:
            print(f"Accidentes del día {year+'/'+month+'/'+str(i['key'])}")
            tabulate_data([lt.firstElement(i)],headers)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    
    date_init=input("Enter first person's date(YYYY/MM/DD) : ")
    date_fin=input("Enter second person's date(YYYY/MM/DD) : ")
    type_acc=input("Enter type accident: ")

    controller.req_8(control,date_init,date_fin,type_acc)
    


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
                data = load_data(control)
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

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
