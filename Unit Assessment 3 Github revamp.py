#DESCRIPTION
#Code will have the user enter a number that will be compared to a randomly
#generated number by a computer. The code will then stat which number was
#higher and keep track of all lower, higher and tied number.
#Upon entering a -1 the program will stop prompting for the user to enter a
#number and then tell the them percentages of how much there number was
#higher, lower or tied with the computers number.

#UNIT 3 ASSESSMENT
import random

#THESE ARE CONSTANTS THAT NEVER CHANGE
prompt = "Enter number: "

#THESE EXIST TO KEEP TRACK OF TOTAL PLAYER AND COMPUTER TIES, WINS AND LOSES
computer_higher = 0
player_higher = 0
ties = 0

#TELLING USER HOW TO USE PROGRAM
print("For this program, you will need to enter an integer between 1 and 20")
print("")

#LOOP THE STATMENT AND CONTINUES ALL PROMPTS
while True:

    #PROMPTING THE USER TO INPUT A NUMBER TO COMPARE TO THE COMPUTERS RANDOM
    #NUMBER WHERE IT THEN TRYS THE INPUT AND CHECKS FOR ERRORS
    try:
        player_number = int(input(prompt))                                                     
        print("")
        
    except:
        print("")
        print("You need to enter an integer")
        print("")
        continue
    
    if player_number > 20:
        print("You need to enter a numbers between 1 and 20")
        print("")
        continue
    
    if player_number < -1:
        print("You need to enter a numbers greater the 0")
        print("")
        continue

    if player_number == 0:
        print("You cannot enter the number Zero")
        print("")
        continue
    
    #WILL STOP THE PROGRAM IF -1 IS ENTERED
    if player_number == -1:

        #THIS EXISTS TO GET THE PERCENTAGE OF PLAYER AND COMPUTER HIGHER,
        #LOWER AND TIES RATHER THEN JUST THE BASE LINE NUMBER AND ROUNDS
        #TO THE NEAREST TENTH
        total = computer_higher + player_higher + ties
        computer_higher = round(computer_higher / total * 100, 1)
        player_higher = round(player_higher / total * 100, 1)
        ties = round(ties / total * 100, 1)
        
        print("The Computers number was greater than your number", str(computer_higher) +
              "%","of the time")
        print("Your number was higher than the computer's number", str(player_higher) +
              "%","of the time")
        print("Both numbers were the same", str(ties) + "%", "of the time")
        break

    #GETS THE COMPUTERS NUMBER
    computer_number = random.randint(1, 20)
    
    #PRINTS COMPUTER NUMBER SO THE PLAYER KNOWS WHAT IT GENERATED
    print("Computers number is", computer_number)  

    #THIS WILL DETERMINE IF THE NUMBER ENTERED BY THE PLAYER WAS LOWER
    if computer_number > player_number:             
        print("The Computers number was higher")
        computer_higher = computer_higher + 1
        print("")
        
    #THIS WILL DETERMINE IF THE NUMBER ENTERED BY THE PLAYER WAS HIGHER
    elif computer_number < player_number:           
        print("The Players number was higher")
        player_higher = player_higher + 1
        print("")
        
    #THIS WILL DETERMINE IF THE NUMBER ENTERED BY THE PLAYER TIED 
    else:                                           
        print("Both numbers where the same")
        ties = ties + 1
        print("")
            








