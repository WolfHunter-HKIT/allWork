try:
    f = open('01data.txt', 'a', encoding='utf-8')
    f.write('Pirmas kartas su byla\n')
    a = 5
    f.write(f'a = {a}\n')
    f.write('ąčęėįšųūž\n')
finally:
    f.close()