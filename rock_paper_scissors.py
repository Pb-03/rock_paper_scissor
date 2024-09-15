import random
def play():
    user=input("What's you're choice? 'r' for rock, 'p' for paper and 's' for scissors.\n")
    computer=random.choice(['r','p','s'])

    if user==computer:
        return print("it's a win")
    
    
    if is_win(user,computer):
        return 'You won'
    

    return print('You lost')


#r>s>p>r
def is_win(player,opponent):
    #returns true if player wins
    if(player=='r' and opponent=='s') or (player=='s' and opponent =='p') or (player=='p' and opponent=='r'):
        return True
play()