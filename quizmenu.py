import os
import quiz

def quiz_function():
    def quiz_menu():
        print('1. First Quiz')
        print('2. Second Quiz')
        print('3. Random Quiz')
        print('0. Return to main menu' '\n')

    quiz_menu()
    option = int(input('Type menu option: '))

    while option != 0:
        if option == 1:
            os.system('cls')
            quiz.QuizOne()
        elif option == 2:
            os.system('cls')
            quiz.QuizTwo()
        elif option == 3:
            os.system('cls')
            quiz.RandomQuiz()
        else:
            os.system('cls')
            print('\n' 'Ogiltigt val')
            print('Press enter to return to main menu')
            input()
 
        quiz_menu()
        option = int(input('Type menu option: '))
        os.system('cls')
