import os

from sequenziamento.model import *

data = DataPortal()
data.load(filename='data_patient.dat')
instance = model.create_instance(data)

# Imposta l'indirizzo email NEOS
os.environ['NEOS_EMAIL'] = 'emanuele.rovaretto@edu.unito.it'

# Imposta il solutore su NEOS
solver_manager = SolverManagerFactory('neos')

# Risolvi il problema di ottimizzazione
results = solver_manager.solve(instance, solver="cplex", load_solutions=True)

# for v in instance.component_data_objects(Var, active=True):
#     print(v, value(v))

patSalaA = {}
patSalaB = {}
patSalaC = {}
for i in instance.I:
    if instance.o[i] == 'A':
        patSalaA[i] = value(instance.c[i])
    elif instance.o[i] == 'B':
        patSalaB[i] = value(instance.c[i])
    else:
        patSalaC[i] = value(instance.c[i])

patSalaA = dict(sorted(patSalaA.items(),key=lambda x:x[1]))
patSalaB = dict(sorted(patSalaB.items(),key=lambda x:x[1]))
patSalaC = dict(sorted(patSalaC.items(),key=lambda x:x[1]))

file = open('data_patient_OUTPUT.data','w')
file.write(patSalaA)
file.write(patSalaB)
file.write(patSalaC)
file.close()

# param q :=
# (Adolfo, 'Adolfo') 1
# ('Adolfo', 'Alessandro') 0
# ('Adolfo', 'Andrea') 1
# ('Adolfo', 'Antonio') 0
# ('Adolfo', 'Arturo') 1
# ('Alessandro', 'Adolfo') 0
# ('Alessandro', 'Alessandro') 1
# ('Alessandro', 'Andrea') 0
# ('Alessandro', 'Antonio') 1
# ('Alessandro', 'Arturo') 0
# ('Andrea', 'Adolfo') 1
# ('Andrea', 'Alessandro') 0
# ('Andrea', 'Andrea') 1
# ('Andrea', 'Antonio') 0
# ('Andrea', 'Arturo') 1
# ('Antonio', 'Adolfo') 0
# ('Antonio', 'Alessandro') 1
# ('Antonio', 'Andrea') 0
# ('Antonio', 'Antonio') 1
# ('Antonio', 'Arturo') 0
# ('Arturo', 'Adolfo') 1
# ('Arturo', 'Alessandro') 0
# ('Arturo', 'Andrea') 1
# ('Arturo', 'Antonio') 0
# ('Arturo', 'Arturo') 1
# ;

