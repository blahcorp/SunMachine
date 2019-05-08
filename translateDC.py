#! /usr/bin/env python3
"""
Script para traducir la tabla de datos
entregada por la bolsa al insert de MySQL
para automatizar la carga
"""


import os

inputFile = "CostoBolsa.txt"
#inputFile = "/home/h4k0/Descargas/SunMachine/CostoBolsa.txt"
#outputFile = "insertChart.sql"

ifstream = open(inputFile, 'r')
#ofstream = open(outputFile, 'w')

for aline in ifstream:
	print(aline, end='')







