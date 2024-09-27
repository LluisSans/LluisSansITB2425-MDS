#Variables del any, mes i dia de neixament
any = int(input("Any de neixament:"))
mes = int(input("Mes de neixament:"))
dia = int(input("Dia de neixament:"))

if any <= 2005:
    print("Ets major d'edat")

else:
    if any == 2006:
        if mes >= 9:
            if dia <= 27:
                print("Ets major d'edat")
            else:
                print("Ets menor")
        else:
            print("Ets major d'edat")
    else:
        print("Ets menor")