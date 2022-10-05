import time
from random import randint

def guessing_game():

    print("Bienvenido al juego de adivinar!")
    print("piensa en un número dentro de un rango, por ejemplo del 1 al 100, y yo intentaré adivinarlo")

    x = "a"
    y = "b"
    
    #definimos un bucle que obligue al usuario a ingresar un numero entero (int) para poder continuar

    while type(x) != int:

        try:
            x = int(input("Dame el número mínimo: ")) #pide el numero minimo y chequea que sea un numero entero, INT
            print(f"""has elegido "{x}" como el mínimo""")
        except:
                print("ERROR: debes ingresar solo números enteros")
                pass
        
    while type(y) != int:

        try:
            y = int(input("Dame el número Máximo: ")) #pide el numero maximo y chequea que sea un numero entero, INT
            print(f"""has elegido "{y}" como el máximo""")
        except:
            print("ERROR: debes ingresar solo números enteros")
            pass

    #definimos un bucle que se asegure que el numero minimo no sea mayor ni igual que el maximo

    while int(x) > int(y) or int(x) == int(y):
        try:
            y = int(input("el número máximo debe ser mas grande que el mínimo: "))
        except:
            try:
                print("ingresaste cualquier cosa")
                y = int(input("recuerda, solo números enteros: "))
            except:
                print("reiterando instrucciones........")
                pass
    

    #determinamos que pasa con cada tipo de respuesta

    count = 0           #contador para obtener la cantidad de intentos
    win_state = 0           #condicion para determinar el fin del bucle

    while win_state == 0 :

        start = int((int(x) + int(y)) / 2)              #se calcula un punto medio entre el minimo y el maximo
        respuesta = input(f"tu número es {start}?: ")

        if respuesta == "menos":
            if start <= int(x):
                print("No podemos ir por debajo del mínimo")
            else:
                y = start
                count += 1
            

        elif respuesta == "mas":

            if start >= int(y):
                print("No podemos sobrepasar el máximo")
            else:
                x = start
                count += 1

        elif respuesta == "correcto":

            count +=1
            win_state = 1

        elif respuesta != "menos" and "mas" and "correcto":

            print("""Debes ingresar "mas" o "menos" y cuando acierte, por favor ingresa "correcto" """)


    return f"Adiviné!, y solo me tomó {count} intentos!"

print(guessing_game())
time.sleep(10)
