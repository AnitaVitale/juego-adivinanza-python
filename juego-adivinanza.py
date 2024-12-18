import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cantidad_max_intentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado and cant_intentos < cantidad_max_intentos:
    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    
    cant_intentos += 1

if not cant_intentos < cantidad_max_intentos:
    print("Game Over!")