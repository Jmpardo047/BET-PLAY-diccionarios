import os
import modulos.reportes as reps
def MenuReportes(equipos):
    lstOpciones = [1,2,3,4,5]
    os.system('cls')
    print('''
        ************** 
        *  REPORTES  *
        **************
    ''')
    try:
        print('1. Tabla de puntos\n2. Tabla de goles anotados\n3. Tabla de partidos ganados\n4. total de goles y promedio\n5. salir')
        op = int(input(')..'))
        if (op not in lstOpciones):
            MenuReportes(equipos)
    except ValueError:
        print('dato invalido')
        os.system('pause')
        MenuReportes(equipos)
    else:
        if (op == 1):
            reps.TopPoints(equipos)
        elif (op == 2):
            reps.TopGoals(equipos)
        elif (op == 3):
            reps.TopWins(equipos)
        elif (op == 4):
            reps.TotalPoints(equipos)
        elif (op == 5):
            pass