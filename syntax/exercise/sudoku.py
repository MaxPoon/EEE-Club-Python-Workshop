import random
from copy import deepcopy
import itertools

def generate_board():    

	board = None 
	count = 0
	while board is None:
		board = attempt_board()
	return board

def attempt_board():
	numbers = list(range(1, 10))
	n = 9
	board = [[None for _ in range(n)] for _ in range(n)]
	# write your code here

def print_board(board):
	numbers = list(range(1, 10))
	omit = 5
	challange = deepcopy(board)
	for i, j in itertools.product(range(omit), range(9)):
		x = random.choice(numbers) - 1
		challange[x][j] = None

	spacer = "++-----+-----+-----++-----+-----+-----++-----+-----+-----++"
	print (spacer.replace('-','='))
	for i, line in enumerate(challange):
		print("||  {}  |  {}  |  {}  ||  {}  |  {}  |  {}  ||  {}  |  {}  |  {}  ||"
			  .format(*(cell or ' ' for cell in line)))
		if (i + 1) % 3 == 0: print(spacer.replace('-', '='))
		else: print(spacer)
	return challange

def print_answers(board):
	spacer = "++-----+-----+-----++-----+-----+-----++-----+-----+-----++"
	print (spacer.replace('-','='))
	for i, line in enumerate(board):
		print("||  {}  |  {}  |  {}  ||  {}  |  {}  |  {}  ||  {}  |  {}  |  {}  ||"
			  .format(*(cell or ' ' for cell in line)))
		if (i + 1) % 3 == 0: print(spacer.replace('-', '='))
		else: print(spacer)


board = generate_board()
print_board(board)
print("Press any key to see the answer\n")
input()
print_answers(board)