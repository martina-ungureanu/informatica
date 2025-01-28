import random

hp=50

turni=0

print(f"/n initial healt points: {hp} \n")

while hp>0:

    dado=random.randint(1,6)

    hp= (hp-dado)

    print(f"danno subito:{dado}")

    print(f"vita rimanente:{hp}")

    turni=turni+1

    print("il tuo personaggio è stato sconfitto")
    
    print(f"quanti turni sono stati giocati:{turni}")
