#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

#Imprort random that will allow us to create a random set of integers
import random


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

	return initializer(n)


def initializer(n):
	'''Creates a random list of values.'''
	try:
		list_of_values = random.sample(range(1, 100), n) 
	except ValueError:
		print('There was a problem creating the list of numbers.')
	print('Original Array: ' + str(list_of_values))

	return list_of_values		


def insertion_sort(values):
	'''Sorting Algorithm'''
	j = 1
	for j in range(j, len(values)):
		key = values[j]
		i = j - 1

		while i >= 0 and values[i] > key:
			values[i + 1] = values[i]
			i -= 1
		values[i + 1] = key
		
		print(values)

	return values




# Gather our code in a main() function
def main():
	n = None # Number of values. 
	values = user_input(n)
	print ('Sorted Array: ' + str(insertion_sort(values)))
  



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()



