# Įrašomas intervalas
start, end = map(int, input('Įveskite intervalo pradžia ir pabaigą, atskirtą tarpais. \n').split(' '))
# Nustatomas pradinis laimėtojų skaičius.
win = 0

# Pradedamas laimėtojų rinkimas
for i in range(start, end + 1):
    # Sudaromas string masyvas
    num = list(str(i))
    # Nustatomi pradinių ir galutinių skaičių masyvai
    numStart = []
    numEnd = []

    # Išrenkami pradiniai bilieto skaičiai
    for i in range(len(num) - 3):
        numStart.append(num[i])
    numStart = int("".join(numStart))

    # Išrenkami galiniai bilieto skaičiai
    for i in range (3, len(num)):
        numEnd.append(num[i])
    numEnd = int("".join(numEnd))

    # Tikrinama ar pradiniai ir galiniai skaičiai sutampa
    if numStart == numEnd:
        win += 1

# Atspausdinamas laimėtojų skaičius
print(f'Laimingus bilietus įsigijo {win} keleivių.')