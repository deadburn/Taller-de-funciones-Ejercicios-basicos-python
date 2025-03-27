import datetime
import random
import time

#### Zona de Funciones ####

def verificar_hora_noche():
    hora_actual = datetime.datetime.now().hour
    return hora_actual >= 18 or hora_actual < 6

def controlar_alarma(sensores, es_noche):
    movimiento_detectado = sum(sensores) >= 2
    return movimiento_detectado and es_noche

def simular_sistema_alarma():
    while True:
        es_noche = verificar_hora_noche()
        sensores = [random.randint(0, 1) for _ in range(3)]
        estado_alarma = controlar_alarma(sensores, es_noche)
        
        print(f"\nSensores: {sensores}")
        print(f"Es de noche: {es_noche}")
        print(f"Alarma activada: {estado_alarma}")
        
        opcion = input("\nPresione Enter para continuar o escriba 'salir' para terminar: ")
        if opcion == " ":
            simular_sistema_alarma()
        if opcion.lower() == 'salir':
            break

def menu():
    while True:
        print("\nMenú de control de la alarma")
        print("1. Iniciar simulación de sensores")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            simular_sistema_alarma()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

#### Codigo principal ####
if __name__ == "__main__":
    menu()
