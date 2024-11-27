# Gaunamas salės eilių kiekis ir pirmos eilės kėdžių skaičius.
n = int(input('Kiek bus salėje eilių?\n'))
k = int(input('Kiek pirmoje eilėje stovės kėdžių?\n'))
# Nusistatomas pradinis visų kėdžių skaičius
s = k

# Didinamas kėdžių skaičius pridedant praetos eilės ilgį + 2
for i in range(2, n + 1):
    k += 2
    s += k
    print(s)

# Rodomas atsakymas
print(f'Reikia užsakyti {s} kėdžių.')