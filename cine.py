##### Zona de Funciones ####
def CrearSillas():
    sillas=int(input("Digite la cantidad de sillas disponibles"))
    return sillas

def tomar_reserva():
    num_reservas=int(input("Digite cuantas sillas quiere reservar"))
    return num_reservas

def validar_sillas(disponible, reserva):
    if disponible > 0 and reserva <= disponible:
        return True
    else:
        return False
    
#### Codigo principal #####
total_sillas=None

while True:
    if total_sillas == 0:
        print("No quedan asientos disponibles")
        break
    print("Digite '1' para hacer una reserva")
    print("Digite '2' para salir ")
    num=input("Elija una opción: ")
    
    try:
        match num:
            case "1":
                if total_sillas==None:
                    total_sillas=CrearSillas()
                    
                if total_sillas <=0:
                    print("No quedan asientos disponibles")
                    break
                
            
                aux_reserva=tomar_reserva()
                aux_validar=validar_sillas(total_sillas, aux_reserva)      
                if aux_validar:
                    total_sillas-=aux_reserva
                    print(f"Reserva confirmada, Quedan {total_sillas} sillas desponibles.")
            
                elif total_sillas=="0":
                    print("No quedan asietos disponibles")
                    break
                else:
                    print(f"No se puede reservar, solo quedan {total_sillas} sillas disponibles. ")
            
            case "2":
                print("Hasta luego")
                break
            case _:
                print("Opcion no válida. Por favor elija 1 o 2.")
    except ValueError:
        print("Digite una opción válida")
            
        