from modulos import menu as m
from modulos import equipos as tm
from modulos import regfechas as rf
from modulos import menureps as rp
from tabulate import tabulate
if __name__=='__main__':
    equipos = {
    }
    regFechas = {
    }
    isRunning = True

    while isRunning:
        n = m.CreateMenu()
        if (n == 1):
            tm.AddTeam(equipos)
        elif (n == 2):
            tm.DlTeam(equipos) 
        elif (n == 3):
            rp.MenuReportes(equipos)
        elif (n == 4):
            rf.AddDate(regFechas,equipos)
        elif (n == 5):
            data = list(equipos.values())
            print(tabulate(data,headers="keys",tablefmt='grid'))
            m.os.system('pause')
        elif (n == 6):
            data = list(regFechas.values())
            print(tabulate(data,headers="keys",tablefmt='grid'))
            m.os.system('pause')
        elif (n == 7):
            isActive = False
            m.os.system('cls')
            print("Hasta pronto")
            m.os.system("pause")
