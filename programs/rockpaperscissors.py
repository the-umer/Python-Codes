import random

# Terminal Colors
CRED = '\033[91m'
CYELLOW = '\33[33m'
CGREEN  = '\33[32m'
CGREENBG  = '\33[42m'
CBLUEBG   = '\33[44m'
CEND = '\033[0m'

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
        print(CBLUEBG +f"\n\t\t*** Round {round} ***" + CEND)
        your_choice = input("\nEnter R for rock, S for scissors, P for paper: ").upper()
        computers_choice = random.choice(choices)
        print(f"You Choose {choosed_item_name(your_choice)} - Computer choose {choosed_item_name(computers_choice)}")
        # draw conditions
        if your_choice == computers_choice:
            print(CYELLOW+f"Draw - Score {computers_score} - {my_score}"+CEND) 
        # Computer's win situation 
        elif your_choice == "S" and computers_choice == "R":
            computers_score += 1
            print(CRED+f"Computer Win - Score {computers_score} - {my_score}"+CEND)
        elif your_choice == "R" and computers_choice == "P":
            computers_score += 1
            print(CRED+f"Computer Win - Score {computers_score} - {my_score}"+CEND)
        elif your_choice == "P" and computers_choice == "S":
            computers_score += 1
            print(CRED+f"Computer Win - Score {computers_score} - {my_score}"+CEND)
        # You Win
        elif your_choice == "S" and computers_choice == "P":
            my_score += 1
            print(CGREEN+f"You Win - Score {computers_score} - {my_score}"+CEND)
        elif your_choice == "P" and computers_choice == "R":
            my_score += 1
            print(CGREEN+f"You Win - Score {computers_score} - {my_score}"+CEND)
        elif your_choice == "R" and computers_choice == "S":
            my_score += 1
            print(CGREEN+f"You Win - Score {computers_score} - {my_score}"+CEND)    
        round+=1

    # Print's final game score at the end....
    if my_score > computers_score:
            print(CGREEN +f"\n\t\t|| YOU WIN [{my_score} : {computers_score}] ||" + CEND)
    elif computers_score > my_score:
            print(CRED + f"\n\t\t|| COMPUTER WIN [{my_score} : {computers_score}] ||" + CEND)
    else:
            print(CYELLOW +f"\n\t\t|| DRAW [{my_score} : {computers_score}] ||" + CEND)
        
    print(CRED + "\n\t\t Game Over " + CEND)


print(CGREENBG + "\n\t   ROCK PAPER SCISSORS GAME   " + CEND)
print(CBLUEBG + "\n  This is a 5 round Rock Paper Scissors Game built in python.   "+ CEND)
while True:
    run_game()
    choice = input("\nDo you want to play again (y/n): ")
    if choice == "n":
        print(CRED + "Exiting the game..." + CEND)
        break
    elif choice == "y":
        continue
    else:
        print(CRED + "You entered invalid operation. Restart the game." + CEND)
        break
