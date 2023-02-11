import random
user_option = input('Piedra, Papel, Tijera =>')
user_option = user_option.lower()
options = 0

if  not user_option in options:
    print('opcion no valido')


computer_option = random.choice(options)
print('user_option => ', user_option )
print('computer options => ', computer_option)


if user_option == computer_option:
    print("Empate!")
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print ("Piedra gana a tijera")
        print ("User Gana!")
    else:
        print('Papel Gana a piedra')
        print("computer gana!")
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a piedra')
        print('User gano!') 
    else:
        print('tijera Gana a papel')
        print('Computer Gano')
elif user_option == 'tijera':
    if computer_option== 'papel':
        print('tijera gana a papel')
        print('User Gana')
    else:
        print('piedra gana a tijera')
        print('computer gana')
