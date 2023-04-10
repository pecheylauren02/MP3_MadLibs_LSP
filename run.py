# imported modules

# Welcome message
print("Welcome to the Maddest Game of Mad Libs you will ever play!")
print("If you are looking for a night of laughter and fun with your friends and family, then look no further!")
print("Mad Libs is one of the world's greatest word games.")
print("It can make anyone the funniest person in the room, without even trying!") 

# Instructions
response = input("Want to learn how to play? Y/N: ")
if response.upper() == "Y":
    print("\nWhat are Mad Libs?\n")
    print("Mad Libs are stories with words removed and replaced by blank spaces.")
    print("\nHere's how to play:")
    print("Choose a story title from the list given, by entering the number of the title.")
    print("1. You will be given a total of 20 prompts, asking you to enter a word, without seeing the story beforehand. E.g. 'Enter a noun: '")
    print("2. When you see a prompt, enter your answer. The prompts will ask you for a mix of adjectives, nouns, exclamations, colours, adverbs, and more!")
    print("3. When you finish entering all of the prompts correctly, these words will be inserted into the blanks of the story title you chose.")
    print("4. Your story will then be displayed for you to read aloud with hilarious results.")
    print("5. There are no winners or losers in this game, only laughter!\n")

    play_response = input("Ready to play? Y/N: ")
    if play_response.upper() == "Y":
        print("Let's get started")
    else: 
        print("Okay, maybe next time!")
else:
    print("Okay, maybe next time!")

# Story Title Selection 

# Define the list of story titles

