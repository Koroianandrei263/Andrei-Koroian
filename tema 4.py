import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișarea șablonului inițial
print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este:", " ".join(progres))

# Bucla principală de joc
while "_" in progres and incercari_ramase > 0:
    # Cererea unei litere
    litera = input("Introdu o literă: ").lower()

    # Verificarea validității
    if len(litera) != 1 or not litera.isalpha():
        print("Eroare: Te rugăm să introduci o singură literă validă.")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja litera aceasta. Te rog să încerci alta.")
        continue

    litere_incercate.append(litera)

    # Verificarea literei în cuvânt
    if litera in cuvant_de_ghicit:
        for index, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[index] = litera
        print("Bravo! Litera '{}' este în cuvânt.".format(litera))
    else:
        incercari_ramase -= 1
        print("Îmi pare rău, litera '{}' nu este în cuvânt. Încercări rămase: {}".format(litera, incercari_ramase))

    # Afișarea progresului și încercărilor rămase
    print("Progresul cuvântului:", " ".join(progres))
    print("Încercări rămase:", incercari_ramase)

# Încheierea jocului
if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul: '{}'".format(cuvant_de_ghicit))
else:
    print("Ai pierdut! Cuvântul era: '{}'".format(cuvant_de_ghicit))
