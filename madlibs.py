'''
Name: Garrett Helms
File: madlibs.py
Date: April 30th 2024
Purpose: to create a madlibs game

'''
#text to welcome the player
begin_game = print("Welcome to the Madlibs Game! to play, enter your words and watch the hilarity ensue! \n")

#player inputs words
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")

#first output story with player's words
first_story = print(f""" All right! here's the first story:
                    
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. \"{exclamation.title()}!\" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.  """)

#player inputs words for second story
second_phase = print("\n Let's keep the game going! add some more hilarious words to your story! \n")

adjective2 = input("adjective: ")
animal2 = input("animal: ")
verb4 = input("verb: ")
exclamation2 = input("exclamation: ")
verb5 = input("verb: ")
verb6 = input("verb: ")

#output for second story, keeps original animal with adjective
second_story = print(f""" Sounds good! let's continue the story:
                    
At this point, I was really confused. What is a {adjective} {animal} 
doing here anyways? But then, all of the sudden, a {adjective2} {animal2} comes and does a 
 {verb4} out of nowhere! \"{exclamation2.title()}!\" I shouted at them, but they where
too busy trying to {verb5} each other. My family finally had to {verb6}
before things got too crazy.  """)



