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
from DISClib.ADT import orderedmap as om
import matplotlib.pyplot as plt 
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit=1000
sys.setrecursionlimit(default_limit*10)

def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller ()
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


def load_data(control, filename="siniestros\datos_siniestralidad-large.csv", memflag=True):
    """
    Carga los datos
    """
    # TODO: Realizar la carga de datos
    control = new_controller()
    answer = controller.load_data(control, filename, memflag)
    data = answer[0]
    llaves = control["datos"]
    print("la cantidad de los datos crgados son: " + str(lt.size(llaves)))
    tamaño = lt.size(llaves)
    listaImprimir = [lt.firstElement(llaves), lt.getElement(llaves, 2), lt.getElement(llaves, 3)]
    ultimosTres = [lt.getElement(llaves, (tamaño-2)),  lt.getElement(llaves, (tamaño-1)), lt.lastElement(llaves)]
    colalign = ["center"] * 6
    colwidth = [10] +[12]+[10]+[12]+[10] *3
    print ("los primero tres son:")
    print(tabulate(listaImprimir, headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    print("los ultimos tres son:")
    print(tabulate(ultimosTres, headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")
    return data


def print_req_1(control, fechaInicia, fechaFinal, mem):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    answer = 0
    answer = controller.req_1(control, fechaInicia, fechaFinal, mem)
    resp = answer[0]
    colalign = ["center"] * 9
    colwidth = [10] +[12]+[10]+[12]+[10] *4
    print ("Existen "+ str(len(resp)) + " datos entre " + str(fechaInicia) +" y "+ str(fechaFinal))
    print(tabulate(resp, headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")



def print_req_2(controler, mes, año, horaInicio, HoraFinal, mem):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    answer = 0
    answer = controller.req_2(controler, mes, año, horaInicio, HoraFinal, mem)
    resp = answer[0]
    colalign = ["center"]
    colwidth = [10] +[12]+[10]+[12]+[10] *4
    print ("Existen "+ str(len(resp)) + " datos entre " + str(fechaInicial) +" y "+ str(HoraFinal))
    print(tabulate(resp, headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")


def print_req_3(control, direccion, accidente, mem):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    answer = controller.req_3(control, direccion, accidente, mem)
    req3 = answer[0]
    imprimir = [lt.firstElement(req3), lt.getElement(req3, 2), lt.getElement(req3, 3)]
    colalign = ["center"]*8
    colwidth = [10] + [12] + [10] + [12] + [10] * 4
    print ("Existen "+ str(len(req3['elements'])) + " datos de tipo " + str(accidente) +" en la vía "+ str(direccion))
    print("Estos son los " + str(len(imprimir)) + ' accidentes más recientes')
    print(tabulate(imprimir, headers='keys', tablefmt="fancy_grid",colalign=colalign, maxcolwidths=colwidth, maxheadercolwidths=colwidth))
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")

def print_req_4(control, fechaInicia, fechaFinal,Gravedad,mem):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    answer = controller.req_4(control, fechaInicia, fechaFinal,Gravedad,mem)
    resp = answer[0]
    colalign = ["center"] * 8
    colwidth = [10] +[12]+[10]+[12]+[10] *4
    print ("Hay "+ str( len(resp))+ " accidentes entre las fechas " + str(fechaInicia) +" y "+ str(fechaFinal)+ " de gravedad "+Gravedad.lower()+ ".")
    print(tabulate(resp[0:5], headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")


def print_req_5(control, mes, año, localidad, mem):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    answer = controller.req_5(control, mes, año, localidad, mem)
    resp = answer[0]
    colalign = ["center"]
    colwidth = [10] + [12] + [10] + [12] + [10]
    print ("Existen "+ str(len(answer)) + " datos de tipo " + str(localidad) +" en la vía "+ str(mes))
    print(tabulate(resp[0:10], headers='keys', tablefmt="fancy_grid",colalign=colalign, maxcolwidths=colwidth, maxheadercolwidths=colwidth))
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")


def print_req_6(control, año, mes, cordenadas, Radio, top, mem):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    answer = controller.req_6(control, año, mes, cordenadas, Radio, top, mem)
    listaImprimir = answer[0]
    colalign = ["center"] * 8
    colwidth = [10] +[12]+[10]+[12]+[10] *4
    print ("Los "+ top+" accidentes más cercanos al punto "+ cordenadas[0]+ ", "+cordenadas[1]+ " dentro de un radio de "+ Radio+ " km para el mes de enero de "+str(año) )
    print(tabulate(listaImprimir, headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")



def print_req_7(control, año, mes, memf):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    answer = controller.req_7(control, año, mes, memf)
    mejorespeores, datosHora = answer[0]
     
    llavesmejorespeores = om.keySet(mejorespeores)
    colalign = ["center"] * 8
    colwidth = [10] +[12]+[10]+[12]+[10] *4
    for dia in lt.iterator(llavesmejorespeores):
        lsita = me.getValue(om.get(mejorespeores, dia))
        listaimprimir = [lt.lastElement(lsita), lt.firstElement(lsita)]
        print ("Accidentes de "+str(mes)+" "+ str(dia)+" del " + año)
        print(tabulate(listaimprimir, headers= 'keys', tablefmt="fancy_grid",colalign=colalign,maxcolwidths=colwidth,maxheadercolwidths=colwidth))
    x = 0
    frecuencia=0
    horasLista = []
    elemtos  = []
    while x <= 23:
        horas = str(x)+":00:00"
        horasLista.append (horas)
        llave = om.contains(datosHora, x)
        if llave:
            elemtos.append(me.getValue(om.get(datosHora, x)))
            frecuencia += me.getValue(om.get(datosHora, x))
        else:
            elemtos.append(0)
        x+=1
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")

    fig, ax = plt.subplots()
    plt.bar(horasLista, elemtos)
    ax.set_xlabel('Hora del día')
    ax.set_ylabel("Numero de accidentes")
    ax.set_title('Frecuencia de ' +str(frecuencia)+ " por hora del dia para el mes " + mes +" de "+año + ".")
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.show()              

def print_req_8(control, fechaInicia, fechaFinal, clase, mem):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    answer = controller.req_8(control, fechaInicia, fechaFinal, clase, mem)
    resp = answer[0]
    
    if len(answer) == 2:
        time = answer[1]
        print("Tiempo [ms]: ", f"{time:.3f}")
    elif len(answer) == 3:
        time = answer[1]
        memory = answer[2]
        print("Tiempo [ms]: ", f"{time:.3f}", "||", "Memoria [kB]: ", f"{memory:.3f}")
    
    return resp

def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ("True", "true", "TRUE", "T", "t", "1", 1, True):
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
                print("\n1. 5% de los datos")
                print("2. 10% de los datos")
                print("3. 20% de los datos")

                print("4. 30% de los datos")
                print("5. 50% de los datos")
                print("6. 80% de los datos")
                print("7. 100% de los datos")
                print("8. Versión reducida de los datos")
                percentage = int(input("Seleccione la cantidad de datos a ser cargados: "))
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                if  (9 > percentage > 0):
                    print("Cargando información de los archivos ....\n")
                    control = load_data(control, percentage, mem)
            elif int(inputs) == 2:
                print('Introduzca los datos de la manera AAAA/MM/DD')
                fechaInicia = (input("Seleccione una fecha de inicio: "))
                fechaFinal = (input("Seleccione una fecha de final: "))
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_1(control, fechaInicia, fechaFinal, mem)

            elif int(inputs) == 3:
                horaInicio = (input("Seleccione una hora de inicio (HH:MM): "))
                HoraFinal = (input("Seleccione una hora de final (HH:MM): "))
                mes = (input("Seleccione un mes (enero - diciembre): "))
                año = (input("Seleccione un año: "))
                fechaInicial = horaInicio, mes, año
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_2(control, mes, año, horaInicio, HoraFinal, mem)

            elif int(inputs) == 4:
                accidente = (input("Indique la clase del accidente: "))
                direccion = (input("Indique la dirección del accidente: "))
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_3(control, direccion, accidente, mem)

            elif int(inputs) == 5:
                fechaInicia = (input("Seleccione una fecha de inicio: "))
                fechaFinal = (input("Seleccione una fecha de final: "))
                Gravedad= input("¿De que gravedad deceas busacar el accidente? ")
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_4(control, fechaInicia, fechaFinal,Gravedad,mem)

            elif int(inputs) == 6:
                mes = (input("Seleccione un mes a buscar: "))
                año = (input("Seleccione una año a buscar: "))
                localidad= input("¿De qué localidad deseas buscar el accidente? ")
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_5(control, mes, año, localidad,mem)

            elif int(inputs) == 7:
                mes = (input("Seleccione un mes (enero - diciembre): "))
                año = (input("Seleccione un año: "))
                cordenadas = tuple(input("Seleccione un punto (latitud, longitud) : ").split(","))
                Radio = (input("Seleccione una radio de busqueda: "))
                top = (input("Seleccione cuantos quiere que imprima: "))
                print_req_6(control, año, mes, cordenadas, Radio, top, mem)

            elif int(inputs) == 8:
                mes = (input("Seleccione un mes (enero - diciembre): "))
                año = (input("Seleccione un año: "))
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_7(control, año, mes, mem)

            elif int(inputs) == 9:
                fechaInicia = (input("Seleccione una fecha de inicio: "))
                fechaFinal = (input("Seleccione una fecha de final: "))
                clase = input("¿De que clase deseas busacar el accidente? ")
                print("Desea observar el uso de memoria? (True/False)")
                mem = input("Respuesta: ")
                mem = castBoolean(mem)
                print_req_8(control, fechaInicia, fechaFinal, clase, mem)
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
