import random

def baraja():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def carta(cartas):
    valor = sum(cartas)
    if valor > 21 and 11 in cartas:
        cartas.remove(11)
        cartas.append(1)
        valor = sum(cartas)
    return valor

def mostrar(jugador, mano):
    print(f"{jugador} tiene las siguientes cartas: {mano} (total: {carta(mano)})")

def blackjack():
    deck = baraja()
    random.shuffle(deck)
    
    jugador = [deck.pop(), deck.pop()]
    maquina = [deck.pop(), deck.pop()]
    
    mostrar("Jugador", jugador)
    mostrar("Máquina", [maquina[0]])
    
    while True:
        if carta(jugador) == 21:
            print("¡Blackjack! ¡Has ganado!")
            break
        elif carta(jugador) > 21:
            print("Has perdido. Te pasaste de 21.")
            break
        
        opcion = input("¿Quieres pedir otra carta? (s/n): ").lower()
        if opcion == 's':
            jugador.append(deck.pop())
            mostrar("Jugador", jugador)
        else:
            break
    
    while carta(maquina) < 17:
        maquina.append(deck.pop())
    
    mostrar("Máquina", maquina)
    
    if carta(maquina) > 21:
        print("La máquina se pasó de 21. ¡Has ganado!")
    elif carta(jugador) > carta(maquina):
        print("¡Has ganado!")
    elif carta(jugador) < carta(maquina):
        print("La máquina ha ganado.")
    else:
        print("Empate.")