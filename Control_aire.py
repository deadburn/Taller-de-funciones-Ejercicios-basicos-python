import random

#### Zona de Funciones

def verificar_temperatura():
   return (random.randint(0,35))

def verificar_humedad():
    return (random.randint(0,80))

def leer_sensores():
    print("\nIniciando lectura de los sensores...")
    temperatura=verificar_temperatura()
    humedad=verificar_humedad()
    if temperatura >=28 and humedad > 60:
                print(f"Temperatura:{temperatura}°C, Humedad {humedad}% Aire acondicionado encendido")
    elif temperatura >=30:
                print(f"Temperatura:{temperatura}°C Aire acondicionado encendido")
    else:
                print(f"Temperatura: {temperatura}°C, Humedad: {humedad}% Aire acondicionado apagado")
                
def Mostrar_menu():
    print("\nControl automatico de Aire Acondicionado")
    print("Digite '1' para verificar el estado del aire")    
    print("Digite '2' para salir")
    opcion=input("Seleciona una opcion: ")
    return opcion

### codigo principal ###
while True:
    aux_opcion = Mostrar_menu()  
    
    if aux_opcion == '1':
        while True:
            leer_sensores()
            control = input("\nPresiona Enter para verificar el estado nuevamente o '2' para salir: ")
            if control == '2':
                break  
    elif aux_opcion == '2':
        print("Saliendo del sistema...")
        break 

    else:
        print("Opción no válida, intenta de nuevo.")