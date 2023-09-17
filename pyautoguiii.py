
import pyautogui as py
import random
import time

confirmation_rulls_game = 0
confirmation_details = 0
number_played_games = 0

all_bot_name = ['Milad', 'Misaq', 'Abas', 'Mohammad', 'Aida', 'Neda', 'Sepideh', 'Mahsa'] 
action = ['Rock', 'Paper', 'Scissor']
user_1 = 0
user_2 = 0
bot_1 = 0
bot_2 = 0
number_played_Rock_Paper_Scissors = 0

welcome_panel = py.confirm(text='              Welcome to the game, before playing \nplease read both of the "Rulls" game and "Details" to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])

while confirmation_rulls_game < 1 or confirmation_details < 1 :

    if welcome_panel == 'Menu game' :
        alert_before_welcome_panel = py.alert(text='You have not read "Rulls game" and "Details" \nplease read and then click on Menu game', title='Welcome panel')
        welcome_panel = py.confirm(text='please read both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
    elif welcome_panel == 'Rulls game' :
        rulls_game_panel = py.confirm(text='Rull of the game: \n1. Playing the games means you have accepted the complete rules of the game \n2. When your opponent is a robot, his movement is chosen by chance and you have to accept the result \n3. If you make a change in the source code of the game, this is cheating and you will lose the game \n4. During the game, two users should not show each other their next move to the opponent \n5. If you quit the game, your opponent will win the game \n6.this version of game is free so you can play just 2 games \n7.for buying full version check "Details" to see communication ways', title='Rulls game panel', buttons=['I agree', 'I dont agree'])
        if rulls_game_panel == 'I agree' :
            confirmation_rulls_game += 1
            welcome_panel = py.confirm(text='Thanks for reading "Rulls" game \nif you dont read "Details" game yet \nread and click on Menu game to start', title='Rulls game panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
        elif rulls_game_panel == 'I dont agree' :
            quit_panel = py.confirm(text='If you want to play read the "Rulls" and "Details" \nIf you dont agree quit the game and click on Exit', title='Rulls game panel', buttons=['Back', 'Exit'])
            if quit_panel == 'Back' :
                welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
            else :
                quit_panel = py.confirm(text='Are you sure to quit ? ', title='Quit panel', buttons=['Yes', 'No'])
                if quit_panel == 'No' :
                    welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
                else :
                    quit_panel = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                    break
    elif welcome_panel == 'Details' :
        confirmation_details += 1
        details_game_panel = py.alert(text='This package game produced by Milad Barouni \nBuying and the Ways of communication : \nby Email : milad.baroun@gmail.com \nPhone number : +989177719601', title='Details panel')
        welcome_panel = py.confirm(text='Thanks for reading "details" game \nif you dont read "rulls" game yet \nread and click on Menu game to start', title='Details game panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
    else :
        quit_panel = py.confirm(text='Are you sure to quit ? ', title='Quit panel', buttons=['Yes', 'No'])
        if quit_panel == 'No' :
            welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
        else :
            quit_panel = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
            break
else :
    welcome_panel = py.confirm(text='Thanks for reading', title='Welcome panel', buttons=['Menu game', 'Set password', 'Exit'])
    while welcome_panel == 'Exit' :
        quit_panel = py.confirm(text='Are you sure to quit ? ', title='Quit panel', buttons=['Yes', 'No'])
        if quit_panel == 'No' :
            welcome_panel = py.confirm(text='Thanks for reading', title='Welcome panel', buttons=['Menu game', 'Set password', 'Exit'])
        else :
            quit_panel = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
            break
    if welcome_panel == 'Set password' :
        password_login = py.prompt(text='Enter your password', title='Password panel')
        password_login_repeat = py.prompt(text='Repeat enter your password', title='Password panel')
        while password_login != password_login_repeat :
            password_login = py.prompt(text='Your password not same enter again', title='Password panel')
            password_login_repeat = py.prompt(text='Repeat enter your password', title='Password panel')

        password_login_input = py.prompt(text='         Your password is set \nTo continue enter your password', title='Password panel')
        password_wrong = 0

        while password_login != password_login_input :
            password_wrong += 1
            if password_wrong < 3 :
                password_login_input = py.prompt(text='      Wrong password \nEnter your password again', title='Password panel')
            else :
                quit_panel = py.alert(text='You entered wrong password 3 times \n        We wish see you later again', title='Quit panel')
                break
        else :
            welcome_panel = py.confirm(text='You logged in', title='Welcome panel', buttons=['Menu game', 'Exit'])
            while welcome_panel == 'Exit' :
                quit_panel = py.confirm(text='Are you sure to quit ? ', title='Quit panel', buttons=['Yes', 'No'])
                if quit_panel == 'No' :
                    welcome_panel = py.confirm(text='Thanks for set your password', title='Welcome panel', buttons=['Menu game', 'Exit'])
                else :
                    quit_panel = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                    break
               
            username = py.prompt(text='First enter your name please', title='Name panel') 
while not username :                                                                                                    
        canceling = py.confirm(text='An error has occurred, this error may be due to exiting the program or due to not entering the name', title='Unknow error panel', buttons=['Enter a name', 'Exit'])
        if canceling == 'Enter a name' :
            username = py.prompt(text='First enter your name please', title='Name panel')
        else :
            canceling_2 = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
            break    
else :
    thanks_user = py.alert(text=f'click "Ok" to start the game', title=f'{username} panel')

number_played_games = 0

menu_game_panel = py.confirm(text=f'{username} Select one of the game', title='Game panel', buttons=['✊_✋_✌️', 'Guess_number', 'Gol_ya_Pooch', 'Jorat_Haghighat', 'Esm_Famil', 'Mouse_Movement', 'Change username', 'Exit'])
while number_played_games < 2 :   #and thanks_user != ''

    if menu_game_panel == 'Change username' :
        username = py.prompt(text=f'{username} Enter your new name please', title='New name panel') 
        while not username :                                                                                                    
            canceling = py.confirm(text='An error has occurred, this error may be due to exiting the program or due to not entering the name', title='Unknow error panel', buttons=['Enter a name', 'Exit'])
            if canceling == 'Enter a name' :
                username = py.prompt(text=f'{username} Enter your new name please', title='New name panel') 
            else :
                canceling_2 = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                break    
        else :
            menu_game_panel = py.confirm(text=f'{username} Select one of the game', title='Game panel', buttons=['✊_✋_✌️', 'Guess_number', 'Gol_ya_Pooch', 'Jorat_Haghighat', 'Esm_Famil', 'Mouse_Movement', 'Change username', 'Exit'])

    elif menu_game_panel == '✊_✋_✌️' :
        number_played_games += 1
        welcome_Rock_Paper_Scissors_panel = py.confirm(text='Welcome to ✊_✋_✌️ game, ready to start ?', title='Welcome ✊_✋_✌️ panel ', buttons=['Yes', 'No'])
        while welcome_Rock_Paper_Scissors_panel == 'No' :
            canceling = py.confirm(text='Are you sure to quit the game ?', title='Quit panel', buttons=['Yes', 'No'])
            if canceling == 'No' :
                welcome_Rock_Paper_Scissors_panel = py.confirm(text='Welcome to ✊_✋_✌️ game, Are you ready to start ?', title='Welcome ✊_✋_✌️ panel ', buttons=['Yes', 'No'])
            else :
                canceling = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                break
        else:
            which_game_Rock_Paper_Scissors = py.confirm(text='which game do you want ?', title='select game panel', buttons=['User - Bot', 'Bot - Bot', 'User - User', 'Exit'])

        round_number = int(py.prompt(text='How many round do you want to play ?', title='round panel', default='How many round'))
        How_determine_winner = py.confirm(text='How to determine the winner ?', title='Determine panel', buttons=['Whoever reaches the entry number', 'Only play the entry number'])
        if which_game_Rock_Paper_Scissors == 'User - Bot' :
            random_bot_name_1 = random.choice(all_bot_name)
            bot_name = py.alert(text=f'Robot name is {random_bot_name_1}', title='User - Bot panel')
            if How_determine_winner == 'Whoever reaches the entry number' :
                while user_1 < round_number and bot_1 < round_number :
                    random_action = random.choice(action)
                    which_game = py.confirm(text=f'{username} which action do you want to select ?', title='select action panel', buttons=['✊', '✋', '✌️'])
                    number_played_Rock_Paper_Scissors += 1
                    if which_game == random_action :
                        user_1 += 1
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} is equal \n{random_bot_name_1} selected {random_action} \nResualt : \n {username} : {user_1} \n {random_bot_name_1} : {bot_1}', title='User - Bot panel')
                    elif ( which_game == '✋' and random_action == '✊' ) or ( which_game == '✊' and random_action == '✌️' ) or ( which_game == '✌️' and random_action == '✋' ) :
                        user_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} You win \n{random_bot_name_1} selected {random_action} \nResualt : \n {username} : {user_1} \n {random_bot_name_1} : {bot_1}', title='User - Bot panel')
                    else :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} You lose \nResualt : \n {username} : {user_1} \n {random_bot_name_1} : {bot_1}', title='User - Bot panel')
                
                if user_1 > bot_1 :
                    finally_resualt = py.alert(text=f'{username} you win the game, Resualt : {user_1} - {bot_1}', title='Finally result')
                elif user_1 < bot_1 :
                    finally_resualt = py.alert(text=f'{username} you lose the game, Resualt : {user_1} - {bot_1}', title='Finally result')
                else :
                    finally_resualt = py.alert(text=f'{username} the game is equal, Resualt : {user_1} - {bot_1}', title='Finally result')
                break

            else :
                while number_played_Rock_Paper_Scissors < round_number :
                    which_game = py.confirm(text=f'{username} which action do you want to select ?', title='select action panel', buttons=['✊', '✋', '✌️'])
                    random_action = random.choice(action)
                    number_played_Rock_Paper_Scissors += 1
                    if which_game == random_action :
                        user_1 += 1
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} is equal \nResualt : \n {username} : {user_1} \n {random_bot_name_1} : {bot_1}', title='User - Bot panel')
                    elif ( which_game == '✋' and random_action == '✊' ) or ( which_game == '✊' and random_action == '✌️' ) or ( which_game == '✌️' and random_action == '✋' ) :
                        user_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} You win \nResualt : \n {username} : {user_1} \n {random_bot_name_1} : {bot_1}', title='User - Bot panel')
                    else :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} You lose \nResualt : \n {username} : {user_1} \n {random_bot_name_1} : {bot_1}', title='User - Bot panel')
            
                if user_1 > bot_1 :
                    finally_resualt = py.alert(text=f'{username} you win the game, Resualt : {user_1} - {bot_1}', title='Finally result')
                elif user_1 < bot_1 :
                    finally_resualt = py.alert(text=f'{username} you lose the game, Resualt : {user_1} - {bot_1}', title='Finally result')
                else :
                    finally_resualt = py.alert(text=f'{username} your game is equal, Resualt : {user_1} - {bot_1}', title='Finally result')
                break  

        elif which_game_Rock_Paper_Scissors == 'User - User' :
            username_1 = py.prompt(text='enter your name please', title='Name panel', default='first name player')
            username_2 = py.prompt(text='enter the second name player please', title='Name panel', default='second name player')
            if How_determine_winner == 'Whoever reaches the entry number' :
                while user_1 < round_number or user_2 < round_number :
                    which_game_1 = py.confirm(text=f'{username_1} which action do you want to select ?', title='select action panel', buttons=['✊', '✋', '✌️'])
                    which_game_2 = py.confirm(text=f'{username_2} which action do you want to select ?', title='select action panel', buttons=['✊', '✋', '✌️'])
                    number_played_Rock_Paper_Scissors += 1
                    if which_game_1 == which_game_2 :
                        user_1 += 1
                        user_2 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} is equal \nResualt : \n {username_1} : {user_1} \n {username_2} : {user_2}', title='User - User panel')
                    elif ( which_game_1 == '✋' and which_game_2 == '✊' ) or ( which_game_1 == '✊' and which_game_2 == '✌️' ) or ( which_game_1 == '✌️' and which_game_2 == '✋' ) :
                        user_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} {username_1} win \nResualt : \n {username_1} : {user_1} \n {username_2} : {user_2}', title='User - User panel')
                    else :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} {username_2} win \nResualt : \n {username_1} : {user_1} \n {username_2} : {user_2}', title='User - User panel')

                if user_1 > user_2 :
                    finally_resualt = py.alert(text=f'{username_1} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='Finally result')
                elif user_1 < user_2 :
                    finally_resualt = py.alert(text=f'{username_2} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='Finally result')
                else :
                    finally_resualt = py.alert(text=f'game is equal, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='Finally result')
                break

            else :
                while number_played_Rock_Paper_Scissors < round_number :
                    which_game_1 = py.confirm(text=f'{username_1} which action do you want to select ?', title='select action panel', buttons=['✊', '✋', '✌️'])
                    which_game_2 = py.confirm(text=f'{username_2} which action do you want to select ?', title='select action panel', buttons=['✊', '✋', '✌️'])
                    number_played_Rock_Paper_Scissors += 1
                    if which_game_1 == which_game_2 :
                        user_1 += 1
                        user_2 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} is equal \nResualt : \n {username_1} : {user_1} \n {username_2} : {user_2}', title='User - User panel')
                    elif ( which_game_1 == '✋' and which_game_2 == '✊' ) or ( which_game_1 == '✊' and which_game_2 == '✌️' ) or ( which_game_1 == '✌️' and which_game_2 == '✋' ) :
                        user_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} {user_1} win \nResualt : \n {username_1} : {user_1} \n {username_2} : {user_2}', title='User - User panel')
                    else :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} {user_2} win \nResualt : \n {username_1} : {user_1} \n {username_2} : {user_2}', title='User - User panel')
                
                if user_1 > user_2 :
                    finally_resualt = py.alert(text=f'{username_1} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='Finally result')
                elif user_1 < user_2 :
                    finally_resualt = py.alert(text=f'{username_2} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='Finally result')
                else :
                    finally_resualt = py.alert(text=f'game is equal, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='Finally result')
                break 

        elif which_game_Rock_Paper_Scissors == 'Bot - Bot' :
            random_bot_name_1 = random.choice(all_bot_name)
            bot_name_1 = py.alert(text=f'First Robot name is {random_bot_name_1}', title='Bot - Bot panel')
            random_bot_name_2 = random.choice(all_bot_name)

            while random_bot_name_1 == random_bot_name_2 :
                random_bot_name_2 = random.choice(all_bot_name)
                if random_bot_name_1 != random_bot_name_2 :
                    random_bot_name_2 = random.choice(all_bot_name)
            pass

            bot_name_2 = py.alert(text=f'Second Robot name is {random_bot_name_2}', title='Bot - Bot panel')

            if How_determine_winner == 'Whoever reaches the entry number' :
                while bot_1 < round_number and bot_2 < round_number :
                    random_action_1 = random.choice(action)
                    random_action_2 = random.choice(action)
                    number_played_Rock_Paper_Scissors += 1
                    if random_action_1 == random_action_2 :
                        bot_1 += 1
                        bot_2 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} is equal \nResualt : \n {random_bot_name_1} {random_action_1} {bot_1} \n {random_bot_name_2} {random_action_2} {bot_1} ', title='Bot - Bot panel')
                    elif ( random_action_1 == '✋' and random_action_2 == '✊' ) or ( random_action_1 == '✊' and random_action_2 == '✌️' ) or ( random_action_1 == '✌️' and random_action_2 == '✋' ) :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} {random_bot_name_1} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                    else :
                        bot_2 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} {random_bot_name_2} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                if bot_1 > bot_2 :
                    finally_resualt = py.alert(text=f'{random_bot_name_1} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                elif bot_1 < bot_2 :
                    finally_resualt = py.alert(text=f'{random_bot_name_2} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                else :
                    finally_resualt = py.alert(text=f'game is equal, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                break

            else :
                while number_played_Rock_Paper_Scissors < round_number :
                    random_action_1 = random.choice(action)
                    random_action_2 = random.choice(action)
                    number_played_Rock_Paper_Scissors += 1
                    if random_action_1 == random_action_2 :
                        bot_1 += 1
                        bot_2 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} is equal, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                    elif ( random_action_1 == '✋' and random_action_2 == '✊' ) or ( random_action_1 == '✊' and random_action_2 == '✌️' ) or ( random_action_1 == '✌️' and random_action_2 == '✋' ) :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors} , Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                    else :
                        bot_2 += 1
                        resualt_game = py.alert(text=f'round {number_played_Rock_Paper_Scissors}, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                
                if bot_1 > bot_2 :
                    finally_resualt = py.alert(text=f'{random_bot_name_1} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                elif bot_1 < bot_2 :
                    finally_resualt = py.alert(text=f'{random_bot_name_2} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                else :
                    finally_resualt = py.alert(text=f'game is equal, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                break

    elif menu_game_panel == 'Guess_number' :
        number_played_games += 1
        rounds = 1
        len_str_number = ''

        how_many_len = int(py.prompt(text='Welcome to Guess number \nHow many digits is the selected number ?', title='Entery len number'))

        while how_many_len > 5 :
            how_many_len = int(py.prompt(text='Your digits number must be lower than 5 ,enter digits the number again ?', title='Entery len number'))

        how_many_round = int(py.prompt(text='How many rounds do you want to try your luck ?', title='Entery round number'))

        for i in range(how_many_len) :
            len_str_number += '9'
            len_int_number = int(len_str_number)

        random_number = random.randint(1, len_int_number + 1)

        entry_random_number = int(py.prompt(text=f'guess and enter your number', title='Entery random number'))

        while rounds < how_many_round :
            rounds += 1
            if entry_random_number == random_number :
                entry_random_number = py.alert(text=f'great {entry_random_number} is the currect number', title='Win panel')
                win_alert = py.alert(text=f'congratulations, you win the game in {rounds - 1} rounds ', title='Win panel')
                break
            elif entry_random_number > random_number :
                entry_random_number = int(py.prompt(text=f'Round {rounds}, {entry_random_number} is bigger than real number guess again enter another number', title='Entery random number'))
            else : #entry_random_number < random_number :
                entry_random_number = int(py.prompt(text=f'Round {rounds}, {entry_random_number} is lower than real number guess again enter another number', title='Entery random number'))
        else: 
            lose_alert = py.alert(text=f'We are sorry your chance is finish, you lose the game \nComputer number was {random_number}', title='Lose panel')

        menu_game_panel = py.confirm(text=f'{username} Select one of the game', title='Game panel', buttons=['✊_✋_✌️', 'Guess_number', 'Gol_ya_Pooch', 'Esm_Famil', 'Mouse_Movement', 'Exit'])

    elif menu_game_panel == 'Gol_ya_Pooch' :
        number_played_games += 1
        user_gol_ya_pooch = 0
        bot_gol_ya_pooch = 0
        name_box = ['Box 1', 'Box 2']
        welcome_panel = py.confirm(text='Welcome to Gol_ya_Pooch game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])
        while welcome_panel == 'No' :
            canceling = py.confirm(text='Are you sure to quit the game ?', title='Quit panel', buttons=['Yes', 'No'])
            if canceling == 'Yes' :
                canceling_2 = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                break
            elif canceling == 'No' :
                welcome_panel = py.confirm(text='Welcome to Gol_ya_Pooch game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])
        
        how_many_round = int(py.prompt(text='How many rounds do you want to try your luck ?', title='Entery round number'))
        round_game_played = 0
        while round_game_played < how_many_round : 
            random_name_box = random.choice(name_box)
            Gol_ya_Pooch_panel = py.confirm(text='Select one of the box ?', title='Gol_ya_Pooch panel', buttons=['Box 1', 'Box 2'])

            round_game_played += 1
            if Gol_ya_Pooch_panel == random_name_box :
                resualt_Gol_ya_Pooch_game = py.alert(text=f'round {round_game_played}/{how_many_round} , Resualt : You win', title='Gol_ya_Pooch panel')
                user_gol_ya_pooch += 1
            else :
                resualt_Gol_ya_Pooch_game = py.alert(text=f'round {round_game_played}/{how_many_round} , Resualt : You lose', title='Gol_ya_Pooch panel')
                bot_gol_ya_pooch += 1

        all_result_gol_ya_pooch = py.alert(text=f'All result : \n{username} {user_gol_ya_pooch} \nRobot {bot_gol_ya_pooch}', title='Lose panel')

        menu_game_panel = py.confirm(text=f'{username} Select one of the game', title='Game panel', buttons=['✊_✋_✌️', 'Guess_number', 'Gol_ya_Pooch', 'Esm_Famil', 'Mouse_Movement', 'Exit'])






    elif menu_game_panel == 'Esm_Famil' :
        number_played_games += 1
        print('d')

    
    elif menu_game_panel == 'Jorat_Haghighat' :
        number_played_games += 1
        jorat_list = ['Kole direct inestat ro neshon bede', 'Dad bezan bego man divoonam', 'Be sorat random be yeki az mokhatabat zang bezan bego dooset daram', 'Ye sandewich be hesab khodet sefaresh bede', 'Az inja ta park tv piade boro', 'Ye music ke doos dari ba sedaye boland bekhon']
        haghighat_list = ['Chandbar ashegh shodi ?', 'Bozorg tarin razet chie ?', 'Ajibtarin adati ke dari chie ?', 'Age ye rooz omr koni chi kar tooye on rooz mikoni ?', 'Age mitonesi chizi ro toye sooratet taghir bedi chi bood ?']

        welcome_Jorat_Haghighat_panel = py.confirm(text='Welcome to Jorat_Haghighat game, Ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])
        while welcome_Mouse_Movement_panel == 'No' :
            canceling = py.confirm(text='Are you sure to quit the game ?', title='Quit panel', buttons=['Yes', 'No'])
            if canceling == 'No' :
                welcome_Jorat_Haghighat_panel = py.confirm(text='Welcome to Jorat_Haghighat game, Ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])
            else :
                canceling = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                break
        else:
                welcome_Jorat_Haghighat_panel = py.confirm(text='Select one of the box', title='Welcome panel', buttons=['Yes', 'No'])




    elif menu_game_panel == 'Mouse_Movement' :
        number_played_games += 1

        screen_size_x, screen_size_y = py.size()

        half_screen_size_x = screen_size_x / 2
        half_screen_size_y = screen_size_y / 2


        welcome_Mouse_Movement_panel = py.confirm(text='Welcome to guess movement game, Ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])
        while welcome_Mouse_Movement_panel == 'No' :
            canceling = py.confirm(text='Are you sure to quit the game ?', title='Quit panel', buttons=['Yes', 'No'])
            if canceling == 'No' :
                welcome_Mouse_Movement_panel = py.confirm(text='Welcome to guess movement game, Ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])
            else :
                canceling = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                break
        else:
            all_round_game = int(py.prompt(text=f'After start, you have 3 second to select a point \nHow many rounds do you want to play ? \n', title='Round number panel'))

        round_win = 0
        round_game_played = 0
        while round_game_played < all_round_game :
            random_screen_size_x = random.randint(0, screen_size_x)
            random_screen_size_y = random.randint(0, screen_size_y)
            time.sleep(1.5)
            user_click_x, user_click_y = py.position()

            round_game_played += 1
            if user_click_x <= half_screen_size_x and user_click_y <= half_screen_size_y :        #up_left
                if random_screen_size_x <= half_screen_size_x and random_screen_size_y <= half_screen_size_y :
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You win \nYou select up and left \ncomputer select up and left', title='Mouse movement game')     
                    round_win += 1
                elif random_screen_size_x <= half_screen_size_x and random_screen_size_y >= half_screen_size_y :     #down_left
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select up and left \ncomputer select down and left', title='Mouse movement game')     
                elif random_screen_size_x >= half_screen_size_x and random_screen_size_y <= half_screen_size_y :    #up_right
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select up and left \ncomputer select up and right', title='Mouse movement game')     
                else : #random_screen_size_x >= half_screen_size_x and random_screen_size_y >= half_screen_size_y :    #down_right
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select up and left \ncomputer select down and right', title='Mouse movement game')     

            elif user_click_x <= half_screen_size_x and user_click_y >= half_screen_size_y :        #down_left
                if random_screen_size_x <= half_screen_size_x and random_screen_size_y >= half_screen_size_y :   
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You win \nYou select down and left \ncomputer select down and left', title='Mouse movement game')     
                    round_win += 1
                elif random_screen_size_x <= half_screen_size_x and random_screen_size_y <= half_screen_size_y :     #up_left
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select down and left \ncomputer select up and left', title='Mouse movement game')     
                elif random_screen_size_x >= half_screen_size_x and random_screen_size_y <= half_screen_size_y :    #up_right
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select down and left \ncomputer select up and right', title='Mouse movement game')     
                else : #random_screen_size_x >= half_screen_size_x and random_screen_size_y >= half_screen_size_y :    #down_right
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select down and left \ncomputer select down and right', title='Mouse movement game')     

            elif user_click_x >= half_screen_size_x and user_click_y <= half_screen_size_y :        #up_right
                if random_screen_size_x >= half_screen_size_x and random_screen_size_y <= half_screen_size_y :   
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You win \nYou select up and right \ncomputer select up and right', title='Mouse movement game')     
                    round_win += 1
                elif random_screen_size_x <= half_screen_size_x and random_screen_size_y <= half_screen_size_y :     #up_left
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select up and right \ncomputer select up and left', title='Mouse movement game')     
                elif random_screen_size_x <= half_screen_size_x and random_screen_size_y >= half_screen_size_y :    #down_left
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select up and right \ncomputer select down and left', title='Mouse movement game')     
                else :     #down_right
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select up and right \ncomputer select down and right', title='Mouse movement game')     

            else : #user_click_x >= half_screen_size_x and user_click_y >= half_screen_size_y :        #down_right
                if random_screen_size_x >= half_screen_size_x and random_screen_size_y >= half_screen_size_y :   
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You win \nYou select down and right \ncomputer select down and right', title='Mouse movement game')     
                    round_win += 1
                elif random_screen_size_x <= half_screen_size_x and random_screen_size_y <= half_screen_size_y :     #up_left
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select down and right \ncomputer select up and left', title='Mouse movement game')     
                elif random_screen_size_x <= half_screen_size_x and random_screen_size_y >= half_screen_size_y :    #down_left
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select down and right \ncomputer select down and left', title='Mouse movement game')     
                else : #random_screen_size_x >= half_screen_size_x and random_screen_size_y <= half_screen_size_y :    #up_right
                    result_point = py.alert(text=f'Round {round_game_played}/{all_round_game} You lose \nYou select down and right \ncomputer select up and right', title='Mouse movement game')     
        else :
            if round_win > (round_game_played / 2) :
                finally_result_point = py.alert(text=f'Finally result {username} win the game \nWin {round_win} round \nLose {round_game_played - round_win} round ', title='result Mouse movement game')     
            elif round_win < (round_game_played / 2) :
                finally_result_point = py.alert(text=f'Finally result {username} lose the game \nWin {round_win} round \nLose {round_game_played - round_win} round', title='result Mouse movement game')     
            else :
                finally_result_point = py.alert(text=f'Finally result {username} draw the game \nWin {round_win} round \nLose {round_game_played - round_win} round', title='result Mouse movement game')     
            menu_game_panel = py.confirm(text=f'{username} Select one of the game', title='Game panel', buttons=['Rock_Paper_Scissors', 'Guess_number', 'Gol_ya_Pooch', 'Esm_Famil', 'Mouse_Movement', 'Exit'])






    elif menu_game_panel == 'Exit' :
        break




else :
    stop_free_game = py.alert(text='Sorry for stopying the game \nYou can just play 2 free games \nfor buying unlimited version check "Details" \nEmail : milad.baroun@gmail.com \nPhone number : +989177719601', title='Finish game :(')     

      




















