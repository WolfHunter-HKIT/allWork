# sukurti 07data.txt, kurioje issaugoti masyvai skirtingose eilutese
# Nuskaityti duomenis

def create():
    with open('07data.txt', 'w') as f:
        f.write('25, 14, -8, 13, -5\n')
        f.write('55, -87, 14, 17, -25, 9\n')

def read():
    with open('07data.txt', 'r') as f:
        eil1 = f.readline()
        eil2 = f.readline()
    return eil1, eil2

create()
smth = read()
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