
import random
import pyautogui as py

all_bot_name = ['Milad', 'Misaq', 'Aida', 'Neda']
action = ['Rock', 'Paper', 'Scissor']
user = 0
user_2 = 0
bot_1 = 0
bot_2 = 0

welcome_panel = py.confirm(text='Welcome to the game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])

while welcome_panel == 'No' :
    canceling = py.confirm(text='Are you sure to quit the game ?', title='quit panel', buttons=['Yes', 'No'])
    if canceling == 'Yes' :
        canceling_2 = py.alert(text='Bye, we will see you soon again', title='quit panel')
        break
    elif canceling == 'No' :
        welcome_panel = py.confirm(text='Welcome to the game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])

if welcome_panel == 'Yes' :
    username = py.prompt(text='Game is started, first enter your name please', title='Name panel', default='Your name')
    while username == '' :                                                                                                    #????????
        canceling = py.confirm(text='Are you sure to quit the game ?', title='Welcome panel', buttons=['Yes', 'No'])
        if canceling == 'Yes' :
            canceling_2 = py.alert(text='Wish see you soon, Thanks for selecting us', title='Welcome panel')
            break
        while canceling == 'No' :
            username = py.prompt(text='Game is started, first enter your name please', title='Name panel', default='Your name')
    else :
        which_game = py.confirm(text=f'{username} which game do you want ?', title='select game panel', buttons=['User - Bot', 'Bot - Bot', 'User - User', 'Rull game', 'Details'])
        round_number = int(py.prompt(text='How many round are played ?', title='round panel', default='How round'))

random_bot_name = random.choice(all_bot_name)

if which_game == 'User - Bot' :
    bot_name = py.alert(text=f'Robot name is {random_bot_name}', title='User - Bot panel')
    for round in range(1, round_number + 1) :
        random_action = random.choice(action)
        which_game = py.confirm(text=f'{username} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
        if which_game == random_action :
            user += 1
            bot_1 += 1
            resualt_game = py.alert(text=f'round {round} is equal, {random_bot_name} selected {random_action}, Resualt : {user} - {bot_1}', title='User - Bot panel')
        elif ( which_game == 'Paper' and random_action == 'Rock' ) or ( which_game == 'Rock' and random_action == 'Scissor' ) or ( which_game == 'Scissor' and random_action == 'Paper' ) :
            user += 1
            resualt_game = py.alert(text=f'round {round} You win, {random_bot_name} selected {random_action}, Resualt : {user} - {bot_1}', title='User - Bot panel')
        else :
            bot_1 += 1
            resualt_game = py.alert(text=f'round {round} You lose, {random_bot_name} selected {random_action}, Resualt : {user} - {bot_1}', title='User - Bot panel')

elif which_game == 'Bot - Bot' :
    bot_name_1 = py.alert(text=f'First Robot name is {random_bot_name}', title='Bot - Bot panel')
    bot_name_1 = random_bot_name
    random_bot_name = random.choice(all_bot_name)
    while bot_name_1 == random_bot_name :
        random_bot_name = random.choice(all_bot_name)
        break
    bot_name_2 = py.alert(text=f'Second Robot name is {random_bot_name}', title='Bot - Bot panel')

    for round in range(1, round_number + 1) :
        random_action_1 = random.choice(action)
        random_action_2 = random.choice(action)

        if random_action_1 == random_action_2 :
            bot_1 += 1
            bot_2 += 1
            resualt_game = py.alert(text=f'round {round} is equal, Resualt : {bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name}', title='Bot - Bot panel')
                                    
        elif ( random_action_1 == 'Paper' and random_action_2 == 'Rock' ) or ( random_action_1 == 'Rock' and random_action_2 == 'Scissor' ) or ( random_action_1 == 'Scissor' and random_action_2 == 'Paper' ) :
            bot_1 += 1
            resualt_game = py.alert(text=f'round {round} {bot_name_1} is win, resualt is : {bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name}', title='Bot - Bot panel')
        else :
            bot_2 += 1
            resualt_game = py.alert(text=f'round {round} {bot_name_2} is win, resualt is : {bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name}', title='Bot - Bot panel')

    if bot_1 == bot_2 :                                                                                          #equalllll
            resualt_game = py.alert(text=f'Extra round ,resualt is equal : {bot_1} - {bot_2} Are you ready ?', title='Bot - Bot panel')

elif which_game == 'User - User' :
    username_1 = py.prompt(text=f'{username} enter the first name player please', title='Name panel', default='first player')
    username_2 = py.prompt(text='And enter the second name player', title='Name panel', default='second player')

    for round in range(1, round_number + 1) :
        random_action_1 = random.choice(action)
        random_action_2 = random.choice(action)

        which_game_1 = py.confirm(text=f'{username_1} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
        which_game_2 = py.confirm(text=f'{username_2} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])

        if which_game_1 == which_game_2 :
            user += 1
            user_2 += 1
            resualt_game = py.alert(text=f'round {round} is equal, Resualt : {username_1} {user} - {user_2} {username_2}', title='User - User panel')
        elif ( which_game_1 == 'Paper' and which_game_2 == 'Rock' ) or ( which_game_1 == 'Rock' and which_game_2 == 'Scissor' ) or ( which_game_1 == 'Scissor' and which_game_2 == 'Paper' ) :
            user += 1
            resualt_game = py.alert(text=f'round {round} {username_1} is win, {username_1} selected {which_game_1}, Resualt : {user} - {user_2}', title='User - Bot panel')
        else :
            user_2 += 1
            resualt_game = py.alert(text=f'round {round} {username_2} is win, {username_2} selected {which_game_2}, Resualt : {user} - {user_2}', title='User - Bot panel')
        
elif which_game == 'Rull game' :
    Rull_game = py.alert(text='This game produced by Milad Barouni and the Ways of communication by Email : milad.baroun@gmail.com and Phone number : +989177719601', title='Details panel')
    which_game = py.confirm(text=f'{username} which game do you want ?', title='select game panel', buttons=['User - Bot', 'Bot - Bot', 'User - User', 'Rull game', 'Details'])
    round_number = int(py.prompt(text='How many round are played ?', title='round panel', default='How round'))

elif which_game == 'Details' :
    pass







#         username = py.prompt(text='Enter your name please', title='Name panel', default='enter your name')

# elif welcome_panel == 'Yes' :       
#     username = py.prompt(text='Enter your name please', title='Name panel', default='enter your name')


#back
#exit
#detail
#rull
#bot bot not equal









