import pyomo.environ as pyo
import os

model = pyo.ConcreteModel()

model.x = pyo.Var([0, 1], domain=pyo.NonNegativeReals)

model.OBJ = pyo.Objective(sense=pyo.maximize, expr= 2 * model.x[0] + model.x[1])

model.Constraint1 = pyo.Constraint(expr= 2 * model.x[0] + 1 * model.x[1] <= 5)
model.Constraint2 = pyo.Constraint(expr= 1 * model.x[0] - 1 * model.x[1] <= 1)
model.Constraint3 = pyo.Constraint(expr=                     model.x[1] <= 4)

# Imposta l'indirizzo email NEOS
os.environ['NEOS_EMAIL'] = 'emanuele.rovaretto@edu.unito.it'

# Imposta il solutore su NEOS
solver_manager = pyo.SolverManagerFactory('neos')

# Risolvi il problema di ottimizzazione
results = solver_manager.solve(model, solver="minos", load_solutions=False)

# Stampa i risultati
print(results)
