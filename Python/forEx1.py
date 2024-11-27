import random

# Įvedamas kalimo ilgis
k = int(input('Kiek centimetrų vienu smūgiu yra kalamas vinis?\n'))

# Įvedamas vinies ilgis
n = random.randrange(4, 18)

# Kalamas vinis
for i in range(1, int((n/k))):
    n = n - k
    print(f'Tuk! {i} : Liko {n}cm vinies.')
    s = i + 1

# Vinis įkalta
print(f'Tuk! {s} : Vinis įkalta.')
