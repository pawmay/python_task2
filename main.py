'''
print("Hello World")

a = 3

if a % 2 == 0:
    print("Liczba a jest parzysta")

c = True
if c:
    print("Warunek prawdziwy")

if a % 2 == 0:
    print("Liczba a jest parzysta")
else:
    print("Liczba a jest nieparzysta")

count = 0
sum = 0
last_number = int(input("Podaj liczbę:"))
while last_number:
    sum += last_number
    count += 1 # count = count + 1
    last_number = int(input("Podaj liczbę:"))
print("Suma: ", sum, "średnia: ", sum/count)
'''

elementsCount = int(input("Podaj maksymalną ilość elementów do wysyłki: "))
if elementsCount <= 0:
    print("Błąd: Nieprawidłowa liczba elementów!")
parcelsNo = 0
parcelsWeight = 0
emptyKgsMaxParcelNo = 0
emptyKgs = 20
emptyKgsMax = 0
parcelsWeightAll = 0
for i in range(elementsCount):
    i += 1
    elementWeight = float(input(f"Podaj wagę {i}. elementu [kg]: "))
    if elementWeight == 0:
        break
    elif elementWeight < 1.0 or elementWeight > 10.0:
        print("Błąd: Nieprawidłowa waga elementu. Element powinien ważyć od 1 do 10 kg.")
        break
    else:
        if i == 1:
            parcelsNo = 1
        parcelsWeight += elementWeight
        parcelsWeightAll += elementWeight
        if parcelsWeight > 20.0:
            parcelsNo += 1
            parcelsWeight = 0
print(f"Liczba paczek wysłanych: {parcelsNo}")
print(f"Suma kilogramów wysłanych: {parcelsWeightAll} kg")
print(f"Suma 'pustych' kilogramów: {parcelsNo * 20 - parcelsWeightAll}")
print(f"Najwięcej 'pustych' kilogramów miała paczka nr {emptyKgsMaxParcelNo}, było to {emptyKgsMax} kg.")