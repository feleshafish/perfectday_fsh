label indoors:
    show leafy

    you "Let's stay home, Leafy."
    l "Homebody much? Seriously, you really have some..."
    "I shoot Leafy a deadpan stare."
    l "Uh. Perfect taste!" 
    l "We might wanna leave your bedroom, though. No point in staying in {i}here{/i} all day!"
    you "Yeah, I guess you have a point."

    scene bg living with fade
    play music "indoorsmusic.mp3" fadein 0.5 volume 0.4

    "Leafy has to rush after me as I walk to the living room."

    show leafy with vpunch

    l "Ooh, this is a cozy little place you've got! You need to direct me to your realtor."
    "I ignore the implication that this amorphous blob somehow lives somewhere, and roll my eyes."
    you "Sooo, you said this was meant to be my perfect day. What should we do now?"

    menu:
        l "I mean, we could..."

        "Watch a movie":
            jump movie
        "Read a book":
            jump book
    


label movie:
    l "Movie it is! Good choice."
    l "I always love watching movies. We can't put any TVs in my treehouse, soooo..."
    l "Go crazy! What movie would you like to watch together?"

    $ movie_name = renpy.call_screen("name", "I'd like to watch...")
    $ movie_name = movie_name.strip()

    if not movie_name:
        $ movie_name = "Interstellar"

    you "I want to watch [movie_name]! I've been reading reviews on Bluedit and Leafstagram recently and it seems cool."
    l "Classic choice! I've watched it, but I promise I won't give spoilers."

    "I shrug, and flip on the TV, making a noise of appreciation."
    "We sit through the long movie, but it was so fun that the experience feels short."
    "I get off of the couch a changed person."



    menu:
        you "Y'know, leafy, we should do something new now. I'm motivated. We can..."

        "Make popcorn":
            jump popcorn

        "Draw":
            jump draw


label popcorn:

    you "I'm seriously {i}so{/i} hungry right now. Let's make popcorn."
    l "Shouldn't we have done this before watching the movie?"
    you "Does it make a difference? Popcorn is always so good. Extra butter."
    l "I prefer caramel."
    you "To each their own."
    "Leafy laughs, and shrugs." 
    l "I have the pan ready. Put the kernels in!"

    "I don't have the time to question where he got the pan spontaneously from, before Leafy starts making up a storm."

    "When we do end up having the popcorn, it's a mess of melty, buttery goodness. And of course, Leafy has a caramel side."
    "After much wrestling, Leafy gets me to admit that caramel {i}is{/i} pretty good on popcorn."


    menu: 
        l "I'm preeeeettttttty full right now. What should we do? We've got so many options, y'know!"

        "Listen to music while crocheting":
            jump crochet

        "Make Buldak":
            you "I'm craving Buldak, honestly."
            l "..."
            l "Guess we're eating good today!"
            jump buldak

        "Make Sourdough":
            you "I'm craving sourdough, honestly."
            l "..."
            l "Guess we're eating good today!"
            jump sourdough

label draw: 

    l "Did ya know I used to be the best artist in my class?"
    you "You went to {i}school{/i}?"
    l "Well, obviously!"
    you "But- you're a-"
    "A leaf? An amorphous blob? A random entity that kinda broke into my house?"
    l "An awesome artist!"
    "I roll my eyes, and shoot a half-grin."
    you "I can assure you, I'm better."
    l "Yeah, well, what are you drawing?"

    $ art_name = renpy.call_screen("name", "I'm making a...")
    $ art_name = art_name.strip()

    if not art_name:
        $ art_name = "cat"
        
    you "I'm making a [art_name]! Isn't it beautiful?"
    l "Hm, it really is. Wow!"

    "We draw for about an hour or two before going onto the next thing."

    l "What do you want to do now?"

    menu: 
        you "I mean, I feel pretty up for..."

        "Listening to music while crocheting":
            l "Whoa, creative much?"
            you "Yup."
            jump crochet

        "Making Buldak":
            jump buldak

        "Making Sourdough":
            jump sourdough


label crochet:

    l "I'll find a pattern for you, I guess..."

    "We go through dozens after dozens of patterns on the the internet before deciding on a lopsided potato."
    "Courtesy of Leafy, not me."
    "We each make our own potato and leave it on display in my living room."

    l "It's so peak."
    you "I know."

    "I can swear leafy is holding back tears of joy."

    jump lunch

