import calendar

any = int(input("Introdueix l'any: "))
mes = int(input("Introdueix el mes (1-12): "))

if 1 <= mes <= 12:
    dies = calendar.monthrange(any, mes)[1]
    print(f"El mes {mes} de l'any {any} té {dies} dies.")
else:
    print("Mes invàlid. Introdueix un valor entre 1 i 12.")
