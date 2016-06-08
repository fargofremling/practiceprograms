
game_moves = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
player1_input = ' '

#def player1_moves():

#	player1_input = raw_input("Player 1, where would you like to place your first X? ").lower
	
	#for player1_input:
# 	if player1_input == "tl":
# 		game_moves[0] = 'X'
# 	
# 	elif player1_input == "tm":
# 		game_moves[1] = 'X'
# 
# 	elif player1_input == "tr":
# 		game_moves[2] = 'X'
# 	
# 	elif player1_input == "ml":
# 		game_moves[3] = 'X'
# 	
# 	elif player1_input == "mm":
# 		game_moves[4] = 'X'
# 	
# 	elif player1_input == "mr":
# 		game_moves[5] = 'X'
# 	
# 	elif player1_input == "bl":
# 		game_moves[6] = 'X'
# 	
# 	elif player1_input == "bm":
# 		game_moves[7] = 'X'
# 	
# 	elif player1_input == "br":
# 		game_moves[8] = 'X'
# 
# 	else:
# 		player1_move1 = raw_input("That is not a valid entry. Please try a different locations. ").lower()
# 		
# 	gameboard()
	
def gameboard():
	
	print game_moves[0],"|",game_moves[1], "|", game_moves[2]
	print "---------"
	print game_moves[3],"|",game_moves[4], "|", game_moves[5]
	print "---------"
	print game_moves[6],"|",game_moves[6], "|", game_moves[8]
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
	
	#player1_move1()
	
	player1_move1 = raw_input("Player 1, where would you like to place your first X? ").lower()
	#if player1_move1 in ["tl", "tm", "tr", "ml", "c", "mr", "bl", "bm", "br"]:
	#player1_move1 = player1_input
	#player1_moves()
	
	while True:
		if player1_move1 == "tl":
			game_moves[0] = 'X'
			break
	
		elif player1_move1 == "tm":
			game_moves[1] = 'X'
			break

		elif player1_move1 == "tr":
			game_moves[2] = 'X'
			break
	
		elif player1_move1 == "ml":
			game_moves[3] = 'X'
			break
	
		elif player1_move1 == "mm":
			game_moves[4] = 'X'
			break
	
		elif player1_move1 == "mr":
			game_moves[5] = 'X'
			break
	
		elif player1_move1 == "bl":
			game_moves[6] = 'X'
			break
	
		elif player1_move1 == "bm":
			game_moves[7] = 'X'
			break
	
		elif player1_move1 == "br":
			game_moves[8] = 'X'
			break
			
		else:
			player1_move1 = raw_input("That is not a valid entry. Please try a different locations.").lower() 
			continue
		
	gameboard()
	
	player2_move1 = raw_input("Player 2, where would you like to place your first O? ").lower()
	while True:	
		if player2_move1 == player1_move1:
			player2_move1 = raw_input("That space has already been taken. Please select another space. ").lower() 		
			continue
			
		elif player2_move1 == "tl":
			game_moves[0] = 'O'
			break

		elif player2_move1 == "tm":
			game_moves[1] = 'O'
			break
	
		elif player2_move1 == "tr":
			game_moves[2] = 'O'
			break

		elif player2_move1 == "ml":
			game_moves[3] = 'O'
			break

		elif player2_move1 == "mm":
			game_moves[4] = 'O'
			break

		elif player2_move1 == "mr":
			game_moves[5] = 'O'
			break

		elif player2_move1 == "bl":
			game_moves[6] = 'O'
			break

		elif player2_move1 == "bm":
			game_moves[7] = 'O'
			break

		elif player2_move1 == "br":
			game_moves[8] = 'O'
			break

		else:
			player2_move1 = raw_input("That is not a valid entry. Please try a different locations.").lower()
			continue
			 
	gameboard()
	
	player1_move2 = raw_input("Player 1, where would you like to place your second X? ").lower()
	
	while True:
		if player1_move2 == player1_move1 or player1_move2 == player2_move1:
			player1_move2 = raw_input("That space has already been taken. Please select another space. ").lower() 		
			continue
		
		elif player1_move2 == "tl":
			game_moves[0] = 'X'
			break

		elif player1_move2 == "tm":
			game_moves[1] = 'X'
			break

		elif player1_move2 == "tr":
			game_moves[2] = 'X'
			break

		elif player1_move2 == "ml":
			game_moves[3] = 'X'
			break

		elif player1_move2 == "mm":
			game_moves[4] = 'X'
			break

		elif player1_move2 == "mr":
			game_moves[5] = 'X'
			break

		elif player1_move2 == "bl":
			game_moves[6] = 'X'
			break

		elif player1_move2 == "bm":
			game_moves[7] = 'X'
			break

		elif player1_move2 == "br":
			game_moves[8] = 'X'
			break
		
		else:
			player1_move2 = raw_input("That is not a valid entry. Please try a different locations.").lower() 
			continue
		
	gameboard()
				
tictactoe()



#def movecheck():
	
#def usermoves():
	
#	game_moves = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
	
#	move0 = raw_input(" ").lower()
#		if move0 in ["tl", "tm", "tr", "ml", "c", "mr", "bl", "bm", "br"]:
 #           continue
        
  #      else:
   #         print "That isn't a legal move. Please try a different space."
    #        break
            
#	move1 = raw_input(" ").lower()
#	move2 = raw_input(" ")
#	move3 = raw_input(" ")
#	move4 = raw_input(" ")
#	move5 = raw_input(" ")
#	move6 = raw_input(" ")
#	move7 = raw_input(" ")
#	move8 = raw_input(" ")
	
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
