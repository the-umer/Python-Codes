import random

def choosed_item_name(item_name):
    match item_name: 
        case "R" : return "Rock"
        case "P" : return "Paper"
        case "S" : return "Scissors"

def run_game():
    my_score = 0
    computers_score = 0
    choices = ["R","P","S"]
    round = 1
    while round <= 5:
        print(f"Round {round}")
        your_choice = input("Enter R for rock, S for scissors, P for paper: ").upper()
        computers_choice = random.choice(choices)
        print(f"You Choose {choosed_item_name(your_choice)} - Computer choose {choosed_item_name(computers_choice)}")
        # draw conditions
        if your_choice == "R" and computers_choice == "R":
            print(f"Draw - Score {computers_score} - {my_score}")
        elif your_choice == "S" and computers_choice == "S":
            print(f"Draw - Score {computers_score} - {my_score}")
        elif your_choice == "P" and computers_choice == "P":
            print(f"Draw - Score {computers_score} - {my_score}")   
        # Computer's win situation 
        elif your_choice == "S" and computers_choice == "R":
            computers_score += 1
            print(f"Computer Win - Score {computers_score} - {my_score}")
        elif your_choice == "R" and computers_choice == "P":
            computers_score += 1
            print(f"Computer Win - Score {computers_score} - {my_score}")
        elif your_choice == "P" and computers_choice == "S":
            computers_score += 1
            print(f"Computer Win - Score {computers_score} - {my_score}")
        # You Win
        elif your_choice == "S" and computers_choice == "P":
            my_score += 1
            print(f"You Win - Score {computers_score} - {my_score}")
        elif your_choice == "P" and computers_choice == "R":
            my_score += 1
            print(f"You Win - Score {computers_score} - {my_score}")
        elif your_choice == "R" and computers_choice == "S":
            my_score += 1
            print(f"You Win - Score {computers_score} - {my_score}")     
        round+=1

    # Print's final game score at the end....
    if my_score > computers_score:
            print(f"\nYOU WIN - [{my_score} : {computers_score}]")
    elif computers_score > my_score:
            print(f"\nCOMPUTER WIN - [{my_score} : {computers_score}]")
    else:
            print(f"\nDRAW - [{my_score} : {computers_score}]")
        
    print("---- Game Over -----")


print("-------ROCK PAPER SCISSORS GAME-------")
while True:
    run_game()
    choice = input("Do you want to play again (y/n): ")
    if choice == "n":
        print("Exiting the game...")
        break
