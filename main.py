import test as t

count = 0

while True:
    roll = input("Enter your choice(d/u/t/r/q): ").lower()
    if roll=='d':
        t.dice_down(t.res)
        d=t.res
        count += 1
    elif roll=='u':
        t.dice_up(t.res)
        d=t.res
        count += 1
    elif roll=='l':
        t.dice_left(t.res)
        d=t.res
        count += 1
    elif roll=='r':
        t.dice_right(t.res)
        d=t.res
        count += 1

    elif roll=='q':
        print('Thanks for Participation, Visit Again!!!')
        break
    else:
        print('Pleas Make correct Choice!!!')
print(f'you roll a Dice for {count} times')
print('The Final Position Of Dice is: \n')
t.dice(t.res)
        
