label outdoors:
    
    you "Let's head outside."
    you "I'm kinda sick of staying in here all the time."
    l "Great! We can finally go out and enjoy the warm weather."
    
    "I grin, and turn my head to the door, as Leafy runs out and I follow suit."

    scene black with fade
    scene city with fade

    show leafy

    "It doesn't take long for Leafy and I to go outside and enjoy the sunny weather."


    "But it's not like we can be in the city forever."
    "It's almost like Leafy reads my mind, though, because he soon poses an important question."
    l "Sooooooo, there are only two really awesome places to go to in a situation like this."


    menu:
        l "D'you wanna visit the beach or walk around?"

        "Beach Day.":
            $ out_loc = "beach"
            jump beach
        "Walk around the city.":
            $ out_loc = "city"
            jump city

label beach:
    l "Beach it is!"
    l "Let's enjoy the cool vibes, buddy!"

    scene black with fade
    scene bg beach with fade

    you "We've arrived at the beach pretty quickly."

    menu:
        you "I can't tell what I'd like to do yet. Maybe we can..."
        
        "Swim":
            $ beach_activity = "swim"
            jump swim
        "Surf":
            $ beach_activity = "surf"
            jump surf

label swim:
    you "Let's go swimming."
    l "Ooh, I didn't know you could swim!"
    l "My favorite stroke is butterfly. What's yours?"
    you "I like freestyle."

    "We swim for a few hours before getting exhausted."

    l "I'm hungry."
    you "Yeah, me too."

    menu:
        l "What should we eat?"
        "Get smoothie bowl":
            $ beach_food = "smoothie"
            jump smoothie
        "Get Jersey Mike's sub":
            $ beach_food = "sub"
            jump sub

label surf:
    l "Let's go surfing."
    l "I see a huge wave coming. Let's go shred it!"

    "We surf for a few hours before getting exhausted."

    l "I'm hungry."
    you "Yeah, me too."
    menu:

        "Get smoothie bowl":
            $ beach_food = "smoothie"
            jump smoothie
        "Get Jersey Mike's sub":
            $ beach_food = "smoothie"
            jump sub

label smoothie:
    l "I'm hungry, let's get food!"
    scene playa bowls with fade
    l "Which one are you getting? I'm getting a Nutella acai bowl."
    $ renpy.call_screen("name", "Which one are you getting?")

    l "Ooh, never heard of it before. It sounds good!"
    you "Yep. Now that we've snacked, we should do something else."

    menu:
        "We should..."

        "Go beachside shopping":
            jump shopping
        "Go to fancy beachside restaurant":
            jump fancy

label sub:
    l "I'm hungry, let's get food!"
    scene mikes subs with fade
    l "What sandwich are you getting? I'm getting a BLT."
    $ renpy.call_screen("name", "What sandwich are you getting?")

    l "Ooh, never heard of it before. It sounds good!"
    you "Yep. Now that we've snacked, we should do something else."

    menu:
        "We should..."

        "Go beachside shopping":
            jump shopping
        "Go to fancy beachside restaurant":
            jump fancy 
        
label shopping:
    you "Shopping it is!"

    "We arrive at the nearest shop within a few minutes."
    scene beachside shop with fade
    # swap scene to shop
    l "Wait, I love that skirt."
    you "You should totally get it!"
    #ADD SKIRT TO LEAFY
    jump ending

label fancy:
    you "To eat! I'm starving."
    l "Didn't we just eat?"
    you "So what?"
    
    "Leafy laughs and concedes, before we head out to the restaurant to eat."
    scene fancy resturant with fade
    l "This looks delicious."
    you "Steak is the best.."
    jump ending

label city:
    l "So where are we heading first?"
    you "I'm not sure. There's the cute froyo place down the street, and a photobooth nearby. And a bunch of other places, like-"

    l "You have a lot of opinions. So, where would you like to go?"

    menu:
        "I can't tell if that was sarcastic or not. But I'll just say, let's go to the..."

        "Froyo place.":
            jump froyo
        "Photobooth.":
            jump photobooth

label froyo:
    you "Let's get froyo."
    l "I'm gonna get a vanilla froyo with gummy bears."
    you "That sounds yummy!"
    scene froyo store with fade
    "We eat for a solid hour or two, before deciding that it's time to go find another place to visit."

    menu:
        l "Now it's time for us to..."

        "Find pop-ups around the city!":
            jump popup
        "Shop at local spots!":
            jump local

label photobooth:
    you "Let's go find a photobooth!"
    l "Yay Let's figure out what poses we'll do first. And what props?!"
    scene photobooth with fade
    "There are fans, sunglasses, and so much more. It ends up being the best photo session I've had in years."

    menu:
        l "Now it's time for us to..."
        "Find pop-ups around the city":
            jump popup
        "Shop at local spots":
            jump local

label popup:
    you "Let's go to the Glossier pop-up nearby. It just opened!"
    l "That sounds fun! I hope I win a lip gloss."
    scene city with fade
    "He did not, in fact, win the lip gloss. We left with nothing besides an empty wallet from all out betting."

    menu:

        "To shake the lossess off, we decide to..."
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
        "Once we finish buying the new skirt for Leafy, we..."

        "Go to famous food spot":
            jump famous
        "Take digicam photos":
            jump digicam

label famous:
    scene daytime beach shop with fade
    you "Let's go to that spot over there. I heard about it on Instagram."
    #this is both outside the resturant
    scene night beach shop with fade
    l "That was delicious."
    jump ending

label digicam:
    scene night beach shop with fade
    you "The sunset looks beautiful, let's take some photos."
    "We take a hundred or so photos. At the end of it all, Leafy says what I was thinking."
    l "These pictures look perfect."
    jump ending
