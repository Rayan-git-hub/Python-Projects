import random
user=int(input('Press 0 for rock🪨\n,1 for paper📰\n,2 for scissor✂️.'))
game=['🪨', '📰', '✂️']
play=random.randint(0,2)
if(user<0 or user>=3):
    print('You typed an invalid number , you lose!')
else:
    print(game[user])
    print(game[play])
    
    if(user==0 and play==2) or (user==1 and play==0) or (user==2 and play==1):
        print('You won')
    elif(user==0 and play==1) or (user==1 and play==2) or (user==2 and play==0):
        print('cpu won')
    else: 
        print('Draw match!')
