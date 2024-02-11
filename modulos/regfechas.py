import os
def AddDate(regFechas:dict,equipos:dict):
    isExist = False
    os.system('cls')
    date = str(input("Ingrese la fecha del juego\n ).."))
    while isExist == False:
        os.system('cls')
        tm1 = str(input("Ingrese el equipo Local\n )..")).upper()
        if (tm1 in equipos):
            gTm1 = int(input("Goles anotados por el equipo Local\n ).."))
            isExist=True
    isExist=False
    while isExist == False:
        os.system('cls')
        tm2 = str(input("Ingrese el equipo Visitante\n )..")).upper()
        if (tm2 in equipos and tm2 != tm1):
            gTm2 = int(input("Goles anotados por el equipo Visitante\n ).."))
            isExist=True
    if ((gTm1-gTm2) > 0):
        winner = tm1
        loser = tm2
        glWinner = gTm1
        glLoser = gTm2
        tie = False
    elif ((gTm1-gTm2) == 0):
        winner ='N/A'
        loser = 'N/A'
        tie = True
    else:
        winner = tm2
        loser = tm1
        glWinner = gTm2
        glLoser = gTm1
        tie = False
    nwDate = {
        'fecha': date,
        'local': tm1,
        'visitante': tm2,
        'golesLocal': gTm1,
        'golesVisitante': gTm2,
        'ganador' : winner,
        'perdedor': loser
    }
    regFechas.update({len(regFechas)+1:nwDate})
    if (tie == True):
        data1 = equipos.get(tm1)
        data1['PJ'] += 1
        data1['PE'] += 1
        data1['GF'] += gTm1
        data1['GC'] += gTm2
        data1['TP'] += 1
        data2 = equipos.get(tm2)
        data2['PJ'] += 1
        data2['PE'] += 1
        data2['GF'] += gTm2
        data2['GC'] += gTm1
        data2['TP'] += 1
    else:
        data1 = equipos.get(winner)
        data1['PJ'] += 1
        data1['PG'] += 1
        data1['GF'] += glWinner
        data1['GC'] += glLoser
        data1['TP'] += 3
        data2 = equipos.get(loser)
        data2['PJ'] += 1
        data2['PP'] += 1
        data2['GF'] += glLoser
        data2['GC'] += glWinner
