
import random
import string

def fortune_teller():
    lucky_number = random.randint(1,100)
    fortune_number = random.randint(1,10)
    fortune_text = ""

    if fortune_number == 1:
        fortune_text = "You will find your way,"
    if fortune_number == 2:
        fortune_text = "The path you take will be perilous, but don't let that stop you from reaching your goal,"
    if fortune_number == 3:
        fortune_text = "Don't avoid what scares you,"
    if fortune_number == 4:
        fortune_text = "The next person you meet will want a friend like you,"
    if fortune_number == 5:
        fortune_text = "Your guide is very close. They will take you where you need to go,"
    if fortune_number == 6:
        fortune_text = "Beware of the ocean today,"
    if fortune_number == 7:
        fortune_text = "Don't give up, and you will get where you need to go,"
    if fortune_number == 8:
        fortune_text = "Accept the things you can't control."
    if fortune_number == 9:
        fortune_text = "There will be obstacles in your path. Face them head-on; you will succeed."
    if fortune_number == 10:
        fortune_text = "Sometimes, it's best to go with the flow."

    input()
    print("'Okay... Ho, hum. Let's see.' The old man peers into the palm of your hand.")
    input()
    print(f"'{fortune_text}' he says. 'That is your fortune.'")
    input()
    print(f"'And your Lucky Number for today is: {lucky_number}!'")
    input()


def parent():
    print("\nYou ask the parent.")
    input()
    
    while True:
        name = input("The parent asks you, 'What's your name?' > ").capitalize()
        if name == "":
            input()
            print("(Write your name after the > )")
            input()
        else:
            print(f"\n'{name}?' the parent asks. 'I'm sorry. I don't know anyone by that name.'")
            input()
            oldman()
            break
    
def oldman():
    print("As you walk away, someone calls you over: 'Hey, kid! Yeah, you. Come here.'")
    input()
    print("It's an old man.")
    
    while True:
        fortune = input("\n'Want me to tell you your fortune?' the old man asks. [Y/N] > ").capitalize()
        if fortune in ["No", "Nah", "N", "2", "2."]:
            print("\n'Okay. Suit yourself,' he says.")
            intro()
            break
        elif fortune in ["Yes", "Yeah", "Okay", "Sure", "Y", "1", "1."]:
            print("\nHe smiles wide. 'Great!! I knew a kid like you would appreciate a good fortune-telling.'")
            fortune_teller() 
            print("Before you can say anything else, the old man's grandkids run over and divert his attention.")
            input()
            intro()
            break
        else:
            print("\n'What's that?' the old man asks, confused. 'I thought I asked a yes or no question.'")
    

def intro():
    action = input("\nWhat do you do? [A. Ask the parent, B. Ask the cat, C. Climb the tree, or D. Imagine going home] > ").capitalize()
    
    if action in ["Ask the parent", "Parent", "Ask parent", "A", "A."]:
        parent()
    elif action in ["Climb the tree", "Tree", "Climb tree", "C", "C."]:
        print("\nYou climb the tree to get a better vantage point.")
        input()
        print("Someone shouts, 'Hey! Get down from there!'")
        input()
        print("You get down from the tree. The cat is closer to you now.")
        input()
        intro()
    elif action in ["Imagine going home", "Home", "Imagine home", "D", "D."]:
        print("\nYou imagine going home:")
        input()
        print("You imagine that you know the way home")
        input()
        print("and that you follow the path home") 
        input()
        print("and that you reach home.")
        input()
        print("You remember vividly what home looks like, but you still don't know how to get there.")
        input()
        print("You feel hopeless, but you know you must do something.")
        input()
        intro()
    elif action in ["Ask the cat", "Cat", "Ask cat", "B", "B."]:
        print("\nYou ask the cat how to get home.")
        input()
        print("The cat blinks at you and walks away.")
        input() 
        while True:
            follow = input("Follow the cat? [Y/N] > ").capitalize() 
            if follow in ["Y", "Yes", "1"]:
                part1()
                break
            elif follow in ["N", "No", "2"]:
                intro()
                break 
            else:
                print("\nPlease choose 'Yes' or 'No'.")    
    else:
        print("\nPlease choose between the stated options.")
        intro()

