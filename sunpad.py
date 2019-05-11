#!/usr/bin/env python3

import os


"""
Sistema de calculo fotovoltaico
empezado el viernes 3 de mayo
por H4K0@BlahCorp
Universidad Tecnologica de Pereira
"""


msga = """
###############################################################################
#                                                                             #
#          Este Script le permite analizar y dimensionar un Sistema           #
#          fotovoltaico. Tenga sus datos a la mano antes de empezar.          #
#                                                                             #
#                                                                             #
# .:. Comparto este script sin garantía alguna .:.                            #
#                                                          H4K0@BlahCorp      #
#                                                                             #
###############################################################################
	   
Presione enter para continuar..."""

msgb = """
       ##############################################################
       #                                                            #
       # Operaciones que puede desarrollar:                         #
       #   1 -> Calcular Facturacion                                #
       #   2 -> Calcular perdida por temperatura                    #
       #   3 -> Diseñar Sistema Off-Grid                            #
       #   4 -> Diseñar Sitema On-Grid / Grid-Tie                   #
       #   5 -> Calcular el banco de baterias                       #
       #                                                            #
       ##############################################################
	   """

msginvoice = """
Para realizar el calculo de la facturacion de cada
mes necesitamos:
			 
			 (Precio Venta 1KW):(Precio Compra 1KW)

  [1] Valor del KW facturado
  [2] Consumo facturado en KW
  [3] KW vendidos 1:1
  [4] KW vendidos 1:Costo comercializacion
  [5] KW vendidos 1:Precio de bolsa
"""

msgHeatLoss = """
Para realizar el calculo de perdida por 
temperatura necesitamos:

  [1] Temperatura de trabajo Optima de la Celula.
  [2] Temperatura ambiente.
  [3] Temperatura de Operacion Nominal de la Celula
  [4] Irradiacion estandar de la zona (W/m2)
  [5] Coeficiente de temperatura VOC del panel.
"""

msgOffGrid = """
Para realizar el calculo de la cantidad de paneles
de un sistema Off-Grid necesitamos:

  [1] Demanda díaria de energía del sistema.
  [2] Horas de Radiación Solar por día (HRS).
  [3] Porcentaje de perdida del sistema
  [4] Potencia del panel.
"""

msgOnGrid = """
Para realizar el calculo de la cantidad de paneles
de un sistema On-Grid/Grid-Tie:

  [1] Demanda díaria de energía del sistema.
  [2] Horas de Radiación Solar por día (HRS).
  [3] Porcentaje de perdida del sistema
  [4] Potencia del panel.
"""

msgBatteryCalc = """
Para dimensionar el sistema de batería requerimos:

  [1] Demanda díaria de energía del sistema.
  [2] Voltaje del sistema.
  [3] Porcentaje de descarga de las baterias
  [4] Días de autonomía del sistema
"""

msgc = """
Hell rocks! lml H4K0@BlahCorp
#############################
"""

msgsharp = "######################"

def clear():
    os.system('clear')

def formLine(text):
    print(text, end=' ')
    z = input()
    return z

def invoiceCalc():
    print (msginvoice)
    a = formLine("Valor del KW facturado(COP):\t")
    b = formLine("Consumo facturado en KW:\t")
    c = formLine("KW vendidos 1:1:\t")
    d = formLine("KW vendidos 1:Costo comercializacion:\t")
    e = formLine("KW vendidos 1:Precio de bolsa: ")
    print(a + b + c + d + e)

def heatLossCalc():
    print (msgHeatLoss)
    a = formLine("Temperatura ambiente:\t")
    b = formLine("Temperatura de Operacion Nominal de la Celula:\t")
    c = formLine("Irradiacion estandar de la zona (W/m2):\t")
    d = formLine("Coeficiente de temperatura VOC del panel:\t")
    e = formLine("VOC del panel:\t")
    print(msgsharp)
    lossHeatForm(a, c, b, d, e)

def offGridDesign():
    print (msgOffGrid)
    a = formLine("Demanda díaria de energía del sistema:\t")
    b = formLine("Horas de Radiación Solar por día (HRS):\t")
    c = formLine("Porcentaje de perdida del sistema:\t")
    d = formLine("Potencia del panel:\t")
    print (a * b + c +d)

def onGridDesig():
    print(msgOnGrid)
    a = formLine("Demanda díaria de energía del sistema:\t")
    b = formLine("Horas de Radiación Solar por día (HRS):\t")
    c = formLine("Porcentaje de perdida del sistema:\t")
    d = formLine("Potencia del panel:\t")
    print (a / b + c + d)

def batteryCalc():
    print(msgBatteryCalc)

def lossHeatForm(ta, gi, tonc, ctvoc, voc):
    tc = (float(ta) + (float(gi) * ((float(tonc)-20.0)/800)))
    scstd = tc - 25.0
    ctxv = (float(ctvoc) * float(ta))/1000
    print("Los paneles están trabajando " + str(scstd) + "°C sobre el ideal STC.")
    print ("Pérdida por Voltio: " + str(format(ctxv, '.2f')) + "V.")
    print("Pérdida total de VOC: " + str(format(((ctxv * float(voc))*10), '.2f')) + "V.")

usos = {
		1:invoiceCalc,
		2:heatLossCalc,
		3:offGridDesign,
		4:onGridDesig,
        5:batteryCalc
		}

###################################################
#         Start Printing in screen (main)         # 
###################################################
clear()
input(msga)
clear()
print (msgb)
###################################################
a = int(input("Elija una operacion: "))
usos[a]()
print (msgc)
print ("Gracias y Chau! :D")
################################################### 