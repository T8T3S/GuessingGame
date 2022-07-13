import random

print('Guess the number!')

def play_game():
    limit = input('\nEnter the limit: ')
    randomNumber = random.randint(1,int(limit))
    print(f'I\'m thinking of a number from 1 and {limit}\n')
    count = 0
    while True:
        count += 1
        playerNumber = input('Your guess: ')
        pn = int(playerNumber)
        if pn > randomNumber:
            print('Too high.')
        if pn < randomNumber:
            print('Too low.')
        if pn == randomNumber:
            print(f'You guessed it in {count} tries.\n')
            break
    playAgain = input('Would you like to play again? (y/n): ')
    if playAgain == 'y':
        play_game()
    else:
        print('\nBye!')
        return

while True:
    play_game()
    break