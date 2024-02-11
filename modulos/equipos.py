import os
def AddTeam(equipos:dict):
    os.system('cls')
    nombre = str(input("Ingrese el nombre del equipo que quiere agregar\n )..")).upper()
    nwTm = {
        'name':nombre,
        'PJ':0,
        'PG':0,
        'PP':0,
        'PE':0,
        'GF':0,
        'GC':0,
        'TP':0,
    }
    if  (nombre in equipos):
        print(f'El equipo {nombre} ya ha sido agregado')
        os.system('pause')
        AddTeam(equipos)
    else:
        equipos.update({nombre:nwTm})
        
def DlTeam(equipos:dict):
    os.system('cls')
    nombre = str(input('Ingrese el nombre del equipo que quiere eliminar\n )..')).upper()
    if(nombre in equipos):
        equipos.pop(nombre)
    else:
        print('el equipo digitado no se encuentra en la lista')
        os.system('pause')
        DlTeam(equipos)