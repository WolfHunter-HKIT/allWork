# Nuskaityti skaicius ir susumuoti tik lyginius
with open('11data.txt', 'r') as f:
    suma = 0
    for line in f:
        txt = line.strip()
        if txt:
            a = int(txt)
            if a % 2 == 0:
                suma += a
    print(suma)