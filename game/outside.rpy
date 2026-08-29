label outdoors:
    
    l "Let's head outside."
    menu:

        "Beach Day.":
            jump beach
        "Walk around the city.":
            jump city
label beach

    l "Let's drive to the beach!"
    menu:
        
        "Swim":
            jump swim
        "Surf":
            jump surf

label swim
    l "Let's go swimming."
    l "My favorite stroke is butterfly. What's yours?"
    you "I like freestyle."
    menu:

        "Get smoothie bowl":
            jump smoothie
        "Get Jersey Mike's sub":
            jump sub

label surf
    l "Let's go surfing."
    l "I see a huge wave coming. Let's go shred it!"
    menu:

        "Get smoothie bowl":
            jump smoothie
        "Get Jersey Mike's sub":
            jump sub

label smoothie
    l "I'm hungry, let's get food!"
    l "Which one are you getting? I'm getting a Nutella acai bowl."
   
    menu:
        "Go beachside shopping":
            jump shopping
        "Go to fancy beachside restaurant":
            jump fancy

label sub
    l "I'm hungry, let's get food!"
    l "What sandwich are you getting? I'm getting a BLT."

    menu:
        "Go beachside shopping":
            jump shopping
        "Go to fancy beachside restaurant":
            jump fancy
        
label s



label city