import csv
from io import StringIO

import numpy
from numpy import random


def extractDistribution(loc, specialty, typePatient):
    file = open('main-distribution.csv', 'r')
    righeFile = csv.reader(StringIO(file.read()))
    opcode_data = {}

    for righe in righeFile:
        print(righe)
        if righe[0] == loc and righe[1] == specialty and righe[2] == typePatient:
            opcode = righe[3]  # Supponendo che l'opcode sia sempre all'indice 3
            if opcode not in opcode_data:
                opcode_data[opcode] = []
            opcode_data[opcode].append((righe[4], righe[5], righe[6], righe[7]))
    file.close()

    return opcode_data


def caluclateDistribution(distribution):
    opcode_distribution = {}
    for op in distribution:
        dist = distribution[op]
        totalTime = 0
        for elem in dist:
            if elem[1] == 'lognormal':
                mean = float(elem[2].replace(",", "."))
                sigma = float(elem[3].replace(",", "."))
                tmp = random.lognormal(mean=mean, sigma=sigma)
                totalTime = totalTime + tmp
            elif elem[1] == 'weibull':
                shape = float(elem[2].replace(",", "."))
                scala = float(elem[3].replace(",", "."))
                tmp = scala * random.weibull(a=shape)
                totalTime = totalTime + tmp
            elif elem[1] == 'gamma':
                shape = float(elem[2].replace(",", "."))
                scala = float(elem[3].replace(",", "."))
                tmp = random.gamma(shape=shape, scale=scala)
                totalTime = totalTime + tmp

        opcode_distribution[op] = numpy.ceil(totalTime)
    return opcode_distribution


#genera pazienti di tutte le specialità
def generateAllPatient():
    distribution = {}
    for loc in ['Basic & Regular', 'Maximum excl. University Clinics', 'Specialized']:
        for speciality in ['General', 'Gyn & Obstetrics', 'Otolaryngology', 'Trauma']:
            for typePatient in ['inpatient', 'outpatient']:
                distribution[loc, speciality, typePatient] = caluclateDistribution(
                    extractDistribution(loc, speciality, typePatient))

    return distribution


#genera pazienti con il minutaggio massimo per ogni specialità
def generatePatientMaxMin(minute):
    distribution = generateAllPatient()
    result = {}
    timeSpeciality = 0
    for speciality in ['General', 'Gyn & Obstetrics', 'Otolaryngology', 'Trauma']:
        while timeSpeciality < minute:
            for typePatient in ['inpatient', 'outpatient']:
                for loc in ['Basic & Regular', 'Maximum excl. University Clinics', 'Specialized']:
                    dist = distribution[loc, speciality, typePatient].popitem()
                    result[speciality, dist[0]] = dist[1]
                    timeSpeciality = timeSpeciality + dist[1]
        print(timeSpeciality)
        timeSpeciality = 0

    for elem in result:
        print(elem, result[elem])

    return result

def createSetI(patient):
    setI = "set I :=\n"
    for row in patient:
        setI = setI + row[1] + " \n"
    setI += ";\n"
    return setI

def createSetK():
    return "set K :=\n"+ "A\n"+ "B\n"+ "C\n"+ "D\n"+ ";\n"


def createSetT():
    return "set T := \nLunedi \nMartedi\nMercoledi\nGiovedi\nVenerdi\n;\n"

def createSetJ():
    return ""

def createFilePatient():
    patient = generatePatientMaxMin(60 * 8 * 5 * 1.5)
    setI = createSetI(patient)
    setK = createSetK()
    setT = createSetT()

    file = open('data_patient.dat', 'w')
    file.write(setI)
    file.close()


createFilePatient()
