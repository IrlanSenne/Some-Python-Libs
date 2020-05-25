import datetime
from colorama import Fore

data=datetime.datetime.now()
print(f"{data.day}/{data.month}/{data.year}")

nasc=datetime.datetime(1989,3,22)
print(nasc.strftime("%A"))

print(nasc.strftime("%a"))
print(nasc.strftime("%w"))
print(nasc.strftime("%d"))
print(nasc.strftime("%b"))
print(nasc.strftime("%B"))
print(nasc.strftime("%m"))
print(nasc.strftime("%Y"))
print(nasc.strftime("%y"))

#Hours

print(nasc.strftime("%H"))
print(nasc.strftime("%I"))
print(nasc.strftime("%p"))
print(nasc.strftime("%M"))
print(data.strftime("%f"))
print(nasc.strftime("%j"))
print(nasc.strftime("%W"))
print()

print(Fore.GREEN + " Aniversário  " + Fore.RESET)
dia=int(input(Fore.YELLOW + "Dia do aniversário...................... : "))
mes=int(input("Mês do aniversário.......................: " + Fore.RESET))

niver=datetime.datetime(data.year,mes,dia)

if niver.strftime("%A") == "Sunday" or niver.strftime("%A") == "Saturday":
    diaSemana = ""
    if niver.strftime("%A") == "Sunday":
        diaSemana = "Domingo"
    elif niver.strftime("%A") == "Saturday":
        diaSemana = "Sábado"
    print(Fore.RED + " -------------------------------------" + Fore.RESET)
    print(Fore.BLUE + " Seu aniversário cai no " + diaSemana + Fore.RESET)
    print(Fore.RED + " -------------------------------------" + Fore.RESET)
else:
    if niver.strftime("%A") == "Monday":
        diaSemana = "Segunda-feira"
    elif niver.strftime("%A") == "Tuesday":
        diaSemana = "Terça-feira"
    elif niver.strftime("%A") == "Wednesday":
        diaSemana = "Quarta-feira"
    elif niver.strftime("%A") == "Thursday":
        diaSemana = "Quinta-feira"
    elif niver.strftime("%A") == "Friday":
        diaSemana = "Sexta-feira"
    print(Fore.RED + " -------------------------------------" + Fore.RESET)
    print(Fore.BLUE + "Seu aniversário cai na " + diaSemana + Fore.RESET)
    print(Fore.RED + " -------------------------------------" + Fore.RESET)


