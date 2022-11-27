import os
import quizmenu
import answers

#List of meny options to pick from.
def main_menu():
    print('1. Quiz')
    print('2. Correct answers')
    print('0. End program' '\n')

print('Welcome to Python Quiz')
input('')

main_menu()
#Makes it so the user can input which menu option to use.
option = int(input('Type menu option: '))

#A while loop is used to make it easier for the user to pick menu options, and if 0 is picked it quits the program.
while option != 0:
    if option == 1:
        os.system('cls')
        quizmenu.quiz_function()
    elif option == 2:
        os.system('cls')
        answers.answers_function()
    else:
    #Failsafe to make sure the user can return to the loop.
        os.system('cls')
        print('\n' 'That option is not available')
        print('Press enter to return to menu')
        input()

  #Iteration so the user can get back to the menu.
    main_menu()
    option = int(input('Type menu option: '))

print('\n' 'Python Quiz is shutting down')
