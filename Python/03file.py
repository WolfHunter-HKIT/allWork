with open('03data.txt', 'w', encoding='utf-8') as f:
    f.write('Pirmas kartas su byla\n')
    a = 5
    f.write(f'a = {a}\n')
    f.write('ąčęėįšųūž\n')
    print(f.closed)
print(f.closed)