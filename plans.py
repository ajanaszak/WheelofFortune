###PSEUDOCODE FOR WHEEL OF FORTUNE GAME
###AARON JANASZAK

### QUESTIONS TO ANSWER: ###
##How are you storing the word or phrase selection? How are you storing its hint?
##How are you managing each player's turn?
##How are you maintaining each player's bank?
##What does the logic look like for managing a round?
##What does the logic look like for buying a vowel?
##How are you running the game overall?

#set up PlayerOne, PlayerTwo, PlayerThree
#set each with individual bank balance = 0
#also round money = 0 at start of each round
#Start with PlayerOne by default

#Store Puzzle Answers in list Answers[]
#Store Puzzle Categories in list Categories[]
#This way, answers and categories can be accessed by index
#Use WordGuessingGame to 'hide' Answer with blank spots (or other ASCII character?)
    # chr(64) = @ symbol, easier to see than underscores, ord('@') = 64
#set turnNum = 1
    #if turnNum % 3 == 1: PlayerOne turn
    #if turnNum % 3 == 2: PlayerTwo turn
    #if turnNum % 3 == 0: PlayerThree turn
#set roundNum = 0

### ROUND ONE ###
#start with playerOne
#turnNum = 1
#Print Category
#Print series of blanks for letters in answer
    
#main() 'screen' options:
    #turn 'flag' set to 'on'/'true'/something
    #spin wheel()
        #buy consonant()
    #buy vowel()
    #solve the puzzle()

#build functions for:
    #spin wheel():
        #randomizes options: ($100-$1000?, 22 wedges), "Lose Turn()", "Bankrupt()"
        #choose random integer to select index for list of wheel options
        #buy consonant() unless "Lose Turn()" or "Bankrupt()"
        #main()

    #lose turn():
        #turn 'flag' changes
        #play moves to next player
        #turnNum += 1
        #main()

    #Bankrupt():
        #set money count for round to 0
        #lose turn()

    #buy consonant():
        #bring in money value from spin wheel()
        #bring in player's round money
        #prompt for letter
        #confirm is consonant (not vowel or number)
        #check if letter in answer
            #if yes: add $$$ to round money for each occurrence
                #update puzzleboard with letters
                #main()
            #if no: no $$$ awarded, lose turn()

    #buy vowel():
        #check money balance (need 250)
        #if > 250, continue
            #deduct 250 from money balance
            #check if letter in answer
                #if yes: update puzzleboard with letters
                    #main()
                #if no: lose turn()
        #if < 250, back to main screen
            #lose turn()

    #solve()
        #checks if input string matches answer
        #if yes:
            #win()
        #if no:
            #Lose Turn()

    #win():
        #add current player round money to player's total bank
        #reset all players' money to zero
        #round counter += 1

### FINAL ROUND ###
    #pick player with highest total bank money after round 2
    #pick random number (10-100), multiply by 5000 to get grand prize amount
    #print player number and congrats
    #Print category
    #print blanks for letters, but show RSTLNE preloaded
    #consonantCount = 0
    #vowelCount = 0
    #prompt for 3 consonants and 1 letter one at a time
    #if consonantCount excedes 3 or vowelCount excedes 1, do not accept and reprompt
    #once all guesses are in, ask to verify [Y/N]
    #apply all letters to final answer using GuessingWordGame idea
    #start timer or allow a single guess
    #if guess string matches Answer:
        #print congratulations, Answer was "Answer"!
        #Show grand prize value
        #add to previous dollar amount to show total winnings
        #thanks for playing!
    #if guess wrong:
        #print Sorry! Answer was "Answer"...
        #Show grand prize value
        #show previous dollar amount (total winnings)
        #thanks for playing!
