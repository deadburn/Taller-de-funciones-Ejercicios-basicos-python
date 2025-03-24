import time
import random

### Zona de Funciones ###
def simular_invernadero():
    print("Iniciando simulación del control de temperatura del invernadero...")
    print("Presiona Ctrl+C para detener la simulacion")
    try:
        while True:
            temperatura = round(random.uniform(5.0, 30.0), 1)
            
            if temperatura < 10.0:
                estado = "CALEFACTOR ACTIVADO"
            elif temperatura <= 25.0:
                estado = "SISTEMA INACTIVO"
            else:
                estado = "VENTILADOR ACTIVADO"
          
            print(f"Temperatura: {temperatura}°C | Estado: {estado}")
            
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nSimulación finalizada por el usuario.")
        
def mostrar_Menu():
    while True:
        print("\nBienvenido al simulador de sensor")
        print("Presiona '1' para iniciar la simulacion")
        opcion=input("Inicia la simulación: ")
        return opcion
    
#### Codigo pruncipal ####
aux_opcion=mostrar_Menu()
if aux_opcion=="1":
    simular_invernadero()
    


