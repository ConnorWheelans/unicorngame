import random
import time

#valide set to false because there has been no valuse entered
valid = False
#start of loop if Valid != True
while not valid:
        error = "|:|Invalid|:|"
       
        try:
                print("Enter amount you would like to pay between $1 and $10 ")
                STARTING_BALANCE = int(input(": "))
               
                #Checks if response is valid
                if 1 <= STARTING_BALANCE <=10:
                        valid = True
               
                #response isn't valid
                else:
                        print (error)
        #loops back to start because valid isn't true                
        except ValueError:
                print()
                print("------------------")
                print(error)

#prints once valid = true
print()
print("-----------------------------")
print("$", STARTING_BALANCE, " is valid and entered")
time.sleep(1)
print()
print("Total amount: $", STARTING_BALANCE)


#defining variables
balance = STARTING_BALANCE

rounds_played = 0
playable_rounds = balance-1

print()
play_again = input("Press <Enter> to play...").lower()
while play_again == "":
                #increase number of rounds played
                rounds_played += 1
               
                #print round number
                print()
                print("***** Rounds #{}*****".format(rounds_played))
               
               
                chosen = random.randint(1, 100)
                   
                    #Balance Adjust
                    #If it generates unicorn adds $5
                if 1 <= chosen <=5:
                                chosen = "Unicorn"
                                balance += 5
                elif  6 <= chosen <= 36:
                                chosen = "Donkey"
                                balance -= 0
                else:
                                if chosen % 2 == 0:
                                                chosen = "Horse"
                                                balance -= 0.5
                                else:
                                                chosen = "Zebra"
                                                balance-= 0.5
                       
                    #output
                print("You got a {}.     Your balance is ${:.2f}".format(chosen, balance))
                print()
                print()
                print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
                print("Final Balance: ${:.2f}".format(balance))
               
                #calculates profit
                mult = balance-STARTING_BALANCE
               
                if mult > 0:
                                print("You made ${:.2f}".format(mult))
                else:
                                print("You lost ${:.2f}".format(0-mult))                
               
       
                if rounds_played - STARTING_BALANCE > 0:
                                print("Sorry you have no more money in your starting balance")
                                play_again = "0"
                else:
                                print()
                                print("Press <Enter> to play again"
                                      " or <Any Other> to quit")
                                play_again = input(": ")
print()
#valide set to false because there has been no valuse entered
valid1 = False
#start of loop if Valid != True
#prints once valid = true
mult = balance-STARTING_BALANCE
print()
print("---------------------------------")
if mult > 0:
        print("You made ${:.2f}".format(mult))
else:
        print("You lost ${:.2f}".format(0-mult))
print("--------------------------------")
            
    
    