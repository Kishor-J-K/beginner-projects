import random

def roll():
    value=random.randint(1,6)
    return value

print("""        welcome snake and ladder game

            important information
      🐍 snake              🪜 ladder
      ----------------------------------
        31->14       |          2->23
        41->20       |          8->12
        58->37       |          17->93
        67->49       |          29->54
        84->62       |          32->51
        92->76       |          39->80
        99->4        |          70->89
                     |          75->96
      """) 

dct1={31:14,41:20,58:37,67:49,84:62,92:76,99:4}
dct2={2:23,8:12,17:93,29:54,32:51,39:80,70:89,75:96}

while True:
    players=input("enter no of of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 1<players<5:
            break
        else:
            print("only 2-4 players can play\nprovide a valid number\n")
    else:
        print("u need to enter a digit\n")
        
max_point=100
each_player=[0 for i in range(players)]

while max_point>max(each_player):
    for player_index in range(players):
        value=0
        print("###########################################")
        print(f"\nplayer {player_index+1} is playing")
        print(f"player current position is {each_player[player_index]}\n")
        while True:
            choice=input("do you want to roll the die(y) or pass: ")
            choice=choice.lower()
            if choice !='y':
                break
            value=roll()
            print(f"the die 🎲 rolled {value}")
            each_player[player_index]+=value
            if each_player[player_index]>100:
                print(f"you got {value}\n")
                print("You cant go beyound 100th box u lost your turn")
                each_player[player_index]-=value 
            elif each_player[player_index] in dct1:
                print(f"oh no 🙀 a snake 🐍 bit😵 you by at {each_player[player_index]}")
                print(f"you have been droped to {dct1[each_player[player_index]]}")
                each_player[player_index]=dct1[each_player[player_index]]
            elif each_player[player_index] in dct2:
                print(f"hurrey 🎉 u got a ladder 🪜 at {each_player[player_index]}")
                print(f"you climbed to {dct2[each_player[player_index]]}\n")
                each_player[player_index]=dct2[each_player[player_index]]
            else:
                print(f"you reached {each_player[player_index]}")
            break
                
winner=each_player.index(100)
print(f"\nplayer no {winner+1} has won ✌️ ✌️ the game 💐")
                