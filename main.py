player = {'name': 'Eka P', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name': 'Max', 'attack': 12, 'health': 100}

print('Welcome to Monster Game!!')
print('Please select action')
print('1) Attack')
print('2) Heal')

player_choice = input()

if player_choice == '1':
  print('Attack')
  
elif player_choice == '2':
  print('Heal player')

else:
  print('Something went wrong')  
