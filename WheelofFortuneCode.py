"""
Wheel of Fortune Game
Aaron Janaszak
"""
import random

#Initialize players total bank
Bank = [0,0,0]

#Initialize players round bank
RoundMoney = [0,0,0]

#Initialize players turn bank
TurnMoney = [0,0,0]

#Load categories and answers into list
PuzzleCategories = ['TV Show Character Catch Phrases', 'Famous Musicians', 'Comic Book Characters']
PuzzleAnswers = ['Bazinga','Johnny Cash','The Martian Manhunter']

#initialize turn number to 1
turnNum = 1

#initialze round number to 0
roundNum = 0

#decide on wheel wedge values
wedges = []
for i in range(1,23):
    wedges.append(i*50)
wedges.append('Lose Turn')
wedges.append('Bankrupt')
vowels = 'AEIOU'



#### FUNCTIONS ####
def main():
    global roundNum
    global turnNum
    global answer
    global blankList
    print()
    print("The category is:",PuzzleCategories[roundNum])
    
    length = len(PuzzleAnswers[roundNum])
    blanks = PuzzleAnswers[roundNum]
    for i in range(length):
        if ord(PuzzleAnswers[roundNum][i]) != 32:
            blanks = blanks.replace(PuzzleAnswers[roundNum][i], '@')
    blankList = list(blanks)
    print()
    answer = blankList
    if roundNum == 2:
        FinalRound()
    else:
        Top()

def Top():
    global roundNum
    global turnNum
    global answer
    global RoundMoney
    global playerNum
    print(*answer)
    
    if turnNum % 3 == 1:
        playerNum = 1
        print("It is Player One's turn.")
        print("You currently have $"+str(RoundMoney[0])+" available.\n")
    if turnNum % 3 == 2:
        playerNum = 2
        print("It is Player Two's turn.")
        print("You currently have $"+str(RoundMoney[1])+" available.\n")
    if turnNum % 3 == 0:
        playerNum = 3
        print("It is Player Three's turn.")
        print("You currently have $"+str(RoundMoney[2])+" available.\n")
        
    turnContinue = True
    ask = 0
    while ask != '1' or ask != '2' or ask != '3':
        print("Menu Options")
        print("============")
        print("1) Spin the Wheel")
        print("2) Buy a Vowel")
        print("3) Attempt to Solve the Puzzle")
        print()
        ask = int(input("Select a menu option: "))
        
        if ask == 1:
            spinWheel()
        elif ask == 2:
            buyVowel()
        elif ask == 3:
            Solve()
        else:
            print("Please select a valid response.")
            ask = int(input("Select from the menu which option you'd like to make: "))

def spinWheel():
    global index
    index = random.randint(0,23)
    global wedges
    
    if index < 22:
        print("The wheel landed on: $"+str(wedges[index]))
        pickConsonant()
    elif index == 22:
        print("The wheel landed on:",wedges[index])
        loseTurn()
    elif index == 23:
        Bankrupt()

def loseTurn():
    print("You lost your turn! Next player!")
    print()
    global turnNum
    turnNum += 1
    Top()

def pickConsonant():
    turnContinue = True
    global blankList
    global answer
    global wedges
    global index
    global playerNum
    
    price = wedges[index]
    letter = input("Please select a consonant: ")
    letter = letter.upper()    
    if letter not in vowels:
        if letter.upper() in PuzzleAnswers[roundNum].upper():
            print("You have selected the letter:",letter.upper())
            print()
            for i in range(len(PuzzleAnswers[roundNum])):
                char = PuzzleAnswers[roundNum][i].upper()
                if letter == char:
                    answer[i] = letter
            moneyWon = price * answer.count(letter)
            print("that won you: $"+str(moneyWon))
            RoundMoney[playerNum-1] += moneyWon
            Top()
        else:
            print('That letter is not in the answer!')
            loseTurn()
        
def buyVowel():
    global playerNum
    global turnNum
    global RoundMoney
    global answer
    print("You need $250 to buy a vowel")
    if RoundMoney[playerNum-1] > 250:
        vowel = input("Which vowel would you like to buy? ")
        vowel = vowel.upper()
        RoundMoney[playerNum-1] -=  250
        if vowel.upper() in PuzzleAnswers[roundNum].upper():
            print("You have selected the letter:",vowel.upper())
            print()
            for i in range(len(PuzzleAnswers[roundNum])):
                char = PuzzleAnswers[roundNum][i].upper()
                if vowel == char:
                    answer[i] = vowel
        Top()
    else:
        print("You do not have enough money this round to buy a vowel.")
        Top()

