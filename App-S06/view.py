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
from DISClib.ADT import orderedmap as om
assert cf
from tabulate import tabulate
import traceback
import datetime
import matplotlib.pyplot as plt
import folium
import webbrowser
import os







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
    return {'control': controller.new_controller()}


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


    

def load_data(control, filename, memory):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data = controller.load_data(control['control'], filename, memory)
    time = data[0]
    numelems = data[1]
    first_3 = data[2][0]
    last_3 = data[2][1]
    if memory:
        mem = data[3]
        return time, numelems, first_3, last_3, mem
    return time, numelems, first_3, last_3

def tabulate_list_headers(list, headers):
    list_present = []
    for elem in lt.iterator(list):
        elem_present = {}
        for key in headers:
            elem_present[key]= elem[key]
        list_present.append(elem_present)
    print(tabulate(list_present, headers='keys', tablefmt='heavy_grid', maxcolwidths=10, maxheadercolwidths=10, numalign='right', stralign='left'))

    
def print_data(data, mem):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    print('Este requerimiento tomó ', data[0], ' ms')
    print('\n')
    if mem:
        print('Este requerimiento tomó ', data[4], ' kB')
        print('\n')
    print('Se cargaron ', data[1], ' accidentes')
    print('\n')
    print('Los primeros tres elementos fueron: ')
    tabulate_list_headers(data[2], ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'LOCALIDAD', 'DIRECCION','GRAVEDAD','CLASE_ACC','LATITUD','LONGITUD'])
    print('Los últimos tres elementos fueron: ')
    tabulate_list_headers(data[3], ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'LOCALIDAD', 'DIRECCION','GRAVEDAD','CLASE_ACC','LATITUD','LONGITUD'])

def print_req_1(control, fecha_inicial_str, fecha_final_str, memflag):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    fecha_inicial_list = fecha_inicial_str.split('/')
    fecha_final_list = fecha_final_str.split('/')
    fecha_inicial = datetime.datetime(int(fecha_inicial_list[2]),int(fecha_inicial_list[1]),int(fecha_inicial_list[0]), 00, 00, 00)
    fecha_final = datetime.datetime(int(fecha_final_list[2]),int(fecha_final_list[1]),int(fecha_final_list[0]), 23, 59, 59)
    result = controller.req_1(control['control'], fecha_inicial, fecha_final, memflag)
    
    num_acc = result[0][0]
    lista_acc = result[0][1]
    tiempo = result[1]
    
    print('Se encontraron ', num_acc, ' accidentes entre ', fecha_inicial_str, ' y ', fecha_final_str)
    if num_acc > 0:
        print('Los accidentes fueron:')
        tabulate_list_headers(lista_acc, ['CODIGO_ACCIDENTE','FECHA_HORA_ACC','DIA_OCURRENCIA_ACC','LOCALIDAD','DIRECCION','GRAVEDAD','CLASE_ACC','LATITUD','LONGITUD'])
    print('Este requerimiento tomó: ', tiempo, ' ms')
    
    if memflag:
        memoria = result[2]
        print('Este requrimiento consumió: ', memoria, ' kB')


def print_req_2(control, mes_, anio, hora_inicial_str, hora_final_str, memflag):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    hora_inicial_list = hora_inicial_str.split(':')
    hora_final_list = hora_final_str.split(':')
    hora_inicial = datetime.time(int(hora_inicial_list[0]), int(hora_inicial_list[1]), 00)
    hora_final = datetime.time(int(hora_final_list[0]), int(hora_final_list[1]), 00)
    anio_int = int(anio)
    mes = mes_.upper()
    
    result = controller.req_2(control['control'], mes, anio_int, hora_inicial, hora_final, memflag)
    
    num_acc = result[0][0]
    lista_acc = result[0][1]
    tiempo = result[1]
    
    print('Se encontraron ', num_acc, ' accidentes ocurridos entre ', hora_inicial_str, ' y ', hora_final_str, ' en ', mes, ' de ', anio)
    if num_acc > 0:
        print('Los accidentes fueron:')
        tabulate_list_headers(lista_acc, ['CODIGO_ACCIDENTE','HORA_OCURRENCIA_ACC', 'FECHA_OCURRENCIA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD','DIRECCION','GRAVEDAD','CLASE_ACC', 'LATITUD','LONGITUD'])
    
    print('Este requerimiento tomó: ', tiempo, ' ms')


    if memflag:
        memoria = result[2]
        print('Este requrimiento consumió: ', memoria, ' kB')


