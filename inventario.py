inventario= 10  ##ESTO ES UN COMENTARIO
 
def vender_Producto():
        global inventario
        print("ingrese la cantidad que desea vender")
        cantidad=int(input("Ingrese la cantidad: "))
        if cantidad<=inventario:
                inventario=inventario-cantidad
                print ("Cantidad existente en el inventario: ",inventario)
        elif inventario==0 and cantidad>inventario:
            print ("Debe reabastecer el inventario")
            print()
        elif cantidad> inventario:
            print ("No tiene disponibilidad suficiente del producto")
            print()
 
def reabastecer():
    global inventario
    cantidad=int(input("Ingrese la cantidad que desea ingresar: "))
    inventario=inventario+cantidad
    print("La cantidad se ha ingresado con exito")
 
 
 
 
def ver_Inventario():
 
	    print("La cantidad en existencia es: ",inventario)
	    print()
 
while  True:
	try:
		print("Menú")
		print ("[1] notebook ")
		print ("[2] Reabastecer el inventario")
		print ("[3] Ver la cantidad existente en el inventario")
		print ("[4] Salir")
 
		opcion = int(input("Que deseas hacer: "))
	except ValueError:
		print("Favor de ingresar una opcion valida")
	else:
		#si no es ninguna de las 4 opciones validas
		if opcion < 1 or opcion >4:
				print ("no es una opcion valida")
				continue
		if opcion == 1:
			vender_Producto()
		elif opcion == 2:
			reabastecer()
		elif opcion == 3:
			ver_Inventario()
		else:
			break
print("Gracias por su compra")

