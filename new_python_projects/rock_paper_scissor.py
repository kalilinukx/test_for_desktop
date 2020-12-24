# First part of code for importing and initialising 
import random as rd 
rnd  = 0
def is_win(player,opponent):
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
                return True

your_win_count = 0 
opponent_win_count = 0
draw = 0

# second part of the code for defining functions 

def win_series():
    global your_win_count 
    global opponent_win_count

    if your_win_count < opponent_win_count:
        return print("You have Lost the series")
        
    else:
        return print("You have won the series ! Yay")
    

#  Third part of the code for calling function and making it a series play
while rnd<3 :
    
    def play():
        global your_win_count
        global opponent_win_count
        
        user = input("What's your choice? 'r', for rock,'p',for paper,'s', for scissors \n ").lower()
        computer = rd.choice(['r', 'p', 's'])
        
        if user == computer:
            global draw 
            draw = draw+1
            return "OmG you both Have Same choice it's a tie"
        
        if is_win(user,computer):
            your_win_count += 1
            return 'You won! this time gracias'
        opponent_win_count = opponent_win_count+1
        return '"Sorry next time" You lost!'
        
    print(play(),f"This is round no {rnd+1}")
    rnd = rnd + 1
user = input("Do you want to play a series: types yes for playing: ")
if user == 'play':
    
    win_series()

print(f"Your win count:{your_win_count} Opponent win count:{opponent_win_count} Draw count : {draw}")
    