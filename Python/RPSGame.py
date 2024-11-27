import random

# Užduotis 1.

def rpsGame():
    gameObjects = ['Rock', 'Paper', 'Scissors']
    computerChoice = gameObjects[random.randint(0, len(gameObjects)-1)]
    userChoice = input('You are playing Rock, Paper Scissors. Choose: Rock(R), Paper(P) or Scissors(S).\n').capitalize()

    match userChoice:
        case 'R':
            userChoice = 'Rock'
        case 'P':
            userChoice = 'Paper'
        case 'S':
            userChoice = 'Scissors'
        case _:
            print(f'{userChoice} is not a valid choice.')
            rpsGame()

    if computerChoice == userChoice:
        print('The game ended in stalemate.')
    elif computerChoice == 'Rock' and userChoice == 'Paper':
        print(f'Congratulations! You won! Computer: {computerChoice}; You: {userChoice}.')
    elif computerChoice == 'Rock' and userChoice == 'Scissors':
        print(f'Unfortunately, computer won. Computer: {computerChoice}; You: {userChoice}.')
    elif computerChoice == 'Scissors' and userChoice == 'Rock':
        print(f'Congratulations! You won! Computer: {computerChoice}; You: {userChoice}.')
    elif computerChoice == 'Scissors' and userChoice == 'Paper':
        print(f'Unfortunately, computer won. Computer: {computerChoice}; You: {userChoice}.')
    elif computerChoice == 'Paper' and userChoice == 'Rock':
        print(f'Congratulations! You won! Computer: {computerChoice}; You: {userChoice}.')
    elif computerChoice == 'Paper' and userChoice == 'Rock':
        print(f'Unfortunately, computer won. Computer: {computerChoice}; You: {userChoice}.')

    if input('Do you want to play again? (Y/N)\n').capitalize == 'Y':
        rpsGame()

# Comment code bellow to stop the RPS game initiation
rpsGame()

# Užduotis 2.

def stoneBagGame():
    inBag = random.randint(10, 30)
    computerStarts = False

    if random.randint(1, 2) == 1:
        computerStarts = True

    if computerStarts:
        print(f'Computer starts the game. There are {inBag} stones in the bag.')
        while computerStarts and inBag > 0:
            # Computer Plays
            player1Takes = random.randint(1, 3)
            if player1Takes > inBag:
                player1Takes = random.randint(1, 3)
            inBag = inBag - player1Takes
            if inBag == 0:
                # Game ends
                print('Unfortunately, Computer won. Better luck next time!')
                break
            print(f'Computer reaches in and takes {player1Takes} stones out of the bag. There are {inBag} stones left.')


            # User plays
            player2Takes = int(input('How many stones do you take? (1-3)\n'))
            while player2Takes > inBag:
                print(f'Not enough stones left in bag. Stones in bag: {inBag}')
                player2Takes = int(input('Choose again.\n'))
            while player2Takes < 1 or player2Takes > 3:
                player2Takes = int(input('Invalid number, try again. (1-3)\n'))
            inBag = inBag - player2Takes
            if inBag == 0:
                # Game ends 
                print('Congratulations, You won!')
                break
            print(f'User reaches in and takes {player2Takes} out of the bag. There are {inBag} stones left.')

    else:
        print(f'User starts the game. There are {inBag} stones in the bag.')
        while computerStarts == False and inBag > 0:
            # User plays
            player2Takes = int(input('How many stones do you take? (1-3)\n'))
            while player2Takes > inBag:
                print(f'Not enough stones left in bag. Stones in bag: {inBag}')
                player2Takes = int(input('Choose again.\n'))
            while player2Takes < 1 or player2Takes > 3:
                player2Takes = int(input('Invalid number, try again. (1-3)\n'))
            inBag = inBag - player2Takes
            if inBag == 0:
                # Game ends 
                print('Congratulations, You won!')
                break
            print(f'User reaches in and takes {player2Takes} out of the bag. There are {inBag} stones left.')


            # Computer Plays
            player1Takes = random.randint(1, 3)
            if player1Takes > inBag:
                player1Takes = random.randint(1, 3)
            inBag = inBag - player1Takes
            if inBag == 0:
                # Game ends
                print('Unfortunately, Computer won. Better luck next time!')
                break
            print(f'Computer reaches in and takes {player1Takes} stones out of the bag. There are {inBag} stones left.')

# Comment code bellow to stop the stone bag game initiation
stoneBagGame()



