import datetime
import random
import time

#### Zona de Funciones ####

def verificar_hora_noche():
    hora_actual = datetime.datetime.now().hour
    return hora_actual >= 18 or hora_actual < 6

def detectar_movimiento():
    return random.choice([True, False])

def controlar_luces(es_noche, hay_movimiento):
    return es_noche and hay_movimiento

def simular_sistema():
    print("\nIniciando simulación del sistema de control de luces...")
    print("Presiona Ctrl+C para detener la simulación")
    try:
        while True:
            es_noche = verificar_hora_noche()
            hay_movimiento = detectar_movimiento()
            luces_encendidas = controlar_luces(es_noche, hay_movimiento)
            
            print(f"\nEs de noche: {es_noche}")
            print(f"Movimiento detectado: {hay_movimiento}")
            print(f"Luces encendidas: {luces_encendidas}")
            
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\nSimulación finalizada por el usuario.")
        
def mostrar_menu():
    print("\nMenú control de luces")
    print("Seleccione '1'para iniciar la simulación de control de luces")
    print("Selecciona '2' para cerrar el sistema")
    opcion=input("Selecione una opción: ")
    return opcion

#### Codigo principal ####
while True:
    aux_opcion=mostrar_menu()
    if aux_opcion=='1':
        simular_sistema()
    if aux_opcion=='2':
        print("Saliendo del sistema....")
        break
