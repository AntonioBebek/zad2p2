import random

radnici = ["John Doe", "Jane Smith", "Mark Johnson", "Emily Brown", "Michael Taylor", "Olivia Davis", "William Wilson", "Sophia Thomas", "Matthew Anderson", "Isabella Martinez", "James Jones", "Emma Garcia", "Christopher Wilson", "Ava Lopez", "Daniel Clark"]

lista_radnika = []

for radnik in radnici:
    ime_prezime = radnik.split()
    radnik_dict = {
        "ime": ime_prezime[0],
        "prezime": ime_prezime[1],
        "satnica": round(random.uniform(4, 6), 2)
    }
    lista_radnika.append(radnik_dict)

for radnik in lista_radnika:
    radnik["tjedni_sati"] = random.randint(20, 30)

isplate = []
for radnik in lista_radnika:
    isplata = round(radnik["satnica"] * radnik["tjedni_sati"], 2)
    isplate.append((radnik["ime"], radnik["prezime"], isplata))

for isplata in isplate:
    print(f"Ime: {isplata[0]}\nPrezime: {isplata[1]}\nIsplata: {isplata[2]}\n")

ukupna_isplata = sum(isplata[2] for isplata in isplate)
prosjecna_isplata= round(ukupna_isplata / len(isplate), 2)

print(f"Ukupna isplata:",ukupna_isplata)
print(f"Prosjecna isplata:",prosjecna_isplata)
