# Exercise 1
# Coins: 10ct, 20ct, 50ct, 1eur, 2eur
coins = [.1, .2, .5, 1, 2]
startPrice = float(input("Kokia pradinė kavos kaina?\n"))
currentMoney = 0
fakeMoney = 0
realMoney = 0


while currentMoney < startPrice:
    enteredMoney = float(input(f"Kokią monetą įmetate (10ct, 20ct, 50ct, 1eur, 2eur)? Jums liko įmesti {format(startPrice-currentMoney, '.2f')}eur\n"))
    if enteredMoney > 2:
        enteredMoney = enteredMoney / 100
    if (enteredMoney in coins) == False:
        print("Jūs įmetėte negerą monetą. Bandykite dar kartą")
        fakeMoney += 1
        continue

    currentMoney += enteredMoney
    realMoney += 1


if currentMoney > startPrice:
    print(f"Jūsų grąža: {format(currentMoney - startPrice, '.2f')}. Skanios Kavos!")
else:
    print(f"Grąžos neliko. Skanios Kavos!")

print(f"Buvo įmesta {fakeMoney} padirbtų monetų ir {realMoney} tikrų monetų.")



# Exercise 2
import random

randomNumber = str(random.randint(1, 1000000))
print(f'Number Generated: {randomNumber}')

deploy = 0
while deploy < len(randomNumber):
    print('*' * int(randomNumber[len(randomNumber) - 1 - deploy]))
    deploy += 1
