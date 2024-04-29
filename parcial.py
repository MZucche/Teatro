
#Esta función se encarga de cargar la informacion que contiene el archivo "espectaculo.txt" en listas para poder usarla
def lecturaArchivo(Lsector, Lentradas, Lprecio):
    try:
        arch=open(r"D:\MARCOS\UADE\Algoritmos y Estructura de Datos I\Parcial\espectaculo.txt", "rt")
    except IOError:
        print("No se puede leer el archivo")
    else:
        try:
            for linea in arch:
                sector , entradas , precio = linea.strip().split(";")
                Lsector.append(sector)
                Lentradas.append(int(entradas))
                Lprecio.append(int(precio))
        finally:
            arch.close()
    
#Esta función le permite al usuario cargar por teclado los datos de la compra
  
def ingresoDatos (Lentradas):
    nombre = validarAlp("Ingrese un nombre: " , "Ingrese un nombre valido: ")
    print()
    apellido = validarAlp("Ingrese un apellido: " , "Ingrese un apellido valido: ")
    print()
    dni = int(input("Ingrese su dni: "))
    while (dni<10000000) or (dni>99999999):
        dni = int(input("Error - Ingrese dni valido - : "))
    print()
    sector = Validar("CAMPO" , "PLATEA" , "VIP" , "Seleccione sector valido - CAMPO , PLATEA , VIP - : "  , "Error - Seleccione sector valido - CAMPO , PLATEA , VIP - : ")
    sector = cantEntradas(sector , Lentradas)
    print()
    entradas = int(input("Ingresar cantidad de entradas: "))
    print()
    flag = validarEntradas(Lentradas , entradas , sector)
    while flag == 1:
        entradas = int(input("Ingresar cantidad de entradas: "))
        print()
        flag = validarEntradas(Lentradas , entradas , sector)
    metPago = Validar("VISA" , "MASTERCARD" , "EFECTIVO" , "Elija metodo de pago - VISA(precio de lista) , MASTERCARD (5% de descuento) , EFECTIVO(10% de descuento): " ,  "Error - Elija metodo de pago - VISA(precio de lista) , MASTERCARD (5% de descuento) , EFECTIVO(10% de descuento): ")
    print()
    return nombre , apellido , dni , sector , entradas , metPago


#Esta función permite validar que los datos ingresados sean del tipo correcto
def validarAlp(mnsj1 , mnsj2):
    var = input(mnsj1)
    while var.isalpha() == False:
        print()
        var = input(mnsj2)
    return var
 
#Esta función permite que los datos ingresados existan dentro del programa
def Validar(n , m , x , mnsj1 , mnsj2):
    variable = input(mnsj1)
    while (variable.upper() != n) and (variable.upper() != m) and (variable.upper() != x):
        variable = input(mnsj2)
    return variable.upper()

#Con esta función el usuario puede saber si hay disponibilidad de entradas
def cantEntradas(sector, Lentradas):
    if sector == "CAMPO":
        var = 0
    elif sector == "PLATEA":
        var = 1
    elif sector == "VIP":
        var = 2
    while Lentradas[var] == 0:
        print("Sector " +  sector + " sin entradas disponibles")
        sector = Validar("CAMPO" , "PLATEA" , "VIP" , "Seleccione sector valido - CAMPO , PLATEA , VIP - : "  , "Error - Seleccione sector valido - CAMPO , PLATEA , VIP - : ")
        print()
        if sector == "CAMPO":
            var = 0
        elif sector == "PLATEA":
            var = 1
        elif sector == "VIP":
            var = 2        
    return sector


#Con esta función el programa verifica si la cantidad de entradas ingresadas po el usuario coincide con la disponibilidad, de ser asi se efectua la compra y se restan las entradas compradas al total
def validarEntradas(Lentradas , entradas , sector):
    flag = 0
    cant = 0
    if sector == "CAMPO":
        var = 0
    elif sector == "PLATEA":
        var = 1
    elif sector == "VIP":
        var = 2
    cant = Lentradas[var]
    if cant < entradas:
        print("Error - cantidad de entradas disponibles - : " , cant)
        print()
        flag = 1
    else:
        Lentradas[var] = Lentradas[var] - entradas
    return flag


#Con esta función se carga la informacion de la venta en un archivo llamado "resumen.txt"
def cargaArchivo(nombre , apellido , dni , sector , entradas , metPago):
    nombre = str(nombre)
    apellido = str(apellido)
    dni = str(dni)
    sector = str(sector)
    entradas = str(entradas)
    metPago = str(metPago)
    
    try:
        arch=open(r"D:\MARCOS\UADE\Algoritmos y Estructura de Datos I\Parcial\resumen.txt", "at")
    except IOError:
        print("No se puede leer el archivo")
    else:
        arch.write(nombre + " " + apellido + ";" + dni + ";" + sector + ";" + entradas + ";" + metPago + "\n")
    finally:
        arch.close()   

