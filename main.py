elementsCount = int(input("Podaj maksymalną ilość elementów do wysyłki: "))
if elementsCount <= 0:
    print("Błąd: Nieprawidłowa liczba elementów!")
parcelsNo = 0
parcelsWeight = 0
emptyKgsMaxParcelNo = 0
emptyKgs = 20
emptyKgsMax = 0
parcelsWeightAll = 0
for element in range(elementsCount):
    element += 1
    elementWeight = float(input(f"Podaj wagę {element}. elementu [kg]: "))
    if elementWeight == 0:
        break
    elif elementWeight < 1.0 or elementWeight > 10.0:
        print("Błąd: Nieprawidłowa waga elementu. Element powinien ważyć od 1 do 10 kg.")
        break
    else:
        if element == 1:
            parcelsNo = 1
        parcelsWeight += elementWeight
        parcelsWeightAll += elementWeight
        if parcelsWeight > 20.0:
            parcelsNo += 1
            parcelsWeight = 0
            emptyKgs = 20
        emptyKgs -= elementWeight
        if parcelsWeight > 20.0 or element == elementsCount:
            emptyKgsMax = max(emptyKgsMax, emptyKgs)
        if emptyKgs >= emptyKgsMax:
            emptyKgsMaxParcelNo = parcelsNo
print(f"Liczba paczek wysłanych: {parcelsNo}")
print(f"Suma kilogramów wysłanych: {parcelsWeightAll} kg")
print(f"Suma 'pustych' kilogramów: {parcelsNo * 20 - parcelsWeightAll}")
print(f"Najwięcej 'pustych' kilogramów miała paczka nr {emptyKgsMaxParcelNo}, było to {emptyKgsMax} kg.")