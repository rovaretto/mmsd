import numpy as np

vetSalaA = np.array([3.0, 8.0, 18.0, 32.0])
vetSalaB = np.array([14.0, 25.0, 32.0])
vetSalaC = np.array([2.0, 6.0, 13.0, 22.0, 32.0])
vetSalaD = np.array([20.0, 32.0])

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

biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
print("BII max iniziale", biiMax)
while 1:
    if calcolaBII(concatenaEordina(primoAllaFine(copiaVetSalaA), copiaVetSalaB, copiaVetSalaC, copiaVetSalaD)) < biiMax:
        copiaVetSalaA = primoAllaFine(copiaVetSalaA)
        biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
        if calcolaBII(concatenaEordina(copiaVetSalaA, ultimoAllInizio(copiaVetSalaB), copiaVetSalaC, copiaVetSalaD)) < biiMax:
            copiaVetSalaB = ultimoAllInizio(copiaVetSalaB)
            biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
            if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 1", biiMax)
                # else:
                #     print("OK 2")
            else:
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 3", biiMax)
                # else:
                #     print("OK 4")
        else:
            if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 5")
                # else:
                #     print("OK 6")
            else:
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 7",biiMax)
                # else:
                #     biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 8",copiaVetSalaA,copiaVetSalaB,copiaVetSalaC,copiaVetSalaD, biiMax)
    else:
        if calcolaBII(concatenaEordina(copiaVetSalaA, ultimoAllInizio(copiaVetSalaB), copiaVetSalaC, copiaVetSalaD)) < biiMax:
            copiaVetSalaB = ultimoAllInizio(copiaVetSalaB)
            biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
            if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 9")
                # else:
                #     print("OK 10")
            else:
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                #     print("OK 11",copiaVetSalaA,copiaVetSalaB,copiaVetSalaC,copiaVetSalaD, biiMax)
                # else:
                #     print("OK 12",copiaVetSalaA,copiaVetSalaB,copiaVetSalaC,copiaVetSalaD, biiMax)
        else:
            if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, primoAllaFine(copiaVetSalaC), copiaVetSalaD)) < biiMax:
                copiaVetSalaC = primoAllaFine(copiaVetSalaC)
                biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                    #print("OK 13",copiaVetSalaA,copiaVetSalaB,copiaVetSalaC,copiaVetSalaD, biiMax)
                #else:
                    #print("OK 14",copiaVetSalaA,copiaVetSalaB,copiaVetSalaC,copiaVetSalaD, biiMax)
            else:
                if calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, ultimoAllInizio(copiaVetSalaD))) < biiMax:
                    copiaVetSalaD = ultimoAllInizio(copiaVetSalaD)
                    biiMax = calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD))
                    #print("OK 15",copiaVetSalaA,copiaVetSalaB,copiaVetSalaC,copiaVetSalaD, biiMax)
                else:
                    print("Nessun miglioramento!!!")

    if (copiaVetSalaA == vetSalaA).all() and (copiaVetSalaB == vetSalaB).all() and (copiaVetSalaC == vetSalaC).all() and (copiaVetSalaD == vetSalaD).all():
        print("BII max finale:", calcolaBII(concatenaEordina(copiaVetSalaA, copiaVetSalaB, copiaVetSalaC, copiaVetSalaD)))
        break