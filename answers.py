import os
import quiz

#list is converted to a dict to make it printable in a nice way.
first_dict = dict(quiz.first_quiz)
second_dict = dict(quiz.second_quiz)

def answers_function():
    def correct_answers():
        print('1. First Quiz answers')
        print('2. Second Quiz answers')
        print('0. Return to main menu' '\n')

    correct_answers()
    option = int(input('Type menu option: '))

    while option != 0:
        if option == 1:
            os.system('cls')
            print('First Quiz answers: \n')
            for key, value in first_dict.items():   #for loop is used to print out dicts in a nice way.
                print(f'{key}: {value}')
                print('')
        elif option == 2:
            os.system('cls')
            print('Second Quiz answers: \n')
            for key, value in second_dict.items():
                print(f'{key}: {value}')
                input('')
        else:
            os.system('cls')
            print('\n' 'Ogiltigt val')
            print('Press enter to return to main menu')
            input()

        correct_answers()
        option = int(input('Type menu option: '))
        os.system('cls')
