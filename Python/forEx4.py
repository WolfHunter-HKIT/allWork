# Įvedama kelintą savaitės dieną prasideda mėnuo
mod = int(input('Įveskite kelintą savaitės dieną prasidėjo mėnuo. (1-7)')) - 1
# Įvedama intervalo pradžia ir pabaiga
start, end = map(int, input('Įveskite dienų intervalą, atskirtą tarpais.').split(' '))

# Apskaičiuojama kelinta savaitės diena bus intervalo pradžioje
for i in range(start):
    mod += 1
    if mod == 8:
        mod = 1

# Išvedamas kalendoriaus atsakymas
for i in range(start, end + 1):
    print(f'{i}-oji mėnesio diena: {mod}')
    mod += 1
    if mod == 8:
        mod = 1