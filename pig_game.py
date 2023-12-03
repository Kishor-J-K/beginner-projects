import random

# function to role a die

def roll():
    min_value=1
    max_value=6
    value=random.randint(min_value,max_value)
    return value

# getting info on numbar of players

while True:
    players=input("Enter no of players(2-4) : ")
    
    if players.isdigit():
        players=int(players)
        if  2<=players<=4:
            break
        else:
            print("\nplayers must be 2-4\n")
    else:
        print("\ninvalid entry, try again\n")


# initialising important data

players_scores=[0 for i in range(players)]
max_score=50


# main activity of the game starts from here

while max(players_scores)<max_score:
    
    for player_index in range(players):
        current_score=0
        print(f"\nplayer {player_index+1} is playing")
        print(f"current score {players_scores[player_index]}\n")
        while True:
            roll_choice=input("\nwould u like to roll (y)?: ")
            roll_choice=roll_choice.lower()
            if roll_choice!='y':
              break
           
            value=roll() 
            if value ==1:
                print("\nu got 1! turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print(f"u got {value}")    
            print(f"your score is {current_score}")
        
        players_scores[player_index]+=current_score
        print(f"\nyour scour is {players_scores[player_index]}")
        print("####################################################################")        

max_score=max(players_scores)
winning_index=players_scores.index(max_score)
print("player number ", winning_index+1," is the winner with the score of:",max_score)