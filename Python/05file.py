txt = ['Pirma eilute\n', 'Antra eilute\n', 'Trecia eilute\n']
sk = [5, 6, 7, 9, 8]
with open('05data.txt', 'w', encoding='utf-8') as f:
    # f.write(str(txt))
    f.writelines(txt)
    # f.writelines(sk)