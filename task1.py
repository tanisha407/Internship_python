# Rock-Paper-Scissor game using python 
import random

list1 = ["Rock", "Paper","Scissor"]


flag = True
while(flag):
        
        user = int(input("Enter Your Choice -> 0/1/2: "))
        user = list1[user]
        com = random.randint(0,2)
        com = list1[com]

        print(f"Your choice is {user} ")
        print(f"Computer choice is {com}")
        if(user == com):
            {
            print("It's tie.No one win")
        }
            
        elif(user == "Rock" and com == "Paper"):{
            print("computer wins")
        }  
            
        elif(user == "Rock" and com == "Scissor"):{
            print("You win")
        }     
            
        elif(user == "Paper" and com == "Scissor"):{
            print("computer wins")
        }      

        elif(user == "Paper" and com == "Rock"):{
            print("you win")
        } 

        elif(user == "Scissor" and com == "Rock"):{
            print("computer wins")
        }    

        else: {
            print("you win")
        }   

        play = input("Want to play again (Yes or No): ")
        if(play == "Yes" or play == "yes"):
            
            flag = True
         
        else:
            flag = False       
    

print("Thanks for playing")