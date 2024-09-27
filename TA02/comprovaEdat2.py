#Saber si ets major o menor d'edat fent servir l'import "datetime"
#Lluis Sans
#27/9/2024
#ASIXc 1A

import datetime

# Variables del any, mes i dia de neixament
any = int(input("Any de neixament:"))
mes = int(input("Mes de neixament:"))
dia = int(input("Dia de neixament:"))

# Obté la data actual
ara = datetime.datetime.now()

# Determina si es major d'edad
if any < ara.year - 18:
    print("Ets major d'edat")
elif mes < ara.month:
    print("Ets major d'edat")
elif dia <= ara.day:
    print("Ets major d'edat")
else:
    print("Ets menor")