def part1():
    print("\nPart 1: The Boat")
    input()
    print("The cat leads you through the undergrowth at the side of your school. You arrive at a lake.")
    input()
    print("There is a teenage girl standing there beside a boat.")
    input()
    print("The cat jumps in the boat.")
    input()
    print("'Hey! You can't take my boat!' the teenager shouts.")
    reply = input("\nYour reply: > ").capitalize()
    print(f"\n'{reply}', you say, but the teenager is staring at the cat and hasn't noticed you said anything.")
    input()
    print("'Wow. This has never happened before. A cat in my boat. I mean, my dad's boat,' the teenager says.")
    input()
    print("She turns to you and says, 'Well, anyway, if you wanna use my boat, you must first pass a series of tests.'")
    input()
    print("'..Unless you have money. Do you have money?' she asks. Your pockets are empty. She sighs.")
    input()
    print("'You must pass a series of tests,' she repeats.")
    input()
    print("'First, you have to beat me at Rock Paper Scissors!'")
    input()
    print("You look over at the cat. The cat has curled up to take a nap on the boat.")
    input()
    why_count = 0
    
    while True:
        response = input("\nYour response: ['Why?' [1] or 'Okay.' [2]] > ").capitalize()
        if response in ["Why?", "Why", "?", "1", "1."]:
            why_count += 1
        if why_count == 1 and response not in ["Okay", "Ok", "2", "2."]:
            print("\n'Because,' the teenager says, rolling her eyes.")
            input()
        elif why_count == 2 and response not in ["Okay", "Ok", "2", "2."]:
            print("\n'Becaaauuse.'")
            input()
        elif why_count == 3 and response not in ["Okay", "Ok", "2", "2."]:
            print("\n'Ugh. Do you want the boat or not?'")
            input()
        elif why_count == 4 and response not in ["Okay", "Ok", "2", "2."]:
            print("\nThe teenager cusses and then covers her mouth.")
            input()
            print("'..Do you really wanna know?' she asks.")
            input("\n[Yes/No] > ")
            print("\n'Okay, okay. I can tell you're dying to know..'")
            input()
            print("'It's because I wanna do something!'")
            input()
            print("'Do you have any idea how long I've been standing out here? I'm so bored!'")
            input()
            print("'I'm supposed to keep people off the water for some reason, but I can't even remember why. And don't you even want to play?'")
            input()
            input("\nYour response: ['I guess so' [1] or 'Not really' [2]] > ")
            input()
            print("Well...You're playing!")
            input()
            print("'It's best out of three, okay?'")
            game1()
            break
        elif response in ["Okay", "Ok", "2", "2."]:
            print("\n'Great! Then let's play Rock Paper Scissors. It'll be best out of three.'")
            game1()
            break
        else:
            print("\n'Huh?'")

#game1: Rock Paper Scissors
def game1():
    input()
    
    player_wins = 0
    teen_wins = 0
    rounds = 3
    
    while rounds > 0:
        player = input("\nRock, Paper, or Scissors? > ").capitalize()
        teen = random.choice(["Rock", "Paper", "Scissors"]).capitalize()
        print("\nYou chose:", player, "\nTeenager chose:", teen)
        if player == teen:
            print("\n'Oh. We're both", teen + ". It's a tie. That doesn't count, okay?'")
        elif (player in ["Rock", "R", "1"] and teen == "Scissors") or (player in ["Scissors", "Scissor", "S", "3"] and teen == "Paper"):
            print("\n'Your", player, "beats my", teen + ". Yeah, yeah. You win this round.'\n")
            player_wins += 1
            rounds -= 1
        elif player in ["Paper", "P", "2"] and teen == "Rock":
            print("\n'..Your", player, "beats my", teen + ".'")
            input()
            print("'...It doesn't even make sense. Rocks could shred through paper easily. But rules are rules.'\n")
            player_wins += 1
            rounds -= 1
        elif (player in ["Scissors", "Scissor", "S", "3"] and teen == "Rock") or (player in ["Paper", "P", "2"] and teen == "Scissors") or (player in ["Rock", "R", "1"] and teen == "Paper"):
            print("\n'Ha! My", teen, "beats your", player + ". I win this round.'\n")
            teen_wins += 1
            rounds -= 1
        else:
            print("'Huh? What the heck is that supposed to be? Choose either Rock, Paper, or Scissors.'\n")
    
    print("'Okay. The rounds are up. Let's see who won...'")
    
    if player_wins > teen_wins:
        print("\n'Aw man. You beat me. We still have two more games to go, though!")
        game2()
    else:
        print("\n'HA. Ha ha. I beat you. You're gonna have to beat me if you want this boat. Let's go again!'")
        game1()

