def skaitom():
    with open('10data.txt', 'r') as f:
        # txt = []
        # while True:
        #     eil = f.readline()
        #     if eil:
        #         txt.append(eil)
        #     else:
        #         break
        txt = f.readlines()
    return txt

visiData = skaitom()
sk = []
for eil in visiData:
    eilSk = [int(x) for x in eil.split()]
    if len(eilSk) != 0:
        sk.append(eilSk)

print(sk)