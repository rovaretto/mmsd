import csv
from io import StringIO

from pyomo.dataportal import DataPortal
def extractDistribution():
    file = open('main-distribution.csv', 'r')
    righeFile = csv.reader(StringIO(file.read()))
    print(righeFile)
    opcode_data = {}

    for righe in righeFile:
        if righe[0] == 'Basic & Regular' and righe[1] == 'Trauma' and righe[2] == 'inpatient':
            opcode = righe[3]  # Supponendo che l'opcode sia sempre all'indice 3
            if opcode not in opcode_data:
                opcode_data[opcode] = []
            opcode_data[opcode].append((righe[4],righe[5],righe[6],righe[7]))
    return opcode_data
    # for opcode, rows in opcode_data.items():
    #     print(f"Opcode {opcode}:")
    #     for row in rows:
    #         print(row)
    #     print("\n")


def caluclateDistribution(distribution):
    opcode_distribution = {}
    for op in distribution:
        dist = distribution[op]
        for elem in dist:
            if elem[1] == 'lognormal':
                print(elem)

caluclateDistribution(extractDistribution())