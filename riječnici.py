import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio', 'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija', 'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan', 'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan', 'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

broj_imena = {}
for ime in imena:
    if ime in broj_imena:
        broj_imena[ime] += 1
    else:
        broj_imena[ime] = 1

for ime, broj in broj_imena.items():
    print(f"{ime}: {broj}")

ocjene = {}
for ime in imena:
    ocjene[ime] = random.randint(1, 5)

broj_ocjena = {}
for ocjena in ocjene.values():
    if ocjena in broj_ocjena:
        broj_ocjena[ocjena]

broj_prolaznih = sum(ocjena >= 2 for ocjena in ocjene.values())
postotak_prolaznosti = (broj_prolaznih / len(ocjene)) * 100
print(f"Postotak prolaznosti: {postotak_prolaznosti}%")