def play_madlibs():
    story_titles = ["A Peculiar Adventure", "A Strange Fairytale", "A Day at the Office", 
                    "One Interesting Vacation", "A Scary Encounter", "A Day at the Beach", 
                    "My First Day at School", "A Wild Party"]

    # Print the list of story titles for the user to see
    print("Please select a story by entering the corresponding number:")
    for i, title in enumerate(story_titles):
        print(f"{i+1}. {title}")

    # Ask the user to select a story
    selected_story_index = int(input("Enter the number of the story you'd like to read: ")) - 1

    # Retrieve the selected story title
    selected_story_title = story_titles[selected_story_index]

    # Print the selected story title for the user to see
    print(f"You have selected the story: {selected_story_title}")

    # Mad Libs One of Eight

    # User inputs One of Eight: Status: DONE ALL 20

    if selected_story_title == "A Peculiar Adventure": 

        words = ['an adjective', 'a feeling', 'a noun', 'a place', 'another adjective', 'an animal', 'a noun', 
        'another adjective', 'a verb ending in -ed', 'a plural noun', 'another adjective', 'an adverb', 'a feeling', 
        'another noun', 'another noun', 'another feeling', 'a number', 'another adjective', 'another feeling', 'a verb in the present tense']

        inputs = [input(f"Enter {word}: ") for word in words]

    # Story Template One of Eight

        story_one = f"""One {inputs[0]} day, I woke up feeling {inputs[1]}
        and decided to go on a crazy adventure. I grabbed my trusty {inputs[2]} and
        set off into the {inputs[3]} wilderness. As I walked, I came across a {inputs[4]}
        {inputs[5]} who asked me for help. 'I've lost my {inputs[6]}!' they exclaimed. Being
        the {inputs[7]} person I am, I offered to help. We {inputs[8]} high and
        low, through dense forests and mysterious {inputs[9]}, until finally we found the
        missing {inputs[6]}. The {inputs[6]} was so {inputs[10]} that we couldn't resist taking
        a selfie {inputs[11]} with it. Feeling {inputs[12]}, I said goodbye to my new friend, {inputs[5]},
        and continued on my wild adventure.

        Soon, I stumbled upon a giant {inputs[13]} who challenged me
        to a {inputs[14]} contest. I was feeling {inputs[15]}, so I accepted. We went back and forth,
        with each of us throwing {inputs[16]} punches at each other back and forth. In the end, I emerged
        victorious, much to the {inputs[17]} disappointment of my opponent. Exhausted but {inputs[18]},
        I returned home and went straight to bed.

        As I drifted off to {inputs[19]}, I couldn't help but think
        that it had been a truly remarkable day. So if you're feeling {inputs[1]} and in need of an adventure,
        grab your {inputs[2]} and set off into the {inputs[10]} unknown. Who knows what kind of
        {inputs[7]} and {inputs[4]} things you might find along the way!"""

        print(story_one)

    # User inputs Two of Eight

    elif selected_story_title == "A Strange Fairytale": 

        words = ['an adjective', 'a noun', 'a verb ending in -ing', 'another verb', 'a place', 'another adjective', 
        'another noun', 'another verb', 'another adjective', 'another noun', 'an exclamation', 'another adjective', 
        'a verb in the past tense', 'another verb ending in -ing', 'an adverb', 'another noun', 'another verb in the past tense', 
        'a random date', 'a random number']

        inputs = [input(f"Enter {word}: ") for word in words]

    # Story Template Two of Eight

        story_two = f"""Once upon a time, in a land far, far away, there was a {inputs[0]} {inputs[1]} who 
        loved to {inputs[2]}. One day, while {inputs[3]} in the {inputs[4]}, the {inputs[0]} {inputs[1]} 
        stumbled upon a {inputs[5]} {inputs[6]} who was {inputs[7]} with a {inputs[8]} {inputs[9]}.
        "Hey there, {inputs[10]}!" exclaimed the {inputs[0]} {inputs[1]}. "Would you like to join us in our 
        {inputs[11]} {inputs[2]}?"

        Without hesitation, the {inputs[5]} {inputs[6]} agreed and soon found themselves {inputs[2]} 
        with the {inputs[5]} {inputs[6]} and their {inputs[8]} {inputs[9]}. They {inputs[12]} and {inputs[12]}, 
        and even did a little {inputs[13]} together.

        But then, out of nowhere, a {inputs[11]} {inputs[15]} appeared and started throwing things {inputs[14]} at them! 
        The {inputs[0]} {inputs[1]} and the {inputs[5]} {inputs[6]} were afraid, but to their surprise, the 
        {inputs[8]} {inputs[9]} stood tall and {inputs[16]} the {inputs[11]} {inputs[15]}.
        From {inputs[17]}, the {inputs[0]} {inputs[1]} made a promise to themselves to always be open to new experiences 
        and never to be afraid of a little {inputs[2]}. And who knows? Maybe they'll even meet another {inputs[18]} 
        {inputs[11]} {inputs[15]} along the way.
        The end"""

        print(story_two)

    # User inputs Three of Eight

    elif selected_story_title == "A Day at the Office":

        words = ['a feeling', 'a city', 'a noun', 'another noun', 'an adjective', 'another feeling', 'a verb ending in -ing', 
        'another noun', 'another verb', 'a random number', 'another adjective', 'another city', 'an adverb', 'another adjective', 
        'another noun', 'another adjective', 'a plural noun', 'another feeling', 'another noun', 'an item of clothing (plural)']

        inputs = [input(f"Enter {word}: ") for word in words]

    # Story Template Three of Eight

        story_three = f'''
        It was just another {inputs[0]} day in the office in {inputs[1]} when I arrived at my 
        large {inputs[2]}. I sat down at my {inputs[2]} and opened up my {inputs[3]} to start my {inputs[4]} work. 
        But before I could even begin, my {inputs[5]} coworker walked in and started {inputs[6]} loudly 
        about their {inputs[7]} problems. I tried to tune them out, but their voice was so annoying that I couldn't {inputs[8]}.
                
        After what felt like {inputs[9]} hours of their constant {inputs[6]}, I decided to take a {inputs[10]} 
        break and visit the office in {inputs[11]}.As I walked {inputs[12]} down the hallway, I noticed a {inputs[13]} 
        smell coming from the break room. I cautiously peeked inside, and to my horror, I saw that someone had left their {inputs[14]} 
        in the microwave for way too long.
        
        The {inputs[14]} was now a {inputs[15]} mess, and the entire room smelled like burnt {inputs[16]}.
        Feeling {inputs[17]}, I quickly made my way back to my {inputs[2]}, only to find that my {inputs[3]} had 
        mysteriously disappeared! After a few minutes of searching {inputs[12]}, I finally found it hiding under a pile of 
        dirty {inputs[18]}.
                
        So if you're ever feeling bored at work, just remember to keep your eyes and ears open for any weird moments that might 
        come your way. You never know what kind of {inputs[19]} might be waiting just around the corner in {inputs[1]}!
        '''

        print(story_three)

    # User inputs Four of Eight

    elif selected_story_title == "One Interesting Vacation":
        
        season_one = input("Enter a season: ")
        adjective_one = input("Enter an adjective: ")
        country = input("Enter the name of a country: ")
        adjective_two = input("Enter another adjective: ")
        feeling_one = input("Enter a feeling: ")
        clothing = input("Enter an item of clothing: ")
        adjective_three = input("Enter another adjective: ")
        adverb_one = input("Enter an adverb: ")
        noun_one = input("Enter a noun: ")
        plural_noun_one = input("Enter a plural noun: ")
        adjective_four = input("Enter another adjective: ")
        adverb_one = input("Enter an adverb: ")
        noun_three = input("Enter another noun: ")
        feeling_two = input("Enter another feeling: ")
        place_one = input("Enter a place: ")
        exclamation_one = input("Enter an exclamation, e.g. 'OMG!': ")
        adjective_five = input("Enter another adjective: ")
        verb_one = input("Enter a verb ending in -ing: ")
        verb_two = input("Enter another verb ending in -ing: ")
        noun_four = input("Enter another noun: ")

    # Story Template Four of Eight

        story_four = f'''Last {season_one}, I decided to take a {adjective_one} vacation to {country}, and boy was it 
        {adjective_two}! On the first day of my trip, I woke up feeling {feeling_one} and ready for adventure. I threw 
        on my {clothing} and headed out into the {adjective_three} unknown.
        
        As I walked {adverb_one} through the streets, I came across a handsome {noun_one} who was juggling {plural_noun_one}. 
        I couldn't help but stop and watch in amazement as they threw the {plural_noun_one} higher and higher into the air.
        After the {noun_one} finished their act, I decided to continue my {adjective_three} journey. But before I could make 
        it very far, a {adjective_four} bird flew {adverb_one} right into my {noun_three}! I was so startled that I nearly 
        fell over, but luckily the bird flew away unharmed.

        Feeling a bit shaken and {feeling_two}, I decided to take a break at a nearby {place_one}. I ordered a {adjective_four} 
        drink and sat down to people-watch. That's when I heard a loud {exclamation_one} coming from outside. I opened my 
        window and saw that a {adjective_five} parade was going by! I quickly got dressed and joined the parade, 
        {verb_one} and {verb_two} along to the music. It was so much fun that I almost forgot about my 
        {noun_four}! I can't wait to see where my next crazy adventure takes me!'''

        print(story_four)

    # User inputs Five of Eight

    elif selected_story_title == "A Scary Encounter":

        adjective_one = input("Enter an adjective: ")
        noun_one = input("Enter a noun: ")
        verb_one = input("Enter a verb ending in -ing: ")
        feeling_one = input("Enter a feeling: ")
        adjective_two = input("Enter an adjective: ")
        adjective_three = input("Enter another adjective: ")
        adverb_one = input("Enter an adverb: ")
        adverb_two = input("Enter another adverb: ")
        clothing_one = input("Enter an item of clothing: ")
        noun_two = input("Enter another noun: ")
        adjective_four = input("Enter another adjective: ")
        clothing_two = input("Enter another item of clothing: ")
        verb_two = input("Enter another verb ending in -ing: ")
        body_part = input("Enter a body part: ")
        feeling_one = input("Enter a feeling: ")
        noun_two = input("Enter another noun: ")
        noun_three = input("Enter another noun: ")
        verb_three = input("Enter another verb ending in -ing: ")
        feeling_two = input("Enter another feeling: ")

    # Story Template One of Eight

        story_five = f'''One {adjective_one} night, I was walking home from a {noun_one} party when I suddenly felt like someone 
        was {verb_one} me. I turned around, but there was no one there. Feeling a bit {feeling_one}, I quickened my pace 
        and started walking faster. But then, I heard a {adjective_two} noise coming from behind me. I turned around again, and 
        this time I saw a {adjective_three} figure lurking {adverb_one} in the shadows.

        I tried to run {adverb_two}, but my {clothing_one} got caught on a {noun_one}, and I fell to the ground. The 
        {adjective_three} figure approached me slowly, and I realized that it was actually a {noun_two} wearing a {adjective_four} 
        {clothing_two}. I screamed for help, but no one seemed to hear me. The {noun_two} just stood there, {verb_two} at 
        me with its tiny {body_part}.

        Feeling {feeling_one}, I tried to think of a way to escape. That's when I remembered the {noun_one} that I had in my {noun_three}. 
        I pulled it out and aimed it at the {noun_two}, hoping that it would scare it away. To my surprise, the {noun_two} started 
        {verb_three} and ran away as fast as it could. I got up and ran home as quickly as possible, feeling {feeling_two} 
        the entire time.

        As I lay in bed that night, I couldn't help but wonder what other {adjective_one} encounters I might have in the future. 
        But for now, I was just grateful to be safe and sound in bed.'''

        print(story_five)

    # User inputs Six of Eight

    elif selected_story_title == "A Day at the Beach":

        adjective_one = input("Enter an adjective: ")
        type_of_holiday = input("Enter a type of holiday, e.g. Christmas: ")
        adjective_two = input("Enter another adjective: ")
        plural_noun_one = input("Enter a plural noun: ")
        noun_two = input("Enter another noun: ")
        plural_noun_two = input("Enter another plural noun: ")
        adjective_three = input("Enter another adjective: ")
        verb_one = input("Enter a verb: ")
        adjective_four = input("Enter another adjective: ")
        verb_two = input("Enter a verb ending in -ing: ")
        body_part = input("Enter a body part: ")
        noun_four = input("Enter another noun: ")
        place_one = input("Enter a place: ")
        adjective_five = input("Enter another adjective: ")
        noun_five = input("Enter another noun: ")
        adverb_one = input("Enter an adverb: ")
        adjective_six = input("Enter another adjective: ")
        noun_six = input("Enter another noun: ")
        animal_one = input("Enter a type of animal: ")
        verb_three = input("Enter another verb: ")
        adverb_two = input("Enter another adverb: ")
        number = input("Enter a random number: ")

    # Story Template Six of Eight

        story_six = f"""One {adjective_one} {type_of_holiday}, I headed to the beach with my {adjective_two} {plural_noun_one}. 
        We packed a {noun_two} full of snacks, sunscreen, and {plural_noun_two} and set off on our adventure. As soon as we 
        arrived, we could feel the {adjective_three} sun beating down on us. We quickly unpacked and set up our {noun_two} and 
        got ready to hit the waves and {verb_one}.
        
        But as soon as I jumped in, I realized that the water was freezing {adjective_four}! I swam out to my friends, who were 
        {verb_two} and having a great time. I decided to join in, even though I could barely feel my {body_part}. As we 
        played in the water, we suddenly heard a loud {noun_four} coming from the {place_one}. We swam back to find a 
        {adjective_five} crowd of people gathered around a {noun_five} that had washed up {adverb_one} on the beach.
        
        Feeling curious, we pushed our way through the crowd to get a closer look. As we approached, we could smell the 
        {adjective_six} stench of the dead {noun_six}. Suddenly, a massive {animal_one}. swooped down and started {verb_three} 
        on the {noun_six}. We all screamed and ran away {adverb_two}, narrowly avoiding being hit {number} by the {animal_one}.
        
        After that crazy encounter, we decided to pack up and head home. As we drove away, we couldn't help but laugh at the 
        absurdity of our day at the beach."""

        print(story_six)

    # User inputs Seven of Eight

    elif selected_story_title == "My First Day at School":

        feeling_one = input("Enter a feeling: ")
        adjective_one = input("Enter an adjective: ")
        adverb_one = input("Enter an adverb: ")
        noun_one = input("Enter a noun: ")
        adjective_two = input("Enter another adjective: ")
        plural_noun_one = input("Enter a plural noun: ")
        verb_one = input("Enter a verb ending in -ing: ")
        verb_two = input("Enter another verb ending in -ing: ")
        verb_three = input("Enter another verb ending in -ing: ")
        noun_three = input("Enter another noun: ")
        adjective_three = input("Enter another adjective: ")
        place = input("Enter a place: ")
        plural_noun_two = input("Enter another plural noun: ")
        plural_noun_three = input("Enter another plural noun: ")
        verb_four = input("Enter another verb ending in -ing: ")
        name = input("Enter the name of someone you know: ")
        superhero = input("Enter the name of your favourite superhero: ")
        plural_noun_four = input("Enter another plural noun: ")
        plural_noun_five = input("Enter another plural noun: ")
        adjective_four = input("Enter another adjective: ")

        story_seven = f"""
        On my first day of school, I felt {feeling_one} as I walked into the classroom. My {adjective_one} teacher greeted 
        me with a big smile and {adverb_one} showed me to my {noun_one}. As I sat down, I couldn't help but notice the 
        {adjective_two} students and {plural_noun_one} around me. Some were {verb_one}, while others were 
        {verb_two} and {verb_three} all over the classroom.
        
        Just as the teacher was about to start the lesson, an enormous {noun_three} burst into the room. It was a 
        {adjective_three} {noun_three} who had lost their way to the {place}. The teacher quickly helped them find their way, 
        and we all had a good laugh about it.
        
        As the day went on, we learned about {plural_noun_two} and {plural_noun_three}. No matter what we were learning, we 
        were always {verb_four} and having a good time. During recess, I made some new friends called {name} and 
        {superhero} who showed me their cool {plural_noun_four} and {plural_noun_five}. We played games and laughed so hard 
        that we almost forgot we were at school.
        
        As the day came to an end, I felt happy and {adjective_four}. So if you're feeling {adjective_four} about your first 
        day of school, just remember that it's a new adventure full of surprises and {adjective_one} moments."""

        print(story_seven)


    # User inputs Eight of Eight

    elif selected_story_title == "A Wild Party":

        adjective_one = input("Enter an adjective: ")
        body_part = input("Enter the name of a body part: ")
        adjective_two = input("Enter another adjective: ")
        adjective_three = input("Enter another adjective: ")
        plural_noun_one = input("Enter a plural noun: ")
        verb_one = input("Enter a verb ending in -ing: ")
        verb_two = input("Enter another verb ending in -ing: ")
        adjective_four = input("Enter another adjective: ")
        noun_one = input("Enter a noun: ")
        adverb_one = input("Enter an adverb: ")
        verb_three = input("Enter another verb ending in -ing: ")
        adjective_five = input("Enter another adjective: ")
        colour = input("Enter a colour: ")
        clothing_plural = input("Enter an item of clothing(plural): ")
        number = input("Enter a random number: ")
        plural_noun_two = input("Enter another plural noun: ")
        adverb_two = input("Enter another adverb: ")
        verb_four = input("Enter another verb ending in -ing: ")
        adjective_six = input("Enter another adjective: ")
        plural_noun_three = input("Enter another plural noun: ")
        verb_five = input("Enter another verb ending in -ing: ")

    # Story Template One of Eight

        story_eight = f""" Last night I went to the craziest party ever. It was so {adjective_one} that my {body_part}
        is still recovering from it. When I arrived, the music was {adjective_two} and the dance floor was packed with 
        {adjective_three} people and wild {plural_noun_one}. I started {verb_one} to the beat and before I knew 
        it, I was {verb_two} with a group of {adjective_four} strangers.

        Things really got out of hand when someone suggested we play {noun_one} pong. I've never been good at that game, 
        but I managed to {adverb_one} {verb_three} a few shots and impress everyone. As the night went on, more and more 
        people and {plural_noun_one} showed up. 
        
        There were {adjective_five} characters in crazy costumes, some wearing {colour}{clothing_plural}. I even saw one 
        magician trying to juggle {number}{plural_noun_two} while riding a unicycle. A lot of the night became blurry 
        after that, but I found myself {adverb_two}{verb_four} on a couch with a {adjective_six} person who I had 
        never met before. We started talking about {plural_noun_three} and ended up {verb_five} all night.

        The party didn't really start to wind down until the early hours of the morning. It was definitely a night I'll 
        never forget!"""

        print(story_eight)


play_madlibs()
