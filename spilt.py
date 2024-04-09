import re

# Dati di esempio (sostituisci con i tuoi dati effettivi)
data = [
    ['Basic & Regular', 'Trauma', 'inpatient', '1-697.1', 'AN emergence', 'weibull', '1,867761378', '10', '98506904',
     '9', '753500151', '29', '40592903'],
    ['Basic & Regular', 'Trauma', 'inpatient', '1-697.1', 'AN emergence', 'weibull', '2,123456789', '20', '98765432',
     '15', '543210987', '30', '135792468'],
    # Aggiungi altre righe se necessario
]

# Inizializza una lista vuota per memorizzare i campi 2, 3 e 4 di ciascuna riga
filtered_data = []

# Itera su ciascuna riga di dati
for row in data:
    field_2 = row[1]  # Campo 2
    field_3 = row[2]  # Campo 3
    field_4 = row[6]  # Campo 4

    # Verifica se il campo 4 è un numero in virgola mobile
    if re.match(r'^\d+\.\d+$', field_4):
        # Se è un numero in virgola mobile, mantieni il campo 4 come stringa
        filtered_data.append((field_2, field_3, field_4))
    else:
        # Altrimenti, splitta il campo 4 sulla virgola e mantieni solo la parte prima della virgola
        field_4_split = field_4.split(',')
        filtered_data.append((field_2, field_3, field_4_split[0]))

# Stampa i campi filtrati
for fields in filtered_data:
    print(fields)
