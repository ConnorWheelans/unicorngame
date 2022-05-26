print ("Lucky Unicorn Game")

Yes = ["yes","Yes","Yea", "yea", "y", "Y", "Ye", "ye"]
No = ["No", "no", "Na", "na", "N", "n"]
Play = input("Do You Want To Play Yes or No? ")
if (Play in Yes):
    Instructions = input("Do you know how to play yes or no? ")
    if (Instructions in Yes): 
        print ("Alright") 
        
        
    elif (Instructions in No):
        print ("the starting user will pay a intial amount to start their game the amoun the user should pay to play the game is $1 per round and the user should press enter to play the game the computer will gnerate a random token that is either a zebra, horse, honkey or a unicorn for the player  ")
        
    
    
elif (Play in No):
    print("you have to play")
    
else:
    print ("Invalid")
    
            
    
    