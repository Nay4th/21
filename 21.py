import random

def baraja():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "k", "A"] * 4

def carta(cartas):
    if "Q" in cartas:
        cartas.remove("Q")
        cartas.append(10)
        valor = sum(cartas)
    if "A" in cartas:
        cartas.remove("A")
        cartas.append(11)
        valor = sum(cartas)
    if "J" in cartas:
        cartas.remove("J")
        cartas.append(10)
        valor = sum(cartas)
    if "K" in cartas:
        cartas.remove("K")
        cartas.append(10)
        valor = sum(cartas)
    valor = sum(cartas)
    if valor > 21 and "A" in cartas:
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
    mostrar("la máquina", [maquina[0]])
    
    while True:
        if carta(jugador) == 21:
            print("¡Blackjack! ¡Has ganado!")
            break
        elif carta(jugador) > 21 and carta(maquina) <=21:
            print("perdiste. Te pasaste de 21.")
            break
        
        opcion = input("¿quieres pedir otra carta? (s/n): ").lower()
        if opcion == 's':
            jugador.append(deck.pop())
            mostrar("Jugador", jugador)
        else:
            break
    
    while carta(maquina) < 17:
        maquina.append(deck.pop())
    
    mostrar("Máquina", maquina)
    
    if carta(maquina) > 21:
        print("la máquina se paso de 21. ¡Has ganado!")
    elif carta(jugador) > carta(maquina) and carta(jugador) <= 21:
        print("¡has ganado!")
    elif carta(jugador) < carta(maquina):
        print("la máquina ha ganado")
    else:
        if jugador <= 21:
            print("empate, nadie gana")
blackjack()