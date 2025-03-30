import datetime
#### Zona de Funciones ####

def verificar_horario_atencion():
    hora_actual = datetime.datetime.now().hour
    return 9 <= hora_actual < 21  # Horario de atención: 9 AM - 9 PM

def verificar_acceso(tiene_membresia, es_empleado):
    horario_valido = verificar_horario_atencion()
    return (tiene_membresia and horario_valido) or es_empleado

def simular_sistema():
    try:
        tiene_membresia = input("¿Tienes membresía? (s/n): ").strip().lower() == 's'
        es_empleado = input("¿Eres empleado? (s/n): ").strip().lower() == 's'
        estado_acceso = verificar_acceso(tiene_membresia, es_empleado)
        print(f"\nCliente con membresía: {tiene_membresia}")
        print(f"Cliente es empleado: {es_empleado}")
        print(f"Horario de atención: {verificar_horario_atencion()}")
        print(f"Acceso: {estado_acceso}")
    except ValueError:
        print("Digiteun valor válido")
            
def mostrar_menu():
    print("\nMenú Control de Acceso")
    print("Seleccione '1' para iniciar la simulación de control de acceso")
    print("Seleccione '2' para salir del sistema")
    opcion = input("Seleccione una opción: ")
    return opcion

#### Código principal ####
while True:
    aux_opcion = mostrar_menu()
    if aux_opcion == '1':
        simular_sistema()
    elif aux_opcion == '2':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
