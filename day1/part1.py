import re
with open('inoutD1.txt', 'r') as myFile:
    lignes = myFile.readlines()

somme = 0

for ligne in lignes:
    num1 = None
    num2 = None
    indexN1 = None
    indexN2 = None
    

    for carac in ligne:
        if carac.isnumeric():
            num1 = int(carac)
            indexN1 = ligne.find(carac)
            break

    for carac in reversed(ligne):
        if carac.isnumeric():
            num2 = int(carac)
            indexN2 = reversed(ligne).find(carac)
            break

    numInStr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num =[1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(0, len(numInStr)):
        results = re.findall(numInStr[i], ligne)
        if len(results) != 0:
            if results[0] < indexN1:
                num1 = i+1
            if results[-1] > indexN2:
                num2 = i+1
    
    print(num1*10+num2)

print(somme)