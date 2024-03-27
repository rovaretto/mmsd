import csv

from pyomo.dataportal import DataPortal
file = open('main-distribution.csv', 'r')
righeFile = file.read().splitlines()
for righe in righeFile:
    righe = righe.split(",")
    if righe[1] == 'Otolaryngology':
        print(righe)