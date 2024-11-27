# sukurti 08data.txt, kurioje issaugoti masyvai skirtingose eilutese
# Nuskaityti duomenis w, r, a, : w+, r+, a+

def create():
    with open('08data.txt', 'r+') as f:
        f.write('25, 14, -8, 13, -5\n')
        f.write('55, -87, 14, 17, -25, 9\n')
        f.seek(0)
        eil1 = f.readline()
        eil2 = f.readline()
    return eil1, eil2


smth = create()
print(smth)

sk = []
for i in smth:
    txt  = []
    txt = i.split(', ')
    print(txt)
    eilSk = [int(j) for j in txt]
    print(eilSk)
    sk.append(eilSk)
print(sk)