def print_req_3(control, clase, via):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    result = controller.req_3(control['control'], clase.upper(), via.upper())
    
    if not lt.isEmpty(result[0][1]):
        num_elems = result[0][0]
        elems = result[0][1]
        time = result[1]
        
        print('Se hallaron ', num_elems, ' accidentes de clase ', clase.upper(), ' ocurridos en ', via.upper())
        tabulate_list_headers(elems, ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'])
        print('Este requerimiento tomó: ', time, " ms")
    else:
        print('No se encontraron accidentes con las características dadas.')
    


def print_req_4(control,fecha_inicial_str,fecha_final_str,gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    fecha_inicial_list=fecha_inicial_str.split("/")
    fecha_final_list=fecha_final_str.split("/")
    fecha_inicial=datetime.date(int(fecha_inicial_list[2]),int(fecha_inicial_list[1]),int(fecha_inicial_list[0]))
    fecha_final=datetime.date(int(fecha_final_list[2]),int(fecha_final_list[1]),int(fecha_final_list[0]))
    result,deltatime=controller.req_4(control["control"],fecha_inicial,fecha_final,gravedad.upper())
    
    if not lt.isEmpty(result):
        num_elems=lt.size(result)
        if num_elems > 5:
            elems=lt.subList(result,1,5)
        else:
            elems=result
    
        print("Se hallaron", num_elems," de gravedad ", gravedad.upper()," durante las fechas ", fecha_inicial_str," y ",fecha_final_str)
        tabulate_list_headers(elems,['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'])
        print("Este requerimiento tomó: ",deltatime," ms")
    else:
        print('No se encontraron accidentes con las características dadas.')
        

def print_req_5(control, localidad,mes,anio):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    result,deltatime = controller.req_5(control['control'], localidad.upper(), mes.upper(), anio.upper())
    
    if not lt.isEmpty(result):
        num_elems = lt.size(result)
        if num_elems > 10:
            elems = lt.subList(result,1,10)
        else:
            elems = result
        
        print('Se hallaron ', num_elems, ' en la localidad ', localidad.upper(), ' durante el año ', anio.upper())
        tabulate_list_headers(elems, ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'])
        print('Este requerimiento tomó: ', deltatime, " ms")
    else:
        print('No se encontraron accidentes con las características dadas.')


def print_req_6(control, mes, anio, radio, latitud, longitud, num_acc):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    result = controller.req_6(control['control'], mes.upper(), int(anio), float(radio), float(latitud), float(longitud), int(num_acc))
    if not lt.isEmpty(result[0]):
        lista_accidentes = result[0]
        time = result[1]
        print('Los ', num_acc, 'accidentes más cercanos al punto (', latitud, ',',longitud,') dentro de un radio de ', radio, ' km para el mes ', mes, ' de ', anio, ' fueron:' )
        tabulate_list_headers(lista_accidentes, ['CODIGO_ACCIDENTE','FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD', 'DISTANCIA'])
        print('Este requerimiento tomó: ', time, " ms")
    else:
        print('No se encontraron accidentes con las características dadas.')

def print_req_7(control, mes, anio):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    result = controller.req_7(control['control'], mes.upper(), int(anio))
    
    accidentes_dias = result[0][1]
    time = result[1]
    hash_frec = result[0][0]
    
    for dia in lt.iterator(accidentes_dias):
        fecha = lt.firstElement(dia)['FECHA_OCURRENCIA_ACC']
        print('Primer y último accidente de ', fecha)
        tabulate_list_headers(dia, ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'])

    x_axis = []
    y_axis = []
    for elem in lt.iterator(om.keySet(hash_frec)):
        key = elem
        value = me.getValue(om.get(hash_frec, elem))
        x_axis.append(key[0:5])
        y_axis.append(value)
    
    plt.bar(x_axis, y_axis)
    title = 'Frecuencia de ' + str(sum(y_axis))+ ' accidentes ocurridos en ' + str(mes) + ' de ' + str(anio)
    plt.xticks(rotation = 90)
    plt.xlabel('Hora del día')
    plt.ylabel('Número de accidentes')
    plt.title(title)
    plt.show(block = False)

    print('Este requerimiento tomó: ', time, " ms")
    
    
def print_req_8(control, clase, fecha_inicial_str, fecha_final_str):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    fecha_inicial_list = fecha_inicial_str.split('/')
    fecha_final_list = fecha_final_str.split('/')
    fecha_inicial = datetime.date(day = int(fecha_inicial_list[0]),month =int(fecha_inicial_list[1]),year= int(fecha_inicial_list[2]))
    fecha_final = datetime.date(day=int(fecha_final_list[0]),month = int(fecha_final_list[1]),year= int(fecha_final_list[2]))
    result = controller.req_8(control['control'], fecha_inicial, fecha_final, clase.upper())
    
    time = result[1]
    num_elems = result[0][0]
    hash_gravedad = result[0][1]
    print('Se encontraron ', num_elems, ' accidentes')
    print('Este requerimiento tomó: ', time, " ms")
    map = folium.Map(location=[4.641667, -74.108611], zoom_start=12)
    list_danos = me.getValue(mp.get(hash_gravedad, 'SOLO DANOS'))
    list_heridos = me.getValue(mp.get(hash_gravedad, 'CON HERIDOS'))
    list_muertos = me.getValue(mp.get(hash_gravedad, 'CON MUERTOS'))
    
    color_gravedad = {'list_danos': (list_danos, 'green', 'SOLO DAÑOS'), 'list_heridos': (list_heridos, 'orange', 'CON HERIDOS'), 'list_muertos': (list_muertos,'red', 'CON MUERTOS')}
    
    for key in color_gravedad.keys():
        list = color_gravedad[key][0]
        for elem in lt.iterator(list):
            elem_codigo = str(elem['CODIGO_ACCIDENTE'])
            elem_fecha = str(elem['FECHA_HORA_ACC'])
            latitud = float(elem['LATITUD'])
            longitud = float(elem['LONGITUD'])
            color = color_gravedad[key][1]
            gravedad = color_gravedad[key][2]
            folium.Marker(location = [latitud, longitud], icon=folium.Icon(color = color), popup = elem_codigo+ '\n' + gravedad + '\n' + elem_fecha).add_to(map)
    map.save('mapa_accidentes.html')
    
    webbrowser.open_new_tab('file:///' + os.getcwd()+'/'+'mapa_accidentes.html')
    
    os.remove('mapa_accidentes.html')


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
                print('1- 1%')
                print('2- 5%')
                print('3- 10%')
                print('4- 20%')
                print('5- 30%')
                print('6- 50%')
                print('7- 80%')
                print('8- 100%')
                input_file = input('Seleccione un tamaño de archivo \n')
                try:
                    if int(input_file) == 1:
                        filename = 'Data/datos_siniestralidad-small.csv'
                    elif int(input_file) == 2:
                        filename = 'Data/datos_siniestralidad-5pct.csv'
                    elif int(input_file) == 3:
                        filename = 'Data/datos_siniestralidad-10pct.csv'
                    elif int(input_file) == 4:
                        filename = 'Data/datos_siniestralidad-20pct.csv'
                    elif int(input_file) == 5:
                        filename = 'Data/datos_siniestralidad-30pct.csv'
                    elif int(input_file) == 6:
                        filename = 'Data/datos_siniestralidad-50pct.csv'
                    elif int(input_file) == 7:
                        filename = 'Data/datos_siniestralidad-80pct.csv'
                    elif int(input_file) == 8:
                        filename = 'Data/datos_siniestralidad-large.csv'
                except Exception as exp:
                    print("ERR:", exp)
                    traceback.print_exc()
                print('1- Si')
                print('2- No')
                input_mem_carga = input('¿Desea medir memoria?\n')
                try:
                    if int(input_mem_carga) == 1:
                        memory_carga = True
                    elif int(input_mem_carga)==2:
                        memory_carga = False
                except Exception as exp:
                    print("ERR:", exp)
                    traceback.print_exc()
                print("Cargando información de los archivos ....\n")
                data = load_data(control, filename, memory_carga)
                print_data(data, memory_carga)
                
                
            elif int(inputs) == 2:
                input_fecha_inicial_req_1 = input('Ingrese una fecha inicial en formato DD/MM/AAAA: ')
                input_fecha_final_req_1 = input('Ingrese una fecha final en formato DD/MM/AAAA: ')
                print_req_1(control, input_fecha_inicial_req_1, input_fecha_final_req_1, False)

            elif int(inputs) == 3:
                input_hora_inicial_req_2 = input('Ingrese una hora inicial en formato HH:MM:SS : ')
                input_hora_final_req_2 = input('Ingrese una hora final en formato HH:MM:SS : ')
                input_mes_req_2= input('Ingrese un mes: ')
                input_anio_req_2= input('Ingrese un año: ')
                print_req_2(control, input_mes_req_2, input_anio_req_2, input_hora_inicial_req_2, input_hora_final_req_2, False)

            elif int(inputs) == 4:
                input_clase_req_3 = input('Ingrese una clase para verificar: ')
                input_via_req_3 = input('Ingrese una vía para verificar: ')
                print_req_3(control, input_clase_req_3, input_via_req_3)

            elif int(inputs) == 5:
                input_fecha_inicio_req_4= input("Ingrese una fecha de inicio en formato DD/MM/AA: ")
                input_fecha_final_req_4=input("Ingrese una fecha final en formato DD/MM/AA: ")
                input_gravedad=input("Ingrese un tipo de gravedad en el accidente: ")
                print_req_4(control,input_fecha_inicio_req_4,input_fecha_final_req_4,input_gravedad)

            elif int(inputs) == 6:
                input_localidad_req_5 = input('Ingrese una localidad de Bogota para verificar: ')
                input_mes_req_5 = input('Ingrese un mes para verificar: ')
                input_anio_req_5 = input('Ingrese un año entre 2015 y 2022 para verificar: ')
                print_req_5(control, input_localidad_req_5, input_mes_req_5, input_anio_req_5 )
        

            elif int(inputs) == 7:
                input_mes_req_6 = input('Ingrese un mes: ')
                input_anio_req_6 = input('Ingrese un año: ')
                input_latitud_req_6 = input('Ingrese una latitud: ')
                input_longitud_req_6 = input('Ingrese una longitud: ')
                input_radio_req_6 = input('Ingrese un radio: ')
                input_num_acc_req_6 = input('Ingrese un número de actividades a consultar: ')
                print_req_6(control, mes = input_mes_req_6, anio = input_anio_req_6, latitud = input_latitud_req_6, longitud = input_longitud_req_6, radio = input_radio_req_6, num_acc = input_num_acc_req_6)

            elif int(inputs) == 8:
                input_mes_req_7 = input('Ingrese un mes: ')
                input_anio_req_7 = input('Ingrese un año: ')
                print_req_7(control, input_mes_req_7, input_anio_req_7)

            elif int(inputs) == 9:
                input_clase_req_8 = input('Ingrese una clase: ')
                input_fecha_inicial_req_8 = input('Ingrese una fecha inicial en el formato DD/MM/AAAA: ')
                input_fecha_final_req_8 = input('Ingrese una fecha final en el formato DD/MM/AAAA: ')
                print_req_8(control, input_clase_req_8, input_fecha_inicial_req_8, input_fecha_final_req_8)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