#game2: Word Guessing Game
#list of words player must guess (all words are related to the teenager/water)
words = ["heedless", "buoyant", "aquatic", "shipyard", "castaway", "desolate", "reservoir", "waves", "downpour", "tide", "waterlogged", "remiss", "oblivious", "disregard",
        "boat", "waterworks", "bored", "solitary", "secluded", "adolescent", "compass", "adrift", "avoidance", "stream", "waterway", "inattentive", "negligent",
        "awkward", "danger", "forgetful", "aqueduct", "condensation", "lake", "meander", "rivulet", "saltwater", "imprudent", "thoughtless", "irresponsible"]

#chooses one random word from this list of words
def get_word():
     word = random.choice(words)
     return word.upper()

def game2():
    input()
    print("Okay, ready? Second game: You have to guess the word I'm thinking of.")
    input()
    word = get_word()
    #letters in the word
    letters = set(word)
    #list of letters in alphabet
    alphabet = set(string.ascii_uppercase)
    #letters player guessed
    guessed = set()

    tries = len(word) + 5

    while len(letters) > 0 and tries > 0:
          word_list = [letter if letter in guessed else '_' for letter in word]
          print("\nMy word: ", " ".join(word_list))
          print("Tries left: ", tries, "\nLetters you've guessed so far: ", " ".join(guessed))
          player_guess = input("Guess a letter > ").upper()
          
          #Keeps track of letters players guesses 
          if player_guess in alphabet - guessed:
               guessed.add(player_guess)
               #if player guess is correct, 
               if player_guess in letters:
                    #remove that letter from the letters in the word
                    letters.remove(player_guess)
               else:
                    tries -= 1
                    print("\n'Nope!", player_guess, "isn't in my word.'")
          elif player_guess in guessed:
               print("\n'You already guessed that letter, remember?'")
          else:
               print("\n'Uh...You know the alphabet, right? Do I need to sing it or, like, are you good?'")

    if tries == 0:
          print("\n'Ha! You couldn't guess it, could ya? The word was", word + ".'")
          input()
          print("'Guess you'll have to try again!.'")
          game2()
    else:
         print("\n'You got it! The word is", word + ".'")
         input()
         if word in ["DOWNPOUR", "WATERLOGGED", "ADOLESCENT", "AVOIDANCE", "WATERWAY", "AWKWARD", "AQUEDUCT", "CONDENSATION", "MEANDER"]:
               print("'You're--a smart kid.'")
         elif word == "WATERWORKS":
              print("...Ugh. You know, my ex used to say I cried too much. You've gotta dump losers like that.'")
              input()
              print("'DUMP 'em.'")
              input()
              print("'Well, anyway...'")
         elif word in ["CASTAWAY", "DESOLATE", "BORED", "SOLITARY", "SECLUDED"]:
              print("'...'")
              input()
              print("'Hm.'")
              input()
              print("'Well, there's still one more game.'")
              input()
              print("'Unless...'")
         else:
              print("'...You know, incidentally, it's important work, guarding a boat.'")
              input()
              print("'I feel kinda bad, though, like--My dad lectured me about it this morning, but I totally zoned out.'")
              input()
              print("'Well, anyway...'")
         
         input()

         while True:
          cont = input("'Think you can beat me again? (Be warned, though: if you lose you'll have to go at least one more round.)' [Y/N] > "). capitalize()
          if cont in ["Y", "Yes", "Definitely", "Absolutely", "For sure!", "Yeah", "Sure", "1"]:
               input()
               print("'Oh heck yeah! Let's go!'")
               game2()
               break
          elif cont in ["N", "No", "Nah", "No thanks", "Next game", "2"]:
               input()
               print("'Okay. On to the FINAL game.'")
               game3()
               break
          else:
               input()
               print("'Huh? I must've heard you wrong.")

