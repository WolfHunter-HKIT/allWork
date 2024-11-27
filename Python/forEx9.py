end = 710
length = 0

for i in range(1, end + 1):
    length += len(str(i))

print(f'Reikės {length} skaitmenų.')