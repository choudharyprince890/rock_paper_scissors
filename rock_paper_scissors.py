import random as a 
number=a.randint(1,3)

if number==1:
    computer='rock'
if number==2:
    computer='paper'    
if number==3:
    computer='scissor'

def z():
    user=input('choose between (rock), (paper) & (scissor)....... ' ).lower()
    
    if user==computer:
            print('match is tie')
    elif computer=='scissor' and user=='paper' or computer=='paper' and user=='scissor' or computer=='scissor' and user=='rock':
            print('congratulations... :) you won the match')
    else:
            print('so sorry... :( you loose the match')
z()
print(f'computer choose...... {computer}')
# ROCK,PAPER,SCISSOR game