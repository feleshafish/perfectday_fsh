label outdoors:
    
    l "Let's head outside."
    scene city with fade
    menu:

        "Beach Day.":
            jump beach
        "Walk around the city.":
            jump city
label beach:
    l "Let's drive to the beach!"
    scene bg beach with fade
    menu:
        
        "Swim":
            jump swim
        "Surf":
            jump surf

label swim:
    l "Let's go swimming."
    l "My favorite stroke is butterfly. What's yours?"
    you "I like freestyle."
    menu:

        "Get smoothie bowl":
            jump smoothie
        "Get Jersey Mike's sub":
            jump sub

label surf:
    l "Let's go surfing."
    l "I see a huge wave coming. Let's go shred it!"
    menu:

        "Get smoothie bowl":
            jump smoothie
        "Get Jersey Mike's sub":
            jump sub

label smoothie:
    l "I'm hungry, let's get food!"
    l "Which one are you getting? I'm getting a Nutella acai bowl."
    $ renpy.call_screen("name", "Which one are you getting?")
    menu:
        "Go beachside shopping":
            jump shopping
        "Go to fancy beachside restaurant":
            jump fancy

label sub:
    l "I'm hungry, let's get food!"
    l "What sandwich are you getting? I'm getting a BLT."
    $ renpy.call_screen("name", "What sandwich are you getting?")
    menu:
        "Go beachside shopping":
            jump shopping
        "Go to fancy beachside restaurant":
            jump fancy
        
label shopping:
    you "Shopping!"
    # swap scene to shop
    l "Wait, I love that skirt."
    you "You should totally get it!"
    #ADD SKIRT TO LEAFY
    jump ending

label fancy:
    you "To eat! I'm starving"
    l "This looks delicious."
    you "Steak is the best.."
    jump ending

label city:
    l "So where are we heading first?"
    menu:
        "Froyo":
            jump froyo
        "Photobooth":
            jump photobooth

label froyo:
    you "Let's get froyo"
    l "I'm gonna get a vanilla froyo with gummy bears."
    you "That sounds yummy!"
    menu:
        "Find pop-ups around the city":
            jump popup
        "Shop at local spots":
            jump local

label photobooth:
    you "Let's go find a photobooth!"
    l "Yay Let's figure out what poses we'll do first. And what props?!"
    menu:
        "Find pop-ups around the city":
            jump popup
        "Shop at local spots":
            jump local

label popup:
    you "Let's go to the Glossier pop-up nearby. It just opened!"
    l "That sounds fun! I hope I win a lip gloss."
    menu:
        "Go to famous food spot":
            jump famous
        "Take digicam photos":
            jump digicam

label local:
    l "I see a store over there, let's go check it out!"
    l "Wait, I love the skirt."
    you "You should totally get it."
    # ADD SKIRT TO LEAFY
    menu:
        "Go to famous food spot":
            jump famous
        "Take digicam photos":
            jump digicam
label famous:
    you "Let's go to that spot over there. I heard about it on Instagram."
    #this is both outside the resturant
    l "That was delicious."
    jump ending

label digicam:
    you "The sunset looks beautiful, let's take some photos"
    l "These pictures look perfect"
    jump ending
