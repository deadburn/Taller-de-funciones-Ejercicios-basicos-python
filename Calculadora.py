#### Zona de funciones #####

def tomarNumero1():
    num1=int(input("Digite un numero"))
    return num1
def tomarNumero2():
    num2=int(input("Digite el segundoo numero"))
    return num2

def procesarDatos(opcion):
    match opcion:
            case "1":
                auxnum1= tomarNumero1()
                auxnum2= tomarNumero2()
                auxresultado=hacerSuma(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
            case "2":
                auxnum1= tomarNumero1()
                auxnum2= tomarNumero2()
                auxresultado=hacerResta(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
            case "3":
                auxnum1= tomarNumero1()
                auxnum2= tomarNumero2()
                auxresultado=hacermMultipli(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
            case "4":
                auxnum1= tomarNumero1()
                auxnum2= tomarNumero2()
                auxresultado=hacerDivi(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
            case "5":
                print("Hasta luego")
            
            
            
def mostrarMenu():
    print("Digite '1' para hacer una suma")            
    print("Digite '2' para hacer una resta")
    print("Digite '3' para hacer una multiplicación")
    print("Digite '4' para hacer una divición")
    print("Digite '5' para salir")
    opcion=input()
    return opcion

def imprimirResultado(auxresultado):
    print(f"El resultado es {auxresultado:.2f} ")

def hacerSuma(num1, num2):
    resultado= num1 + num2 
    return resultado
    
def hacerResta(num1, num2):
    resultado= num1 - num2 
    return resultado
    
def hacermMultipli(num1, num2):
    resultado= num1 * num2 
    return resultado
    
def hacerDivi(num1, num2):
    resultado= num1 / num2 
    return resultado
    
    
##### Codigo Principal ########
while True:
    auxopcion=mostrarMenu()
    procesarDatos(auxopcion)
    if auxopcion=="5":
        break            