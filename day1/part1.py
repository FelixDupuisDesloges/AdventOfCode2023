with open('inoutD1.txt', 'r') as myFile:
    lignes = myFile.readlines()

somme = 0

for ligne in lignes:
    for carac in ligne:
        if carac.isnumeric():
            somme += int(carac)*10
    for carac in reversed(ligne):
        if carac.isnumeric():
            somme += int(carac)

print(somme)