import random
import time
ODDEL = 40 * "="


def pozdrav():
    print("Hi there!")
    print(f"{ODDEL}\nI've generated a random 4 digit number for you.\nLet's play s bulls and cows game.")


def generovani_cisla():
    nahodne_cislo = []
    cisla_misto_nuly = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(nahodne_cislo) < 4:
        cislo = random.randint(0, 9)
        if cislo not in nahodne_cislo:
            nahodne_cislo.append(cislo)
    if nahodne_cislo[0] == 0:
        for cislo in nahodne_cislo:
            if cislo in cisla_misto_nuly:
                cisla_misto_nuly.remove(cislo)
        nahodne_cislo[0] = random.choice(cisla_misto_nuly)
    return nahodne_cislo


def hadej_cislo():
    duplicity = 0
    while True:
        hadane_cislo = input("Enter a number:")
        if len(hadane_cislo) != 4:
            print("Prosím zadej číslo o délce přesně 4 znaků.")
            continue
        elif hadane_cislo[0] == "0":
            print("Prosím zadej číslo které nezačíná nulou.")
            continue
        elif not hadane_cislo.isnumeric():
            print("Prosím zadej pouze číslo, jiné znaky nejsou povoleny.")
            continue
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


def game():
    start_time = time.time()
    pozdrav()
    generovane_cislo = generovani_cisla()
    pozice = 0
    pozice_i_hodnota = 0
    pocet_pokusu = 0
    tabulka_hodnoceni = ["amazing", "good", "average", "not so good"]
    index_hodnoceni = ""
    casy = [10, 30, 60]
    while True:
        print(generovane_cislo)
        print(ODDEL)
        hadane_cislo = hadej_cislo()
        for index, i in enumerate(hadane_cislo):
            if i in generovane_cislo and hadane_cislo[index] == generovane_cislo[index]:
                pozice_i_hodnota += 1
            elif i in generovane_cislo:
                pozice += 1
        if pozice_i_hodnota == 4:
            pocet_pokusu += 1
            total_time = round(time.time() - start_time, 1)
            if pocet_pokusu == 1:
                print(ODDEL)
                print(f"Correct, you've guessed the right answer\nin {pocet_pokusu} guess.")
                print(f"It took you {total_time} seconds.")
            else:
                print(ODDEL)
                print(f"Correct, you've guessed the right answer\nin {pocet_pokusu} guesses.")
                print(f"It took you {total_time} seconds.")
            for index, cas in enumerate(casy):
                if total_time <= cas:
                    index_hodnoceni = tabulka_hodnoceni[index]
                    break
                else:
                    index_hodnoceni = tabulka_hodnoceni[-1]
            print(f"That's {index_hodnoceni}")
            print(ODDEL)
            exit()
        elif pozice_i_hodnota == 1 and pozice == 1:
            print("1 bull, 1 cow")
        elif pozice_i_hodnota != 1 and pozice == 1:
            print(f"{pozice_i_hodnota} bulls, 1 cow")
        elif pozice_i_hodnota == 1 and pozice != 1:
            print(f"1 bull, {pozice} cows")
        else:
            print(f"{pozice_i_hodnota} bulls, {pozice} cows")
        pozice = 0
        pozice_i_hodnota = 0
        pocet_pokusu += 1


game()
