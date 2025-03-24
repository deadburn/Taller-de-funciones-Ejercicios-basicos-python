#### Zona de Funciones ####

def imprimir_numero():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 ==0:
            print(f"{num}= FizzBuzz.")
        elif num % 3 ==0:
            print(f"{num}= fizz.")
        elif num % 5 == 0:
            print(f"{num}=buzz")
        else:
            print(f"{num}={num}")

def mostrar_menu():
    while True:
        print("Juego FizzBuzz")
        print("1. Iniciar juego")
        print("2. salir")
        opcion = input("selecciona una opcion:" )
        return opcion
    
#### Codigo principal ####

while True:
    aux_Opcion= mostrar_menu()
    imprimir_numero()
    if aux_Opcion=="2":
        print("Hasta luego...")
        break