#Esta función va sumando la cantidad recaudada por metodo de pago en una lista
def cargaPrecioF(metPago , precioF ,LcantVen):
    if metPago == "VISA":
        LcantVen[0] += precioF
    if metPago == "MASTERCARD":
        LcantVen[1] += precioF
    if metPago == "EFECTIVO":
        LcantVen[2] += precioF


#Esta función devuelve el precio final de la compra con el descuento aplicado
def precio(entradas , sector , metPago , Lprecio , descuentos):
    precio = 0
    var =- 1
    if sector == "campo":
        var = 0
    elif sector == "platea":
        var = 1
    elif sector == "vip":
        var = 2
    
    precio = Lprecio[var]
    precioF = (entradas * precio) * descuentos[metPago]
    return precioF
    
#Con esta función se cargan los datos en la matriz
def cargaDatos(metPago , entradas , sector , matrizVenta):
    if metPago == "VISA":
        var1 = 0
    elif metPago == "MASTERCARD":
        var1 = 1
    elif metPago == "EFECTIVO":
        var1 = 2
    if sector == "CAMPO":
        var2 = 0
    elif sector == "PLATEA":
        var2 = 1
    elif sector == "VIP":
        var2 = 2
    matrizVenta[var1][var2] += entradas

        

#Esta función imprime la matriz
def imprimirMatriz(matrizVenta, LmetPago):
    LmetPago[0] = "VISA       "
    print()
    print("MÉTODO DE PAGO/SECTOR   CAMPO          PLATEA           VIP" + "\n")
    for f in range(len(LmetPago)):
        print(LmetPago[f], end=" ")
        for c in range(len(matrizVenta[f])):
            print("\t" , "\t" , matrizVenta[f][c], end=" ")
        print()
        print("\n")


#Esta función ordena las lista de medo de pago y dinero recaudado de forma ascendente para luego imprimirla
def ordenarLista(LcantVen , LmetPago):
    LmetPago[0] = "VISA       "
    print("\nMETODO DE PAGO              CANTIDAD VENDIDA\n")

    for cant, uso in sorted(zip(LcantVen, LmetPago), reverse = True):
        print(str(uso) +"\t" + "\t" + "\t" + str(cant) + "\n")


#Esta funcion actualiza la cantidad de entradas restantes en el archivo "espectaculo.txt" 
def actualizarAcrh(Lsector, Lentradas, Lprecio):
    try:
        arch=open(r"D:\MARCOS\UADE\Algoritmos y Estructura de Datos I\Parcial\espectaculo.txt", "wt")
    except IOError:
        print("No se puede leer el archivo")
    else:
        try:
            for i in range (3):
                arch.write(str(Lsector[i])+";"+str(Lentradas[i])+";"+str(Lprecio[i])+"\n")
        finally:
            arch.close()



# PROGRAMA PRINCIPAL    
    

Lsector = []
Lentradas = []
Lprecio = []
LcantVen = 3*[0]
LmetPago = ["VISA" , "MASTERCARD" , "EFECTIVO"]
LprecioFinal = []
descuentos = {"VISA":1 , "MASTERCARD":0.95 , "EFECTIVO":0.9}
matrizVenta= [[0 for c in range(3)]for f in range(3)]



lecturaArchivo(Lsector, Lentradas, Lprecio)
print(Lentradas)
comenzar = int(input("Ingresar 1 para comenzar: "))
print()

while comenzar == 1 and comenzar != 99 and (Lentradas[0 or 1 or 2] > 0):
    
    nombre , apellido , dni , sector , entradas , metPago = ingresoDatos(Lentradas)
    cargaArchivo(nombre , apellido , dni , sector , entradas , metPago)
    precioF = precio(entradas , sector , metPago , Lprecio , descuentos)
    cargaPrecioF(metPago , precioF, LcantVen)    
    cargaDatos(metPago , entradas , sector , matrizVenta)
    
    
    if (Lentradas[0]==0 and Lentradas[1]==0 and Lentradas[2]==0):
        print("Entradas agotadas")
        break
    
    comenzar = int(input("Ingresar 1 para continuar o 99 para finalizar: "))


actualizarAcrh(Lsector, Lentradas, Lprecio)

print()
print()
print()
print()
print()

imprimirMatriz(matrizVenta , LmetPago)

print()
print()

ordenarLista(LcantVen , LmetPago)

