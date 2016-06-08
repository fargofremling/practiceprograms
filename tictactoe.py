
game_moves = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']

def player1_moves(player1_input):
	
	while True:
		if player1_input == "tl":
			game_moves[0] = 'X'
			break
	
		elif player1_input == "tm":
			game_moves[1] = 'X'
			break

		elif player1_input == "tr":
			game_moves[2] = 'X'
			break
	
		elif player1_input == "ml":
			game_moves[3] = 'X'
			break
	
		elif player1_input == "mm":
			game_moves[4] = 'X'
			break
	
		elif player1_input == "mr":
			game_moves[5] = 'X'
			break
	
		elif player1_input == "bl":
			game_moves[6] = 'X'
			break
	
		elif player1_input == "bm":
			game_moves[7] = 'X'
			break
	
		elif player1_input == "br":
			game_moves[8] = 'X'
			break
			
		else:
			player1_input = raw_input("That is not a valid entry. Please try a different locations.").lower() 
			continue
			
	gameboard()
	
def player2_moves(player2_input):
	
	while True:
		if player2_input == "tl":
			game_moves[0] = 'O'
			break
	
		elif player2_input == "tm":
			game_moves[1] = 'O'
			break

		elif player2_input == "tr":
			game_moves[2] = 'O'
			break
	
		elif player2_input == "ml":
			game_moves[3] = 'O'
			break
	
		elif player2_input == "mm":
			game_moves[4] = 'O'
			break
	
		elif player2_input == "mr":
			game_moves[5] = 'O'
			break
	
		elif player2_input == "bl":
			game_moves[6] = 'O'
			break
	
		elif player2_input == "bm":
			game_moves[7] = 'O'
			break
	
		elif player2_input == "br":
			game_moves[8] = 'O'
			break
			
		else:
			player2_input = raw_input("That is not a valid entry. Please try a different locations.").lower() 
			continue
			
	gameboard()
	
def gameboard():
	
	print game_moves[0],"|",game_moves[1], "|", game_moves[2]
	print "---------"
	print game_moves[3],"|",game_moves[4], "|", game_moves[5]
	print "---------"
	print game_moves[6],"|",game_moves[7], "|", game_moves[8]
	print "\n"

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

	player1_move1 = raw_input("Player 1, where would you like to place your first X? ")
	player1_moves(player1_input = player1_move1.lower())
	
	player2_move1 = raw_input("Player 2, where would you like to place your first O? ").lower()
	
	if player2_move1 == player1_move1:
		player2_move1 = raw_input("That space has already been taken. Please select another space. ").lower() 
		player2_moves(player2_input = player2_move1.lower())		
	else:
		 player2_moves(player2_input = player2_move1.lower())

	player1_move2 = raw_input("Player 1, where would you like to place your second X? ").lower()
	
	if player1_move2 == player1_move1 or player1_move2 == player2_move1:
		player1_move2 = raw_input("That space has already been taken. Please select another space. ").lower() 
		player1_moves(player1_input = player1_move2.lower())		
	else:
		player1_moves(player1_input = player1_move2.lower())

	player2_move2 = raw_input("Player 2, where would you like to place your second 0? ").lower()
	
	if player2_move2 == player1_move1 or player2_move2 == player2_move1 or player2_move2 == player1_move2:
		player2_move2 = raw_input("That space has already been taken. Please select another space. ").lower() 
		player2_moves(player2_input = player2_move2.lower())		
	else:
		player2_moves(player2_input = player2_move2.lower())
	
	player1_move3 = raw_input("Player 1, where would you like to place your third X? ").lower()
	if player1_move3 == player1_move1 or player1_move3 == player2_move1 or player1_move3 == player1_move2 or player1_move3 == player2_move2:
		player1_moves(player1_input = player1_move3.lower())
	else:
		player1_moves(player1_input = player1_move3.lower())
	
	player2_move3 = raw_input("Player 2, where would you like to place your third O? ").lower()

	if player2_move3 ...
		player2_moves(player2_input = player2_move3.lower())
	else:
		player2_moves(player2_input = player2_move3.lower())
			
	player1_move4 = raw_input("Player 1, where would you like to place your fourth X? ").lower()

	if player1_move4 ...
		player1_moves(player1_input = player1_move4.lower())	
	else:
		player1_moves(player1_input = player1_move4.lower())	
	
	player2_move4 = raw_input("Player 2, where would you like to place your last O? ").lower()

	if player2_move4 ...
		player2_moves(player2_input = player2_move4.lower())
	else:
		player2_moves(player2_input = player2_move4.lower())	

	player1_move5 = raw_input("Player 1, where would you like to place your last X? ").lower()
	
	if player1_move5 ...
		player1_moves(player1_input = player1_move5.lower())	
	else:
		player1_moves(player1_input = player1_move5.lower())	

tictactoe()

# if player2_move3 == player1_move1 or player2_move3 == player2_move1 or player2_move3 == player1_move2 or player2_move3 == player2_move2 or player2_move3 == player1_move3:
# 			player1_move3 = raw_input("That space has already been taken. Please select another space. ").lower() 		
# 			continue

#def movecheck():
	
#def usermoves():
	
#	game_moves = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
	
#	move0 = raw_input(" ").lower()
#		if move0 in ["tl", "tm", "tr", "ml", "c", "mr", "bl", "bm", "br"]:
 #           continue
        
  #      else:
   #         print "That isn't a legal move. Please try a different space."
    #        break

	
#	game_moves = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
#	TL = game_moves[0]
#	TM = game_moves[1]
#	TR = game_moves[2]
#	ML = game_moves[3]
#	MM = game_moves[4]
#	MR = game_moves[5]
#	BL = game_moves[6]
#	BM = game_moves[7]
#	BR = game_moves[8]
