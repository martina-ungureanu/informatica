import random

print('\n\n******** #1: CHARACTER CREATION ********\n')
# 1. Crea un dizionario inserendo al suo interno:
#     - Un nome scelto a caso dalla lista di nomi
#     - Chiedi all'utente di inserire una classe per il proprio personaggio a scelta tra Guerriero, Mago, Chierico, Ladro
#     Memorizza queste informazioni in un dizionario chiamato 'character'.
names = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr",
         "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]

# ****************************************

character = {}
character['name'] = random.choice(names)  # Seleziona un nome casuale
character['class'] = input("Choose a class for your character (Warrior, Mage, Cleric, Rogue): ")  # Chiedi la classe

print(character)
# ****************************************

print('\n\n******** #2: CHARACTER ATTRIBUTES ********\n')


# 2. Aggiungi al dizionario i seguenti punti caratteristica generati casualmente.
# Ogni caratteristica è determinata lanciando 4d6dl
#    - Forza
#    - Destrezza
#    - Costituzione
#    - Intelligenza

# ****************************************

def roll_4d6():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort()  # Ordina i dadi
    return sum(rolls[1:])  # Somma i tre dadi più alti


# Aggiungi le caratteristiche al dizionario
character['strength'] = roll_4d6()
character['dexterity'] = roll_4d6()
character['constitution'] = roll_4d6()
character['intelligence'] = roll_4d6()

print(character)
# ****************************************

print('\n\n******** #3: ADDING A BAG ********\n')
# 3. Aggiungi al dizionario un nuovo attributo chiamato 'inventory' (zaino),
#    che sia a sua volta un dizionario contenente:
#      - 'gold': le monete in possesso dal personaggio. È un lancio di 17+3d10
#      - 'items': 1d4 oggetti casuali estratti dalla lista di oggetti
#      - 'weapon': un oggetto casuale estratto dalla lista delle armi della propria classe
#        Usa la seguente regola: i personaggi magici (mago e chierico) usano le armi magiche,
#        i personaggi corpo a corpo usano le armi fisiche

# ****************************************
items = [
    "Healing Potion", "Grappling Hook", "Rations", "Rope",
    "Torch", "Lockpicks", "Spell Scroll", "Gemstone", "Bedroll"
]

weapons = {
    "Warrior": ["Sword", "Dagger", "Bow", "Crossbow", "Axe", "Mace", "Spear"],
    "Mage": ["Magic Staff", "Wand", "Orb", "Tome of Spells"],
    "Cleric": ["Magic Staff", "Wand", "Orb", "Tome of Spells"],
    "Rogue": ["Sword", "Dagger", "Bow", "Crossbow", "Axe"]
}


# Funzione per generare oro
def generate_gold():
    return 17 + sum(random.randint(1, 10) for _ in range(3))


# Funzione per generare oggetti casuali
def generate_items():
    return random.sample(items, k=random.randint(1, 4))


# Funzione per generare un'arma in base alla classe
def generate_weapon(character_class):
    return random.choice(weapons[character_class])


# Aggiungi l'inventario al personaggio
character['inventory'] = {
    'gold': generate_gold(),
    'items': generate_items(),
    'weapon': generate_weapon(character['class'])
}

print(f"Character inventory: {character['inventory']}")
# ****************************************

print('\n\n******** #4: PRINT CHARACTER ********\n')


# 4. Stampa a video tutte le informazioni del personaggio usando un ciclo for su chiave-valore.

# ****************************************

def print_character(character):
    for key, value in character.items():
        print(f"{key}: {value}")


print_character(character)
# ****************************************

print('\n\n******** #5: FUNCTIONS: Create a random character ********\n')
# 5. Trasforma il codice della creazione di un personaggio in una funzione chiamata 'create_character'.
#    La funzione non deve richiedere input e deve restituire un dizionario con i dati del personaggio.

# ****************************************
classes = ["Warrior", "Mage", "Cleric", "Rogue"]


def create_character():
    character = {}
    character['name'] = random.choice(names)
    character['class'] = random.choice(classes)
    character['strength'] = roll_4d6()
    character['dexterity'] = roll_4d6()
    character['constitution'] = roll_4d6()
    character['intelligence'] = roll_4d6()

    character['inventory'] = {
        'gold': generate_gold(),
        'items': generate_items(),
        'weapon': generate_weapon(character['class'])
    }
    return character


random_character = create_character()
print(random_character)

# ****************************************

print('\n\n******** #6: FUNCTIONS - Print the cheatsheet ********')
# 6. Trasforma il codice della visualizzazione di un personaggio (punto 4) in una funzione chiamata 'print_character(character:dict)'.

# ****************************************

# La funzione è già stata definita sopra. La chiamerò per stampare il personaggio appena creato.
print_character(random_character)
# ****************************************

print('\n\n******** #7: FUNCTIONS - Create a random party ********\n')


# 7. Scrivi una funzione chiamata 'create_party' che riceve in input un intero n compreso tra 1 e 5 e
#    restituisce una lista di personaggi (lista di dizionari).

# ****************************************

def create_party(n):
    return [create_character() for _ in range(n)]


n = int(input("How many characters do you want to create? "))
party = create_party(n)
print(party)
# ****************************************

print('\n\n******** #8: FUNCTIONS - Party print ********\n')


# 8. Scrivi una funzione chiamata 'print_party(party:list)'.
#    La funzione deve ricevere una lista di dizionari come parametro e stampa i dati di ogni personaggio.

# ****************************************

def print_party(party):
    for character in party:
        print_character(character)
        print("\n---")


print_party(party)
# ****************************************

print('\n\n******** #9: Search for the richest guy ********\n')


# 9. Scrivi una funzione search_the_richest(party:list) che cerca il personaggio con più monete d'oro
#    nella sua borsa e restituisce il nome e la quantità di monete.

# ****************************************

def search_the_richest(party):
    richest = max(party, key=lambda x: x['inventory']['gold'])
    return richest['name'], richest['inventory']['gold']


name, gold = search_the_richest(party)
print(f"The richest in the party is {name}. They have {gold} coins of gold in their bag!")
# ****************************************