#game3: Madlibs
def game3():
    input()
    print("'Okay, okay. You ready for the last one? Ready? The FINAL game is:' She pauses dramatically.")
    input()
    print("'Mad Libs!'")
    input()
    print("'Yeah, I know. You can't really lose at Mad Libs. I just felt like playing.'")
    input()
    print("The teenager takes out a wrinkled old madlibs booklet. 'Okay, give me a:")
    input()

    madlib1 = """Boating Safety Basics:  
        {s}! Are you about to just {v1} in your boat?
        You can't do that!
        Before you take your boat into the deep, dark {n1}, follow the following steps:
        1. Wear a well-fitted, {adj1} {n2} that includes a {n3} to call out for help.
        2. In case you end up out on the {n1} for more than just {num1} days, make sure you bring enough {n4} and {b} with you. 
        3. To avoid losing your way, keep a {n5} and a {n6} with you at all times.
        Have fun out there, but remember: following those steps and staying {adj2} are essential to staying safe out in the deep, dark {n1}."""

    madlib2 = """The Story of the Traveler:
        Once upon a time, there was a {adj1}, {adj2} traveler who was lost in the {n1}. 
        The traveler {v1} for a long time and wandered a long way, 
        through the vast {n2}, the majestic {n3} (where they met a beautiful {n4}), and finally through the deep, {adj3} sea.
        The traveler had been {v2} almost {num1} days by this point and was very tired. 
        They let out a loud "{s}!" to express just how tired they were.
        Soon after that, the traveler found their way and lived {adv} ever after."""

    madlib3 = """Recipe for a delicious {f1}: 
        For this recipe, you'll need 3 cups of {f2}, 2 tablespoons of {f3}, and 1/2 teaspoon of {f4}. 
        Step 1: First, you'll need to {v2} the {f2} with the {f3}. If you did it right, it should look like a {n2}. 
        Step 2: Next, {v4} in the {f4}. Preheat your {n3} to {num1} degrees. Bake for {num2} minutes.
        Step 3: By this point, you should start to smell {n4} wafting through the kitchen. 
                Poke a {n5} into your {f1} to ensure that it's ready and take your delicious baked {f1} out of the oven. 
        Step 4: Enjoy!"""
   
    #a list of the three madlibs
    madlibs_list = [madlib1, madlib2, madlib3] 
    
    #one madlibs is randomly chosen
    madlibs = random.choice(madlibs_list)

    #prompt the user for inputs for the chosen madlib
    if madlibs == madlib1:
        inputs = {"s": input("Silly Word > ").upper(),
                  "v1": input("Verb (the teenager whispers: 'an action word') > ").upper(),
                  "n1": input("Noun ('a person, place, or thing') > ").upper(),
                  "adj1": input("Adjective ('a word that describes somebody or something') > ").upper(),
                  "n2": input("Something you wear > ").upper(),
                  "n3": input("Noun > ").upper(),
                  "num1": input("Number > ").upper(),
                  "n4": input("Plural Noun > ").upper(),
                  "b": input("Beverage > ").upper(),
                  "n5": input("Noun > ").upper(),
                  "n6": input("Noun > ").upper(),
                  "adj2": input("Adjective > ").upper()                 
                  }
    elif madlibs == madlib2:
        inputs = {"adj1": input("Adjective (the teenager whispers: 'a word that describes somebody or something') > ").upper(),
                  "adj2": input("Adjective > ").upper(),
                  "n1": input("Noun ('a person, place, or thing') > ").upper(),
                  "v1": input("Verb ('an action word'), past tense > ").upper(),
                  "n2": input("A Place ('be as general or as specific as you want') > ").upper(),
                  "n3": input("A Place > ").upper(),
                  "n4": input("Noun > ").upper(),
                  "adj3": input("Adjective > ").upper(),
                  "v2": input("Verb ending in -ing > ").upper(),
                  "num1": input("Number > ").upper(),
                  "s": input("Silly Word > ").upper(),
                  "adv": input("Adverb ('that one that ends in -ly') > ").upper()
                  }
    elif madlibs == madlib3:
        inputs = {"f1": input("Food > ").upper(),
                  "f2": input("Food > ").upper(),
                  "f3": input("Food > ").upper(),
                  "f4": input("Food > ").upper(),
                  "v1": input("Verb (the teenager whispers: 'an action word') > ").upper(),
                  "n1": input("Noun ('a person, place, or thing') > ").upper(),
                  "v2": input("Verb > ").upper(),
                  "n2": input("Noun > ").upper(),
                  "num1": input("Number > ").upper(),
                  "num2": input("Number > ").upper(),
                  "n3": input("Noun > ").upper(),
                  "n4": input("Noun > ").upper()
                  }

    #fill in the chosen madlib with the user's inputs
    filled_madlib = madlibs.format(**inputs)

    print("'Okay! Here's the madlib:'")
    input()
    print(filled_madlib)    
    input()
    print("'Lol! That was great!'")
    input()
    print("'...'")
    input()
    print("'Well, those are all the games. I guess you get the boat now.'")
    input()
    
    reply = input("'..You'll come back sometime to hang out, won't you? I have, like, so many more games.' [Y/N] > ").capitalize()
    
    while True:
        if reply in ["Y", "Yes", "Definitely", "1"]:
            print("\nThe teenager smiles wide and waves as you set off with the cat napping in the boat.")
            part2()
            break
        elif reply in ["N", "No", "2"]:
            print("\n'W-Well--I didn't even want to!' the teenager huffs, and as you get into the boat (where the cat still naps), she pushes it out into the lake.")
            part2()
            break
        else:
            print("\nThe teenager stares at you, confused. 'Can you repeat that? I must've heard you wrong,' she says.")

