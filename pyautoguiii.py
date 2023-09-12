
import pyautogui as py
import random

confirmation_rulls_game = 0
confirmation_details = 0

welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])

while confirmation_rulls_game < 1 or confirmation_details < 1 :

    if welcome_panel == 'Menu game' :
        alert_before_welcome_panel = py.alert(text='You have not read Rulls game and Details ,read and then click on Menu game', title='Welcome panel')
        welcome_panel = py.confirm(text='please read both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
    elif welcome_panel == 'Rulls game' :
        rulls_game_panel = py.confirm(text='Rull of the game: \n1. Playing the games means you have accepted the complete rules of the game \n2. When your opponent is a robot, his movement is chosen by chance and you have to accept the result \n3. If you make a change in the source code of the game, this is cheating and you will lose the game \n4. During the game, two users should not show each other their next move to the opponent \n5. If you quit the game, your opponent will win the game.', title='Rulls game panel', buttons=['I agree', 'I dont agree'])
        if rulls_game_panel == 'I agree' :
            confirmation_rulls_game += 1
            welcome_panel = py.confirm(text='Thanks for reading Rulls game ,if you have not readen Details else please read it and then click on Menu game to start', title='Rulls game panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
        elif rulls_game_panel == 'I dont agree' :
            quit_panel = py.confirm(text='if you want to play click on Back button and read it or if you want quit the game click on Exit button', title='Rulls game panel', buttons=['Back', 'Exit'])
            if quit_panel == 'Back' :
                welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
            if quit_panel == 'Exit' :
                quit_panel = py.confirm(text='Are you sure to quit ? ', title='Quit panel', buttons=['Yes', 'No'])
                if quit_panel == 'Yes' :
                    quit_panel = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
                    break
                elif quit_panel == 'No' :
                    welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
    elif welcome_panel == 'Details' :
        confirmation_details += 1
        details_game_panel = py.alert(text='This package game produced by Milad Barouni the Ways of communication by \nEmail : milad.baroun@gmail.com \nPhone number : +989177719601', title='Details panel')
        welcome_panel = py.confirm(text='Thanks for reading details game ,if you have not readen rulls game else please read it and then click on Menu game to start', title='Details game panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
    elif welcome_panel == 'Exit' :
        quit_panel = py.confirm(text='Are you sure to quit ? ', title='Quit panel', buttons=['Yes', 'No'])
        if quit_panel == 'Yes' :
            quit_panel = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
            break
        elif quit_panel == 'No' :
            welcome_panel = py.confirm(text='Welcome to the game, before play please read \n     both of the Rulls game and Details to start', title='Welcome panel', buttons=['Menu game', 'Rulls game', 'Details', 'Exit'])
   



number_played_games = 0

while number_played_games <= 2 and welcome_panel == 'Menu game' :
    menu_game_panel = py.confirm(text='Select one of the game', title='Menu panel', buttons=['Rock_Paper_Scissors', 'Guess_number', 'Gol_ya_Pooch', 'Esm_Famil', 'Mouse_Movement', 'Exit'])
    
    if menu_game_panel == 'Rock_Paper_Scissors' :
        number_played_games += 1



        
    all_bot_name = ['Milad', 'Misaq', 'Abas', 'Mohammad', 'Aida', 'Neda', 'Sepideh', 'Mahsa']
    action = ['Rock', 'Paper', 'Scissor']
    user_1 = 0
    user_2 = 0
    bot_1 = 0
    bot_2 = 0
    number_played = 0

    welcome_panel = py.confirm(text='Welcome to Rock_Paper_Scissors game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])

    while welcome_panel == 'No' :
        canceling = py.confirm(text='Are you sure to quit the game ?', title='Quit panel', buttons=['Yes', 'No'])
        if canceling == 'Yes' :
            canceling_2 = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
            break
        elif canceling == 'No' :
            welcome_panel = py.confirm(text='Welcome to the game, Are you ready to start ?', title='Welcome panel', buttons=['Yes', 'No'])

    if welcome_panel == 'Yes' :
        username = py.prompt(text='First enter your name please', title='Name panel') 

    while not username :                                                                                                    
        canceling = py.confirm(text='An error has occurred, this error may be due to exiting the program or due to not entering the name', title='Unknow error panel', buttons=['Enter a name', 'Exit'])
        if canceling == 'Exit' :
            canceling_2 = py.alert(text='Bye, we hope see you soon again', title='Quit panel')
            break
        if canceling == 'Enter a name' :
            username = py.prompt(text='First enter your name please', title='Name panel')
    else :
        which_game = py.confirm(text=f'{username} which game do you want ?', title='select game panel', buttons=['User - Bot', 'Bot - Bot', 'User - User', 'Rull game', 'Details', 'Exit'])


    while which_game == 'User - Bot' or 'Bot - Bot' or 'User - User' :
        round_number = int(py.prompt(text='How many round do you want to play ?', title='round panel', default='How many round'))
        How_determine_winner = py.confirm(text='How to determine the winner ?', title='Determine panel', buttons=['Whoever reaches the entry number', 'Only play the entry number'])
        if which_game == 'User - Bot' :
            random_bot_name_1 = random.choice(all_bot_name)
            bot_name = py.alert(text=f'Robot name is {random_bot_name_1}', title='User - Bot panel')
            if How_determine_winner == 'Whoever reaches the entry number' :
                while user_1 < round_number and bot_1 < round_number :
                    random_action = random.choice(action)
                    which_game = py.confirm(text=f'{username} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
                    number_played += 1
                    if which_game == random_action :
                        user_1 += 1
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played} is equal, {random_bot_name_1} selected {random_action}, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                    elif ( which_game == 'Paper' and random_action == 'Rock' ) or ( which_game == 'Rock' and random_action == 'Scissor' ) or ( which_game == 'Scissor' and random_action == 'Paper' ) :
                        user_1 += 1
                        resualt_game = py.alert(text=f'round {number_played} You win, {random_bot_name_1} selected {random_action}, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                    else :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played} You lose, {random_bot_name_1} selected {random_action}, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                if user_1 > bot_1 :
                    finally_resualt = py.alert(text=f'{username} you win the game, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                elif user_1 < bot_1 :
                    finally_resualt = py.alert(text=f'{username} you lose the game, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                else :
                    finally_resualt = py.alert(text=f'{username} your game is equal, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                break

            else :
                while number_played < round_number :
                    random_action = random.choice(action)
                    which_game = py.confirm(text=f'{username} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
                    number_played += 1
                if which_game == random_action :
                    user_1 += 1
                    bot_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} is equal, {random_bot_name_1} selected {random_action}, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                elif ( which_game == 'Paper' and random_action == 'Rock' ) or ( which_game == 'Rock' and random_action == 'Scissor' ) or ( which_game == 'Scissor' and random_action == 'Paper' ) :
                    user_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} You win, {random_bot_name_1} selected {random_action}, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
                else :
                    bot_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} You lose, {random_bot_name_1} selected {random_action}, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
            if user_1 > bot_1 :
                finally_resualt = py.alert(text=f'{username} you win the game, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
            elif user_1 < bot_1 :
                finally_resualt = py.alert(text=f'{username} you lose the game, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
            else :
                finally_resualt = py.alert(text=f'{username} your game is equal, Resualt : {user_1} - {bot_1}', title='User - Bot panel')
            break  
        if which_game == 'User - User' :
            username_1 = py.prompt(text=f'{username} enter the first name player please', title='Name panel', default='first player')
            username_2 = py.prompt(text='enter the second name player', title='Name panel', default='second player')
            if How_determine_winner == 'Whoever reaches the entry number' :
                while user_1 < round_number and user_2 < round_number :
                    which_game_1 = py.confirm(text=f'{username_1} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
                    which_game_2 = py.confirm(text=f'{username_2} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
                    number_played += 1
                    if which_game_1 == which_game_2 :
                        user_1 += 1
                        user_2 += 1
                        resualt_game = py.alert(text=f'round {number_played} is equal, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
                    elif ( which_game_1 == 'Paper' and which_game_2 == 'Rock' ) or ( which_game_1 == 'Rock' and which_game_2 == 'Scissor' ) or ( which_game_1 == 'Scissor' and which_game_2 == 'Paper' ) :
                        user_1 += 1
                        resualt_game = py.alert(text=f'round {number_played} {user_1} win, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
                    else :
                        bot_1 += 1
                        resualt_game = py.alert(text=f'round {number_played} {user_2} win, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')

            if user_1 > user_2 :
                finally_resualt = py.alert(text=f'{username_1} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            elif user_1 < user_2 :
                finally_resualt = py.alert(text=f'{username_2} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            else :
                finally_resualt = py.alert(text=f'game is equal, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            break

        else :
            while number_played < round_number :
                which_game_1 = py.confirm(text=f'{username_1} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
                which_game_2 = py.confirm(text=f'{username_2} which action do you want to select ?', title='select action panel', buttons=['Rock', 'Paper', 'Scissor'])
                number_played += 1
                if which_game_1 == which_game_2 :
                    user_1 += 1
                    user_2 += 1
                    resualt_game = py.alert(text=f'round {number_played} is equal, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
                elif ( which_game_1 == 'Paper' and which_game_2 == 'Rock' ) or ( which_game_1 == 'Rock' and which_game_2 == 'Scissor' ) or ( which_game_1 == 'Scissor' and which_game_2 == 'Paper' ) :
                    user_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} {user_1} win, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
                else :
                    bot_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} {user_2} win, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            if user_1 > user_2 :
                finally_resualt = py.alert(text=f'{username_1} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            elif user_1 < user_2 :
                finally_resualt = py.alert(text=f'{username_2} win the game, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            else :
                finally_resualt = py.alert(text=f'game is equal, Resualt : {username_1} {user_1} - {user_2} {username_2}', title='User - User panel')
            break 

    if which_game == 'Bot - Bot' :
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
                number_played += 1
                if random_action_1 == random_action_2 :
                    bot_1 += 1
                    bot_2 += 1
                    resualt_game = py.alert(text=f'round {number_played} is equal, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                elif ( random_action_1 == 'Paper' and random_action_2 == 'Rock' ) or ( random_action_1 == 'Rock' and random_action_2 == 'Scissor' ) or ( random_action_1 == 'Scissor' and random_action_2 == 'Paper' ) :
                    bot_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} {random_bot_name_1} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                else :
                    bot_2 += 1
                    resualt_game = py.alert(text=f'round {number_played} {random_bot_name_2} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
            if bot_1 > bot_2 :
                finally_resualt = py.alert(text=f'{random_bot_name_1} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
            elif bot_1 < bot_2 :
                finally_resualt = py.alert(text=f'{random_bot_name_2} win the game, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
            else :
                finally_resualt = py.alert(text=f'game is equal, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
            break

        else :
            while number_played < round_number :
                random_action_1 = random.choice(action)
                random_action_2 = random.choice(action)
                number_played += 1
                if random_action_1 == random_action_2 :
                    bot_1 += 1
                    bot_2 += 1
                    resualt_game = py.alert(text=f'round {number_played} is equal, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                elif ( random_action_1 == 'Paper' and random_action_2 == 'Rock' ) or ( random_action_1 == 'Rock' and random_action_2 == 'Scissor' ) or ( random_action_1 == 'Scissor' and random_action_2 == 'Paper' ) :
                    bot_1 += 1
                    resualt_game = py.alert(text=f'round {number_played} , Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
                else :
                    bot_2 += 1
                    resualt_game = py.alert(text=f'round {number_played}, Resualt : {random_bot_name_1} {random_action_1} {bot_1} - {bot_2} {random_action_2} {random_bot_name_2} ', title='Bot - Bot panel')
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
            elif entry_random_number < random_number :
                entry_random_number = int(py.prompt(text=f'Round {rounds}, {entry_random_number} is lower than real number guess again enter another number', title='Entery random number'))
        else: 
            lose_alert = py.alert(text=f'We are sorry your chance is finish, you lose the game', title='Lose panel')



    elif menu_game_panel == 'Gol_ya_Pooch' :
        number_played_games += 1
        print('d')
    elif menu_game_panel == 'Esm_Famil' :
        number_played_games += 1
        print('d')
    elif menu_game_panel == 'Mouse_Movement' :
        number_played_games += 1
        print('d')
    elif menu_game_panel == 'Exit' :
        break





























