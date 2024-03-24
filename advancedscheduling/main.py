import os

from advancedscheduling.model import *

data = DataPortal()
data.load(filename="data.dat")
instance = model.create_instance(data)

# Imposta l'indirizzo email NEOS
os.environ['NEOS_EMAIL'] = 'emanuele.rovaretto@edu.unito.it'


# Imposta il solutore su NEOS
solver_manager = SolverManagerFactory('neos')

# Risolvi il problema di ottimizzazione
results = solver_manager.solve(instance, solver="minos", load_solutions=True)


# Stampa i risultati
print(results)