def part2():
    input()
    print("You find oars in the boat. You pick them up and start rowing out into the lake.")
    input()
    print("'Oh! I just remembered!' the teenager calls out from the shore.")
    input()
    print("'I was supposed to tell anyone taking the boat not to--'")
    input()
    print("You can't hear the end of what she said. You're too far out to hear each other now.")
    input()
    print("The lake seems larger than before. It looks more like an ocean. The shore you came from has disappeared.")
    input()
    print("Part 2: Out In the Ocean")
    input()
    
    while True:
        reaction = input("Do you: Panic [1] or Relax [2]? > ").capitalize()
        if reaction in ["panic", "1", "1."]:
            print("\nThe world around you seems to swirl and distort as your breathing grows faster.")
            input()
            print("You have no idea what to do. You don't know how things have turned out this way.")
            input()
            print("You feel a weight settle in your lap.")
            input()
            print("The cat has curled up on your lap and has begun to purr softly.")
            input()
            print("You take a deep breath and feel calmer as you pet the cat.")
            input()
            break
        elif reaction in ["relax", "2", "2."]:
            print("\nYou take a few deep breaths.")
            input()
            print("You notice the warm breeze and the way the clouds make shapes in the blue sky. The cat is purring at your feet.")
            input()
            print("You think that everything might just be okay.")
            input()
            break
        else:
            print("\nPlease choose either 1 or 2.")
            input()

    print("You notice a lighthouse up ahead, and to your excitement, you see a place you recognize!")
    input()
    print("If you can get there, you'll probably find your way home!")
    input()
    print("You look down at the cat eagerly, but the cat's fur is now standing up and its tail is between its legs.")
    input()
    print("You look ahead.")
    input()
    print("Monsters have risen up from the water before you. You are too afraid to look straight at them. A great, rattling growl emanates from them.")
    input()
    print("They are constricting your path.")
    input()

    while True:
        choice1 = input("What do you do? [Row backwards [1], Row around them [2], or Row through them [3]] > ").capitalize()
        if choice1 in ["Row backwards", "Row away", "Backwards", "1", "1."]:
            input()
            print("You row backwards, trying to escape the monsters, though it pains you to turn away from home.")
            input()
            print("The monsters in front of you ram against the water, pushing you further back.")
            input()
            print("Before you can react, you're pushed forward again, which makes you realize: there are monsters behind you, too.")
            input()
            print("Both sides push you back and forth violently. There is no way to avoid this.")
            persist()
            break
        elif choice1 in ["Row around them", "Row around", "Around", "2", "2."]:
            input()
            print("You think you can get around them, but as you try, they push your boat back.")
            input()
            print ("You hold on tight as you skid backwards.")
            input()
            print("You feel a push at the back of your boat, and you are shoved forwards again. This makes you realize: there are monsters behind you, too.")
            input()
            print("You're shoved back and forth by either side. There is no easy way out.")
            persist()
            break
        elif choice1 in ["Row through them", "Row through", "Through", "3", "3."]:
            sure = input("\nAre you sure? You are scared of them. [Y/N] > "). capitalize()
            if sure in ["Y", "Yes", "1", "1."]:
                input()
                print("You start rowing through the monsters in front of you with a bravery you didn't realize you possessed.")
                input()
                print("As you do, there is a great commotion! The monsters have begun pushing against the water, forcing you backwards.")
                input()
                print("You turn and see that a line of monsters have risen on the other side and are pushing you back in the other direction.")
                input()
                print("In a moment of clarity, you realize that you've been caught in the middle of a war: a battle between the monsters.")
                persist()
                break
            else:
                print("\nFeeling panicked, you decide to reconsider your options.")
                input()
        else:
            print("\nPlease choose 1, 2, or 3.")
            input()

