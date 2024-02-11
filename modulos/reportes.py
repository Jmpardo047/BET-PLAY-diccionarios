import os
from tabulate import tabulate
def TopPoints(equipos:dict):
    os.system('cls')
    data = list(equipos.values())
    data.sort(key=lambda item: item['TP'],reverse=True)
    winner = dict(data[0])
    nWin = winner['name']
    print(tabulate(data,headers="keys",tablefmt='grid'))
    print(f'el equipo con mas puntos fue {nWin}')
    os.system('pause')

def TopGoals(equipos:dict):
    os.system('cls')
    data = list(equipos.values())
    data.sort(key=lambda item: item['GF'],reverse=True)
    winner = dict(data[0])
    nWin = winner['name']
    print(tabulate(data,headers="keys",tablefmt='grid'))
    print(f'el equipo con mas goles fue {nWin}')
    os.system('pause')

def TopWins(equipos:dict):
    os.system('cls')
    data = list(equipos.values())
    data.sort(key=lambda item: item['PG'],reverse=True)
    winner = dict(data[0])
    nWin = winner['name']
    print(tabulate(data,headers="keys",tablefmt='grid'))
    print(f'el equipo que mas partidos ganó fue {nWin}')
    os.system('pause')

def TotalPoints(equipos:dict):
    SumGoals = 0
    divPromedio = 0
    for keys,values in equipos.items():
        SumGoals += values['GF']
        divPromedio += 1
    promedio = SumGoals/divPromedio
    print(f'el total de puntos fue {SumGoals}')
    print(f'el promedio de goles entre los equipos fue {promedio}')
    os.system('pause')