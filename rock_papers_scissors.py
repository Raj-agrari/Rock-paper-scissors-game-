import random 

while True:
    
    user_choice = input("enter your choice : (rock,paper,scissors ): ")
    possible_actions = [ "rock" , "paper", "scissors" ]
    computer_actions = random.choice(possible_actions)
    print("enter your choice: ", user_choice)
    print("computer choose: ", computer_actions)

    if user_choice == computer_actions:
        print("its a tie")

    elif user_choice == "rock" and computer_actions == "scissors":
        print("`you win")

    elif user_choice =="paper" and computer_actions == "rock":
        print("you win")

    elif user_choice == "scissors" and computer_actions =="paper":
        print("you win")

    else:
        print("computer wins")