label buldak:

    l "Wow, I seriously forgot how much I love Buldak noodles. They're soooooo good."
    you "You're a leaf... or something. How do you like Buldak (or eat it)?"
    l "..."

    "Leafy doesn't speak for the rest of the meal and steals two of my noodles. I steal a mushroom right back."

    you "I sorta wanna eat again..."
    l "Yeah?"

    jump lunch

label sourdough:

    l "You have a sourdough starter?"
    you "Yup. Wanna feed it?"

    "It was then that I learned Leafy has trypophobia. That's probably why Leafy doesnt look at the stomata of the leaf on their head."

    you "Hm... now that we've made the sourdough, let's eat something with less holes."
    l "Sounds good!"

    jump lunch
    
label lunch:
    scene bg living with fade
    l "Well, now that we've done that, let's go out to eat. Whatcha craving?"
    
    menu: 

        "A niche spot":
            jump niche

        "Go to Thai Diner":
            jump thai


label niche:
    you "I saw this super niche spot on the way back!"

    scene bg city with fade

    "When I said niche, it seems Leafy didn't expect it to be so unknown that there were only two other customers besides us."

    l "Dang, that food was pretty good considering that the restaurant wasn't very packed."
    l "We should totally go again sometime!"
    you "We should. But for now, let's go home."

    jump ending

label thai:
    you "I'm really craving some Thai food right now... Wanna get? Let's go get some mango sticky rice too!"
    l "For sure. I love mangos!"
    you "Have you had sticky rice before?"
    "With Leafy's shake of the head, I laugh."
    you "You're in for the best experience of your life."

    "On our way home after eating, Leafy doesn't stop gushing over the food."


    jump ending



label book:
    you "I'm going to read a book."
    l "Yeah? Well, which one?"

    $ book_name = renpy.call_screen("name", "I'm reading...")
    $ book_name = book_name.strip()

    if not book_name:
        $ book_name = "The Art of War"

    you "I want to watch {i}[book_name]{/i}!"
    "I read the book for two hours. Leafy reads along too, almost falling asleep twice."

    l "Neat! What should we do now?"
    
    menu: 
        you "I'm thinking..."
        "Make cupcakes":
            jump cupcakes

        "Take a nap":
            jump nap


label cupcakes:
    you "Let's make cupcakes!"
    l "I'm an amazing baker. Heh."
    you "How is that possible...? You're a leaf."
    l "You'll see! Never judge a leaf by its cover."
    "Leafy does not fully mix the baking soda. Or the salt. Or anything, actually."
    you "Why is this so bitter? And- hold up- is this a {i}baked egg{/i}?!"
    l "..."
    jump book2

label nap:
    you "I'm going to take a nap."
    l "Alright, sleep well!"
    "I sleep for 3 hours, while Leafy does who-knows-what."
    you "That was a nice nap. I feel refreshed."
    l "Yippee!"
    jump book2

label book2:
    l "What do you want to do now?"

    menu: 
        you "I'm thinking..."

        "Self-care routine":
            jump selfcare

        "Make fun drinks":
            jump drinks

label selfcare:
    you "Let's do some skincare."
    l "I love this moisturizer!"
    jump hungry


label drinks:
    you "Let's make drinks! I'd love some boba right now."
    l "Ooh, I can help! I could brew some tea."
    you "You do know tea is made up of crushed up leaves, right..."

    "Leafy gets an irked look in their eyes when I mention that."
    "We don't talk about the leaves for the rest of our boba trip."

    "The boba was pretty good, though. Crushed up leaves aside!"
    jump hungry

label hungry: 
    you "I'm getting hungry... Let's make some food!"
    menu: 
        l "What food?"

        "Make pizza":
            jump pizza

        "Make chicken biryani":
            jump biryani

label pizza:
    you "Let's make pizza."
    l "I want a margarita pizza."
    you "Hm... you know, basil is kind of like a leaf."
    l "Are you KIDDING me?!"
    jump ending

label biryani:
    you "Let's make chicken biryani."
    l "Finally! I'm getting my macronutrients up."
    you "What macronutrients? You're a leaf."
    jump ending



