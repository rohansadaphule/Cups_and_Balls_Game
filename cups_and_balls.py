import os
from random import shuffle

cups_list = ['--','O','--']
flag = 'y'

def shuffle_list(my_list):
	shuffle(my_list)
	return my_list
	
	
def user_guess():
	num_guess = ''
	
	while num_guess not in ['1','2','3']:
		num_guess = input('Enter your guess (1/2/3): ')
		
		if num_guess not in ['1','2','3']:
			print('Enter a valid number')
	return int(num_guess)
	
	
def check_guess(cups_list,user_guess):
	user_guess = user_guess -1
	
	if cups_list[user_guess] == 'O':
		print('Congratulations your guess was correct')
		print(cups_list)
	else :
		print('Sorry your guess was incorrect, \n Better luck next time')
		print(cups_list)
	

while flag.lower()=='y':
	os.system('cls') #change it to 'clear' for LINUX systems
	shuffled_list = shuffle_list(cups_list)
	guess = user_guess()
	check_guess(shuffled_list,guess)
	flag = input('Would you like to play again enter (y/n): ')
	flag.lower()
