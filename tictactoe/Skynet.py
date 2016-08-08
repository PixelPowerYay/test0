import copy
import random

def getSymbol(x):
	if x == 0:
		return " "
	elif x == 1:
		return "X"
	else:
		return "O"

def showLine(lineNr, line):
	print(str(lineNr) + '| ' + getSymbol(line[0]) + ' | ' + getSymbol(line[1]) + ' | ' + getSymbol(line[2]) + ' |')
	
def showPlayfield(playfield):
	"""
	 +---|---|---+
	1| X | O | O |
	 |---|---|---|
	2| O |   |   |
	 |---|---|---|
	3|   | X |   |
	 +---|---|---+
	   a   b   c
	"""
	lineEnds = ' +---|---|---+'
	separator = ' |---|---|---|'
	print(lineEnds)
	showLine(1, playfield[0])
	print(separator)
	showLine(2, playfield[1])
	print(separator)
	showLine(3, playfield[2])
	print(lineEnds)
	print('   a   b   c')
	
def getLine(l):
	if l == '1':
		return 0
	elif l == '2':
		return 1
	elif l == '3':
		return 2
	else:
		return -1
		
def getColumn(l):
	if l == 'a':
		return 0
	elif l == 'b':
		return 1
	elif l == 'c':
		return 2
	else:
		return -1
		
def checkGameState(playfield, line, col):
	if (playfield[line][0] == playfield[line][1]) and (playfield[line][2] == playfield[line][1]):
		return 1
	if (playfield[0][col] == playfield[1][col]) and (playfield[2][col] == playfield[0][col]):
		return 1
	if (line == col) and (playfield[0][0] == playfield[1][1]) and (playfield[0][0] == playfield[2][2]):
		return 1
	if (line + col == 2) and (playfield[0][2] == playfield[1][1]) and (playfield[0][2] == playfield[2][0]) :
		return 1
	for i in range(3):
		for j in range(3):
			if playfield[i][j] == 0:
				return -1
	return 0

def moveAI(playfield, currentPlayer):
	moves = []
	for i in range(3):
		for j in range(3):
			if playfield[i][j] == 0:
				move = [i, j]
				moves.append(move)
	
	if currentPlayer == 1:
		bestScore = -10000000000000
	else:
		bestScore = 10000000000000
	bestMove = None
		
	for move in moves:
		newPlayfield = copy.deepcopy(playfield)
		line, col = move
		newPlayfield[line][col] = currentPlayer + 1
		score = checkGameState(newPlayfield, line, col)
		if score == -1:
			score, _ = moveAI(newPlayfield, (currentPlayer + 1) % 2)
		elif score == 1:
			if currentPlayer == 0:
				score = -1
		if currentPlayer == 1:
			if score > bestScore:
				bestScore = score
				bestMove = move
		else:
			if score < bestScore:
				bestScore = score
				bestMove = move
		
	return bestScore, bestMove

def Skynet(playfield):
	_, move = moveAI(playfield, 1)
	return move
	
def runGame():
	print('New Game\n')
	playfield = [
		[0,0,0],		
		[0,0,0],
		[0,0,0]
	]
	currentPlayer = 0
	
	while True:
		showPlayfield(playfield)
		if currentPlayer == 0:
			playerName = "X"
			move = input("Enter your move, X:")
			if (move == 'quit') or (move == 'q'):
				return False
			
			if move == "win":
				print('You Won!')
				continue
			
			if len(move) != 2:
				print('Illegal move!')
				continue
			
			if move == "c4":
				print("BOOM!")
				continue
			line = getLine(move[1])
			col = getColumn(move[0])
		else:
			playerName = "Skynet"
			line, col = Skynet(playfield)
		
		if (line == -1) or (col == -1):
			print('Illegal move!')
			continue
			
		if playfield[line][col] != 0:
			print('Illegal move!')
			continue
			
		playfield[line][col] = currentPlayer + 1
		result = checkGameState(playfield, line, col)
		if result == 0:
			print("Draw")
			break
		elif result == 1:
			print(playerName + " has won!")
			break
		else:
			pass
		currentPlayer = (currentPlayer + 1) % 2
	return True
		
def main():
	while True:
		if not runGame():
			return
	
main()