import random
import time
ODDEL = 40 * "="


# Pozdraví uživatele
def pozdrav():
    print("Hi there!")
    print(f"{ODDEL}\nI've generated a random 4 digit number for you.\nLet's play s bulls and cows game.")


# Vygeneruje náhodné orignální 4-ciferné číslo a ověří, jestli nezačíná nulou
# Jestli nulou začíná tak toto číslo nahradí originálním číslem
def generovani_cisla() -> list:
    nahodne_cislo = []
    cisla_misto_nuly = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(nahodne_cislo) < 4:
        cislo = random.randint(0, 9)
        if cislo not in nahodne_cislo:
            nahodne_cislo.append(cislo)
    # Zde ověřuji, jestli číslo nezačíná nulou
    if nahodne_cislo[0] == 0:
        # for cyklus, který vyřadí z pomocného listu čísel čísla, která se již v našem náhodném čísle nachází,
        # následně z něj jedno náhodně vybere a dosadí ho do našeho náhodného čísla místo nechtěné nuly
        for cislo in nahodne_cislo:
            if cislo in cisla_misto_nuly:
                cisla_misto_nuly.remove(cislo)
        nahodne_cislo[0] = random.choice(cisla_misto_nuly)
    return nahodne_cislo


# Funkce zhodnocuje vstup uživatele a ověřuje, jeslti splňuje podmínky
def hadej_cislo() -> list:
    duplicity = 0
    while True:
        hadane_cislo = input("Enter a number:")
        # Ověřuji délku čísla
        if len(hadane_cislo) != 4:
            print("Prosím zadej číslo o délce přesně 4 znaků.")
            continue
        # Ověřuji zda číslo nezačíná nulou
        elif hadane_cislo[0] == "0":
            print("Prosím zadej číslo které nezačíná nulou.")
            continue
        # Ověřuji za číslo obsahuje pouze číslice
        elif not hadane_cislo.isnumeric():
            print("Prosím zadej pouze číslo, jiné znaky nejsou povoleny.")
            continue
        # For cyklus pro ověření originality číslic
        for index, cislo in enumerate(hadane_cislo):
            if cislo in hadane_cislo[index+1:]:
                duplicity += 1
        if duplicity != 0:
            print("Číslo nesmí obsahovat duplicity.")
            duplicity = 0
            continue
        list_hadanych_cisel = []
        for i in hadane_cislo:
            list_hadanych_cisel.append(int(i))
        return list_hadanych_cisel


# Hlavní funkce
def game():
    start_time = time.time()
    pozdrav()
    generovane_cislo = generovani_cisla()
    pozice = 0
    pozice_i_hodnota = 0
    pocet_pokusu = 0
    tabulka_hodnoceni = ["amazing", "good", "average", "not so good"]
    index_hodnoceni = ""
    casy = [30, 60, 120]
    while True:
        print(ODDEL)
        hadane_cislo = hadej_cislo()
        # Ověřujeme zda je shoda mezi náhodným číslem a tipem uživatele
        for index, i in enumerate(hadane_cislo):
            # Přídělujeme hodnoty proměnným reprezentujícím hodnoty Cows a Bulls
            if i in generovane_cislo and hadane_cislo[index] == generovane_cislo[index]:
                pozice_i_hodnota += 1
            elif i in generovane_cislo:
                pozice += 1
        # V případě, že uživatel uhodne všechny 4 čísla (Bulls)
        if pozice_i_hodnota == 4:
            pocet_pokusu += 1
            total_time = round(time.time() - start_time, 1)
            # Podmínka učuje, zda uživatel uhodl číslo na 1 nebo více pokusů
            if pocet_pokusu == 1:
                print(ODDEL)
                print(f"Correct, you've guessed the right answer\nin {pocet_pokusu} guess.")
                print(f"It took you {total_time} seconds.")
            else:
                print(ODDEL)
                print(f"Correct, you've guessed the right answer\nin {pocet_pokusu} guesses.")
                print(f"It took you {total_time} seconds.")
            # For cyklus pro výběr hodnocení délky hry
            for index, cas in enumerate(casy):
                if total_time <= cas:
                    index_hodnoceni = tabulka_hodnoceni[index]
                    break
                else:
                    index_hodnoceni = tabulka_hodnoceni[-1]
            print(f"That's {index_hodnoceni}")
            print(ODDEL)
            exit()
        # Přídělujeme a tiskneme hodnoty Cows a Bulls
        elif pozice_i_hodnota == 1 and pozice == 1:
            print("1 bull, 1 cow")
        elif pozice_i_hodnota != 1 and pozice == 1:
            print(f"{pozice_i_hodnota} bulls, 1 cow")
        elif pozice_i_hodnota == 1 and pozice != 1:
            print(f"1 bull, {pozice} cows")
        else:
            print(f"{pozice_i_hodnota} bulls, {pozice} cows")
        # Vynulování počítadel před dalším pokusem
        pozice = 0
        pozice_i_hodnota = 0
        pocet_pokusu += 1


if __name__ == "__main__":
    game()
