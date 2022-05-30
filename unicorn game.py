print ("Lucky Unicorn Game")

Yes = ["yes","Yes","Yea", "yea", "y", "Y", "Ye", "ye"]
No = ["No", "no", "Na", "na", "N", "n"]
Play = input("Do You Want To Play Yes or No? ")
if (Play in Yes):
    Instructions = input("Do you know how to play yes or no? ")
    if (Instructions in Yes): 
        print ("Alright") 
        
        
    elif (Instructions in No):
        print ("the starting player will pay a intial amount to start their game the amount the player should pay to play the game is $1 per round and the player should press enter to play the game the computer will generate a random token that is either a zebra, horse, donkey or a unicorn for the player the token should be displayed to the user if the token is a unicorn the user will win $5 and if the token is a zebra or a horse they will win 50c and if the token is a donkey the user will win nothing the maxium amount you can spend on the game at one time is $10 per session also the game allows you to continue/quit provided if you have lost all your money or not the game will supply the right feedback how much money you have won/lost after each round and how much money you have left")
        
    
    
elif (Play in No):
    print("you have to play")
    
else:
    print ("Invalid")
    
            
    
    