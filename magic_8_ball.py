import random

print "Give me a quarter, and I'll tell you your fortune."

raw_input("Or you could just ask a question. \n> ")

def magic_eight():
    while True:
        response = ["Huh?",
                    "Speak up! I can't hear you!",
                    "BINGO!",
                    "Dumb question.",
                    "Reception poor. Try again later.",
                    "You really don't want to know the answer, so I'm just going to pretend you didn't ask that.",
                    "Maybe?",
                    "Hell yes!",
                    "Sure",
                    "Yepper!",
                    "You know it!",
                    "If you're lucky.",
                    "Green means go.",
                    "Eh",
                    "Could be.",
                    "Fuck no.",
                    "No, no, no.",
                    "Yeah, and monkeys might fly out of my butt.",
                    "Outlook not so good. Actually, outlook quite awful.",
                    "Doubtful"]
            
        print (random.choice(response))
        
        print "Would you like ask another question? Y or N"
        another_question = raw_input("> ").lower()
                
        if another_question in ["y", "yes"]:
            raw_input("Ask away! \n> ")
            continue
        elif another_question in ["n", "no"]: 
            print "Later alligator!"
            break        
        else:
            print "Hmm, that wasn't Y or N. I'm going to assume you meant Y."
            raw_input("What is your next question? \n> ")
            continue

magic_eight()
