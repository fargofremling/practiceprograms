boardstatus = {'tl':' ', 'tm':' ', 'tr':' ', 'ml':' ', 'mm':' ', 'mr':' ', 'bl':' ', 'bm':' ', 'br':' '}

isWinner = False

player_name = " "

# draws the board
def gameboard():

	print boardstatus['tl'],"|",boardstatus['tm'], "|",boardstatus['tr']
	print "---------"
	print boardstatus['ml'],"|",boardstatus['mm'], "|",boardstatus['mr']
	print "---------"
	print boardstatus['bl'],"|",boardstatus['bm'], "|",boardstatus['br']
	print "\n"

# winning logic
def player_wins():
	global isWinner
	if boardstatus['mm'] == 'X' or boardstatus['mm'] == 'O':
	
		if boardstatus['ml'] == boardstatus['mm'] and boardstatus['mm'] == boardstatus['mr']:
			print "Nice job; you've won!"
			isWinner = True
		
		elif boardstatus['tl'] == boardstatus['mm'] and boardstatus['mm'] == boardstatus['br']: 
			print "Well done; you've won!"
			isWinner = True
			
		elif boardstatus['tr'] == boardstatus['mm'] and boardstatus['mm'] == boardstatus['bl']: 
			print "Good move; you've won!"
			
			isWinner = True
		elif boardstatus['tm'] == boardstatus['mm'] and boardstatus['mm'] == boardstatus['bm']:  
			print "Sweet! You've won!"
			isWinner = True
	
	if boardstatus['tl'] == 'X' or boardstatus['tl'] == 'O':
	
		if boardstatus['tl'] == boardstatus['tm'] and boardstatus['tm'] == boardstatus['tr']:
			print "Congratulations, you've won!"
			isWinner = True
	
		elif boardstatus['tl'] == boardstatus['ml'] and boardstatus['ml'] == boardstatus['bl']:  
			print "Rock on; you've won!"
			isWinner = True
	
	if boardstatus['br'] == 'X' or boardstatus['br'] == 'O':
	
		if boardstatus['bl'] == boardstatus['bm'] and boardstatus['bm'] == boardstatus['br']:
			print "Well played; you've won!"			
			isWinner = True
			
		elif boardstatus['tr'] == boardstatus['mr'] and boardstatus['mr'] == boardstatus['br']:  
			print "Look at you, Player 1; you've won!"
			isWinner = True

# used to determine what moves are valid and available (i.e. not already played on the board)
def available_moves():
	# list comprehension
	return [key for key,value in boardstatus.iteritems() if value == ' '] 

# personalized prompt for Player 1 (X) and Player 2 (O) 
def prompt_player(player_name, game_marker):
	
	string ="{}, where would you like to place your {}? ".format(player_name, game_marker)
	player_move = raw_input(string).lower()
	return player_move

# main game function	
def tictactoe():

	print "Welcome to Tic Tac Toe."
	print "Your move options are:\n"
	print "Top Left: TL"
	print "Top Middle: TM"
	print "Top Right: TR"
	print "Middle Left: ML"
	print "Middle Middle: MM"
	print "Middle Right: MR"
	print "Bottom Left: BL"
	print "Bottom Middel: BM"
	print "Bottom Right: BR\n"

	print "TL|TM|TR"
	print "---------"
	print "ML|MM|MR"
	print "---------"
	print "BL|BM|BR"
	print "\n"
	gameboard()
	
	names = ["Player 2", "Player 1"]
	markers = ["O", "X"]
	turn_number = 1 
	
	# since there can only be 9 moves in a tic-tac-toe game
	while turn_number != 10:

		player_name = names[turn_number % 2]
		game_marker = markers[turn_number % 2]
		
		move = prompt_player(player_name, game_marker)
		
		while move not in available_moves():
			move = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
			
		
		boardstatus[move] = 'X' if turn_number % 2 else 'O'
		
		gameboard()
		
		player_wins()
		if isWinner:
			break
		
		turn_number += 1		

	if turn_number == 10:	
		print "Looks like the cat won this game. Better luck next time!"

# want to work in a prompt to ask "play again?"		 
# 	else:
# 		play_again = raw_input("Would you like to play again? Y or N \n")
# 
# 		if play_again in ["y", "Y", "yes", "YES"]:
# 			tictactoe()			
# 	
# 		else:
# 			print "Ciao!"
			
tictactoe()