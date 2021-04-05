import random
res = [1,2,3,4,5,6]
sh = random.randint(0,10)
print(res)
def dice(x):
    print(f'         {x[1]}       ')
    print('    +---------+')
    print('   /|        /|')
    print(f'  / |   {x[2]}   / |')
    print(' +--+------+  +')
    print(f'{x[5]}|  /      |  /',f'{x[0]}')
    print(f' | /   {x[4]}   | /')
    print(' |/        |/')
    print(' +---------+')
    print(f'    {x[3]}  ')
print(sh)
for i in range(sh):
    def random_shuffl_1(res):
        res[1],res[2],res[3],res[4]=res[3],res[1],res[4],res[2]
        res1 = res
    random_shuffl_1(res)
    def random_shuffl_2(res):
        res[0],res[1],res[4],res[5]=res[4],res[0],res[5],res[1]
    random_shuffl_2(res)
dice(res)


def dice_down(down):
    down[1],down[2],down[3],down[4]=down[3],down[1],down[4],down[2]
    dice(down)

def dice_up(up):
    up[1],up[2],up[3],up[4]=up[2],up[4],up[1],up[3]
    dice(up)

def dice_left(left):
    left[0],left[1],left[4],left[5]=left[1],left[5],left[0],left[4]
    dice(left)

def dice_right(right):
    right[0],right[1],right[4],right[5]=right[4],right[0],right[5],right[1]
    dice(right)


