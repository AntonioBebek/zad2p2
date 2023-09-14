import csv

data = []
grade_counts = {
    'Nedovoljan': 0,
    'Dovoljan': 0,
    'Dobar': 0,
    'Vrlodobar': 0,
    'Izvrstan': 0
}

with open('rezultati.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append((row[0], row[1], int(row[2])))

for student in data:
    points = student[2]

    if points < 50:
        grade_counts['Nedovoljan'] += 1
    elif points < 66:
        grade_counts['Dovoljan'] += 1
    elif points < 81:
        grade_counts['Dobar'] += 1
    elif points < 91:
        grade_counts['Vrlodobar'] += 1
    else:
        grade_counts['Izvrstan'] += 1

print(grade_counts)
