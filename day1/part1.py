with open('inoutD1.txt', 'r') as myFile:
    lignes = myFile.readlines()

somme = 0

for ligne in lignes:


    for carac in lignes[0]:
        if carac.isnumeric():
            value = int(carac)*10
            print(value)
            somme += value
            break
    for carac in reversed(lignes[0]):
        if carac.isnumeric():
            value = int(carac)
            print(value)
            somme += value
            break

print(somme)