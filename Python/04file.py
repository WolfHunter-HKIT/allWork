with open('43data.txt', 'w', encoding='utf-8') as f:
    print('Pirmas kartas su byla\n', file=f)
    a = 5
    print(f'a = {a}\n', file=f)
    print('ąčęėįšųūž\n', file=f)
    print(f.closed)
print(f.closed)