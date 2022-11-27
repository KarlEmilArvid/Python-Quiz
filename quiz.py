import os
import random
#Quiz lists are placed outside of functions to easier modify/add new quizzes or questions.

first_quiz = [
  ('What is the most used JavaScript framework in 2022', 'React'),
  ('Who directed the movie Jaws', 'Steven Spielberg'),
  ('What company owns GitHub', 'Microsoft Corporation'),
  ('The american actor Tom Hanks was born in 1956, what colour is blue', 'blue'),
  ('Which built-in Python function do you use to answer this question', 'input'),
  ('Does the Earth rotate clockwise', 'no')
]

second_quiz = [
  ('When was Python first released', 1991),
  ('When was C++ first released', 1985),
  ('What is 24 divided by 3', 8),
  ('If a decade is 10 years, how many decades ago was the launch of the Commodore 64', 4),
  ('Which year was the first Jurassic Park movie released', 1993)
]

geography_quiz = [
	('What is the capital of South Korea', 'Seoul'),
	('Which country would you be in if you were visiting Mont Saint-Michel', 'France'),
	('What country was formally known as Siam', 'Thailand'),
	('In which country is the Atacama Desert', 'Chile'),
	('Which is the worlds largest active volcano', 'Mauna Loa'),
	('In which Indian city is the Taj Mahal', 'Agra'),
	('What is the largest country in the world by surface area', 'Russia'),
	('Which continent has the highest population in the world', 'Asia'),
	('In what year did construction of the Eiffel Tower in Paris begin', 1887),
	('How many states does America have', 50),
	('Taiwan is located closest to the coast of which country', 'China'),
	('Just prior to 1935, the Islamic State of Iran was known as', 'Persia'),
	('Which country was invaded by the Turkish in 1974', 'Cyprus')
]

#TODO:
#function/menu option to add questions
#new quiz with a,b,c,d/1,2,3,4 answers
#make a quiz that can handle several correct answers, be it upper or lowercase and or just one out of two words
# - example: microsoft instead of "Microsoft Corporation"
#Randomize order of questions in all quizzes
#place quizzes in seperate file and import them into quiz.py?

def QuizOne():
	quiz_score = 0
	quiz_length = len(first_quiz)

	for question, correct_answer in first_quiz:
		answer = input(f'{question}? ') #input(f) is used to easier handle data types.
		try:
			answer = int(answer) #try/except is used to catch correct data type from users input.
		except:
			print()
		if answer == correct_answer:
			quiz_score += 1
			print()
			print('Correct answer!\n')
			input('')
			os.system('cls')
		else:
			print()
			print(f'The answer is {correct_answer!r}, not {answer!r}\n')
			input('')
			os.system('cls')
	print(f'\nYou got {quiz_score} correct answers out of {quiz_length} questions')
	input('') #input at the end of the loop to give user time to read the above print.
	os.system('cls')

def QuizTwo():
	quiz_score = 0
	quiz_length = len(second_quiz)

	for question, correct_answer in second_quiz:
		answer = input(f'{question}? ')
		try:
			answer = int(answer)
		except:
			print()
		if answer == correct_answer:
			quiz_score += 1
			print()
			print('Correct answer!\n')
			input('')
			os.system('cls')
		else:
			print()
			print(f'The answer is {correct_answer!r}, not {answer!r}\n')
			input('')
			os.system('cls')
	print(f'\nYou got {quiz_score} correct answers out of {quiz_length} questions')
	input('')
	os.system('cls')

def RandomQuiz():
	quiz_score = 0
	random_list = first_quiz + second_quiz + geography_quiz #Makes a new list out of several quizzes.
	random_quiz = random.sample(random_list, 8) #Takes out 8 questions to form a quiz of random questions.
	quiz_length = len(random_quiz)

	for question, correct_answer in random_quiz:
		answer = input(f'{question}? ')
		try:
			answer = int(answer)
		except:
			print()
		if answer == correct_answer:
			quiz_score += 1
			print()
			print('Correct answer!\n')
			input('')
			os.system('cls')
		else:
			print()
			print(f'The answer is {correct_answer!r}, not {answer!r}\n')
			input('')
			os.system('cls')
	print(f'\nYou got {quiz_score} correct answers out of {quiz_length} questions')
	input('')
	os.system('cls')
