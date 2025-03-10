import random

sacchetto = []


def crea_sacchetto(n):
    global sacchetto
    totale_numeri = n * n
    sacchetto = []
    for i in range(totale_numeri):
        sacchetto.append(i + 1)


def genera_numero():
    global sacchetto
    numero_casuale = random.choice(sacchetto)
    sacchetto.remove(numero_casuale)
    return numero_casuale


def genera_matrice(n):
    crea_sacchetto(n)
    matrice = []
    for riga in range(n):
        riga_attuale = []
        for colonna in range(n):
            riga_attuale.append(genera_numero())
        matrice.append(riga_attuale)
    return matrice


def verifica_quadrato_magico(matrice):
    """Verifica se la matrice è un quadrato magico."""

    def verifica_riga(matrice):
        precedente = sum(matrice[0])
        for riga in range(1, len(matrice)):
            somma_riga_matrice = sum(matrice[riga])
            if precedente != somma_riga_matrice:
                return False, 0  # Non è un quadrato magico
        return True, precedente  # La somma della prima riga

    def verifica_colonne(matrice):
        somma = 0
        for colonna in range(len(matrice)):
            somma_colonna = sum(matrice[riga][colonna] for riga in range(len(matrice)))
            if somma_colonna != somma:
                return False  # Non è un quadrato magico
            if colonna == 0:
                somma = somma_colonna
        return True

    # Verifica righe
    righe_ok, somma_riga = verifica_riga(matrice)
    if not righe_ok:
        return False, 0

    # Verifica colonne
    if not verifica_colonne(matrice):
        return False, 0

    # Verifica diagonali
    somma_diagonale_principale = sum(matrice[i][i] for i in range(len(matrice)))
    somma_diagonale_secondaria = sum(matrice[i][len(matrice) - 1 - i] for i in range(len(matrice)))

    if somma_diagonale_principale != somma_riga or somma_diagonale_secondaria != somma_riga:
        return False, 0

    return True, somma_riga  # Ritorna True se è un quadrato magico con la costante magica


def stampa_matrice(matrice, costante_magica=None):
    """Stampa la matrice in un formato leggibile, aggiungendo la costante se è disponibile."""
    for riga in matrice:
        print(riga)
    if costante_magica:
        print(f"Costante magica: {costante_magica}")


def main():
    global sacchetto
    for n in range(3, 11):
        test_quadrato_magico = False
        while not test_quadrato_magico:
            quadrato_magico = genera_matrice(n)
            test_quadrato_magico, costante_magica = verifica_quadrato_magico(quadrato_magico)

        # Stampa il quadrato magico trovato
        print(f"\nQuadrato magico di ordine {n}:")
        stampa_matrice(quadrato_magico, costante_magica)


if __name__ == "__main__":
    main()
