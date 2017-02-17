#Chess

# Calculate the possible moves
def possibleMoves(cur):
	moves = []

	ver = cur / 8
	hor = cur % 8

	# Up move
	if ver - 2 >= 0:
		# Up Left
		if hor - 1 >= 0:
			moves += [(ver - 2) * 8 + (hor - 1)]
		# Up Right
		if hor + 1 <= 7:
			moves += [(ver - 2) * 8 + (hor + 1)]

	# Down move
	if ver + 2 <= 7:
		# Down Left
		if hor - 1 >= 0:
			moves += [(ver + 2) * 8 + (hor - 1)]
		# Down Right
		if hor + 1 <= 7:
			moves += [(ver + 2) * 8 + (hor + 1)]

	# Left move
	if hor - 2 >= 0:
		# Left Up
		if ver - 1 >= 0:
			moves += [(ver - 1) * 8 + (hor - 2)]
		# Left Down
		if ver + 1 <= 7:
			moves += [(ver + 1) * 8 + (hor - 2)]

	# Right move
	if hor + 2 <= 7:
		# Right Up
		if ver - 1 >= 0:
			moves += [(ver - 1) * 8 + (hor + 2)]
		# Right Down
		if ver + 1 <= 7:
			moves += [(ver + 1) * 8 + (hor + 2)]

	return moves

# Calc distance from Destination
def dist(mov,dst):
	ver = mov / 8
	hor = mov % 8
	verd = dst / 8
	hord = dst % 8
	return (abs(ver) - abs(verd)) + (abs(hor) - abs(hord))

# Remove "bad" moves
def heuristic(moves, dst):
	for i in moves:
		if dist(i,dst) <= 2:
			moves.remove(i)

	return moves

# Initialize the board
board = [[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' '],
				[' ',' ',' ',' ',' ',' ',' ',' ']]

# Print the current state of the board
def printBoard(board):
	print "\n     0     1     2     3     4     5     6     7   ",
	for i in range(8):
		for j in range(8):
			if j == 0:
				print "\n", i, "| ",
			print board[i][j], " | ",
		print "\n---------------------------------------------------"
	print "\n"

src = 0
dst = 1
board[src/8][src%8] = 'S'
board[dst/8][dst%8] = 'D'
#src = int(raw_input())
#dst = int(raw_input())

done = False
cur = src
numMoves = 0

while not(done):
	# Calculate possible moves
	moves = possibleMoves(cur)

	# Display possible moves
	#for i in moves:
	#	board[i/8][i%8] = 'X'

	# Apply heuristic
	moves = heuristic(moves, dst)

	# TODO: Make Move
	numMoves += 1

	if cur == dst:
		done = True

	printBoard(board)

print numMoves