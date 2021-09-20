
def start():
    print('\nThis is my Rock Paper Scissors Game!\n\n')
    Player_one = "Kaly"
    Player_two = "Erik"

    def choices(Player_one_choice, Player_two_choice):
        if Player_one_choice == 'rock' and Player_two_choice == 'paper':
            return('Paper cover Rock! ' + Player_two + ' Wins !')
        elif Player_one_choice == 'paper' and Player_two_choice == 'rock':
            return('Paper cover Rock! ' + Player_one + ' Wins !')
        elif Player_one_choice == 'scissors' and Player_two_choice == 'paper':
            return('Scissors cuts Paper! ' + Player_one + ' Wins !') 
        elif Player_one_choice == 'paper' and Player_two_choice == 'scissors':
            return('Scissors cuts Paper! ' + Player_two + ' Wins !')
        elif Player_one_choice == 'scissors' and Player_two_choice == 'rock':
            return('Rock smashes Scissors! ' + Player_two + ' Wins !')
        elif Player_one_choice == 'rock' and Player_two_choice == 'scissors':
            return('Rock smashes Scissors! ' + Player_one + ' Wins !')
        elif Player_one_choice == Player_two_choice:
            return(Player_one+' and '+ Player_two + ' tied!')
        else:
            return('Please type Rock, Paper or Scissors!')

    Player_one_choose = input('Does '+ Player_one + ' choose Rock, Paper or Scissors? ').lower()
    Player_two_choose = input('Does '+ Player_two + ' choose Rock, Paper or Scissors? ').lower()

    print(choices(Player_one_choose, Player_two_choose))

    def Play_Again():
        Again = input("Would you like to play the game again? ").lower()
        if Again == 'no':
            quit()
        if Again == 'yes':
            start()
        else:
            print('Please enter Yes or No. Thank you!')
            Play_Again()
    Play_Again()
start()