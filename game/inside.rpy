label indoors:

    you "Let's stay home, Leafy."

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

        

    return






label book: