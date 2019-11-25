import random
import time

play_again = 'Yes'
choices = ('rock', 'paper', 'scissors')
pc_score = 0
player_score = 0


def plagain():
    proceed = input('Wish to continue (Y/N)? ')
    if proceed == 'N':
        play_again = 'No'


while play_again != 'No':
    pc_choice = random.choice(choices)

    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)
    player_choice = input('rock, paper or scissors?')

    if player_choice == 'rock' and pc_choice == 'rock':
        print('PC chose rock, go again!')
        print('PC: ', pc_score, 'You: ', player_score)
    elif player_choice == 'rock' and pc_choice == 'paper':
        print('PC picked paper and won this round! +1 score to it.')
        pc_score += 1
        print('PC: ', pc_score, 'You: ', player_score)
        plagain()
    elif player_choice == 'rock' and pc_choice == 'scissors':
        print('PC picked scissors, you won this round!')
        player_score += 1
        print('PC: ', pc_score, 'You: ', player_score)
        plagain()

    elif player_choice == 'paper' and pc_choice == 'paper':
        print('PC chose paper, go again!')
        print('PC: ', pc_score, 'You: ', player_score)
    elif player_choice == 'paper' and pc_choice == 'scissors':
        print('PC picked scissors and won this round! +1 score to it.')
        pc_score += 1
        print('PC: ', pc_score, 'You: ', player_score)
        plagain()
    elif player_choice == 'paper' and pc_choice == 'rock':
        print('PC picked rock, you won this round!')
        player_score += 1
        print('PC: ', pc_score, 'You: ', player_score)
        plagain()

    elif player_choice == 'scissors' and pc_choice == 'scissors':
        print('PC chose scissors, go again!')
        print('PC: ', pc_score, 'You: ', player_score)
    elif player_choice == 'scissors' and pc_choice == 'rock':
        print('PC picked rock and won this round! +1 score to it.')
        pc_score += 1
        print('PC: ', pc_score, 'You: ', player_score)
        plagain()
    elif player_choice == 'scissors' and pc_choice == 'paper':
        print('PC picked paper, you won this round!')
        player_score += 1
        print('PC: ', pc_score, 'You: ', player_score)
        plagain()

    elif player_choice not in choices:
        print('Please type \'rock\', \'paper\' or \'scissor\'')
