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
linea = "DELETE FROM sunpad;"
lineb = "INSERT INTO 'sunpad' VALUES ('"

def sysDir(chdir):
	os.chdir(chdir)

def cwd():
	a = os.getcwd()
	return a

def transMonth(MM):
	mm = months[MM]
	return mm

def translate(line):
	DD   = line[:2]
	MM   = line[3:6]
	YYYY = line[7:11]
	month = transMonth(MM)
	date = YYYY + '-' + month + '-' + DD
	return date

def valueOnStack(line):
	line = line[12:18]
	char = line[5]
	if char.isnumeric():
		value = str(line[:6])
	else:
		value = str(line[:5])
	return value

def deepTranslate(iFile, oFile):
	ifstream = open(iFile, 'r')
	ofstream = open(oFile, 'w')
	ofstream.write(linea + "\n\n")
	for aline in ifstream:
		line = translate(aline)
		valueOS = valueOnStack(aline)
		line = lineb + line + "', '" + valueOS +"');"
		ofstream.write(line + "\n")
		print(line)
	ifstream.close()
	ofstream.close()

sysDir(cwd())
deepTranslate(inputFile, outputFile)