def Bankrupt():
    global turnNum
    print("You're Bankrupt!")
    print("Player "+str(playerNum)+" now has $0.")
    RoundMoney[playerNum-1] = 0
    loseTurn()

def Solve():
    global turnNum
    global roundNum
    global PuzzleAnswers
    
    attempt = input("Please type your guess at the solution: ")
    attempt = attempt.upper()
    if attempt == PuzzleAnswers[roundNum].upper():
        Win()
    else:
        print("That was not the answer.")
        loseTurn()

def Win():
    global turnNum
    global roundNum
    global RoundMoney
    global PuzzleAnswers
    global playerNum
    global Bank
    print("You got it!")
    print("Player "+str(playerNum)+" won this round and added",RoundMoney[playerNum-1],"to their total!")
    Bank[playerNum-1] += RoundMoney[playerNum-1]
    RoundMoney = [0,0,0]
    roundNum += 1
    main()

def FinalRound():
    global turnNum
    global roundNum
    global RoundMoney
    global PuzzleAnswers
    global playerNum
    global Bank
    global vowels
    print("Player One had: $"+str(Bank[0])+".")
    print("Player Two had: $"+str(Bank[1])+".")
    print("Player Three had: $"+str(Bank[2])+".")
    maxIndex = Bank.index(max(Bank))
    print("Player",(maxIndex+1),"had the most money and gets to play the 3rd round!")
    print("They are coming in with $"+str(Bank[maxIndex])+"!")
    print()
    print("The category is:",PuzzleCategories[roundNum])
    length = len(PuzzleAnswers[roundNum])
    blanks = PuzzleAnswers[roundNum]
    for i in range(length):
        if ord(PuzzleAnswers[roundNum][i]) != 32:
            blanks = blanks.replace(PuzzleAnswers[roundNum][i], '@')
    blankList = list(blanks)
    print()
    answer = blankList
    print(*answer)
    print("We'll start you with the letters RSTLNE.")
    given = 'rstlne'
    given = given.upper()   
    print(given)
    for letter in given:
        letter = letter.upper()
        PuzzleAnswers[roundNum] = PuzzleAnswers[roundNum].upper()
        if letter in PuzzleAnswers[roundNum]:
            for i in range(len(PuzzleAnswers[roundNum])):
                char = PuzzleAnswers[roundNum][i].upper()
                if letter == char:
                    answer[i] = letter
    print(*answer)
    consCount = 0
    vowelCount = 0
    print("After submitting the last letter, you'll have one last guess to solve the puzzle!")
    print("Now please input 3 consonants and a vowel.")
    first = input("First Letter: ")
    first = first.upper()
    second = input("Second Letter: ")
    second = second.upper()
    third = input("Third Letter: ")
    third = third.upper()
    fourth = input("Fourth Letter: ")
    fourth = fourth.upper()
    final = [first, second, third, fourth]
    print(final)
    for letter in final:
        letter = letter.upper()
        PuzzleAnswers[roundNum] = PuzzleAnswers[roundNum].upper()
        if letter in PuzzleAnswers[roundNum]:
            for i in range(len(PuzzleAnswers[roundNum])):
                char = PuzzleAnswers[roundNum][i].upper()
                if letter == char:
                    answer[i] = letter
    print(*answer)
    print("You've got one final guess!")
    guess = input("What do you think the answer is? ")
    guess = guess.upper()
    bonusPrize = random.randint(10, 100) * 500
    if guess == PuzzleAnswers[roundNum]:
        print("You won!")
        print("Your bonus prize was: $"+str(bonusPrize)+'!!!')
        print("Your grand total today is: $"+str(bonusPrize + Bank[maxIndex])+"!!!")
        exit()
    else:
        print("You Lost....")
        print("You're walking away with $"+Bank[maxIndex]+".")
        exit()
    
    

#### timer taken from https://www.pythonpool.com/python-timer/

        
if CONT == True:
    main()
else:
    exit()
