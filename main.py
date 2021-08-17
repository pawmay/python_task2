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

counter = 0
product = 1
while counter < 10:
  counter += 1
  product *= counter
  if product > 1000:
      break
  print("{}: {}".format(counter, product))