def persist():
    while True:
        input()
        choice2 = input("Do you: Try to stop the monsters [1] or Push through the monsters in front of you [2]? > ").capitalize()
        if choice2 in ["Try to stop the monsters", "Stop", "1", "1."]:
            input()
            print("Frustrated with the turn of events, you shout at the monsters to stop and let you pass.") 
            input()
            print("You shout while being tossed back and forth; You shout until your throat is hoarse.")
            input()
            print("The monsters only continue to push your boat back and forth, seemingly harder than before.")
        elif choice2 in ["Push through the monsters in front of you", "Push through", "Push", "2", "2."]:
            input()
            print("With home on the horizon, you struggle to push through the monsters.")
            input()
            print("You grow tired as you continue to row.")
            break
        else:
            print("\nPlease choose either 1 or 2.")

    keep_count = 0 

    while True:
        input()
        keep = input("Keep rowing? [Y/N] > ").capitalize()
        if keep in ["Y", "Yes", "1", "1."]:
            keep_count += 1
        elif keep in ["N", "No", "2", "2."]:
            print("\nYou take a rest. The monsters continue to push you back and forth, so it isn't much of a rest. Any progress you have made is undone.")
            input()
            print("You feel hopeless.")
            keep_count = 0
        else:
            print("\nPlease choose Yes or No.")
            continue

        if keep_count == 1:
            print("\nYou keep rowing, seeming to make very little progress.")
        elif keep_count == 2:
            print("\nYou keep rowing, your muscles aching, your lungs burning, but you are almost past the monsters.")
        elif keep_count == 3:
            print("\nYou keep rowing until you have finally pushed beyond the monsters.")
            break
            
    input()
    print("You are very tired.")
    input()
    print("Your boat is now moving frighteningly fast. The monsters have sped up the flow of water, turning it into rapids. The cat clings to your leg.")
    input()
    print("You are afraid that you won't be able to get home this way, and that something terrible will happen in these waters.")    
    input()

    let_go()

