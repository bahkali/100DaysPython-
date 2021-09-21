Name = input('Please enter the name of the person who created this game: ')
print('This game was made by the amazing '+ Name+"!")
print('Welcom to my guessing game!')
print('Good luck')

def start():
    Player_name = input('What is the name of the  player? ')
    print('Greeting, '+ Player_name +'! It is time to guess!')
    secret_word = 'Ostrich'.lower()
    guesses = ''
    Turns_left = 11
    while Turns_left > 0:
        wrong_answers = 0
        for Letter in secret_word:
            if Letter in guesses:
                print(Letter)
            else:
                print('_')
                wrong_answers +=1
        if wrong_answers == 0:
            print('You Win! You guessed my word: ' + secret_word + '!!!!')
            break
        Guess = input('Guess a letter here: ').lower()
        guesses += Guess

        if Guess not in secret_word:
            Turns_left -= 1
            print('Oops! This letter is not in my word. Please try again.')
            print('You have '+ str(Turns_left) + ' more guesses left. You can do it!')
            if Turns_left == 0:
                print('GAME OVER')
    
    def Play_Again():
        Again = input('Would you like to play again? ').lower()
        if Again == 'No'.lower():
            quit()
        if Again == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thank you!')
            Play_Again()
    Play_Again()
start()