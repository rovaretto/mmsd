import numpy as np

# vetSalaA = [64.0, 135.0, 62.0, 66.0, 80.0, 73.0]
# vetSalaB = [107.0, 135.0, 221.0, 17.0]
# vetSalaC = [29.0, 129.0, 88.0, 234.0]
# vetSalaD = [130.0, 36.0, 61.0, 29.0, 68.0, 81.0, 75.0]

vetSalaA = np.array([64.0, 135.0, 62.0, 66.0, 80.0, 73.0])
vetSalaB = np.array([107.0, 135.0, 221.0, 17.0])
vetSalaC = np.array([29.0, 129.0, 88.0, 234.0])
vetSalaD = np.array([130.0, 36.0, 61.0, 29.0, 68.0, 81.0, 75.0])

vetSalaA.sort()
vetSalaB.sort()
vetSalaB = vetSalaB[::-1]
vetSalaC.sort()
vetSalaD.sort()
vetSalaD = vetSalaD[::-1]

def concatenaEordina(salaA,salaB,salaC,salaD):
    allVet = np.concatenate((salaA, salaB, salaC, salaD))
    allVet.sort()
    return(allVet)

def calcolaBII(vet):
    diff = np.array([abs(0-vet[0])])
    i = 0
    while i < len(vet)-1:
        diff = np.append(diff, abs(vet[i] - vet[i+1]))
        i = i + 1
    return(max(diff))

def primoAllaFine(vetSala):
    #print("Sala prima:", vetSala)
    vetSala = vetSala[::-1]
    vetSala = np.roll(vetSala,1)
    vetSala = vetSala[::-1]
    #print("Sala dopo", vetSala)

def ultimoAllInizio(vetSala):
    #print("Sala prima:", vetSala)
    vetSala = np.roll(vetSala,1)
    #print("Sala dopo:", vetSala)

# biiMax = calcolaBII(concatenaEordina(vetSalaA, vetSalaB, vetSalaC, vetSalaD))
# vetSalaADopo = primoAllaFine(vetSalaA)
# if calcolaBII(concatenaEordina(vetSalaADopo, vetSalaB, vetSalaC, vetSalaD)) >= biiMax:
#     vetSalaADopo = vetSalaA
# elif calcolaBII(concatenaEordina(vetSalaADopo, vetSalaB, vetSalaC, vetSalaD)) < biiMax:
#     vetSalaBDopo = ultimoAllInizio(vetSalaB)
#     if calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaC, vetSalaD)) >= biiMax:
#         vetSalaBDopo = vetSalaB
#     elif calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaC, vetSalaD)) < biiMax:
#         vetSalaCDopo = primoAllaFine(vetSalaC)
#         if calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaD)) >= biiMax:
#             vetSalaCDopo = vetSalaC
#         elif calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaD)) < biiMax:
#             vetSalaDDopo = ultimoAllInizio(vetSalaD)
#             if calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaD)) >= biiMax:
#                 vetSalaDDopo = vetSalaD
#             elif calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaD)) < biiMax:
#                 vetSalaADopo = primoAllaFine(vetSalaA)

biiMax = calcolaBII(concatenaEordina(vetSalaA, vetSalaB, vetSalaC, vetSalaD))
vetSalaADopo = primoAllaFine(vetSalaA)
vetSalaBDopo = ultimoAllInizio(vetSalaB)
vetSalaCDopo = primoAllaFine(vetSalaC)
vetSalaDDopo = ultimoAllInizio(vetSalaD)
i = 0
while i < 20:
    if calcolaBII(concatenaEordina(vetSalaADopo, vetSalaB, vetSalaC, vetSalaD)) < biiMax:
        calcola = calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaC, vetSalaD))
        if calcola < biiMax:
            calcola = calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaD))
            if calcola < biiMax:
                calcola = calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaDDopo))
                if calcola < biiMax:
                    print("BII", calcolaBII(concatenaEordina(vetSalaADopo, vetSalaBDopo, vetSalaCDopo, vetSalaDDopo)))
    i += 1


# primoAllaFine(vetSalaA)
# ultimoAllInizio(vetSalaB)

# print("BII MAX:", calcolaBII(concatenaEordina(vetSalaA, vetSalaB, vetSalaC, vetSalaD)))