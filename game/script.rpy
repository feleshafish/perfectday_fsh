# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character(_("Leafy"), color="#49ec36")
define you = Character(_("[player_name]"), color="#74b7f2")


# character variables

default my_name = ""

default journal_text = ""

default setting = 0


# page flip sound effect credits:Sound Effect by Alex from Pixabay Sound Effect by <a href="https://pixabay.com/users/oxidvideos-37598254/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=178322">Alex</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=178322">Pixabay</a>

# The game starts here.

label start:

    $ player_name = renpy.call_screen("name", "Nice to meet you! What is your name?")
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Gerald"

    $ name = my_name
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with fade

    "The morning comes slowly, like any other day."
    "I raise my head to gaze at the sun shining down."
    "Today will probably be another drag. Another day of cramming assignments, of running to work right after said assignments, of-"

    l "Rise and shine, [player_name]! Your perfect day awaits!"

    "..."

    you "What?"

    "A little leaf-like creature pops up in front of me and grins."

    show leafy with vpunch

    l "I'm Leafy, your new assistant, and you can count on me to make TODAY the BEST DAY EVER!"
    l "Whaddya say?"

    you "I don't even know you, dude."

    l "That doesn't matter! I'm gonna make your day awesome anyways. You look like you have a free schedule!"

    you "I don't."

    "Leafy shrugs."

    l "Well, ya do now! You can do anything!"
    you "Seriously?"
    l "Yeah! All I need you to do, though, is to journal whatever you do. That way you have records of your perfect day going just as planned!"
    you "How?"
    l "Press the 'J' key, or your \"Journal\" button down below to do it! Write away!"
    l "And now for the fun part..."
    l "Select whatever you'd like to do until your day is filled with 5 events. The final event is journaling!"

    you "Mhm..."

    menu:

        l "So, what would you like to do first on your dream day?"

        "Go outside.":
            $ setting = 1
            jump outdoors
        "Stay home.":
            $ setting = 2
            jump indoors



    return

label ending:
    scene bg room with fade
    "Goes back home to bedroom"
    you "That was a perfect day."
    l "Let's look back at the journals to see what we did today!"
    you "Wow, today was amazing."
    l "Perhaps I'll meet you again on your next perfect day. Sweet dreams, [player_name]"
    "Your eyes go dark..."
    scene bg black with fade