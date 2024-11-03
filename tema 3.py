# Datele inițiale
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Variabile pentru inventar și finanțe
comenzi_efectuate = {"papanasi": 0, "ceafa": 0, "guias": 0}
total_incasari = 0

# Dictionar pentru prețurile produselor pentru calcul rapid
preturi_dict = {produs: pret for produs, pret in preturi}

# 1. Comenzi - simulăm servirea comenzilor pentru fiecare student
print("Simularea comenzilor:")
while studenti and comenzi and tavi:
    student = studenti.pop(0)  # extragem primul student
    comanda = comenzi.pop(0)  # extragem prima comandă
    tava = tavi.pop()  # extragem o tavă din stivă

    # Afisăm detalii despre comanda studentului
    print(f"{student} a comandat {comanda}.")

    # Actualizăm inventarul
    meniu.remove(comanda)
    istoric_comenzi.append(comanda)
    comenzi_efectuate[comanda] += 1
    total_incasari += preturi_dict[comanda]

print("\nInventar final:")

# 2. Inventar - afisăm statistici
print(
    f"S-au comandat {comenzi_efectuate['guias']} guias, {comenzi_efectuate['ceafa']} ceafa, {comenzi_efectuate['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {'ceafa' in meniu}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu}.")
print(f"Mai sunt guias: {'guias' in meniu}.")

print("\nFinanțe:")

# 3. Finanțe - calculăm veniturile și produsele sub 7 lei
print(f"Cantina a încasat: {total_incasari} lei.")
