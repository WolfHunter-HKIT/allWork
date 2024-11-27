def kuriam(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)

for i in range(1, 100):
    kuriam(f'Labas\\{i}data.bat', f'{i}-oje byloje įrašyta informacija\n')