import numpy as np

vetSalaA = np.array([5.0, 10.0, 14.0, 3.0])
vetSalaB = np.array([14.0, 11.0, 7.0])   # [7.0, 14.0, 11.0]
                                         # []
vetSalaC = np.array([2.0, 4.0, 7.0, 9.0, 10.0])
vetSalaD = np.array([20.0, 12.0])

# vetSalaA = np.array([3.0, 8.0, 18.0, 32.0])  [5.0, 15.0, 29.0, 32.0]
# vetSalaB = np.array([14.0, 25.0, 32.0])      [7.0, 21.0, 32.0]
# vetSalaC = np.array([2.0, 6.0, 13.0, 22.0, 32.0])
# vetSalaD = np.array([20.0, 32.0])

vetSalaA.sort()
# vetSalaB.sort()
# vetSalaB = vetSalaB[::-1]
vetSalaC.sort()
vetSalaD.sort()
vetSalaD = vetSalaD[::-1]

copiaVetSalaA = vetSalaA
copiaVetSalaB = vetSalaB
copiaVetSalaC = vetSalaC
copiaVetSalaD = vetSalaD

def concatenaEordina(salaA, salaB, salaC, salaD):
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
    vetSala = vetSala[::-1]
    vetSala = np.roll(vetSala,1)
    vetSala = vetSala[::-1]
    return(vetSala)

def ultimoAllInizio(vetSala):
    vetSala = np.roll(vetSala,1)
    return(vetSala)

def durataInTempoFine(salaA, salaB, salaC, salaD):
    copiaSalaA = salaA
    i = 1
    while i < len(salaA):
        copiaSalaA[i] = copiaSalaA[i-1] + salaA[i]
        i += 1



    copiaSalaC = salaC
    i = 1
    while i < len(salaC):
        copiaSalaC[i] = copiaSalaC[i - 1] + salaC[i]
        i += 1

    return(copiaSalaA, copiaSalaB, copiaSalaC, copiaSalaD)

print(vetSalaA)
print(durataInTempoFine(vetSalaA))


# biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
# print("BII max iniziale", biiMax)
# while 1:
#     if calcolaBII(concatenaEordina(primoAllaFine(copiaVetSalaA), copiaVetSalaB, copiaVetSalaC, copiaVetSalaD)) < biiMax:
#         copiaVetSalaA = primoAllaFine(copiaVetSalaA)
#         biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#         if calcolaBII(concatenaEordina(copiaVetSalaA, ultimoAllInizio(copiaVetSalaB), copiaVetSalaC, copiaVetSalaD)) < biiMax:
#             copiaVetSalaB = ultimoAllInizio(copiaVetSalaB)
#             biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#             if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
#                 copiaVetSalaC = primoAllaFine(copiaVetSalaC)
#                 biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#             else:
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#         else:
#             if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
#                 copiaVetSalaC = primoAllaFine(copiaVetSalaC)
#                 biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#             else:
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#     else:
#         if calcolaBII(concatenaEordina(copiaVetSalaA, ultimoAllInizio(copiaVetSalaB), copiaVetSalaC, copiaVetSalaD)) < biiMax:
#             copiaVetSalaB = ultimoAllInizio(copiaVetSalaB)
#             biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#             if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
#                 copiaVetSalaC = primoAllaFine(copiaVetSalaC)
#                 biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#             else:
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#         else:
#             if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
#                 copiaVetSalaC = primoAllaFine(copiaVetSalaC)
#                 biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#             else:
#                 if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
#                     copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
#                     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
#                 else:
#                     print("Nessun miglioramento!!!")
#
#     if (copiaVetSalaA == vetSalaA).all() and (copiaVetSalaB == vetSalaB).all() and (copiaVetSalaC == vetSalaC).all() and (copiaVetSalaD == vetSalaD).all():
#         print("BII max finale:", calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD)))
#         break