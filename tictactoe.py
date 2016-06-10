boardstatus = {'tl':' ', 'tm':' ', 'tr':' ', 'ml':' ', 'mm':' ', 'mr':' ', 'bl':' ', 'bm':' ', 'br':' '}

isWinner = False

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
		
# 	else:
# 		print "Not a win yet."
		
# def validentry(player_move):
	
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
	
	while True:
	
		player1_move1 = raw_input('Player 1, where would you like to place your first X? ').lower()
		while player1_move1 not in boardstatus:
			player1_move1 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
		boardstatus[player1_move1] = 'X'
		gameboard()

		player2_move1 = raw_input("Player 2, where would you like to place your first O? ").lower()
		while player2_move1 not in boardstatus or player2_move1 == player1_move1:
			if player2_move1 not in boardstatus:
				player2_move1 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player2_move1 == player1_move1:
				player2_move1 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player2_move1] = 'O'
		gameboard()

		player1_move2 = raw_input("Player 1, where would you like to place your second X? ").lower()
		while player1_move2 not in boardstatus or player1_move2 in (player1_move1, player2_move1):
			if player1_move2 not in boardstatus:
				player1_move2 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player1_move2 in (player1_move1, player2_move1):
				player1_move2 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player1_move2] = 'X'
		gameboard()
		
		player2_move2 = raw_input("Player 2, where would you like to place your second O? ").lower()
		while player2_move2 not in boardstatus or player2_move2 in (player1_move1, player2_move1, player1_move2):
			if player2_move2 not in boardstatus:
				player2_move2 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player2_move2 in (player1_move1, player2_move1, player1_move2):
				player2_move2 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player2_move2] = 'O'
		gameboard()
		
		player1_move3 = raw_input("Player 1, where would you like to place your third X? ").lower()
		while player1_move3 not in boardstatus or player1_move3 in (player1_move1, player2_move1, player1_move2, player2_move2):
			if player1_move3 not in boardstatus:
				player1_move3 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player1_move3 in (player1_move1, player2_move1, player1_move2, player2_move2):
				player1_move3 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
 		else:
 			boardstatus[player1_move3] = 'X'
		gameboard()

		player_wins()
		if isWinner:
			break

		player2_move3 = raw_input("Player 2, where would you like to place your third O? ").lower()
		while player2_move3 not in boardstatus or player2_move3 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3):
			if player2_move3 not in boardstatus:
				player2_move3 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player2_move3 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3):
				player2_move3 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player2_move3] = 'O'
		gameboard()

		player_wins()
		if isWinner:
			break
	
		player1_move4 = raw_input("Player 1, where would you like to place your fourth X? ").lower()
		while player1_move4 not in boardstatus or player1_move4 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3, player2_move3):
			if player1_move4 not in boardstatus:
				player1_move4 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player1_move4 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3, player2_move3):
				player1_move4 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player1_move4] = 'X'
		gameboard()
		
		player_wins()
		if isWinner:
			break
			
		player2_move4 = raw_input("Player 2, where would you like to place your last O? ").lower()
		while player2_move4 not in boardstatus or player2_move4 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3, player2_move3, player1_move4):
			if player2_move4 not in boardstatus:
				player2_move4 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player2_move4 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3, player2_move3, player1_move4):
				player2_move4 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player2_move4] = 'O'
		gameboard()
		
		player_wins()
		if isWinner:
			break
			
		player1_move5 = raw_input("Player 1, where would you like to place your last X? ").lower()
		while player1_move5 not in boardstatus or player1_move5 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3, player2_move3, player1_move4, player2_move4):
			if player1_move5 not in boardstatus:
				player1_move5 = raw_input('That is not a valid entry. Please try a different spaces. ').lower()
				continue
			elif player1_move5 in (player1_move1, player2_move1, player1_move2, player2_move2, player1_move3, player2_move3, player1_move4, player2_move4):
				player1_move5 = raw_input("That space has already been taken. Please select another space. ").lower()
				continue
		else:
			boardstatus[player1_move5] = 'X'
		gameboard()
		
		player_wins()
		if isWinner:
			break
		else:
			print "Looks like the cat won this game. Better luck next time!"
			break
# 		 
# 	else:
# 		play_again = raw_input("Would you like to play again? Y or N \n")
# 
# 		if play_again in ["y", "Y", "yes", "YES"]:
# 			tictactoe()			
# 	
# 		else:
# 			print "Ciao!"
			
tictactoe()