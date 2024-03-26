import os

from sequenziamento.model import *

data = DataPortal()
data.load(filename='data.dat')
instance = model.create_instance(data)

# Imposta l'indirizzo email NEOS
os.environ['NEOS_EMAIL'] = 'emanuele.rovaretto@edu.unito.it'

# Imposta il solutore su NEOS
solver_manager = SolverManagerFactory('neos')

# Risolvi il problema di ottimizzazione
results = solver_manager.solve(instance, solver="cplex", load_solutions=True)

for v in instance.component_data_objects(Var, active=True):
    print(v, value(v))

for i in instance.I:
    print(i, value(instance.c[i]))



# Stampa i risultati
print(results)