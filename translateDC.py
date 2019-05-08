#! /usr/bin/env python3
"""
Script para traducir la tabla de datos
entregada por la bolsa al insert de MySQL
para automatizar la carga
"""


import os

def clear():
	os.system('clear')

def cwd():
	a = os.getcwd()
	return a


os.chdir(cwd())

inputFile = "CostoBolsa.txt"
outputFile = "insertChart.sql"

ifstream = open(inputFile, 'r')
ofstream = open(outputFile, 'w')

for aline in ifstream:
	print(aline, end='')







