# GOAL
# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

# RULES
# 1. If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
# 2. Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# 3. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# 4. Put a blank line between each verse of the song.

def the_song():

	for bottle_count in range(99, 0, -1):

		chorus1 = "bottles of beer on the wall."
		chorus2 = "bottles of beer."
		chorus3 = "Take one down; pass it around."

		if bottle_count > 2:
			print bottle_count, chorus1, bottle_count, chorus2
			print chorus3
			print bottle_count-1, chorus1, "\n"

		elif bottle_count == 2:
			print bottle_count, chorus1, bottle_count, chorus2
			print chorus3
			print bottle_count-1, "bottle of beer on the wall.\n"

		else:
			print bottle_count, "bottle of beer on the wall.", bottle_count, "bottle of beer."
			print chorus3
			print "No more", chorus1, "\n"
			print "No more", chorus1, "No more", chorus2
			print "Go to the store and buy some more."
			print "99 bottles of beer on the wall.\n"

the_song()