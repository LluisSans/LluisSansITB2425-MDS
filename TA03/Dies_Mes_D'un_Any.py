#Demanar dades
#Validar dades
#Procesar dades

any = int(input("Introdueix l'any: "))
mes = int(input("Introdueix el mes (1-12): "))

if mes >=1 and mes <=12:
    print("OK")
    if mes == 12 or mes == 10 or mes == 8 or mes == 7 or mes == 5 or mes == 3 or mes == 1:
        print("31 dies")
    elif mes == 11 or mes == 9 or mes == 6 or mes == 4:
        print("30 dies")
else:
    print("Error de numero del mes")