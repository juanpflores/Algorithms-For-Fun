#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

#Miscelaneous fucntions for the example.
def user_input(n):
	''' Allows the user to create a list with his specidifications'''
	
	while not n:
		print('How many elements you want to create?')
		try:
			n = int(input())
		except ValueError:
			print('The input is not a valid number.')
	print('The number of values to create is: ' + str(n))




def initializer():
	'''Creates a random list of values.'''

def insertion_sort():
	'''Sorting Algorithm'''


# Gather our code in a main() function
def main():
	n = None # Number of values. 
	user_input(n)	
  



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()



