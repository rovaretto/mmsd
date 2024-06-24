import numpy as np

vetSalaA = np.array([135.0, 62.0, 66.0, 80.0, 73.0, 64.0])
vetSalaB = np.array([107.0, 135.0, 221.0, 37.0])
vetSalaC = np.array([29.0, 129.0, 88.0, 234.0])
vetSalaD = np.array([130.0, 36.0, 61.0, 29.0, 68.0, 81.0, 75.0])

vetSalaA.sort()
vetSalaB.sort()
vetSalaB = vetSalaB[::-1]
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

def durataInTempoFineA(salaA):
    copiaSalaA = salaA.copy()
    i = 1
    while i < len(salaA):
        copiaSalaA[i] = copiaSalaA[i-1] + salaA[i]
        i += 1
    return(copiaSalaA)

def durataInTempoFineB(salaB):
    copiaSalaB = salaB.copy()
    i = 1
    while i < len(salaB):
        copiaSalaB[i] = copiaSalaB[i-1] + salaB[i]
        i += 1
    return(copiaSalaB)

def durataInTempoFineC(salaC):
    copiaSalaC = salaC.copy()
    i = 1
    while i < len(salaC):
        copiaSalaC[i] = copiaSalaC[i-1] + salaC[i]
        i += 1
    return(copiaSalaC)

def durataInTempoFineD(salaD):
    copiaSalaD = salaD.copy()
    i = 1
    while i < len(salaD):
        copiaSalaD[i] = copiaSalaD[i-1] + salaD[i]
        i += 1
    return(copiaSalaD)

biiMaxIniziale = biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
print("BII max iniziale", biiMaxIniziale, "con questa configurazione:", "Sala A", copiaVetSalaA, "Sala B", copiaVetSalaB, "Sala C", copiaVetSalaC, "Sala D", copiaVetSalaD)
while 1:
    if calcolaBII(concatenaEordina(durataInTempoFineA(primoAllaFine(copiaVetSalaA)), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD))) < biiMax:
        copiaVetSalaA = primoAllaFine(copiaVetSalaA)
        biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
        if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(ultimoAllInizio(copiaVetSalaB)), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD))) < biiMax:
            copiaVetSalaB = ultimoAllInizio(copiaVetSalaB)
            biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
            if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(primoAllaFine(copiaVetSalaC)), durataInTempoFineD(copiaVetSalaD))) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
            else:
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
        else:
            if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(primoAllaFine(copiaVetSalaC)), durataInTempoFineD(copiaVetSalaD))) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
            else:
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
    else:
        if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(ultimoAllInizio(copiaVetSalaB)), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD))) < biiMax:
            copiaVetSalaB = ultimoAllInizio(copiaVetSalaB)
            biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
            if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(primoAllaFine(copiaVetSalaC)), durataInTempoFineD(copiaVetSalaD))) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
            else:
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
        else:
            if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(primoAllaFine(copiaVetSalaC)), durataInTempoFineD(copiaVetSalaD))) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
            else:
                if calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(ultimoAllInizio(copiaVetSalaD)))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
                else:
                    biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
                    print("BII max finale:", biiMax, "con questa configurazione:", "Sala A", copiaVetSalaA, "Sala B", copiaVetSalaB, "Sala C", copiaVetSalaC, "Sala D", copiaVetSalaD)
                    break

    if (copiaVetSalaA == vetSalaA).all() and (copiaVetSalaB == vetSalaB).all() and (copiaVetSalaC == vetSalaC).all() and (copiaVetSalaD == vetSalaD).all():
        biiMax = calcolaBII(concatenaEordina(durataInTempoFineA(copiaVetSalaA), durataInTempoFineB(copiaVetSalaB), durataInTempoFineC(copiaVetSalaC), durataInTempoFineD(copiaVetSalaD)))
        print("BII max finale:", biiMax, "con questa configurazione:", "Sala A", copiaVetSalaA, "Sala B", copiaVetSalaB, "Sala C", copiaVetSalaC, "Sala D", copiaVetSalaD)
        break

if biiMaxIniziale != biiMax:
    print("BII MAX MIGLIORATO!!!")
else:
    print("BII max NON migliorato!!!")