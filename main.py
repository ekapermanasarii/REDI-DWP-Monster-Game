def my_function(first_name):
    print("hi, this game is called " + first_name)
my_function("Monster game")


game_running =  True

while game_running == True:
    new_round = True

    import random
    player = {'name': 'player 1 Eka', 'attack': 10, 'heal': 15, 'health': 100}
    print(player)

    monster = {'name': 'Monster Bobi', 'attack': 13, 'heal': 17, 'health': 100}
    print(monster)

    print('-----' *3)
    print('Enter Player name')
    player['name'] = input ()

    #print(player['name'] + ' has ' +  player ['health'])

    while new_round == True:

        print('Welcome to Monster Game!!')
        print('Please select action')
        print('1) Attack')
        print('2) Heal')

        while monster ['health']>= 0 and player ['health']>=0:
            player_choice = (input("insert the type of action"))
            if player_choice ==  "1":
                player_attack = random.randint(10, 15)
                monster['health'] = monster ['health'] - player ['attack']
                print ('Monster Health:' + str(monster['health']))

                monster_attack=random.randint(11,15)
                player['health'] = player ['health'] - monster ['attack']
                print ('Player health:' + str(player ['health']))

                if player_attack > monster_attack:
                    print('You defeat the Monster')
                elif monster_attack > player_attack:
                    print ('Monster defeats you')
                else:
                    print('you lost the same amount')

                print('The Monster lost' + str(player_attack) + 'points with your attack')
                print('The monster attacked you back and you lost' + str(monster_attack) + 'points')


            if player_choice ==  "2":
                monster_health = random.randint(15,25)
                monster['health'] = monster ['health'] + monster ['heal']
                print ('Monster Health:' + str(monster['health']))

                player['health'] = player['health'] + player['heal']
                print('Player health:' + str(player['health']))

            else:
                print ('valid input is only 1 or 2')


        if player['health'] <= 0 or monster['health'] <= 0:
            new_round = False
            game_running = False
