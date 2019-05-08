#! /usr/bin/env python3
"""
Script para traducir la tabla de datos
entregada por la bolsa al insert de MySQL
para automatizar la carga
"""
import os
months= {
             'ene':'01',
             'feb':'02',
             'mar':'03',
             'abr':'04',
             'may':'05',
             'jun':'06',
             'jul':'07',
             'ago':'08',
             'sep':'09',
             'oct':'10',
             'nov':'11',
             'dic':'12',
	        }
inputFile = "CostOnStack.txt"
outputFile = "insertChart.sql"

def clear():
	os.system('clear')

def cwd():
	a = os.getcwd()
	return a

def transMonth(MM):
	mm = months[MM]
	return mm

def translate(line):
	#line = str(line)
	DD   = line[:2]
	MM   = line[3:6]
	YYYY = line[7:11]
	month = transMonth(MM)
	date = YYYY + '-' + month + '-' + DD
	return date

os.chdir(cwd())
ifstream = open(inputFile, 'r')
ofstream = open(outputFile, 'w')

for aline in ifstream:
	line = translate(aline)
	print(line)








