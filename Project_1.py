# Proměnné
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

slovnik_uzivatelu_hesel = {"bob": "123", "ann": "pass123", "mike": "password123", "lizz": "pass123"}

# Zjistuji vstupni data od uzivatele a overuji jejich spravnost
user = input("Username:")
password = input("Password:")
if user in slovnik_uzivatelu_hesel.keys() and password == slovnik_uzivatelu_hesel[user]:
    print("Welcome to the app, ", user.title(), ".", sep="")
    print("We have 3 texts to be analyzed.")
else:
    print("Sorry, user name or password incorrect.")
    exit()

oddelovac = 60 * "-"
print(oddelovac)

# Zjistuji vybrany text a overuji spravnost vstupu
chosen_text = input("Enter a number between 1 and 3 to select:")
if not chosen_text.isnumeric():
    print("Sorry, has to be a number!")
    exit()
else:
    chosen_text = int(chosen_text)

if chosen_text in range(1, 4):
    print(oddelovac)
else:
    print("Sorry, input number is out of range")
    exit()

# Rozdělení vybraného textu
index_textu = chosen_text - 1
jednotliva_slova = TEXTS[index_textu].replace("-", " ").split(" ")

# Ořezání textu o nechtěné znaky
slova_bez_znaku = []
for i in jednotliva_slova:
    slova_bez_znaku.append(i.strip(" \n,.- "))

# Výpočet součtu všech slov
pocet_slov = len(slova_bez_znaku)
print("There are", pocet_slov, "words in the selected text.")

# Výpočet součtu slov začínajících velkým písmenem
velkym_pismenem = []
for i in slova_bez_znaku:
    if i.istitle() or (len(i) < 3 and i.istitle() and (i.isalpha() or i.isalnum())) and (i.isalpha() or i.isalnum()):
        velkym_pismenem.append(i)
print("There are", len(velkym_pismenem), "titlecase words.")

# Výpočet součtu slov psaných velkými písmeny
cele_velkym_pismem = []
for i in slova_bez_znaku:
    if i.isupper() and i.isalpha():
        cele_velkym_pismem.append(i)
print("There are", len(cele_velkym_pismem), "uppercase words.")

# Výpočet součtu slov psaných malými písmeny
malym_pismenem = []
for i in slova_bez_znaku:
    if i.islower() or (len(i) < 3 and i.islower() and (i.isalpha() or i.isalnum())) and (i.isalpha() or i.isalnum()):
        malym_pismenem.append(i)
print("There are", len(malym_pismenem), "lowercase words.")

# Výskyt číslic v textu
pocet_cisel = []
for i in slova_bez_znaku:
    if i.isnumeric():
        pocet_cisel.append(i)
print("There are", len(pocet_cisel), "numeric strings.")

# Součet hodnot číslic v textu
sum_cisel = []
for i in slova_bez_znaku:
    if i.isnumeric():
        i = int(i)
        sum_cisel.append(i)
print("The sum of all the numbers: ", sum(sum_cisel), ".", sep="")

# Sloupcový graf
slovnik_delek = {}
for slovo in slova_bez_znaku:
    slovnik_delek[len(slovo)] = slovnik_delek.setdefault(len(slovo), 0) + 1
list_delek = list(slovnik_delek.items())

# Hlavička grafu
print(oddelovac)
print("LEN|     OCCURENCES     |NR.")
print(oddelovac)

# Seřazení prvků v grafu podle délky
novy_slovnik_delek = dict()
for cislo in range(1, 100):
    for velikost, hodnota in list_delek:
        if cislo == velikost:
            novy_slovnik_delek[str(velikost)] = novy_slovnik_delek.setdefault(str(velikost), hodnota)
novy_list_delek = list(novy_slovnik_delek.items())

# Tisk grafu
for cislo, hodnota in novy_list_delek:
    if int(cislo) < 10:
        print("  ", cislo, "|     ", (hodnota * "*"), ((15 - hodnota) * " "), "|", hodnota, sep="")
    else:
        print(" ", cislo, "|     ", (hodnota * "*"), ((15 - hodnota) * " "), "|", hodnota, sep="")
