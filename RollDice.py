
res = [1,2,3,4,5,6]

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
dice(res)

def dice_down(down):
    down[2],down[1],down[4],down[3]=down[1],down[3],down[2],down[4]
    dice(down)
    print(down[1],down[3],down[2],down[4])
    print('down')
    

 

def dice_up(up):
    up[1],up[2],up[4],up[3]=up[2],up[4],up[3],up[1]
    dice(up)
    print('up')

 


def dice_left(left):
    left[0],left[1],left[5],left[4]=left[1],left[5],left[4],left[0]
    dice(left)
    print('left')

 


def dice_right(right):
    right[4],right[5],right[1],right[0]=right[5],right[1],right[0],right[4]
    dice(right)
    print('right')

 


