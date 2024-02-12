import random

def baraja():
    return [("diamantes", 2), ("diamantes", 3), ("diamantes", 4), ("diamantes", 5), ("diamantes", 6), ("diamantes", 7), ("diamantes", 8), ("diamantes", 9), ("diamantes", 10), ("diamantes", "Q"), ("diamantes", "J"), ("diamantes", "k"), ("diamantes", "A")] + [("picas", 2), ("picas", 3), ("picas", 4), ("picas", 5), ("picas", 6), ("picas", 7), ("picas", 8), ("picas", 9), ("picas", 10), ("picas", "Q"), ("picas", "J"), ("picas", "k"), ("picas", "A")] + [("treboles", 2), ("treboles", 3), ("treboles", 4), ("treboles", 5), ("treboles", 6), ("treboles", 7), ("treboles", 8), ("treboles", 9), ("treboles", 10), ("treboles", "Q"), ("treboles", "J"), ("treboles", "k"), ("treboles", "A")] + [("corazones", 2), ("corazones", 3), ("corazones", 4), ("corazones", 5), ("corazones", 6), ("corazones", 7), ("corazones", 8), ("corazones", 9), ("corazones", 10), ("corazones", "Q"), ("corazones", "J"), ("corazones", "k"), ("corazones", "A")]

def carta(cartas):
    if ("diamantes", 2) in cartas:
        cartas.remove(("diamantes", 2))
        cartas.append(2)
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
    elif carta(jugador) > carta(maquina):
        print("¡has ganado!")
    elif carta(jugador) < carta(maquina):
        print("la máquina ha ganado")
    else:
        print("empate, nadie gana")
blackjack()