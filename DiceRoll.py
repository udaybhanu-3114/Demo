import RollDice as r
import random
res = [1,2,3,4,5,6]
count = 0
sh = random.randint(0,5)
print(sh)
for i in range(sh):
    def random_shuffl_1(res):
        res[1],res[2],res[3],res[4]=res[3],res[1],res[4],res[2]
        res1 = res
    random_shuffl_1(res)
    def random_shuffl_2(res):
        res[0],res[1],res[4],res[5]=res[4],res[0],res[5],res[1]
    random_shuffl_2(res)
r.dice(res)
while True:
    roll = input("Enter your choice(d/u/l/r/q): ").lower().strip()
    if roll == 'd' or roll =='down':
        r.dice_down(res)
        count+=1
    elif roll == 'u' or roll =='up':
        r.dice_up(res)
        count+=1
    elif roll == 'l' or roll =='left':
        r.dice_left(res)
        count+=1
    elif roll == 'r' or roll =='right':
        r.dice_right(res)
        count+=1

    elif roll == 'q' or roll =='quit':
        print('Thanks for Participation, Visit Again!!!')
        break
    else:
        print('Please Make Correct Choice!!! ')
    
print(f'You roll a Dice for {count} times')
print('The Final Position Of Dice is: \n')
r.dice(res)




