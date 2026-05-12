import random 

computer = random.choice([-1,0,1])

youstr = input("Enter your choice (rock/paper/sisscor): ").lower()
youDict = {"rock": 1, "paper": -1, "sissor": 0}
reverseDict = {1: "rock", -1: "paper", 0: "sissor"}

# Input validation 
if youstr not in youDict:
    print("Invalid input!")
    exit()

you = youDict[youstr]

# we have 3 cases: first is draw, second is computer wins, third is you win

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1): #-2
        print("You Lose!")

    elif(computer == -1 and you == 0):#-1
        print("You Win!")

    elif(computer == 1 and you == -1):#2
        print("You Win!")

    elif(computer == 1 and you == 0): #1
        print("You Lose!")

    elif(computer == 0 and you == -1): #1
        print("You Lose!")

    elif(computer == 0 and you == 1):#-1
        print("You win!")

    else:
        print("Something went wrong!")
 

