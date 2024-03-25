from pyomo.environ import *

model = AbstractModel()

model.BigM = 1000

model.I = Set()

# sala del paziente i
model.o = Param(model.I)
# tempo di inizio della sala del paziente i
model.s = Param(model.I)
# tempo di fine della sala del paziente i
model.e = Param(model.I)
# se 1 i e l stanno nella stessa sala operatoria
model.q = Param(model.I, model.I, domain=Binary)
# durata degli interventi del paziente i
model.p = Param(model.I, domain=NonNegativeReals)

model.y = Var(model.I, model.I, domain=Binary)
model.c = Var(model.I, domain=NonNegativeReals)
model.d = Var(model.I, model.I, domain=Binary)
model.v = Var(model.I, domain=Binary)
model.w = Var(model.I, domain=Binary)
model.h = Var([1],domain=NonNegativeReals)
model.z = Var(model.I, domain=NonNegativeIntegers)


##F OBBIETTIVO
def obj_exp(model):
    return model.h[1]


model.obj = Objective(expr=obj_exp, sense=minimize)


# VINCOLO 1
def const_1(model, i, l):
    return model.y[i, l] + model.y[l, i] == 1


model.const_1 = Constraint(model.I, model.I, rule=const_1)


# VINCOLO 2
def const_2(model, i):
    return model.z[i] == 1 + sum(model.y[l, i] for l in model.I)


model.const_2 = Constraint(model.I, rule=const_2)


# VINCOLO 3
def const_3(model, i, l):
    return model.z[i] <= model.z[l] - 1 + model.BigM * model.y[l, i]


model.const_3 = Constraint(model.I, model.I, rule=const_3)


# VINCOLO 4
def const_4(model, i, l):
    return model.c[i] - model.BigM * (1 - model.y[i, l]) <= model.c[l]


model.const_4 = Constraint(model.I, model.I, rule=const_4)


# VINCOLO 5  -- RIGURDARE I_{O(I)}
def const_5(model, i):
    return model.c[i] == model.s[i] + sum(model.q[i, l] * model.p[l] * model.y[l, i] for l in model.I)


model.const_5 = Constraint(model.I, rule=const_5)


# VINCOLO 6
def const_6(model, i, l):
    return model.z[l] - model.z[i] >= 2 - model.BigM * model.d[i, l]


model.const_6 = Constraint(model.I, model.I, rule=const_6)


# VINCOLO 7
def const_7(model, i):
    return model.c[i] >= model.e[i] - model.BigM * model.v[i]


model.const_7 = Constraint(model.I, rule=const_7)


# VINCOLO 8
def const_8(model, i):
    return model.c[i] <= model.s[i] + model.BigM * model.w[i]


model.const_8 = Constraint(model.I, rule=const_8)


# VINCOLO 9
def const_9(model, i, l):
    return model.h[1] >= model.c[i] - model.c[l] - model.BigM * (1 - model.d[i, l]) - model.BigM * (
            1 - model.v[i]) - model.BigM * (1 - model.w[l])


model.const_9 = Constraint(model.I, model.I, rule=const_9)
