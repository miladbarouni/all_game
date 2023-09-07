
import random
import pyautogui as py

all_bot_name = ['Milad', 'Misaq', 'Aida', 'Neda']
action = ['Rock', 'Paper', 'Scissor']
user = 0
bot = 0

welcome_panel = py.confirm(text='Welcome to the game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])

while welcome_panel == 'No' :
    canceling = py.confirm(text='Are you sure to quit the game ?', title='Welcome panel', buttons=['Yes', 'No'])
    if canceling == 'Yes' :
        canceling_2 = py.alert(text='Wish see you soon, Thanks for selecting us', title='Welcome panel')
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

for round in range(1, round_number + 1) :
    if which_game == 'User - Bot' :
        random_action = random.choice(action)
        canceling_2 = py.alert(text=f'Robot name is {random_bot_name}', title='User - Bot panel')
        which_game = py.confirm(text=f'{username} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
        if which_game == random_action :
            user += 1
            bot += 1
            resualt_game = py.alert(text=f'equal, {random_bot_name} selected {random_action}, Resualt : {user} - {bot}', title='User - Bot panel')
        elif ( which_game == 'Paper' and random_action == 'Rock' ) and ( which_game == 'Rock' and random_action == 'Scissor' ) and ( which_game == 'Scissor' and random_action == 'Paper' ) :
            user += 1
            resualt_game = py.alert(text=f'You win, {random_bot_name} selected {random_action}, Resualt : {user} - {bot}', title='User - Bot panel')
        else :
            bot += 1
            resualt_game = py.alert(text=f'You lose, {random_bot_name} selected {random_action}, Resualt : {user} - {bot}', title='User - Bot panel')

    elif which_game == 'Bot - Bot' :
        pass
    elif which_game == 'User - User' :
        pass    



#         username = py.prompt(text='Enter your name please', title='Name panel', default='enter your name')

# elif welcome_panel == 'Yes' :       
#     username = py.prompt(text='Enter your name please', title='Name panel', default='enter your name')


#back
#exit
#detail
#rull
#bot bot not equal













