'''
Name: Garrett Helms
File: chrono_bound.py
Date: May 24th 2024

Purpose: to create a text-based action game in a a/b decision format

'''
#welcoming text
welcome = input("""Welcome to ChronoBound. before we begin, it is recommended that you increase the terminal 
                window to accomodate the text prompts. press ENTER once you've done this  """)

#prompts user for name
mc_name = input("What is your name?")

#prompts user for gender
gender = input(" \nAre you a boy or a girl?")

#create an empty sibling variable
sibling = ""

#assign sibling gender 
if gender.lower() == "boy":
    sibling = "brother"

else: sibling = "sister"

#introduction paragraph
intro = print(f""" \n \n ChronoBound
              
              It's a hot summer day. You're riding in a moving truck with your dad.

              \"Supposed to cool down later with the stormfront coming in. That's what
                 they said on the radio anyway. Hey, {mc_name}! Look! We're almost there!\"

             Up ahead, you see a rolling countryside surrounded by a canopy of trees.

             near the edge of the woods you can make out the roof of an old House.

""")

#while loop ensures proper input 
while True:
 decision_1 = input( """  \n What do you do? (type the letter A or B)

             A. ask if that's the new house
             B. stay silent \n
""")

 if decision_1.upper() == "A":
    # Special dialogue for decision A
    scenario_1 = input(""" \n Sure is! Here, take a look through my spyglass.
                       careful though! Don't SPY the sun, it'll blind ya!

                       OBTAINED THE SPYGLASS. \n
""")
    break
 elif decision_1.upper() == "B":
     # Continue as if nothing happened
     break
 else: 
    # Handle unexpected input and re-prompt
    print("Invalid decision. Please choose either A or B.")

#second scene, beginning of branching paths
scene_2 = print(f"""\n After a while, the moving truck slowly makes its way
                down the gravel driveway, rattled and tossed about by several potholes.
                Sure enough, its begun to rain, and as the truck pulls into the turnaround,
                you can see puddles filling up the potholes in the gravel.
                
                outside, your Mom and Sister, who have been following the moving truck in their Van,
                are already outside. You're sister is dressed in a yellow raincoat and jumping in the puddles.

                She looks up at you and grins.
                
                \"Hey! Big {sibling}! look at all these oceans! Come on lets make waves!\"    """)

decision_2 = input("""  \n What do you do? (type PLAY or LEAVE)
                   
                   1. PLAY with sister in the puddles
                   
                   2. LEAVE to go towards house""")

scene_3a = ""

scene_3b = ""

if decision_2.lower() == "play":
   
  scene_3a = print(f""" \n \"Yeah! this'll be fun!\" your sister yells, and splashes into an even bigger puddle.
                  
                  You both jump and splash in the rain, little sister yelling about some pirate king and his treasured gold, 
                  sweeping her jacket back like the cloak of some Sea Baron.
                  
                  Suddenly, little sister stops and stares at a puddle near the edge of the driveway. 
                  
                  \"Look {mc_name}, what is that!?\"
                       
                    From the seemingly shallow puddle, a massive salamander-like creature suddenly emerges! 
                    As it slowly pulls itself from the puddle, its dull eyes reflecting off the water, you
                         estimate it to be over 2 feet long!
                    
                    it suddenly rears up and looks at the two of you, and in a blinding flash begins crawling away!
                    
                 \"C'mon let's catch it!\" Your sister says.
            
                """)
  decision_3 = input("""\n What do you do? (type FOLLOW or STAY)
                   
                   1. FOLLOW strange creature with sister
                   
                   2. STAY put and see what happens """)
  if decision_3.lower() == "follow":
    scene_5a = print(f""" You both race after the salamander thing, trampling down a narrow and muddy pathway.""")
  elif decision_3 == "stay":
        scene_5b = print(f""" \n You decide to stay put, watching as the creature disappears into the underbrush.""")
  

 #the player chooses the "LEAVE" option
elif decision_2.lower() == "leave":
   scene_3b = print(f"""You head towards the house, ignoring your sister. 
                    
                    \"Hey! No fair! Fine, I'll catch pirates by myself!\" she says.

                    She begins an imaginative game of pirates, throwing her cloak around and shouting incoherent pirate words 
                    without knowing their meaning. 
                    
                    You walk into the house and see your dad is moving furniture into the house.
                    
                    \"{mc_name}! I thought you were watching your sister! Remember we're in a new place and that 
                    IMAGINATION of her's tends to lead her wandering off. But if you're mother's watching her, mind helping
                    me bring this furniture in?\" 
                    """)
   decision_4 = input("""\n What do you do? (type LIE or CONFESS)
                   
                   1. LIE and say Mom's watching little sister
                   
                   2. CONFESS that you left her alone """) 
    
   if decision_4.lower() == "confess":
    scene_4a = print(f""" \"Thanks for being honest with me {mc_name}, now go outside and check on your sister \" """)
   elif decision_4.lower() == "lie":
    scene_4b = print(f""" \"Great! come help me lift this couch\" 
                    You go and lift the couch; a small, sinking feeling settling in about your sisters satefy. You ignore it. """)
   
else:
    # Handle unexpected input and re-prompt
    print("Invalid decision. Please choose either PLAY or LEAVE.")
    



