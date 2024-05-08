import numpy as np

# vetSalaA = [64.0, 135.0, 62.0, 66.0, 80.0, 73.0]
# vetSalaB = [107.0, 135.0, 221.0, 17.0]
# vetSalaC = [29.0, 129.0, 88.0, 234.0]
# vetSalaD = [130.0, 36.0, 61.0, 29.0, 68.0, 81.0, 75.0]

vetSalaA = np.array([64, 135, 62, 66, 80, 73])
vetSalaB = np.array([107, 135, 221, 17])
vetSalaC = np.array([29, 129, 88, 234])
vetSalaD = np.array([130, 36, 61, 29, 68, 81, 75])

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
    diff = [abs(0-vet[0])]
    i = 0
    while i < len(vet)-1:
        diff.append(abs(vet[i] - vet[i+1]))
        i = i + 1
    return(max(diff))

print(calcolaBII(allVet))

# print(allVet)
# print(diff)