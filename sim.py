import random
import sys

#Assume we always switch
def monty_hall(DOORS=3):

    chose = random.randint(0,DOORS - 1)
    prize = random.randint(0,DOORS- 1)

    revealed_options = [i for i in range(DOORS) if i != chose and i != prize]
    revealed = random.choice(revealed_options)

    options = [i for i in range(DOORS) if i != revealed]
    choice = [i for i in options if i != chose]

    return choice[0] == prize    
    
if __name__ == "__main__":
    count = int(sys.argv[1])
    win,loss = 0,0
    for i in range(count):
        if monty_hall(): win += 1
        else: loss += 1
    
    win = (win / count) * 100
    loss = (loss / count) * 100
    
    print(f'When switching, we won the prize {win}%, and lost the prize {loss}%')