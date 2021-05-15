def my_function(first_name):
    print("hi, this game is called " + first_name)
my_function("Monster game")

player = {'name': 'player 1 Eka', 'attack': 10, 'heal': 15, 'health': 100}
print(player)

monster = {'name': 'Monster Bobi', 'attack': 13, 'heal': 17, 'health': 100}
print(monster)

print('Welcome to Monster Game!!')
print('Please select action')
print('1) Attack')
print('2) Heal')

player_choice = (input("insert the type of action"))
if player_choice == '1':
    print ('Attack')
if player_choice == '2':
    print ('Heal')
elif player_choice == '3':
    print ('Exit')
else:
    print ('not working')

while monster ['health']>= 0 or player ['health']>=0:
    if player_choice ==  "1":
        monster['health'] = monster ['health'] - player ['attack']
        print (monster['health'])

        player['health'] = player ['health'] - monster ['attack']
        print (player ['health'])

    if player_choice ==  "2":
        player['health'] = player['health'] + player['heal']
        print(player['health'])

        monster['health'] = monster ['health'] + monster ['heal']
        print (monster['health'])

    elif player_choice == '2':
        print ('Heal player')
    else:
        print ('not working')

    if player ['health'] <=0:
        print ('you lost the game')

    if monster ['health'] <=0:
        print ('you win!')

#while monster ['health']>=0:
    #player_choice = (input("insert the type of action"))

    #if player_choice == "1":
        #monster['health'] = monster['health'] - player['attack']
        #player['health'] = player['health'] - monster['attack']
        #print(monster['health'])
        #print(player['health'])
    #elif player_choice == '2':
        #print('Heal player')
    #else:
        #print('not working')
