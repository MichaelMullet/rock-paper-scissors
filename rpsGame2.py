import random, sys

# Assign a name to the player - like a title screen.

while True: # The player name loop.
    print('What is your name?')
    playerName = input()
    if playerName == '':
        print('Don\'t be shy!')
    else:
        break
print('Hello, ' + playerName + '!')

# Transition to Gameplay
while True: # The keyPress loop.
    print('Press enter to continue, ' + playerName + '.')
    keyPress = input()
    if keyPress == '':
        break

# Gameplay starts

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the numbers of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print(playerName + ' has %s Wins, %s Losses, and %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print(playerName + ' has left the game.')
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie! Try again!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win, unfortunately.')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win. Good job I guess, ' + playerName + '.')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win. But only through luck, ' + playerName +'.')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose! Rocky start ' + playerName + ' :/.')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Ouch, paper cut! (You lose!)')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose! Sucks to suck!')
        losses = losses + 1