def let_go():
    while True:
        choice3 = input("What do you do? [Hold on tight [1] or Row against the rapids [2]] > ").capitalize()
        if choice3 in ["Hold on tight", "Hold on", "1", "1."]:
            print("\nYou hold on tight to the boat and let the rapids pull you along.")
            break
        elif choice3 in ["Row against the rapids", "Row against", "Row", "2", "2."]:
            print("\nYou row against the rapids.")
            input()
            print("You row and row until your arms give out. It seems that the rowing hasn't had much of an effect.")
            input()
            keep2 = input("What do you do? [Keep rowing [1] or Stop rowing [2]] > ").capitalize()
            if keep2 in ["Keep rowing", "Keep", "1", "1."]:
                print("\nYou continue to row, but can't make much of an effort because your arms are so tired.")
                input()
                print("In a moment of weakness, you accidentally drop the oars and lose them to the rapids.")
                input()
                print("All you can do now is cling to the boat, trying to calm your racing heart. The cat licks your sore fingers.")
                break
            elif keep2 in ["Stop rowing", "Stop", "2", "2."]:
                print("You hold on tight to your boat as it races through the rapids.")
                break
            else:
                print("\nPlease choose 1 or 2.")
        else:
            print("\nPlease choose 1 or 2.")

    input()
    print("You look around.")
    input()
    print("Your heart leaps as you realize that the rapids are actually helping to take you closer to home.")
    input()
    print("You relax a little and trust the water.")
    input()
    print("Soon, your boat knocks hard against something.")
    input()
    print("You fly off the boat, landing on a warm wooden dock.")
    input()
    print("The cat jumps off the boat and grooms itself as though nothing had happened.")
    input()
    print("You get on your feet and--you recognize where you are!")
    input()
    print("You know how to get home!")
    input()

    end()

def end():
    print("Final Part: Home")

    input()
    print("The cat rubs against your leg, purring, and then takes off. You see the cat disappear behind the cat door of a nearby home.")
    input()
    print("You hope to see that cat again.")
    input()
        
    while True:
        pace = input("Do you run [R] or walk [W] home? > ").capitalize()
        if pace in ["Run", "R", "1", "1."]:
            print("\nYou run all the way home, nearly tripping over your feet.")
            break
        elif pace in ["Walk", "W", "2", "2."]:
            print("\nYou walk home, enjoying the scenery on the way.")
            input()
            print("You recognize the corner store, your neighbor's houses, and the trees and flowers that are in bloom.")
            input()
            print("You stop to smell the lilies and notice that that same cat is out again.")
            input()
            print("The world seems to sing a thousand different songs, and you want to hear them all.")
            input()
            print("All is well.")
            break
        else:
            print("Please choose either Walk or Run.")
            
    input()
    print("You reach home. You're very happy, because though you were frightened, you still found your way.")
    input()
    print_the_end()
    input()
    quit()

#made using https://www.ascii-art-generator.org/, "big" font, max line width 40
def print_the_end():
    print(" _______ _            ______           _ ")
    print("|__   __| |          |  ____|         | |")
    print("   | |  | |__   ___  | |__   _ __   __| |")
    print("   | |  | '_ \ / _ \ |  __| | '_ \ / _` |")
    print("   | |  | | | |  __/ | |____| | | | (_| |")
    print("   |_|  |_| |_|\___| |______|_| |_|\__,_|")

def print_going_home():
    print("  _____       _               _    _  ")                    
    print(" / ____|     (_)             | |  | |")                     
    print("| |  __  ___  _ _ __   __ _  | |__| | ___  _ __ ___   ___ ")
    print("| | |_ |/ _ \| | '_ \ / _` | |  __  |/ _ \| '_ ` _ \ / _ \ ") 
    print("| |__| | (_) | | | | | (_| | | |  | | (_) | | | | | |  __/")
    print(" \_____|\___/|_|_| |_|\__, | |_|  |_|\___/|_| |_| |_|\___|")
    print("                       __/ | ")                             
    print("                      |___/ ")                              

def main():
    print_going_home() #Game title card 
    print(input("\nPress Enter to continue "))
    print("The school bell rings. It's the end of the day and you can go home.") 
    input()
    print("But...What was the way home again? You look around, not sure what to do. You see a parent, a wandering cat, and a tall climbing tree.")
    input()
    intro()

main()

#used this tutorial: https://github.com/codinggrace/text_based_adventure_game/tree/master