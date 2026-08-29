label indoors:

    you "Let's stay home, Leafy."

    scene bg living with fade

    menu:

        l "Sure! What do you want to do now?"

        "Watch a movie":
            jump movie
        "Read a book":
            jump book
    


label movie:


    l "Awesome. What movie would you like to watch together?"

    $ movie_name = renpy.call_screen("name", "What movie are you guys watching?")
    $ movie_name = movie_name.strip()

    if not movie_name:
        $ movie_name = "Interstellar"

    you "I want to watch [movie_name]! I want to do something else too, though."

    menu:

        "Make popcorn":
            jump popcorn

        "Draw":
            jump draw


label popcorn:

    you "I'm hungry. Let's make popcorn."

    l "I have the pan ready. Put the kernels in!"

    you "Let's add LOTS of butter."

    jump movie2

label draw: 

    $ art_name = renpy.call_screen("name", "What are you drawing?")
    $ art_name = art_name.strip()

    if not art_name:
        $ art_name = "cat"
        
    you "I want to draw [art_name]!"

    jump movie2


label movie2:

    l "What do you want to do now?"

    menu: 

        "Listen to music while crocheting":
            jump crochet

        "Make Buldak":
            jump buldak

        "Make Sourdough":
            jump sourdough

label crochet:

    l "I'll find a pattern for you, I guess..."

    jump lunch

label buldak:

    l "Oh my gosh, I love Buldak noodles! Let's make it."
    you "You're a leaf... How do you like Buldak (or eat it)?"
    l "..."

    jump lunch

label sourdough:

    l "You have a sourdough starter?"
    you "Yup. Wanna feed it?"

    jump lunch
    
label lunch:
    scene bg living with fade
    l "Now that we've done that, let's go out to eat. Whatcha craving?"
    
    menu: 

        "A niche spot":
            jump niche

        "Go to Thai Diner":
            jump thai


label niche:
    you "I saw this super niche spot on the way back!"

    scene bg city with fade

    l "Wow, that food was pretty good considering that the restaurant wasn't very packed."

    jump ending

label thai:
    you "I'm really craving some Thai food right now... Wanna get? Let's go get some mango sticky rice too!"
    l "For sure. I love mangos!"






label book: