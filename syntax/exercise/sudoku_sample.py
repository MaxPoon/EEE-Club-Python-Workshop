import random
from copy import deepcopy
import itertools

def generate_board():    
	board = None 
	while board is None:
		board = attempt_board()
	return board

def attempt_board():
	numbers = list(range(1, 10))
	n = 9
	board = [[None for _ in range(n)] for _ in range(n)]

	for i in range(9):
		for j in range(9):
			# the starting row and column number of the 3*3 square
			i0, j0 = i - i % 3, j - j % 3 
			# shuffle the list so that the board won't be the same
			random.shuffle(numbers)
			no_solution = True
			for x in numbers:
				# check the row, column and the 3*3 square
				if (x not in board[i] and 
					all([row[j] != x for row in board]) and 
					all(x not in row[j0:j0+3] for row in board[i0:i])):     
					board[i][j] = x
					no_solution = False
					break
			if no_solution:
				return None
	return board

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
input("Press any key to see the answer\n")
print_answers(board)