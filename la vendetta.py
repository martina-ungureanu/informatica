import random


# Funzione per creare un giocatore con salute, scudo e attacco
def create_player(dice_string: str) -> list:
    #  valori casuali per la salute e lo scudo
    health = random.randint(80, 100)
    shield = random.randint(5, 10)
    return [health, shield, dice_string]


# Funzione per calcolare il danno inflitto in base ai dadi e scudo
def attack(attacker: list, defender: list) -> int:

    dice = attacker[2].split('d')
    num_dice = int(dice[0])
    die_faces = int(dice[1])

    damage = sum(random.randint(1, die_faces) for _ in range(num_dice))


    actual_damage = max(0, damage - defender[1])
    return actual_damage



def main_loop(player1: list, player2: list) -> None:
    turn = 1
    while player1[0] > 0 and player2[0] > 0:  # Entrambi devono avere punti vita > 0
        print(f"\n***Turn {turn}***")

        # Calcoliamo i danni
        damage_player1 = attack(player1, player2)
        damage_player2 = attack(player2, player1)

        # Aggiorniamo la salute dei giocatori
        player2[0] -= damage_player1
        player1[0] -= damage_player2

        # Mostriamo i risultati del turno
        print(f"[Player1] Damage: {damage_player1} ({sum(random.randint(1, 6) for _ in range(4))}-{player2[1]})")
        print(f"[Player2] Health: {player2[0]}")

        print(f"[Player2] Damage: {damage_player2} ({sum(random.randint(1, 12) for _ in range(2))}-{player1[1]})")
        print(f"[Player1] Health: {player1[0]}")

        # Incrementiamo il numero di turni
        turn += 1

    # Risultato finale
    if player1[0] > 0 and player2[0] <= 0:
        print("\nPlayer 1 wins!")
    elif player2[0] > 0 and player1[0] <= 0:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a draw!")

    print(f"Total turns played: {turn}")



def main():
    player1 = create_player("4d6")
    player2 = create_player("2d12")

    print(f"Player1 starting health: {player1[0]}")
    print(f"Player1 shield: {player1[1]}")
    print(f"Player2 starting health: {player2[0]}")
    print(f"Player2 shield: {player2[1]}")

    main_loop(player1, player2)


# Avvio del programma
if __name__ == "__main__":
    main()
