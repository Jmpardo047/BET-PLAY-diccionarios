import os
def CreateMenu()->int:
    lstOpciones = [1,2,3,4,5,6,7]
    opciones ="1. Agregar equipo\n2. eliminar equipo\n3. reportes\n4. Agregar fecha jugada\n5. Ver tabla de equipos\n6. Ver registro de fechas\n7. salir "
    titulo = '''
        *****************************
        *  BIENVENIDO A LA BETPLAY  *
        *****************************
    '''
    os.system('cls')
    print(titulo)
    print(opciones)
    try:   
        n = int(input(").."))
        if (n not in lstOpciones):
            CreateMenu()
    except ValueError:
        print('dato invalido')
        os.system('pause')
        CreateMenu()
    else:
        return n
