from random import randint


user1 = 0
user2 = 0
tirada1 = 0
tirada2 = 0
ronda = 0

while user1 or user2 != 100:
    ronda += 1
    tirada1 = randint(1,10)
    tirada2 = randint(1,10)
    user1 += tirada1
    user2 += tirada2
    print(f"Ronda {ronda}")
    print(f"Jugador 1: {user1} (Tirada: {tirada1}) \nJugador 2: {user2} (Tirada: {tirada2}) \n")
    if user1 >= 100:
        print("El Jugador 1 ha ganado")
        break
    elif user2 >= 100:
        print("El Jugador 2 ha ganado")
        break


        
    
